"""Check generated resources, local links and release hashes; no third-party packages."""
import hashlib
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
skill=root/'skills/carlet-boolean-research'
assert (skill/'SKILL.md').is_file()
assert (skill/'resources/research_core.py').read_bytes()==(root/'tools/research_core.py').read_bytes()
assert (skill/'resources/research_extensions.py').read_bytes()==(root/'tools/research_extensions.py').read_bytes()
cards=list((skill/'references/capabilities').glob('*.md'))
planned=json.loads((root/'books/carlet-2021/capability-plan.json').read_text(encoding='utf-8'))
assert {f.stem for f in cards}=={x['slug'] for x in planned}
for f in cards:
    t=f.read_text(encoding='utf-8')
    assert all(f'## {h}' in t for h in ('R —','I —','A1 —','A2 —','E —','B —')),f
for folder in (root/'books',skill,root/'docs'):
    for f in folder.rglob('*.md'):
        if '.cangjie/runs/' in f.as_posix():
            continue
        t=f.read_text(encoding='utf-8')
        assert not re.search(r'[A-Z]:[\\/](?:Users|Program Files)',t),f'private path: {f}'
        for link in re.findall(r'\]\(([^\s)]+)\)',t):
            if '://' in link or link.startswith('#'):
                continue
            assert (f.parent/link.split('#')[0]).exists(),f'broken link {f}: {link}'
manifest=root/'release-manifest.json'
if manifest.exists():
    for p,digest in json.loads(manifest.read_text(encoding='utf-8'))['files'].items():
        assert hashlib.sha256((root/p).read_bytes()).hexdigest()==digest,p
print(f'{len(cards)} cards, resource consistency, local references, private-path checks and available manifest: PASS')
