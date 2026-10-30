# 全书关键任务覆盖审计

“有去向”不等于“全部实现”。以下14项按原书目录先建立，再与候选及交付映射；没有把计算子集冒充全书算法。

|任务|卡片|实际范围|
|---|---|---|
|T01|[cards/representation](.cangjie/capabilities/cards/representation.md)|ANF完整有限实现；EA/CCZ关系参考保留，无证书检查器|
|T02|[cards/scalar-spectrum](.cangjie/capabilities/cards/scalar-spectrum.md)|全谱/NL实现；最近仿射由全谱手工读取|
|T03|[cards/vector-metrics](.cangjie/capabilities/cards/vector-metrics.md)|全部分量与DDT实现；AB谱条件手工核验|
|T04|[cards/reed-muller](.cangjie/capabilities/cards/reed-muller.md)|RM参数实现；其他函数生成码、一般高阶距离为参考|
|T05|[cards/quadratic-rank](.cangjie/capabilities/cards/quadratic-rank.md)|次数<=2的极化秩与谱预测实现；其他低度族为参考|
|T06|[cards/bent-construction](.cangjie/capabilities/cards/bent-construction.md)|MM与有限谱检验实现；其他bent族、拼接为参考|
|T07|[cards/resilience](.cangjie/capabilities/cards/resilience.md)|有限全谱CI/韧性实现；韧性MM构造为参考|
|T08|[cards/propagation](.cangjie/capabilities/cards/propagation.md)|SAC/PC与AC实现；EPC、有阶PC未实现|
|T09|[cards/algebraic-immunity](.cangjie/capabilities/cards/algebraic-immunity.md)|标量AI n<=6；FAI/向量AI为参考|
|T10|[cards/symmetry](.cangjie/capabilities/cards/symmetry.md)|对称、旋转对称和层计数实现；Krawtchouk等为参考|
|T11|[cards/field-power](.cangjie/capabilities/cards/field-power.md)|小维域幂函数、DDT实现；分类与无限族新颖性未做|
|T12|[cards/model-review](.cangjie/capabilities/cards/model-review.md)|模型假设审查及symmetry层计数；TI/FHE/PRG/Gowers算法为参考|
|T13|[cards/research-triage](.cangjie/capabilities/cards/research-triage.md)|出版时问题台账和有限研究计划；当前状态需文献核查|
|T14|[cards/field-power](.cangjie/capabilities/cards/field-power.md)|GF(2^n)商环幂运算实现；迹和对偶基算法为参考|

## 候选去向

framework f01/f02/f04/f05/f07/f08/f11/f12/f14/f17的限定计算部分进入对应active卡。f03等价证书、f06一般函数生成码、f09拼接、f10韧性MM、f13 Krawtchouk、f15 TI具体实现、f16受限域指标及f18问题文本的数学背景保留为reference；模型选择和历史研究计划另有受限契约。
principles中P02/P05–P10/P12/P14–P16/P18–P20/P22–P25/P29/P30的已实现或核查部分由13卡承接。P01/P03/P04/P11/P13/P17/P21/P26–P28/P31，以及上述候选的未实现部分，保留于references.md及发布overview参考区。P02与f01为同一Möbius能力，合并而非再造入口。
cases c01–c16只作证据与例子，counter-examples ce01–ce16进入B边界与参考区；术语统一进入glossary。候选原始证据随books发布，可从ID回查。

## 限制
当前状态、新族证明和全空间分类未核查，见needs-review。没有发现无去向的目录级主题；许多具体定理和构造只保留参考，不能宣称逐条公式无遗漏或所有原书算法可执行。