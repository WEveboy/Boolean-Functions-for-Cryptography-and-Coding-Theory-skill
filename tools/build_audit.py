"""Produce scope accounting from reviewed extraction IDs; not an automatic truth judge."""
import hashlib
import json
import re
from pathlib import Path
from build_bundle import DATA
from extension_capabilities import DATA as EXTENSIONS

R=Path(__file__).resolve().parents[1]
B=R/'books/carlet-2021'
scope={
'T01':('representation','ANF与位序；给定EA/CCZ证书在equivalence-certificate实现，未知变换搜索未做'),
'T02':('scalar-spectrum','全谱/NL与最近仿射见证；higher-order-distance实现预算内精确高阶距离'),
'T03':('vector-metrics','全部分量/次数、DDT/见证、AB；boomerang实现置换BCT'),
'T04':('reed-muller','RM参数；higher-order-distance与function-code分别实现有限距离和秩去重重量分布'),
'T05':('quadratic-rank','次数<=2的极化秩与谱预测实现；其他低度族为参考'),
'T06':('bent-construction','MM与有限谱检验实现；其他bent族、拼接为参考'),
'T07':('resilience','有限全谱CI/韧性实现；韧性MM构造为参考'),
'T08':('propagation','SAC/PC与AC实现；EPC、有阶PC未实现'),
'T09':('algebraic-immunity','标量AI n<=6；FAI/向量AI为参考'),
'T10':('symmetry','对称、旋转对称和层计数实现；Krawtchouk等为参考'),
'T11':('field-power','小维域幂函数、DDT实现；分类与无限族新颖性未做'),
'T12':('model-review','模型假设审查及symmetry层计数；TI/FHE/PRG/Gowers算法为参考'),
'T13':('research-triage','出版时问题台账和有限研究计划；当前状态需文献核查'),
'T14':('field-power','GF(2^n)商环幂运算；field-trace-dual实现绝对迹与多项式基对偶基')}

