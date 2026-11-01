import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/install.py'
spec = importlib.util.spec_from_file_location('bundle_install', SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / 'repo'
        self.bundle = self.source / 'skills/ai-short-video-creation'
        self.bundle.mkdir(parents=True)
        self.skill = self.bundle / 'SKILL.md'
        self.skill.write_text('---\nname: ai-short-video-creation\ndescription: test\n---\n', encoding='utf-8')
        (self.bundle / 'modules/demo').mkdir(parents=True)
        (self.bundle / 'modules/demo/rules.md').write_text('nested module', encoding='utf-8')
        self.manifest()
        self.dest = self.root / 'host/skills'

    def tearDown(self):
        self.tmp.cleanup()

    def manifest(self):
        fs = {f.relative_to(self.bundle).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest()
              for f in self.bundle.rglob('*') if f.is_file() and f.name != 'bundle-manifest.json'}
        (self.bundle / 'bundle-manifest.json').write_text(json.dumps({'version': 1, 'files': fs}), encoding='utf-8')

    def test_install_preserves_nested_modules(self):
        installer.install(self.source, self.dest)
        self.assertEqual((self.dest / 'ai-short-video-creation/modules/demo/rules.md').read_text(), 'nested module')
        self.assertTrue(self.skill.exists())

    def test_existing_skill_refuses_and_preserves_content(self):
        old = self.dest / 'ai-short-video-creation'
        old.mkdir(parents=True)
        (old / 'user.txt').write_text('keep me')
        with self.assertRaises(FileExistsError):
            installer.install(self.source, self.dest)
        self.assertEqual((old / 'user.txt').read_text(), 'keep me')

    def test_force_backs_up_old_skill_outside_discovery_root(self):
        old = self.dest / 'ai-short-video-creation'
        old.mkdir(parents=True)
        (old / 'user.txt').write_text('old settings')
        result = installer.install(self.source, self.dest, force=True)
        backup = Path(result['backup'])
        self.assertFalse(backup.is_relative_to(self.dest))
        self.assertEqual((backup / 'user.txt').read_text(), 'old settings')
        self.assertTrue((old / 'SKILL.md').is_file())

    def test_dry_run_creates_no_host_directories(self):
        result = installer.install(self.source, self.dest, dry_run=True)
        self.assertTrue(result['dry_run'])
        self.assertFalse(self.dest.parent.exists())

    def test_tampered_content_rejected_before_any_write(self):
        self.skill.write_text('modified after manifest')
        with self.assertRaises(ValueError):
            installer.install(self.source, self.dest)
        self.assertFalse(self.dest.exists())

    def test_unlisted_file_rejected(self):
        (self.bundle / 'extra-secret.txt').write_text('must not be copied')
        with self.assertRaises(ValueError):
            installer.install(self.source, self.dest)

    def test_manifest_traversal_rejected(self):
        (self.bundle / 'bundle-manifest.json').write_text(json.dumps({'version': 1, 'files': {'../outside.txt': '0' * 64}}))
        with self.assertRaises(ValueError):
            installer.install(self.source, self.dest)
        self.assertFalse(self.dest.exists())

    def test_source_destination_overlap_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.source / 'skills')
        self.assertTrue(self.skill.exists())


if __name__ == '__main__':
    unittest.main()
