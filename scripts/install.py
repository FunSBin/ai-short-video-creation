#!/usr/bin/env python3
"""Install the self-contained skill from a local clone; Python 3.10+, stdlib only."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import uuid

NAME = 'ai-short-video-creation'


def verify_bundle(bundle):
    bundle = Path(bundle).resolve()
    manifest_file = bundle / 'bundle-manifest.json'
    if not manifest_file.is_file() or manifest_file.is_symlink():
        raise ValueError('Missing or linked bundle-manifest.json')
    manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
    expected = manifest.get('files')
    if manifest.get('version') != 1 or not isinstance(expected, dict) or not expected:
        raise ValueError('Unsupported or empty bundle manifest')
    for name, digest in expected.items():
        path = PurePosixPath(name)
        if (not isinstance(name, str) or path.is_absolute() or '..' in path.parts
                or '\\' in name or ':' in name or str(path) != name
                or not re.fullmatch(r'[0-9a-f]{64}', str(digest))):
            raise ValueError('Unsafe manifest entry')
        target = bundle.joinpath(*path.parts)
        if not target.resolve().is_relative_to(bundle):
            raise ValueError('Manifest path leaves bundle')
    actual = set()
    for file in bundle.rglob('*'):
        if file.is_symlink():
            raise ValueError('Symlinks are not accepted in an install bundle')
        if file.is_file() and file != manifest_file:
            actual.add(file.relative_to(bundle).as_posix())
    if actual != set(expected):
        raise ValueError('Bundle has missing or unlisted files')
    if 'SKILL.md' not in expected:
        raise ValueError('Bundle does not contain SKILL.md')
    for name, digest in expected.items():
        if hashlib.sha256((bundle / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Checksum mismatch: ' + name)
    return len(expected)


def install(source, dest_root, force=False, dry_run=False):
    source = Path(source).expanduser().resolve()
    bundle = (source / 'skills' / NAME).resolve()
    dest_root = Path(dest_root).expanduser().resolve()
    destination = dest_root / NAME
    if destination.is_relative_to(source) or source.is_relative_to(destination):
        raise ValueError('Source and destination overlap')
    count = verify_bundle(bundle)
    if destination.is_symlink():
        raise ValueError('Destination must not be a symlink')
    if destination.exists() and not destination.is_dir():
        raise ValueError('Destination exists and is not a directory')
    if destination.exists() and not force:
        raise FileExistsError('Skill already exists; use --force to back it up and replace it')
    backup = None
    if destination.exists():
        backup = dest_root.parent / 'skill-backups' / (NAME + '-' + uuid.uuid4().hex)
        if backup.resolve().is_relative_to(dest_root):
            raise ValueError('Backup must be outside the skill discovery root')
    result = {'destination': str(destination), 'files': count, 'dry_run': dry_run,
              'backup': str(backup) if backup else None}
    if dry_run:
        return result
    dest_root.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.' + NAME + '-', dir=dest_root)).resolve()
    if not stage.is_relative_to(dest_root):
        raise ValueError('Unexpected staging directory')
    moved_old = False
    try:
        shutil.copytree(bundle, stage, dirs_exist_ok=True)
        verify_bundle(stage)
        # Check again before mutating an existing installation.
        if destination.exists() and not force:
            raise FileExistsError('Destination appeared during installation')
        if destination.is_symlink():
            raise ValueError('Destination changed to a symlink')
        if backup:
            backup.parent.mkdir(parents=True, exist_ok=True)
            destination.rename(backup)
            moved_old = True
        elif destination.exists():
            raise FileExistsError('Destination appeared during installation; refusing to overwrite')
        stage.rename(destination)
    except BaseException:
        if moved_old and not destination.exists():
            backup.rename(destination)
        raise
    finally:
        if stage.exists():
            # Only our resolved, verified staging folder may be removed.
            if not stage.is_relative_to(dest_root) or stage == dest_root:
                raise ValueError('Refusing to clean an unexpected directory')
            shutil.rmtree(stage)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1],
                        help='Local repository root (default: this clone)')
    codex_root = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    parser.add_argument('--dest', type=Path, default=codex_root / 'skills',
                        help='Host skill root directory, not the final skill folder')
    parser.add_argument('--dry-run', action='store_true', help='Verify and show the plan without writing')
    parser.add_argument('--force', action='store_true', help='Back up an existing skill before replacing it')
    args = parser.parse_args()
    try:
        result = install(args.source, args.dest, args.force, args.dry_run)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, str(error) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
