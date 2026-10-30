"""Numerical checks from the finite examples fixed before independent execution."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
a=json.loads((root/'docs/eval-with-skill.json').read_text(encoding='utf-8'))
tasks=json.loads((root/'docs/eval-tasks.json').read_text(encoding='utf-8'))
assert all(t['id'] in a and a[t['id']]['answer'] for t in tasks)
assert all(a[t['id']]['selected_capability']==t['capability'] for t in tasks)
expected={
'representation':{'anf_masks':[3],'degree':2},
'scalar-spectrum':{'walsh':[2,2,2,-2],'NL':1,'parseval_sum':16},
'vector-metrics':{'vector_balanced':False,'vector_NL':0},
'reed-muller':{'length':8,'dimension':4,'minimum_distance':4,'dual_order':1},
'quadratic-rank':{'rank':4,'predicted_nonzero_amplitude':4,'predicted_support_size':16},
'bent-construction':{'NL':6,'balanced':False},
'resilience':{'CI_order':2,'resiliency_order':2,'NL':0},
'propagation':{'AC':[4,0,0,0],'PC_order':2},
'algebraic-immunity':{'algebraic_immunity':1},
'symmetry':{'symmetric':True,'layer_sizes':[1,3,3,1],'layer_weights':[0,3,0,1]},
'field-power':{'table':[0,1,3,4,5,6,7,2],'delta':2,'permutation':True}}
for slug,values in expected.items():
    answer=a[slug+'-normal']['answer']
    for k,v in values.items():
        assert answer[k]==v,(slug,k,answer[k],v)
assert len(a['negative_triggers'])==3
assert all(not x['invoke_skill'] for x in a['negative_triggers'].values())
b=json.loads((root/'docs/eval-without-skill.json').read_text(encoding='utf-8'))
assert all(t['id'] in b and b[t['id']]['answer'] for t in tasks)
print('With skill: 26 answers, 26 routes, 11 numerical cases, 3 negative triggers PASS; baseline: 26 answers present. Semantic judgments are recorded separately.')
