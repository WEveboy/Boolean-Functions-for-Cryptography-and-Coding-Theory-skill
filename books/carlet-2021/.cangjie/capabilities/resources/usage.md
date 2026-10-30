# 使用合同 v0.1.0

Python 3.10+标准库，无需网络。资源目录相对已安装技能目录定位；输出写用户工作目录。实现D为本项目独立编写，理论B来自Carlet 2021，H为待证假设。

CLI：`python <skill>/resources/research_core.py spec.json --out result.json`。
输入JSON：`{"n":2,"m":1,"table":[0,0,0,1]}`。m默认1；x的第i位表示x_i，输出同理。输出包含完整输入规格、规范化规格SHA256及有限全算标记。SHA256用于一致性核对，不是身份认证。文件原字节变化可能不改变规范化规格哈希。

标量n<=10；向量n<=8、m<=8、n+m<=14；精确AI仅n<=6。预算在执行前拒绝，避免把未完成搜索误报为通过。二次极化只用于次数<=2。函数API（可用importlib加载resources/research_core.py）：

|API|输入与输出|
|---|---|
|anf(table)|真值表↔ANF系数，两次应用还原|
|scalar(table,n)|Walsh、AC、NL、平衡、次数、CI、韧性、PC、bent、plateaued|
|vector(table,n,m)|全部非零分量谱、NL、DDT、delta、平衡、置换性|
|quadratic(table,n)|极化矩阵、GF(2)秩、谱幅度与支撑预测|
|mm(k,pi,g)|2k变量MM函数表，k<=5|
|rm(r,n)|RM参数，0<=r<=n<=20|
|immunity(table,n)|AI及非零零化子ANF证书，n<=6|
|field_power(n,mod,d)|多项式基幂函数表，先验证域模型，n<=8,d>=1|
|symmetry(table,n)|对称/旋转对称及重量层统计|

零函数次数D约定-1（原书p.35约定0）；常函数相关免疫可达n但不具韧性。plateaued采用非零Walsh绝对幅度唯一的口径，包括仿射函数。PC忽略零方向。AB需在奇数n下另核全部非零分量的谱值集合。CLI不自动输出AB、最近仿射见证或PC失败掩码，需按能力卡从完整谱/AC读取。

不实现：所有原书构造族、一般高阶距离、EA/CCZ搜索或分类、BCT/DLCT、FAI、向量AI、TI安全验证、受限域NL/AI、迹/对偶基计算。相应主题的定理、模型审查或参考定位不等于软件已实现。第13章仅保留出版时状态；查询当前状态需另行联网核查。

测试：仓库根目录运行 `python -m unittest discover -s tools -p "test_*.py" -v`。来源检查、有限算法测试与独立Agent使用评测分别记账；本项目未做宿主new/without随机对照，不宣称提升比例。
