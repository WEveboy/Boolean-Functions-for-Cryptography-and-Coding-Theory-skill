# 案例提取候选池

提取日期：2026-10-30。来源：Claude Carlet, *Boolean Functions for Cryptography and Coding Theory* (2021)，用户指定的577页PDF；下列页码为印刷页，PDF页码加15（1起算）。原书实例是数学演示或文献转述，不是作者个人经历。

取材方式：对 `tmp/study/ch01.txt` 至 `ch14.txt` 的 Example / Table / for instance / Maiorana / Gold / majority 等锚点检索，并回读命中处完整页及邻页；本候选池是代表性案例提取，不宣称穷尽原书全部算例。表格抽取易错列，最终数值实现应回查PDF页面或另行复算。第13章本身主要列问题，仅提取其具体构造示范，不把问题表当已完成案例。

## c01 Hamming码与simplex码的具体联系

- type: case
- example_kind: worked_example
- source_chapter: §1.2，p.8（PDF23）
- source_quote: “The dual of the binary Hamming code is called the simplex code.”
- 输入与条件：取所有非零m位列组成H，m≥2；对应二元Hamming码长2^m−1。
- summary：没有零列和相同列，排除一列及两列依赖；存在三个相加为零的不同非零列，最小距离为3。H同时是simplex对偶码生成矩阵，其码字是所有线性函数在非零输入的取值表。
- bound_to: 校验矩阵列依赖与最小距离；函数真值表到码字
- outcome：原书给出距离3和对偶解释。取m=3得到[7,4,3]属于由原书规则实例化，不是另一个原书数值例题。
- 边界：列顺序影响具体码字表示；等价码参数相同不意味矩阵相同。

## c02 三变量真值表的原子函数分解

- type: case
- example_kind: worked_example
- source_chapter: §2.2.1，pp.31–32（PDF46–47）
- source_quote: “It is the sum (modulo 2 or not, no matter) of the atomic functions”
- 输入与条件：p.31表采用x1为最高位的十六进制输入编号；函数仅在1、5、7处取1。
- summary：把支撑点各自写为Dirac指示函数，再用F2上的展开化简得到ANF；“modulo 2 or not”只适用于这些互不相交的原子支撑，不能推广到任意函数之和。
- bound_to: 真值表→ANF；支撑集分解
- outcome：展示函数可以由单点指示函数构成。确切展开应使用p.32或二元Möbius变换核对。
- 边界：与表2.1的低位在左位序不同，两个例子不能直接共用整数到坐标映射。

## c03 同一四变量函数的双向Möbius变换和Walsh变换

- type: case
- example_kind: worked_example
- source_chapter: §2.2.1 表2.1 p.35；§2.3.2 算法2、表2.2 pp.55–56（PDF50,70–71）
- source_quote: “Truth table and Walsh spectrum of f”
- 输入与条件：f=x1x2x3⊕x1x4⊕x2；表格整数序号的第一个坐标x1为最低位，x∈F2^4。
- summary：表2.1把真值表经二元Möbius变换变为ANF再变回；表2.2把符号向量(−1)^f经加减蝶形变换得到未归一化Walsh谱。
- bound_to: 表示转换；FWHT；位序审计
- outcome：两种变换作用于不同的对象、使用不同的加法。表2.2显示最大绝对Walsh系数8；结合p.57距离公式及p.79非线性定义可推出NL=8−8/2=4（此NL数值是跨公式复算，不冒充表中的原文结论）。
- 边界：不能把0/1真值表的普通Hadamard变换当作符号Walsh变换。

## c04 实用S盒的不同输入输出规格

