import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
tasks=[
('representation','输入n=2，x_i是整数x的第i位，表[0,0,0,1]，求ANF掩码与次数。','输入n=3，但只给表[0,1,0,1]，应如何处理？'),
('scalar-spectrum','n=2，表[0,0,0,1]，给完整未归一化Walsh谱、NL和Parseval平方和。','LAT表只写“2”没有归一化定义，能否直接作Walsh系数使用？'),
('vector-metrics','n=m=2，表[0,3,0,3]，求全部非零分量的平衡性与向量NL。','某4位S盒只检测了4个坐标函数，都平衡，是否足以判定向量平衡？'),
('reed-muller','求RM(1,3)长度、维数、最小距离、对偶阶数。','有人把RM最小距离4解释为所有8位向量到码的最大距离4，指出问题。'),
('quadratic-rank','n=4，f=x0*x1 XOR x2*x3，给极化秩和非零谱幅度、支撑大小。','n=3，f=x0*x1*x2，能直接套二次极化谱公式吗？'),
('bent-construction','k=2，pi=[0,1,2,3]，g=[0,0,0,0]，求MM构造的NL、平衡性。','k=2，pi=[0,0,1,2]，能引用MM置换构造保证bent吗？'),
('resilience','n=3，f=x0 XOR x1 XOR x2，给相关免疫阶数、韧性阶数和NL。','常零函数应称n阶韧性函数吗？'),
('propagation','n=2，f=x0*x1，给AC全表和PC阶数。','一个函数满足SAC，是否可不检查就宣布满足PC(n)？'),
('algebraic-immunity','n=2，f=x0，给AI及一个非零零化子的ANF。','给n=7函数，能否使用包内AI工具宣称精确结果？若无该工具，也说明精确枚举需预算。'),
('symmetry','n=3，f=输入重量奇偶，给对称性和各重量层大小、层内1数。','完整域上AI为2，限制到一个重量层后是否必然AI<=2？说明是否需要区分受限函数非零条件。'),
('field-power','GF(8)模X^3+X+1，F=x^3，求整数顺序0..7真值表、delta和置换性。','有人用X^3+1作GF(8)模多项式，请检查是否合法。'),
('model-review','只提供“8位S盒delta=4”，目标是阈值实现侧信道安全，请给假设审查表和缺失证据。','只有S盒数学指标，能否宣布毛刺环境下一定侧信道安全？'),
('research-triage','围绕原书§13.6问题16，给一个有限候选搜索计划，写清何种结果可声称以及文献核查义务。','能否凭2021年的第13章断言问题截至2026年仍开放？')]
cases=[]
for slug,normal,bound in tasks:
    cases.extend([dict(id=slug+'-normal',capability=slug,prompt=normal),dict(id=slug+'-boundary',capability=slug,prompt=bound)])
(root/'docs/eval-tasks.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),encoding='utf-8')
trigger=[dict(id='trigger-'+s,type='should_trigger',prompt=n,expected_behavior='route to '+s) for s,n,b in tasks]
trigger += [dict(id='negative-'+str(i),type='should_not_trigger',prompt=q,expected_behavior='do not invoke this skill') for i,q in enumerate(['帮我写生日祝福','修改这份旅游日程','给我的网页按钮改颜色'])]
(root/'books/carlet-2021/test-prompts.json').write_text(json.dumps({'skill':'carlet-boolean-research','version':'0.1.0','test_cases':trigger},ensure_ascii=False,indent=2),encoding='utf-8')
print('Prepared 26 output tasks and 16 routing prompts; no expected numerical answers in task pack.')
