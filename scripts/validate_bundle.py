#!/usr/bin/env python3
"""Check the portable skill, local references and manifest without third-party packages."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote

from install import verify_bundle


def validate(root):
    root = Path(root).resolve()
    bundle = root / 'skills/ai-short-video-creation'
    count = verify_bundle(bundle)
    problems = []
    module_count = 0
    link_count = 0
    for f in root.rglob('*'):
        if not f.is_file() or any(x in f.parts for x in ['.git', '__pycache__']):
            continue
        if f.suffix == '.py':
            compile(f.read_text(encoding='utf-8'), str(f), 'exec')
        if f.suffix not in ['.md', '.yaml', '.json', '.py', '.txt']:
            continue
        content = f.read_text(encoding='utf-8')
        if re.search(r'(?i)(?:[cd]:[/\\](?:users|codexworkspace)[/\\]|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{25,}|sk-[A-Za-z0-9]{25,}|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY)', content):
            problems.append('Private path or credential pattern: ' + str(f.relative_to(root)))
        if f.name == 'SKILL.md':
            module_count += 1
            if not content.startswith('---\n') or '\n---\n' not in content[4:]:
                problems.append('Missing frontmatter: ' + str(f))
                continue
            front = content.split('---', 2)[1]
            if not re.search(r'^name: [a-z0-9-]+\s*$', front, re.M) or not re.search(r'^description:', front, re.M):
                problems.append('Invalid skill identity: ' + str(f))
        if f.suffix != '.md':
            continue
        for target in re.findall(r'\]\(([^)]+)\)', content):
            target = target.strip().strip('<>')
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            if any(marker in target for marker in ['[', ']', '绝对路径', '真实文件', '<', '>']):
                continue  # Deliberate template placeholders, not deployed links.
            path = unquote(target.partition('#')[0])
            if not path:
                continue
            actual = (f.parent / path).resolve()
            link_count += 1
            if not actual.is_relative_to(root) or not actual.exists():
                problems.append('Broken or external local reference: ' + str(f.relative_to(root)) + ' -> ' + target)
    if problems:
        raise ValueError('\n'.join(problems))
    return {'bundle_files': count, 'skills_including_main': module_count,
            'local_links': link_count, 'private_patterns': 0, 'status': 'passed'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, SyntaxError) as error:
        parser.exit(1, str(error) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
