# 原则与计算口径候选池

提取器：principle-extractor；日期：2026-10-30。唯一来源为 Claude Carlet《Boolean Functions for Cryptography and Coding Theory》(2021)，来源 ID `carlet-2021`。按14章497个正文印刷页作全量页结构扫描（逐页识别定义、定理、命题、表格、脚注信号），再精读下列命中页；不宣称逐一复证全部定理或穷尽每条公式。PDF页号为印刷页号+15，均为1起算。以下是候选而非已完成三重验证的能力。公式为规范化转写；引号内仅为短原文。

共同字段：`type=calculation`（特别注明者除外）；单位均为比特数、整数计数或无量纲概率；所有输入/输出有限集合的顺序必须显式固定。缺失条件不可从名称猜测。未在本文件执行算法，预期可核对实例不是“实测通过”。

## P01 线性码重量枚举器的对偶变换

- 来源：§1.2 pp.14–16，MacWilliams identity (1.1)。原文锚点：“Some authors call weight enumerator”。
- inputs：有限域大小q、线性码C、码长N、各重量计数A_i。
- formula：W_C(X,Y)=Σ_i A_i X^(N−i)Y^i；W_(C⊥)(X,Y)=|C|^(−1) W_C(X+(q−1)Y,X−Y)。
- output：对偶重量计数；核对总数q^(N−dim C)、A_0=1、系数为非负整数。
- missing_conditions / boundary：必须线性且明确同一基域；一般非线性码不能直接套用线性码对偶公式。函数变量数n不是码长N。

## P02 Möbius变换连接真值表与ANF

- 来源：§2.2.1 p.33，Theorem 1，(2.4)；p.34顺序警告。原文：“The converse is also true”。
- inputs：n和按坐标字典序排列的2^n个比特。
- formula：a_I=⊕_(supp(x)⊆I) f(x)。同一二元Möbius变换反向恢复真值表。
- output：平方自由ANF、最高非零项次数、往返一致性。
- boundary：运算在F₂；按输入重量排序的表不能直接送入字典序蝶形算法；零函数次数约定由实现另标。

## P03 导数的次数下降

- 来源：§2.2.1 pp.38–39，Definition 7、Proposition 5、Corollary 1。原文：“Algebraic degree and derivation”。
- inputs：布尔函数f、方向a及必要时k个方向。
- formula：D_a f(x)=f(x)⊕f(x+a)；deg(D_a f)<deg(f)（f非恒定）；k次导数在deg(f)≥k时次数≤deg(f)−k。
- output：导数真值表及次数证书。
- boundary：这是有限差分，不是形式多项式微分；重复或相关方向可能使导数更早归零，不能声称等号总成立。

## P04 单变量表示的二进制重量次数

- 来源：§2.2.2 pp.45–46，Propositions 6–7。原文：“has algebraic degree”。
- inputs：F_(2^n)中约化的单变量多项式及非零系数位置。
- formula：代数次数为非零项指数的最大二进制重量；非零迹单项式tr_n(a x^k)次数为w₂(k)，须遵守原文指数/迹轨道口径。
- output：代数次数与约化表示。
- boundary：先合并同类项及迹轨道抵消；零函数不能套非零迹单项式结论。普通多项式次数不是代数次数。

## P05 统一Walsh的符号和归一化

- 来源：§2.3.2 p.55，Definition 16，(2.32)。原文：“the sign function”。
- inputs：f∈BF_n、非退化内积与掩码u。
- formula：W_f(u)=Σ_x(−1)^(f(x)⊕u·x)；W_f=2^n δ_0−2 f̂，其中f̂是对0/1值f的Fourier–Hadamard变换。
- output：全部2^n个整数谱值及归一化说明。
- boundary：不能把对0/1值函数的变换当成Walsh；概率、相关系数、Walsh整数三种量不能混报。

## P06 平衡、重量和最近仿射函数

