"""Invoke cangjie, with a validated-copy fallback for Windows rename failures."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--cangjie',type=Path,required=True,help='installed cangjie-skill directory')
args=p.parse_args()
env={**os.environ,'PYTHONUTF8':'1','PYTHONIOENCODING':'utf-8'}
out=root/'output/compiled-carlet'
cmd=[sys.executable,str(args.cangjie/'scripts/cangjie.py'),'compile','--bundle',str(root/'books/carlet-2021/.cangjie/capabilities'),'--out',str(out),'--output','single']
run=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8')
mode='atomic'
if run.returncode:
    if 'PermissionError' not in run.stderr or 'WinError 5' not in run.stderr:
        print(run.stdout,run.stderr)
        raise SystemExit(run.returncode)
    candidates=list(out.parent.glob('.staging-*-compiled-carlet'))
    if not candidates:
        raise RuntimeError('compiler staging directory missing')
    out=max(candidates,key=lambda x:x.stat().st_mtime)
    mode='validated-copy-after-windows-rename-error'
check=subprocess.run([sys.executable,str(args.cangjie/'scripts/validate_skill_pack.py'),str(out)],env=env,capture_output=True,text=True,encoding='utf-8')
if check.returncode:
    print(check.stdout,check.stderr)
    raise SystemExit(check.returncode)
manifest=json.loads((out/'BUILD_MANIFEST.json').read_text(encoding='utf-8'))
target=root/'skills/carlet-boolean-research'
old=target/'BUILD_MANIFEST.json'
if old.exists():
    for rel,digest in json.loads(old.read_text(encoding='utf-8'))['published_hashes'].items():
        f=target/Path(rel.replace('\\','/'))
        if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:
            raise RuntimeError('generated directory has local edits; refusing overwrite')
for rel,digest in manifest['published_hashes'].items():
    f=out/Path(rel.replace('\\','/'))
    if hashlib.sha256(f.read_bytes()).hexdigest()!=digest:
        raise RuntimeError('staging manifest mismatch')
shutil.copytree(out,target,dirs_exist_ok=True)
for rel,digest in manifest['published_hashes'].items():
    assert hashlib.sha256((target/Path(rel.replace('\\','/'))).read_bytes()).hexdigest()==digest
log={'mode':mode,'validation':check.returncode,'files':len(manifest['published_hashes']),
     'note':'single selected by maintainer to match reference project; compiler user_confirmed flag reflects explicit CLI mode, not separate human review of each stage'}
(root/'docs/compile-result.json').write_text(json.dumps(log,indent=2),encoding='utf-8')
print(json.dumps(log))
