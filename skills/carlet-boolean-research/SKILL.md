---
name: carlet-boolean-research
description: |
  基于Claude Carlet专著的布尔函数与向量函数研究：ANF、Walsh、RM、bent、APN、韧性、传播和代数免疫；提供有限真值表精确核验及来源边界。适用于构造分析、条件核对和研究规划，不证明系统安全或自动完成分类。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.carlet-boolean-research
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# Boolean Functions for Cryptography and Coding Theory — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 一般译码、完整EA/CCZ分类、系统安全证明；未提供的BCT/DLCT/FAI算法。

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 先固定n、m、真值表位序和域模型；按意图读一张能力卡。
2. 区分B原书、D独立实现、H猜想；有限全算不冒充无限族证明。
3. 向量性质检查所有非零分量；置换、APN、AB和平衡各自核验。
4. 命令和预算见resources/usage.md；结果写用户工作目录。
5. 第13章仅表示出版时状态；当前开放性和新颖性另查一手文献。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 表示、位序与ANF | references/capabilities/representation.md | — |
| Walsh谱与非线性度 | references/capabilities/scalar-spectrum.md | references/capabilities/representation.md |
| 全部分量、DDT与S盒指标 | references/capabilities/vector-metrics.md | references/capabilities/representation.md |
| Reed–Muller距离与码参数 | references/capabilities/reed-muller.md | references/capabilities/representation.md |
| 二次极化秩与谱支撑 | references/capabilities/quadratic-rank.md | references/capabilities/representation.md |
| 构造并核验bent与plateaued | references/capabilities/bent-construction.md | references/capabilities/representation.md |
| 相关免疫与韧性阶数 | references/capabilities/resilience.md | references/capabilities/representation.md |
| 自相关、SAC与传播准则 | references/capabilities/propagation.md | references/capabilities/representation.md |
| 代数免疫与零化子证书 | references/capabilities/algebraic-immunity.md | references/capabilities/representation.md |
| 对称族与受限输入核查 | references/capabilities/symmetry.md | references/capabilities/representation.md |
| 有限域模型与APN幂函数实验 | references/capabilities/field-power.md | references/capabilities/representation.md |
| 攻击模型与实现假设审查 | references/capabilities/model-review.md | references/capabilities/representation.md |
| 历史开放问题与证据分级 | references/capabilities/research-triage.md | references/capabilities/representation.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 缺规格时先补齐；超预算或定理前提不满足时报告未算/未证。