- 来源：§2.3.2 p.57，(2.35)、(2.37)；§3.1.3 p.79，Definition 18、(3.1)。原文：“minimum Hamming distance”。
- inputs：完整Walsh谱。
- formula：wt(f)=2^(n−1)−W_f(0)/2；NL(f)=2^(n−1)−max_u|W_f(u)|/2；d(f,u·x⊕c)=2^(n−1)−(−1)^c W_f(u)/2。
- output：重量、平衡性、NL及达到最小距离的(u,c)。
- boundary：最大值含零掩码；计算离散距离不用浮点取整掩盖错误。

## P07 Parseval与逆变换作为计算核对

- 来源：§2.3.3 pp.59–61，Corollaries 4–5，(2.42)、(2.48)。原文：“Parseval’s relation for Walsh transform”。
- inputs：按同一内积排列的完整谱。
- formula：Σ_u W_f(u)^2=2^(2n)；Σ_u W_f(u)(−1)^(u·x)=2^n(−1)^f(x)。
- output：精确整数校验及恢复的符号表。
- boundary：Parseval只是必要校验，不能单凭平方和宣称任意整数向量为某函数的Walsh谱；逆变换还要只取±1。

## P08 自相关与平方Walsh谱

- 来源：§2.3.3 p.62，(2.53)–(2.54)。原文：“the autocorrelation function”。
- inputs：f或完整Walsh谱。
- formula：AC_f(a)=Σ_x(−1)^(f(x)⊕f(x+a))=2^(−n)Σ_u W_f(u)^2(−1)^(u·a)。
- output：全部方向AC及直接导数计数对拍。
- boundary：a=0的值固定为2^n；绝对指标取非零方向，不能把零方向混入最大值。

## P09 全分量向量Walsh与平衡判据

- 来源：§2.3.6 p.71；§3.2.1 pp.112–113；§3.2.3 p.117。原文：“every value ... the same number”（此锚点为定位短语，省略号非连续引文）。
- inputs：F:F₂^n→F₂^m、输入与输出内积。
- formula：W_F(u,v)=Σ_x(−1)^(v·F(x)⊕u·x)。F平衡 iff W_F(0,v)=0 对所有v≠0；NL(F)=min_(v≠0) NL(v·F)。
- output：全部2^m−1个非零分量的谱、最弱分量及输出原像计数。
- boundary：只测m个坐标不充分；平衡要求m≤n；m=n时等价于置换。

## P10 相关免疫与韧性的零谱条件

- 来源：§3.1.4 p.87，Theorem 5；§7.1 p.284。原文：“Golomb–Xiao–Massey characterization”。
- inputs：f、n、目标t∈[0,n]。
- formula：t阶CI iff W_f(u)=0 对1≤wt(u)≤t；t-resilient iff 对wt(u)≤t全部为0。
- output：CI阶数、是否平衡、韧性阶数或最低重量非零谱掩码。
- boundary：CI不自动平衡，常函数可以CI；未平衡时不能给出非负韧性阶数。

## P11 Siegenthaler的次数与韧性约束

- 来源：§7.1.2 pp.285–286，Proposition 117。原文：“The Siegenthaler bound states”。
- inputs：n、t、是否CI/韧性。
- formula：t-CI时wt(f)被2^t整除、deg(f)≤n−t；t-resilient且t≤n−2时deg(f)≤n−t−1；t=n−1时deg(f)≤1。
- output：参数可行性诊断。
- boundary：不能将n−t−1公式不加条件地用于t=n−1；必要界不提供构造或完整安全证明。

## P12 零化子矩阵计算AI

- 来源：§3.1.5 pp.91–92，Proposition 25及M_(f,d)；§9.1 p.321，Definition 73。原文：“nonzero annihilators”。
- inputs：f、n、次数预算d。
- formula：AI(f)=min{deg(g):g≠0, fg=0或(f⊕1)g=0}。列为次数≤d单项式、行分别为supp(f)及supp(f⊕1)，元素u^I；GF(2)非零核向量给出零化子。
- output：最小d及非零g的ANF，并逐点验证乘积为0。
- boundary：必须两侧都检查；若仅找到d次见证而未排除低次，只能给AI≤d，不能称精确值。

## P13 AI上界与FAI口径分开