- type: case
- example_kind: reported_case
- source_chapter: §3.5.1，pp.142–143（PDF157–158）
- source_quote: “Examples of S-boxes used in practice”
- 输入与条件：原书列举(4,4) PRESENT等、(6,4) DES、(8,8) AES等；此处仅记录本书时代的实例。
- summary：设计需求取决于网络：SPN要求双射；Feistel中的S盒可有不同输入输出维。实现效率与物理防护需求也参与选择。
- bound_to: S盒输入合同；攻击模型→指标选择
- outcome：这些实际应用证明不能把n=m、置换性或单一最优指标硬套到所有S盒任务。
- 边界：书中列出名字不代表此仓库实现或重新审计了对应密码系统；没有提供完整真值表的案例不能自动当计算回归输入。

## c05 小维RM覆盖半径表：精确值与区间并存

- type: case
- example_kind: worked_example
- source_chapter: §4.1.6，表4.1，p.158（PDF173）
- source_quote: “Lower and upper bounds on the covering radii of Reed–Muller codes for small n.”
- 输入与条件：以(r,n)索引RM(r,n)，不是码长n；码长为2^n。
- summary：表中r=1、n=4为6，n=8为120；n=9给242–244，展示表内既有精确值也有上下界。
- bound_to: 高阶非线性度↔RM距离；上下界状态记录
- outcome：对于n=4，最大普通非线性度6；n=9的区间只能作为出版时知识，不能包装成精确分类。
- 边界：该表具有时效性；印刷表的错列风险要求回看页面。不能把覆盖半径当码的最小距离。

## c06 二次对称bent函数的具体模型

- type: case
- example_kind: worked_example
- source_chapter: §6.1，p.206（PDF221）；配套§5.2.1 pp.170–171
- source_quote: “The elementary quadratic symmetric Boolean function”
- 输入与条件：n为正偶数，σ2(x)=⊕_{i<j}x_i x_j。
- summary：原书把其极化形式的核化为对每个i均有⊕_{j≠i}x_j=0；偶数n使核仅为零，得到bent性。
- bound_to: 二次极化秩；bent构造；对称函数检验
- outcome：产生一个有可证明bent性的对称二次函数族。小维数值核验应由工具另行计算，并标明是独立复算。
- 边界：偶数维是证明条件；不能把σ2在任意n上都称作bent。

## c07 Maiorana–McFarland原始构造及对偶

- type: case
- example_kind: worked_example
- source_chapter: §6.1.15，公式(6.9)–(6.10)、命题77，p.209（PDF224）
- source_quote: “Any function of the form (6.9) is bent if and only if π is a permutation.”
- 输入与条件：n=2k；x,y∈F2^k；π:F2^k→F2^k；g为任意k变量布尔函数。
- summary：令f(x,y)=x·π(y)⊕g(y)。对x求和将Walsh系数的支持限制在π的相应原像；π为置换时原像恰为一个点，所有谱绝对值为2^k。
- bound_to: MM bent构造；谱证书；对偶恢复
- outcome：原书给出对偶 f~(a,b)=b·π^{-1}(a)⊕g(π^{-1}(a))，可用全谱符号复算。
- 边界：输入分成等长两部分；不等长推广不能沿用“π为置换”的同一判据。取π=id,g=0是该公式的合成实例化；具体4变量真值表不声称由原书列出。

## c08 由线性码生成相关免疫函数

- type: case
- example_kind: worked_example
- source_chapter: §7.1，推论22，p.292（PDF307）
- source_quote: “Corollary 22 Let C be any (linear) [n, k, d]-code”
- 输入与条件：二元线性[n,k,d]码C，满行秩生成矩阵G，任意k变量g。
- summary：f(x)=g(xG^t)，由对偶距离/陪集的均匀投影性质得到(d−1)阶相关免疫；g平衡时f为(d−1)阶韧性。
- bound_to: 码→相关免疫；相关免疫与平衡的区分
- outcome：原书提供通用演示和证明；若要生成小维实例，矩阵与g必须另行明确，并核验低重量掩码的零谱。
- 边界：不能丢掉满秩和g平衡条件；不能从相关免疫直接推断韧性。

