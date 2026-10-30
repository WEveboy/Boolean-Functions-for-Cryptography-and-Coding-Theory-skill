"""Replay fixed numerical assertions on saved independent task outputs; no model calls."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'docs/eval-with-skill-0.2.0.json').read_text(encoding='utf-8'))
a={record['id']:record for record in records}
tasks=json.loads((root/'docs/eval-tasks-0.2.0.json').read_text(encoding='utf-8'))
assert set(a)=={x['id'] for x in tasks}
assert a['bct-normal']['tool_result']['boomerang_uniformity']==6
assert a['trace-normal']['tool_result']['dual_basis']==[1,4,2]
assert a['trace-normal']['tool_result']['duality_matrix']==[[1,0,0],[0,1,0],[0,0,1]]
assert a['certificate-normal']['tool_result']['equivalent_under_certificate']
assert not a['certificate-boundary']['tool_result']['equivalent_under_certificate']
assert a['higher-normal']['tool_result']['distance']==1
assert a['higher-normal']['tool_result']['enumerated_codewords']==128
assert a['code-normal']['tool_result']['dimension']==3
assert a['code-normal']['tool_result']['minimum_distance']==2
assert a['code-boundary']['tool_result']['minimum_distance']==1
assert a['batch-normal']['tool_result']['completed']==2 and a['batch-normal']['tool_result']['failed']==1
for name in ('bct-boundary','trace-boundary','higher-boundary','batch-boundary'):
    assert a[name]['execution']['returncode']==2
assert all(x['answer'] for x in records)
print('12 independent v0.2 task outputs: numerical and exit-status checks PASS; semantic boundaries reviewed separately')