- 来源：p.92，Proposition 26；pp.321–322，Definition 73。原文：“fast algebraic immunity”。
- inputs：f及AI(f)。
- formula：AI(f)≤min(deg(f),ceil(n/2))；FAI(f)=min(2AI(f), min_(1≤deg(g)<AI(f)) [deg(g)+deg(fg)])。
- output：AI上界、FAI的搜索域及所得见证。
- boundary：AI最优不意味着FAI最优；AI≤1时内层为空的实现约定需明确，不能报程序的空集最小值为实际数值。FAC与FAI在p.322分别定义，不能混用。

## P14 DDT差分均匀度

- 来源：§3.4.1 p.135，Definition 40、(3.37)。原文：“difference distribution table”。
- inputs：F及n,m。
- formula：DDT[a,b]=#{x:F(x)⊕F(x+a)=b}；δ(F)=max_(a≠0,b) DDT[a,b]；最大单步差分概率δ/2^n。
- output：DDT、δ、最大值见证(a,b)、每行和2^n。
- boundary：零输入差分必须从δ最大值排除；a≠0时计数为偶数。低δ不是整套密码安全结论。

## P15 APN与AB的不同判据

- 来源：p.137，Definition 41；p.119，Definition 31；pp.371–372，Propositions 156–157。原文：“The converse ... is false in general”（省略号表示非连续定位）。
- inputs：F:F₂^n→F₂^n、DDT及全分量谱。
- formula：APN iff 对a≠0所有DDT值为0或2；奇数n的AB要求各非零分量Walsh值属于{0,±2^((n+1)/2)}。奇数维AB⇒APN，反向一般不成立。
- output：两个性质分别判定及失败见证。
- boundary：不可从APN名字推置换性；AB的奇数维口径不可搬到偶数维。

## P16 Reed–Muller参数和高阶距离

- 来源：§4.1 pp.151–152，Definition 42、Theorem 7；§4.1.6 pp.156–158。
- 原文：“The codes have then length ... and not n”（非连续定位；完整含数学式见原页）。
- inputs：0≤r≤n。
- formula：RM(r,n)的码长2^n、维数Σ_(i=0)^r C(n,i)、最小距离2^(n−r)；NL_r(f)=min_(g∈RM(r,n)) d_H(f,g)。
- output：参数及距离的证明/穷举状态。
- boundary：最小距离是码内距离；覆盖半径是对所有f的最坏最近距离；不能相互替代。一般高阶精确距离有指数开销。

## P17 RM最小重量词的几何识别

- 来源：§4.1.1 p.154，Theorem 8。原文：“indicators ... dimensional flats”（非连续定位）。
- inputs：次数r且重量2^(n−r)的布尔函数。
- formula：其支撑为(n−r)维仿射子空间；反向，余维r仿射空间指示函数具有该次数和重量。
- output：仿射空间基、平移、维数及逐点支撑一致性。
- boundary：重量相同但没有次数前提不能判成flat；支撑空集不适用。

## P18 二次函数由极化核计算谱幅

- 来源：§5.2.1 pp.170–173，Proposition 55、Dickson form。原文：“its associated symplectic form”。
- inputs：次数≤2的f。
- formula：B_f(x,y)=f(0)⊕f(x)⊕f(y)⊕f(x+y)；若其核E_f维k，则非零Walsh幅为2^((n+k)/2)；W_f(a)≠0 iff (f⊕a·x)|E_f为常数。
- output：极化矩阵、偶数秩r=n−k、谱支撑及幅。
- boundary：核上f可为非恒定线性限制，不能只看“核维数”判f本身是否平衡。次数>2不能套双线性秩公式。

## P19 bent的谱和导数等价判据

- 来源：§6.1 pp.190–192，Lemma 5、Theorem 12；p.80上界。
- 原文：“Characterization of bentness by the derivatives”。
- inputs：偶数n及f。
- formula：bent iff 全部|W_f(u)|=2^(n/2)，iff 每个a≠0的D_a f平衡；NL=2^(n−1)−2^(n/2−1)。
- output：全谱/全导数证书、重量2^(n−1)±2^(n/2−1)。
- boundary：bent不能平衡；n=2的次数例外与一般n/2次数界需分开（p.190）。