## c09 Dobbertin构造在传播准则上的失败边界

- type: case
- example_kind: worked_example
- source_chapter: §8.1，p.319（PDF334），回引公式(7.9) p.296
- source_quote: “Dobbertin’s construction cannot produce functions satisfying PC(l) with l≥n/2.”
- 输入与条件：书中Dobbertin构造及其公式(7.9)；n为该构造的偶数输入维数。
- summary：选前n/2位为零、后n/2位为一的u，构造的谱在所有w⪯u处均为零，与命题129要求的平方谱和非零值矛盾。
- bound_to: 构造可行性预筛；PC与高非线性度的区分
- outcome：给出明确的不可达参数区，而不是以构造名推断任意传播阶都可实现。
- 边界：是针对指定构造的否定结果，不是对所有函数的PC(l)不可行证明。

## c10 Majority最优AI仍有非线性及FAA弱点

- type: case
- example_kind: worked_example
- source_chapter: §9.1，p.335及后续分析pp.336–337（PDF350–352）
- source_quote: “It has two main weaknesses: its nonlinearity is weak”
- 输入与条件：f(x)=1当wt(x)≥n/2，否则0；奇数n时阈值等于(n+1)/2。
- summary：原书通过低重量输入上的零化条件与ANF系数关系，说明其AI最优；同时明确非线性较低及快速代数攻击抵抗差。奇数维时平衡，偶数维时不能照搬平衡结论。
- bound_to: AI零化子证书；多指标筛选；阈值函数
- outcome：是“最优AI不等于密码学全面优秀”的具体反例。小维AI=ceil(n/2)可由另写工具验证，不冒充书中有具体真值表。
- 边界：不把“最优”理解为全指标最优；也不把作者的历史评价自动当成现实密码系统攻击结论。

## c11 九变量旋转对称搜索超越二次界

- type: case
- example_kind: reported_case
- source_chapter: §10.2，pp.360–361（PDF375–376）
- source_quote: “a 9-variable function of nonlinearity 241 could be found”
- 输入与条件：原书引文献[684,686]中的9变量旋转对称搜索；二次界为240，覆盖半径上界244。
- summary：以受限对称族压缩搜索空间，找到超越二次界的实例，再通过与二次函数的直接和得到11变量NL=994及13变量NL=4036的实例。
- bound_to: 对称族搜索；直接和；实例与最优值的区分
- outcome：证明二次界并非普遍最优界。书中下一页还说明九变量旋转对称族最优241与更广义族得到242的区别，应保留搜索域标签。
- 边界：本段未提供完整9变量真值表，因此不能标为仓库已重现实验；不能从族内最优宣称全空间最优。

## c12 Gold幂函数的APN证明与奇偶条件

- type: case
- example_kind: worked_example
- source_chapter: §11.4.1 p.394；§11.5.2 p.400（PDF409,415），表11.2
- source_quote: “The proof that these functions are APN (whatever is the parity of n) is easy”
- 输入与条件：F(x)=x^(2^i+1)定义于F_(2^n)，gcd(i,n)=1；具体域模型用于计算时必须另给。
- summary：利用幂函数缩放，研究步长1的导数；同一导数值对应x,y满足(x+y)^(2^i)=x+y，互素条件使x+y仅为0或1，故每个差分方程至多两个解。
- bound_to: 有限域APN构造；差分方程计数；参数条件审计
- outcome：APN不要求n奇数；原书§11.4.1给奇数n下的Gold AB族。参数i的表格范围用于去除等价重复，不能误作APN成立的全部必要条件。
- 边界：偶数n时不能继承奇数维AB或置换结论。F=x^3、n=3或4是适合计算测试的合成实例化，不声称原书列出其真值表。

## c13 逆函数的奇数维APN与偶数维4均匀

