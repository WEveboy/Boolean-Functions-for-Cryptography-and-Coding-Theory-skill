# 使用合同 v0.2.0

Python 3.10+标准库，无需网络。资源目录相对已安装技能目录定位；输出写用户工作目录。实现D为本项目独立编写，理论B来自Carlet 2021，H为待证假设。

CLI：`python <skill>/resources/research_core.py spec.json --out result.json`。
输入JSON：`{"n":2,"m":1,"table":[0,0,0,1]}`。m默认1；x的第i位表示x_i，输出同理。输出包含完整输入规格、规范化规格SHA256及有限全算标记。SHA256用于一致性核对，不是身份认证。文件原字节变化可能不改变规范化规格哈希。

标量n<=10；向量n<=8、m<=8、n+m<=16；精确AI仅n<=6。预算在执行前拒绝，避免把未完成搜索误报为通过。二次极化只用于次数<=2。函数API（可用importlib加载resources/research_core.py）：

|API|输入与输出|
|---|---|
|anf(table)|真值表↔ANF系数，两次应用还原|
|scalar(table,n)|Walsh、快速AC、NL、最近仿射见证、CI/PC失败方向、平衡、次数、韧性、bent/plateaued|
|vector(table,n,m)|全部分量谱/次数、最弱掩码、NL、DDT/解见证、delta、APN/AB、vectorial bent、置换性|
|quadratic(table,n)|极化矩阵、GF(2)秩、谱幅度与支撑预测|
|mm(k,pi,g)|2k变量MM函数表，k<=5|
|rm(r,n)|RM参数，0<=r<=n<=20|
|immunity(table,n)|AI及非零零化子ANF证书，n<=6|
|field_power(n,mod,d)|多项式基幂函数表，先验证域模型，n<=8,d>=1|
|symmetry(table,n)|对称/旋转对称及重量层统计|

零函数次数D约定-1（原书p.35约定0）；常函数相关免疫可达n但不具韧性。plateaued采用非零Walsh绝对幅度唯一的口径，包括仿射函数。PC忽略零方向。APN与AB按本书采用n=m，AB还要求n为奇数；矩形函数不使用该标签。自相关使用FWHT(W²)/2^n精确计算，时间O(n*2^n)。

## 扩展命令

所有命令仍使用同一CLI；JSON设置operation，省略时保持原analyze行为。扩展输出含完整输入、SHA256、操作名和工具版本。基础分析的规范化规格哈希保留旧定义，新增扩展的哈希涵盖完整JSON输入，二者不混作同一格式。

|operation|必填字段|预算和输出|
|---|---|---|
|boomerang|n,table|n<=8且为置换；完整BCT、均匀度及(a,b)解见证；排除a=0或b=0求最大|
|field-trace|n,modulus|n<=8；不可约正整数模多项式；迹表、多项式基与对偶基、单位配对核验|
|higher-order|n,table,r|n<=8；0<=r<=n；一般枚举RM维数<=16；若输入已属于RM，直接返回0及ANF证书|
|function-code|n,m,table|n<=8,n+m<=16；include_constant默认true；实际秩、不同码字重量分布及最小距离|
|ea-certificate|n,m,table,target,input_rows,output_rows|n<=8,n+m<=16；可选add_rows/input_offset/output_offset/add_offset|
|ccz-certificate|n,m,table,target,graph_rows|n<=8,n+m<=16；可选offset；图按x+(F(x)<<n)编码|
|batch|jobs|1..32个非嵌套任务；逐项结果/错误与completed/failed计数；不因一项错误丢弃其余结果|

矩阵为整数行掩码：第i输出位是parity(rows[i]&x)，不是原书行向量记法。EA精确验证G(x)=Aout(F(Ain(x))) XOR L(x)，offset分别在对应输出端异或。格式或秩非法是输入错误；合法证书逐点不成立返回false和见证。一个证书失败不代表函数不等价。

示例：`{"operation":"field-trace","n":2,"modulus":7}`；`{"operation":"higher-order","n":3,"r":2,"table":[0,0,0,0,0,0,0,1]}`。完整范例见resources/examples.json及仓库examples目录。

函数码精确定义为全部输入上的C={a·x+b·F(x)+c}，先取生成行实际秩再枚举，参数重复不重复计码字。只有含常数且F无仿射分量等原书p.160前提满足时才能套维数n+m+1及d=NL；退化情形报告实际结果。

不实现：全部原书构造族、预算外高阶距离、未知EA/CCZ变换搜索与分类、DLCT/FAI、向量AI、TI安全验证、受限域NL/AI。相应参考内容不等于软件已实现。第13章仅保留出版时状态；查询当前状态需另行联网核查。

测试：仓库根目录运行 `python -m unittest discover -s tools -p "test_*.py" -v`。来源检查、有限算法测试与独立Agent使用评测分别记账；历史0.1版new/without评测及本版新增评测见docs，不宣称统计显著的提升比例。