def main():
    meta=json.loads((R/'source-manifest.json').read_text())
    research=B/'references/research'
    research.mkdir(parents=True,exist_ok=True)
    (research/'01-sources.md').write_text(f'''# 来源清单

唯一原始研究来源：Claude Carlet，Boolean Functions for Cryptography and Coding Theory，Cambridge University Press，2021。
577个PDF页；正文印刷页1–497；References始于498，Index始于557。印刷页p对应PDF第p+15页（1起算）。
用户指定PDF的SHA256：`{meta['sha256']}`。既有抽取文件源文件哈希相同，故复用14章文本而非重复OCR。文本可检索，公式仍需核原页；p.489已渲染目视核对。

来源可信度：一手数学专著；并不保证所有排印公式无误。p.489的迹线性域冲突及同书位序差别见formula-audit与counter-examples。
方法来源：本机已安装cangjie-skill v2.5，非人物扮演版仓颉。框架、原则、案例、反例、术语五类提取在3个并行槽中分两轮完成。没有原书之外的新数学结论用于冒充原书能力。

没有调用外网补充2026年数学结果；GitHub只用于目标仓库检查与上传。因此所有开放问题沿用2021历史状态，不声称已复核当前状态。
原始PDF、整章文本不进入发布目录。实际计算程序是独立实现D，方法性改写为原创说明，书中短引为来源定位B。
''',encoding='utf-8')
    (research/'02-extraction-notes.md').write_text('''# 提取记录索引

完整证据分别保存于candidates/frameworks.md（18）、principles.md（31）、cases.md（16）、counter-examples.md（16）、glossary.md及GLOSSARY.md。每条有节/页、类型、机制或区别。它们属于技术文本提取，不补造人物信念形成、心理或人生失败。案例与反例只是支持材料，不单独晋级。

两名提取器扫描14章497个正文页的结构信号，再精读候选命中位置；不是逐行证明所有定理。模型审查、研究计划为本项目受限输出契约D，源书主题与历史问题为B。候选分流见coverage-audit与references。

独立审阅发现：零函数次数D=-1，与原书p.35的0约定不同；绝对迹采用Fp线性；矩形映射delta=2不以本书APN命名；AB要求n=m且n奇数。已在卡片、使用合同和回归测试中处理。
''',encoding='utf-8')
    import yaml
    txt=(B/'candidates/frameworks.md').read_text(encoding='utf-8')
    f=yaml.safe_load(txt.split('```yaml')[1].split('```')[0])
    (research/'03-key-quotes.md').write_text('# 关键短引\n\n摘引均来自指定PDF，空格经抽取规范化；每段短引不代替完整定理条件。\n\n'+'\n\n'.join(f"## {x['id']}\n\n> {x['source_quote']}\n\n出处：{x['source_chapter']}。" for x in f),encoding='utf-8')
    table=['# 全书关键任务覆盖审计\n','“有去向”不等于“全部实现”。以下14项按原书目录先建立，再与候选及交付映射；没有把计算子集冒充全书算法。\n','|任务|卡片|实际范围|','|---|---|---|']
    for t,(s,note) in scope.items():
        table.append(f'|{t}|[cards/{s}](.cangjie/capabilities/cards/{s}.md)|{note}|')
    table += ['\n## 候选去向\n', 'framework f01/f02/f04/f05/f07/f08/f11/f12/f14/f17的限定计算部分进入对应active卡。f03/f06由0.2版equivalence-certificate/function-code承接，f09拼接、f10韧性MM、f13 Krawtchouk、f15 TI具体实现、f16受限域指标及f18问题文本的数学背景保留为reference；模型选择和历史研究计划另有受限契约。',
              'principles中P02/P05–P10/P12/P14–P16/P18–P20/P22–P25/P29/P30的已实现或核查部分由18卡承接。P01/P03/P04/P11/P13/P17/P21/P26–P28/P31，以及上述候选的未实现部分，保留于references.md及发布overview参考区。P02与f01为同一Möbius能力，合并而非再造入口。',
              'cases c01–c16只作证据与例子，counter-examples ce01–ce16进入B边界与参考区；术语统一进入glossary。候选原始证据随books发布，可从ID回查。',
              '\n## 限制\n当前状态、新族证明和全空间分类未核查，见needs-review。没有发现无去向的目录级主题；许多具体定理和构造只保留参考，不能宣称逐条公式无遗漏或所有原书算法可执行。']
    (B/'coverage-audit.md').write_text('\n'.join(table),encoding='utf-8')
    verified=['# 三重验证与晋级记录\n','V1依据：五类提取、formula-audit、card-review、code-review及v0.2-source-audit。V2纸面演练见每卡A1；实际26项任务输出另见docs评测。V3为可检查的口径统一与遗漏预防目标，未以自评证明效果提升。\n','|能力|V1|V2限定契约|V3任务价值|去向|','|---|---|---|---|---|']
    for slug,title,task,loc,rule,keys,method,ex,bound,cmd in DATA+EXTENSIONS:
        verified.append(f'|{slug}|{loc}及审阅记录|{ex}|{rule}|single内部router卡|')
    verified.append('\n独立意图/契约可成立，但这些卡共享规格与资源；采用single入口符合参考项目形态，不声称用户逐项批准了每个中间门。模型审查与研究计划只验证限定表格/计划输出，不宣称数学应用算法全实现。')
    (B/'verified.md').write_text('\n'.join(verified),encoding='utf-8')
    refs='''# 参考内容与未实现算法

以下有原书依据但本版不提供完整自动算法；保留为来源参考，不能由本页名称重建或声称已经实现。

|内容|原书定位|参考候选|可用范围|
|---|---|---|---|
|MacWilliams重量变换、设计和认证|§1.2,§3.6,§4.2|P01,f06|解释函数与码联系，需具体码定义|
|EA/CCZ未知变换搜索|§2.1 pp.27–30|f03,ce03|给定证书已实现；搜索/分类仍为参考|
|导数次数、单变量次数|§2.2 pp.38–46|P03,P04|解释次数，非族证明器|
|拼接、直接和、其他bent族|第5–6章|f09,P21|仅MM和谱检测实现|
|韧性MM、Siegenthaler|第7章|f10,P11|CI检测已实现，构造算法参考|
|FAI/FAC与向量AI|第9章|P13|标量AI不代替这些指标|
|Krawtchouk、幂等、单调函数|第10章|f13,P24|只实现对称/旋转与层计数|
|TI均匀性、FHE、局部PRG|第12章|f15,f16,P26,P27|模型审查，不做完整实现与系统证明|
|Gowers范数|§12.4|P28|需说明阶数/归一化，无自动范数工具|
|Artin–Schreier方程|第14章|f17,P30,P31|幂运算、绝对迹与对偶基已实现；一般方程求解为参考|
|历史开放问题|第13章|f18,P29|仅出版时问题与有限研究计划|

所有案例和反例见candidates，所有术语见GLOSSARY。完整提取证据随books目录发布；编译技能overview附本参考区，避免安装后失联。
'''
    (B/'references.md').write_text(refs,encoding='utf-8')
    base=(B/'BOOK_OVERVIEW.md').read_text(encoding='utf-8')
    (B/'.cangjie/capabilities/book/overview.md').write_text(base+'\n\n'+refs,encoding='utf-8')
    (B/'needs-review.md').write_text('''# 需要另行研究的项目

- 第13章每道题在2026年的状态：未联网核查，不进入“当前仍开放”的active结论。
- 新函数族的无限维证明和EA/CCZ新颖性：有限工具不能完成，需独立论文级证据。
- TI/FHE/PRG/Gowers及受限域安全：本版只做假设审查/参考，完整算法与安全验证未实现。
- 全书具体构造的穷尽覆盖：本版按14个目录级任务审计，不声称每个定理、练习或构造均已可执行化。
- 原书p.489冲突与位序不统一已记录；没有独立核实全书所有排印公式是否存在其他错误。
''',encoding='utf-8')
    (B/'rejected').mkdir(exist_ok=True)
    (B/'rejected/duplicate-mobius.md').write_text('# P02独立入口候选：去重合并\n\nP02与f01描述同一Möbius变换。保留全部来源，合入representation，不再创建第二个可发现Skill。数学内容未淘汰。',encoding='utf-8')
    (B/'PIPELINE_STATE.md').write_text('# 流水线状态\n\n0.2版包含18张能力卡；来源审阅与有限测试完成。最新使用评测、编译与交付状态见docs/VALIDATION-0.2.0.md及实际提交的CI。\n',encoding='utf-8')
    print('Wrote source records, triple verification, 14-task scope accounting and reference destinations.')

if __name__=='__main__':
    main()