## P20 Maiorana–McFarland带前提构造

- 来源：§5.1.1 pp.165–166的一般形式；§6.1.15 p.209，(6.9)、Proposition 77；p.206二次MM例。
- 原文锚点（p.209）：“π is any permutation”。
- inputs：x,y∈F₂^k、置换π、函数h。
- formula：f(x,y)=x·π(y)⊕h(y)；Proposition 77给出此形式bent iff π为置换，h可为任意k变量布尔函数。对偶为f*(a,b)=b·π⁻¹(a)⊕h(π⁻¹(a))。
- output：构造及Walsh直接求和证明、π的置换检验、对偶谱核验。
- boundary：输入必须等分成两个k位块；p.209脚注8明确不等长分块时不能用同一置换充要判据。p.206的二次例不能被当作任意h下仍二次的承诺。本次已补读p.209原始类，来源缺口解决。

## P21 partially-bent与plateaued不混同

- 来源：§6.2.1 p.256，Proposition 94、Definition 62；§6.2.2 pp.258起。
- 原文：“either balanced or constant”。
- inputs：AC与Walsh的非零支撑。
- formula：|supp(AC)|·|supp(W)|≥2^n；等号当且仅当所有导数均平衡或常数，称partially-bent。
- output：两个支撑大小、乘积及全部导数分类。
- boundary：plateaued的谱仅有0和单一非零绝对幅并不自动推出partially-bent；此候选只执行已定位p.256的等号判据。

## P22 向量bent存在维数门

- 来源：§6.4 pp.268–269，Proposition 104。原文：“exist if and only if”。
- inputs：n,m≥1及目标性质。
- formula：bent(n,m)存在 iff n偶数且m≤n/2；等价地每个非零分量bent，或每个非零方向导数向量映射平衡。
- output：参数可行性及各分量证书。
- boundary：n=m的正维置换不可能向量bent；不能要求所有坐标bent就停止检查其余分量。

## P23 SAC与PC(l)

- 来源：§8.1 pp.318–319，Definition 71、Proposition 129。
- 原文：“Strict avalanche criterion”。
- inputs：f、l∈[1,n]。
- formula：PC(l) iff AC_f(a)=0 对1≤wt(a)≤l；SAC=PC(1)。
- output：最大传播阶数、失败方向及导数重量。
- boundary：只测试单比特方向只证明SAC；SAC不等于差分均匀度最优或整套密码雪崩性质。

## P24 对称函数简化向量和Lucas判据

- 来源：§10.1 pp.352–354，(10.2)及初等对称函数段。
- 原文：“depends then only on the Hamming weight”。
- inputs：n+1位简化值向量v_k或初等对称次数i。
- formula：f(x)=v_(wt(x))；σ_i(x)=C(wt(x),i) mod2=1 iff i的二进制1位被wt(x)覆盖。
- output：真值表、重量Σ_k v_k C(n,k)、ANF/谱核验。
- boundary：对称函数低成本表示不保证密码安全；固定重量层上对称函数必为常数，不能宣称保持全域指标。

## P25 Gold幂函数与逆函数的维数条件

- 来源：§11.5.2 p.400 Table 11.2；p.401逆函数段。
- 原文：“Known APN exponents”。
- inputs：域F_(2^n)模型、指数i、n。
- formula：Gold d=2^i+1，在gcd(i,n)=1时APN；逆函数x^(2^n−2)在奇数n为APN，在偶数n差分均匀度4（零点延拓须显式）。
- output：域多项式、真值表、DDT证书及满足的定理前提。
- boundary：表格是2021年已知族；有限维实验不证明无限族；指数写法不能丢掉n或gcd前提。

## P26 TI的correctness、noncompleteness与uniformity