- type: case
- example_kind: worked_example
- source_chapter: §11.5.2，pp.400–401（PDF415–416）
- source_quote: “admits four solutions (the elements of F4) if b=1”
- 输入与条件：F(x)=x^(2^n−2)，非零点为乘法逆，F(0)=0；n≥2。
- summary：导数步长1的端点x=0,1与其余点分别处理；其余解满足x²+x=1/b。b=1时，是否额外存在两解由tr_n(1)控制。
- bound_to: 逆映射差分谱；零点分支；奇偶维条件
- outcome：奇数n为APN；偶数n在b=1有四个解，因此差分均匀度4。此结论解释逆函数S盒为什么不自动成为APN。
- 边界：不能对0直接计算1/0；实现必须明确0映到0。

## c14 受限输入AI可能下降，也可能上升

- type: case
- example_kind: worked_example
- source_chapter: §12.2，p.464（PDF479）
- source_quote: “but it may also increase the algebraic immunity”
- 输入与条件：取(n−1)变量f且AI(f)≥2，扩展f'(x,0)=f(x)、f'(x,1)=0；限制域E=F2^(n−1)×{0}。
- summary：整体函数f'有低次数零化子（最后一位），故AI(f')=1；限制到E后该零化子在E上恒零，按受限AI定义不合法，因此AI_E(f')=AI(f)≥2。多数函数则在固定重量层上恒定，展示相反的退化方向。
- bound_to: 受限域零化子；输入模型变化；非零性检查
- outcome：限制输入并不具有AI单调下降定理；必须在E上检查零化子非零，不能只要求全空间非零。
- 边界：保留受限定义及原书假设；不能用全空间AI工具的结果直接充当固定重量层AI。

## c15 GF(4)与GF(27)算术例题

- type: case
- example_kind: worked_example
- source_chapter: §14.1 pp.481–482；§14.2 p.484（PDF496–497,499）
- source_quote: “we conclude that the inverse of x²+1 is x²+x.”
- 输入与条件：GF(4)=F2[X]/(X²+X+1)，α为X的像；另一个独立例题GF(27)=F3[X]/(X³+2X²+1)。
- summary：GF(4)加乘表把加法形式1+α与乘法形式α²接通，α²=α+1且α³=1。GF(27)例题通过扩展Euclidean算法求X²+1的逆，得到X²+X。
- bound_to: 有限域规格；多项式约减；逆元证书
- outcome：两例均有明确输入、约减多项式和可核验输出；GF(27)必须按模3算术，不可复用仅支持二元域的XOR工具。
- 边界：GF(4)的不可约多项式与GF(27)的不可约多项式不能混用；域同构不意味相同整数标签下乘法表相同。

## c16 第13章非二次bent函数的仿射导数示范

- type: case
- example_kind: worked_example
- source_chapter: §13.3 问题14，pp.476–477（PDF491–492）
- source_quote: “take a quadratic bent function g in n−6 variables and a cubic bent function h in 6 variables”
- 输入与条件：偶数n≥6，g为n−6变量二次bent；六变量h是原书给出的MM函数x1y1⊕x2y2⊕(x1x2⊕x3)y3。
- summary：通过不相交变量的直接和，展示具有至少2^(n−3)个不同仿射导数的非二次bent函数；这只是开放问题前的下界示范。
- bound_to: 直接和；高阶结构；实例下界与最优值区分
- outcome：提供2^(n−3)这个可达到数量；原书并未据此给出一般最大值。
- 边界：不要把第13章问题视为已解决；n=6时零变量g需按常数约定处理，计算器若不支持零变量应改用n≥8实例。

## 对下游A1的使用说明

本池16条候选未执行三重筛选，也未宣称每条都应成为独立能力。c03、c06、c07、c08、c10、c12、c13、c14、c15适合提供可检验数学实例或边界；c04、c11是文献/应用转述，缺具体真值表的部分不能用作数值回归已通过的证据。所有工具输出均须另留执行日志。引文只是定位锚点，规则以被标明的完整页及前提为准。
