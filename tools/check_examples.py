"""Run the published CLI against every bundled example and check meaningful outcomes."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

root=Path(__file__).resolve().parents[1]
cli=root/'skills/carlet-boolean-research/resources/research_core.py'
with tempfile.TemporaryDirectory() as directory:
    results={}
    for example in sorted((root/'examples').glob('*.json')):
        target=Path(directory)/(example.stem+'.json')
        subprocess.run([sys.executable,str(cli),str(example),'--out',str(target)],check=True,capture_output=True)
        result=json.loads(target.read_text(encoding='utf-8'))
        assert result['tool_version']=='0.2.0'
        assert len(result['input_sha256'])==64
        results[example.stem]=result
    assert results['quadratic-bent']['bent'] and results['quadratic-bent']['nonlinearity']==6
    assert results['gold-gf8']['ab'] and results['gold-gf8']['differential_uniformity']==2
    assert results['bct-identity']['boomerang_uniformity']==4
    assert results['trace-gf4']['dual_basis']==[3,1]
    assert results['nl2-cubic']['distance']==1
    assert results['code-identity']['dimension']==3 and results['code-identity']['minimum_distance']==2
    assert results['ccz-inverse-gf8']['equivalent_under_certificate']
    assert results['ea-identity']['equivalent_under_certificate']
    assert (results['batch-mixed']['completed'],results['batch-mixed']['failed'])==(2,1)
print(f'{len(results)} published CLI examples: PASS')