- type：checklist；来源：§12.1.3 pp.437–441，Definition 86、Proposition 189。
- 原文：“correctness and incompleteness”。
- inputs：原函数F及t+1个输入/输出share函数。
- formula/规则：输出share异或须等于F(输入share异或)；每个输出函数满足规定noncompleteness；uniformity按p.440纤维计数另验；t-mask TI要求deg(F)≤t。
- output：三项分别核查的模型内结论和缺失实现假设。
- boundary：不能把正确重组或次数门当作uniformity充分条件；不从数学检查直接宣称实际电路对glitch安全。

## P27 受限输入的平衡与非线性

- 来源：§12.2.2 pp.457–459，Definition 89、Proposition 192。
- 原文：“weightwise perfectly balanced”。
- inputs：明确集合E（例如En,k={x:wt(x)=k}）、f|E。
- formula：wt(f|En,k)=#{x∈En,k:f(x)=1}；在非端点层平衡要求该计数=C(n,k)/2；NL_E(f)=min_(a,c)#{x∈E:f(x)≠a·x⊕c}。
- output：各层大小、重量、偏差、限制距离。
- boundary：奇数层大小不能精确平衡；WPB另要求f(0)=0及f(1)=1（p.457）；全域平衡甚至(n−1)-resilience不保证固定重量层平衡。

## P28 Gowers范数采用均匀期望

- 来源：§12.4 pp.470–473，Definition 90、Proposition 198、Corollary 32。
- 原文：“expectation in uniform probability”。
- inputs：实值ϕ或符号函数(−1)^f；k<n。
- formula：||ϕ||_(U^k)^(2^k)=E_(x,a1,...,ak) ∏_(S⊆[k])ϕ(x+Σ_(i∈S)ai)。符号函数可由k次导数的符号均值计算。
- output：均值、范数与对次数≤k−1符号函数的相关上界。
- boundary：0/1函数f和符号函数fχ的范数不同；不可漏除均匀平均因子；特征2下不能无条件套用未经修正的逆猜想。

## P29 出版时开放问题保留时间标签

- type：principle；来源：第13章 pp.475–479。
- 原文：“In this chapter, we list open problems”。
- inputs：问题编号、2021年陈述与拟研究参数。
- 规则：保存原始问题、已知条件和书内出处；任何“现仍开放/首次解决”说法另行查最新一手文献与等价性。
- output：历史问题台账和当前状态`未核查`。
- boundary：这条时效处理规范是蒸馏者的D类维护约定，不伪称作者预见2026年研究状态。书内小例和计算不能替代文献查新。

## P30 有限域模型与绝对迹

- 来源：§14.2 pp.483–486；§14.3 pp.488–489。
- 原文：“an Fp-linear form over the space Fq”。
- inputs：不可约多项式p(X)、基、域元素编码及n。
- formula：F_(2^n)=F₂[X]/(p(X))；tr_n(x)=Σ_(j=0)^(n−1)x^(2^j)∈F₂；tr是F₂线性，tr_n(ax)在a≠0时为非零线性形式。
- output：不可约性核查、迹表、基/对偶基及可复算表示。
- boundary：不可约不等于本原；p.489首段“linear over Fq”与同页后文冲突，规范内容采用同页明确的Fp线性表述，详见formula-audit。

## P31 域二次方程的迹门

- 来源：§14.5 p.495，Equations of degree 2定理。
- 原文：“A necessary and sufficient condition”。
- inputs：β∈F_(2^n)、域模型。
- formula：x²+x=β有解 iff tr_n(β)=0；有解时两解相差1。
- output：可解性及逐点代回的两个解，或无解证书tr=1。
- boundary：特征2、指定域内的结论；不能混同在扩域中求解或把普通整数二次公式搬来。

## 扫描覆盖与候选限制

第1章P01；第2章P02–P08/P30；第3章P06/P09/P10/P12–P15；第4章P16–P17；第5章P18/P20；第6章P19–P22；第7章P10–P11；第8章P23；第9章P12–P13；第10章P24；第11章P15/P25；第12章P26–P28；第13章P29；第14章P30–P31。本表说明14章均参与候选发现，不等于所有小节已实现。复杂族表、CCZ分类、FHE系统、PRG安全和一般高阶距离尚未成为本提取器的可执行交付。
