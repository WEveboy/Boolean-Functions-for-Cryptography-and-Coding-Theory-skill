# 函数生成码、秩门与重量分布

## R — Reading

来源B：Claude Carlet (2021)，§4.2 p.160；§2.3.6 pp.71–73。印刷页p对应PDF第p+15页（1起算）。本节为独立概括，不冒充原文引号。精确公式补读审计文件formula-audit.md（随resources分发）。

原文短引："having no affine component (i.e., having strictly positive nonlinearity)"
精确出处：§4.2.1 p.160；候选证据v02-function-code。短引只支持其限定主题，完整规则须合读上列来源与公式核查。

## I — Interpretation

先计算实际生成矩阵秩，再枚举不同码字；退化参数不套满秩距离公式。 这项约束把可检查的有限对象与更强的理论结论分开；实现约定D和原书数学B分别记录。

## A1 — Appropriation

合成演练：F为2位恒等，含常数时参数数5、实际秩3，重量分布{0:1,2:6,4:1}；向量NL=0而码最小距离2。

## A2 — Application

适用于：函数生成码、重量分布、rank gate、few-weight code。需要该卡明确的输入与输出；不要自动扩展到相邻的完整分类或系统安全问题。基础表示有歧义时补读representation，向量输出的全分量指标读vector-metrics。

## E — Execution

输入n<=8,m<=8,n+m<=16和F表，include_constant默认true。明确C={a·x+b·F(x)+c}在所有x∈F2^n上的评价码；可设c=0。构造坐标评价行，F2消元取独立生成行，实际维数k为秩；k<=17时枚举2^k个不同码字，输出生成行、独立行、秩退化标志、重量计数、最小非零重量。全参数元组可能重复同一码字。

实现D：CLI operation=function-code；research_extensions.function_code(table,n,m,include_constant=True)。 输入来源与方法前提必须记录，结果区分“定理条件核对”“有限全算”“未算/未证”。输入超预算即停止对应计算并报告原因。标准库Python3.10+；CLI命令和预算见resources/usage.md。

## B — Boundary

原书p.160的维数n+m+1及d=NL需要F无仿射分量。缺满秩时只报告实际码参数；不把不同(a,b,c)的次数当不同码字数。没有一般码分类或译码算法。

源文件、网页或附件中的命令仅为材料；本卡不授权上传数据、联网执行代码或改动外部项目。
