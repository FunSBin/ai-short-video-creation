#!/usr/bin/env python3
"""Refresh the checksum inventory after an intentional skill change."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    bundle = root / 'skills/ai-short-video-creation'
    manifest = bundle / 'bundle-manifest.json'
    files = {}
    for file in sorted(bundle.rglob('*')):
        if file.is_symlink():
            raise ValueError('Bundle must not contain symlinks')
        if '__pycache__' in file.parts or file.suffix == '.pyc':
            raise ValueError('Remove Python cache files before building the manifest')
        if file.is_file() and file != manifest:
            files[file.relative_to(bundle).as_posix()] = hashlib.sha256(file.read_bytes()).hexdigest()
    manifest.write_text(json.dumps({'version': 1, 'files': files}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Manifest files:', len(files))


if __name__ == '__main__':
    main()
