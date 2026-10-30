"""Allowlist publication, exclude source books/caches and emit hashes plus Git tree entries."""
import hashlib
import json
import re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
files=[]
for name in ['README.md','AGENTS.md','LICENSE','.gitignore','source-manifest.json']:
    files.append(root/name)
for name in ['.github','docs','tools','examples','skills/carlet-boolean-research','books/carlet-2021']:
    for f in (root/name).rglob('*'):
        if not f.is_file() or f.suffix in ('.pyc','.pdf') or '__pycache__' in f.parts:
            continue
        rel=f.relative_to(root).as_posix()
        if '/.cangjie/runs/' in rel or '/.cangjie/snapshots/' in rel:
            continue
        if f.is_symlink():
            raise ValueError('symlink not permitted')
        files.append(f)
manifest={'version':'0.1.0','hash_algorithm':'SHA256','files':{}}
entries=[]
for f in sorted(set(files)):
    rel=f.relative_to(root).as_posix()
    content=f.read_text(encoding='utf-8')
    if re.search(r'[A-Z]:[\\/](?:Users|Program Files)',content):
        raise ValueError('private path detected: '+rel)
    if f.suffix in ('.txt','.pdf'):
        raise ValueError('raw source not permitted: '+rel)
    manifest['files'][rel]=hashlib.sha256(f.read_bytes()).hexdigest()
    entries.append(dict(path=rel,mode='100644',type='blob',content=content))
mf=root/'release-manifest.json'
mf.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
entries.append(dict(path='release-manifest.json',mode='100644',type='blob',content=mf.read_text(encoding='utf-8')))
(root/'tmp/upload-tree.json').write_text(json.dumps(entries,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'files':len(entries),'text_bytes':sum(len(e['content'].encode()) for e in entries)}))
