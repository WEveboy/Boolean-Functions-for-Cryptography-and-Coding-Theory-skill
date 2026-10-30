# 框架与流程候选池

来源统一为 src-carlet-2021，Claude Carlet《Boolean Functions for Cryptography and Coding Theory》(2021)。印刷页 p 对应用户 PDF 第 p+15 页（1 起算）。以下是候选，不代表已通过后续三重验证。英文摘引按文本层整理空格，不修补数学符号；公式以独立释义给出。

```yaml
- id: f01
  title: 真值表与ANF的二元Möbius变换
  type: procedure
  task: T01
  source_chapter: §2.2.1 pp.33–35，Theorem 1、Algorithm 1及位序备注
  source_quote: "There exists a simple divide-and-conquer butterfly algorithm to compute the ANF from the truth table (or vice versa)"
  summary: 以平方自由单项式的掩码为索引，通过子集异或变换在真值表和ANF系数表间转换；变换为自身的逆。
  inputs: n、长度2^n的二进制表、坐标到掩码的位序
  outputs: ANF系数表、非零单项式与代数次数、往返核对
  steps: 固定置换字典序；每一位将未包含该位的系数异或到包含该位的系数；重复全部n位；再次变换核对输入。
  missing_conditions: 无；实现需明确常零函数次数约定，不冒充原书规定。
  boundary: 按输入重量排序不能直接套蝶形算法；非二元输出应先逐坐标处理。
  tags: [representation, mobius, algorithm]
- id: f02
  title: 快速Walsh谱到最近仿射逼近
  type: procedure
  task: T02
  source_chapter: §2.3.1–2.3.3 pp.53–61；§3.1.3 p.79式(3.1)
  source_quote: "The nonlinearity can be computed through the Walsh transform"
  summary: 先将f转换为符号表(-1)^f，再作和差蝶形；最大绝对谱值给出非线性度，谱值符号给出最佳仿射常数项。
  inputs: n、完整二进制真值表、内积与位序
  outputs: W_f(a)全表、Parseval核验、NL及一个最近仿射函数
  steps: 在整数上计算和差蝶形；检验ΣW²=2^(2n)；计算NL=2^(n-1)-max|W|/2；对达到最大值的a按W符号选择常数项并直接计算距离。
  missing_conditions: 无；FFT不是复数离散傅里叶库的默认归一化。
  boundary: 不把f本身的Fourier变换当作符号函数的Walsh；结果取决于约定的内积及坐标顺序。
  tags: [spectrum, nonlinearity, algorithm]
- id: f03
  title: EA及给定CCZ变换的等价性核验
  type: procedure
  task: T01
  source_chapter: §2.1 pp.27–30，Definition 5
  source_quote: "This may be a huge work."
  summary: 在宣称构造新颖前明确保留目标性质的等价关系；EA检验仿射复合，CCZ检验图像的可逆仿射映射。
  inputs: F、G、维数及给定EA或图像仿射变换
  outputs: 变换的可逆性、逐点恒等式或失败见证；允许仅给不变量排除证据
  steps: 核验线性部分秩；EA计算L'∘F∘L+L''是否等于G；CCZ把全部(x,F(x))映射后检查集合是否等于G图像。
  missing_conditions: 找到未知变换的通用搜索流程不由本候选提供。
  boundary: 不变量相同不能证明等价；不同谱可能排除等价但不是完整分类；行向量与列向量约定要显式转置。
  tags: [equivalence, certificate, novelty]
- id: f04
  title: 从全部非零分量分析向量函数
  type: framework
  task: T03
  source_chapter: §2.3.6 pp.71–73；§3.2.1 p.112；§3.2.3 pp.117–119
  source_quote: "its component functions v·F, v≠0, are all balanced"
  summary: 把每个非零输出掩码v作用于F形成标量分量；平衡要求全部分量平衡，向量非线性度取全部分量的最小值。
  inputs: n、m、F的完整映射表、输入输出位序
  outputs: 各分量谱与非线性度、最弱掩码、输出原像计数
  steps: 遍历1≤v<2^m；生成v·F并作谱分析；核验输出频数与全分量零频谱的平衡结论相符；报告最小NL及其掩码。
  missing_conditions: 无。
  boundary: 仅测m个坐标不足；m>n时不存在均匀满输出分布；分量最小次数不同于向量代数次数。
  tags: [vectorial, component, spectrum]
- id: f05
  title: 导数方程计数与APN证书
  type: procedure
  task: T03/T11
  source_chapter: §3.4.1 pp.134–137；第11章 pp.369–424
  source_quote: "the equation F(x)+F(x+a)=b has 0 or 2 solutions"
  summary: 对全部非零输入差a统计导数输出b的原像数，最大表项是差分均匀度；n到n映射最大值2时为APN。
  inputs: n、m、完整F表
  outputs: DDT、delta、达到最大值的(a,b)、置换性独立结论
  steps: 对每个a≠0和x计算F(x) XOR F(x XOR a)；累加计数；核验每行和2^n且计数为偶数；取最大值并保留解集合。
  missing_conditions: 无；无限族APN性仍需证明全部维数上的方程性质。
  boundary: 不能从抽样零失败推出APN；APN不自动意味着置换，AB结论另需输入维数与谱条件。
  tags: [differential, apn, certificate]
- id: f06
  title: 函数生成码的秩门与谱重量翻译
  type: procedure
  task: T04
  source_chapter: §4.2 pp.159–161
  source_quote: "having no affine component (i.e., having strictly positive nonlinearity)"
  summary: 用列(1,x,F(x))生成扩展函数码；码字对应v·F(x)+u·x+epsilon，重量可从Walsh值求出。
  inputs: n、m、F表、是否加入全1行
  outputs: 生成矩阵实际秩、重量分布、实际参数；前提成立时标注[2^n,n+m+1,NL(F)]
  steps: 构造生成矩阵并作F2消元；先检验无仿射非零分量；按重量=2^(n-1)-(-1)^epsilon W_F(u,v)/2计数；独立核验不同参数是否映为同一码字。
  missing_conditions: 若有仿射分量，标准维数和距离公式不能直接套用，需退到实际码计算。
  boundary: 定义集构造的维数也要求支持集满秩；穷举参数的重复不能重复计入重量枚举器。
  tags: [code, rank, weight]
- id: f07
  title: 二次函数的极化核控制Walsh幅值
  type: procedure
  task: T05
  source_chapter: §5.2.1 pp.170–175，Proposition 55、Corollary 9、Proposition 57
  source_quote: "Ef is the radical of the quadratic form."
  summary: 对代数次数至多2的函数，极化B(x,y)=f(x+y)+f(x)+f(y)+f(0)为交错双线性型；其核维数k给出非零谱幅2^((n+k)/2)。
  inputs: 二次ANF或完整表、n
  outputs: 极化矩阵、偶数秩r、核基、谱支撑及幅值预期、NL
  steps: 先确认次数≤2；按标准基求极化矩阵；F2消元求秩r与k=n-r；检查W(a)非零当且仅当f(x)+a·x在核上常值；用幅值2^(n-r/2)核验全谱。
  missing_conditions: 无。
  boundary: 高次数函数不能套用双线性型秩公式；核维数决定幅值但不独自决定谱符号或平衡性。
  tags: [quadratic, rank, spectrum]
- id: f08
  title: Maiorana–McFarland bent构造及对偶
  type: procedure
  task: T06
  source_chapter: §6.1.15 pp.209–210，Proposition 77
  source_quote: "Any function of the form (6.9) is bent if and only if π is a permutation."
  summary: 在2r变量上构造f(x,y)=x·π(y)+g(y)；π为r位置换时Walsh幅恒2^r，对偶为b·π^(-1)(a)+g(π^(-1)(a))。
  inputs: r、π表、g的r变量表、内积约定
  outputs: f表、π逆表、bent谱证书、对偶表与双对偶核对
  steps: 核验π为置换；按公式生成f；全谱核对幅值2^r；按谱符号及显式逆公式分别求对偶并比较。
  missing_conditions: 无。
  boundary: x和y不等长时双射条件不是本定理的充要条件；bent不平衡，不能直接当流密码平衡组合器。
  tags: [bent, construction, dual]
- id: f09
  title: 拼接与直接和的谱组合
  type: procedure
  task: T06/T07
  source_chapter: §6.1.16 pp.232–234；§6.2.6 p.265；§7.1.9 pp.298–299，式(7.11)
  source_quote: "the truth table of h can be obtained by concatenating the truth tables of f and g"
  summary: 直接和的Walsh谱相乘；拼接h(x,z)=(1+z)f(x)+zg(x)的谱为W_f(a)+(-1)^bW_g(a)，据此核验bent、plateaued或韧性继承条件。
  inputs: f、g完整表与维数，组合方式
  outputs: 新函数表、组合谱预测、直接全谱交叉核验
  steps: 固定变量分块；直接和使用独立输入，拼接使用同一输入及选择位；先按对应谱恒等式预测；再实算新表谱并检验目标性质。
  missing_conditions: 无；更复杂Rothaus或间接和必须另读其全部初始函数条件。
  boundary: 拼接不等于直接和；两个任意bent函数的拼接不自动bent；提升韧性阶数还需t+1重量处谱抵消。
  tags: [secondary-construction, concatenation, spectrum]
- id: f10
  title: 用输出掩码重量设计韧性MM函数
  type: procedure
  task: T07
  source_chapter: §7.1.8 p.293，式(7.4)–(7.5)
  source_quote: "if every element in φ(Fs2) has Hamming weight strictly larger than t, then fφ,g is t-resilient"
  summary: 令n=r+s且f(x,y)=x·φ(y)+g(y)；将φ像限制在重量>t的r位向量，保证低重量输入谱为零且平衡。
  inputs: r、s、t、φ表和g表
  outputs: f表、φ像重量检查、0≤wt(u)≤t的零谱证书
  steps: 检查r,s>0且t<r；核验φ每个输出重量>t；构造f；计算低重量Walsh值，包括零掩码；报告至少t阶韧性而非擅称精确阶数。
  missing_conditions: 无；允许重量等于t的推广需检查各对应纤维上的g平衡。
  boundary: 相关免疫不包含平衡；严格重量条件是充分条件，不能用于否定所有不满足该条件的函数。
  tags: [resilient, construction, low-weight-spectrum]
- id: f11
  title: 传播准则的导数平衡检验
  type: procedure
  task: T08
  source_chapter: §3.1.7 pp.96–98；§8.1 p.318
  source_quote: "Strict avalanche criterion (SAC) corresponds to PC(1)"
  summary: 对所有1≤wt(a)≤l的方向a，要求导数D_af平衡；自相关和为零即为相应方向通过。
  inputs: n、f表、目标l
  outputs: 按方向导数重量、自相关、PC(l)结论与失败方向
  steps: 限定1≤l≤n；遍历规定重量方向；统计f(x)+f(x+a)为1的数量；核验恰为2^(n-1)并汇总最小失败重量。
  missing_conditions: 无；PC(l)的order k是另一个参数，不与l混淆。
  boundary: SAC仅检查重量1；标量传播不能替代S盒完整差分分析；不能把SAC等同于bent。
  tags: [propagation, autocorrelation, sac]
- id: f12
  title: 零化子评估矩阵计算代数免疫
  type: procedure
  task: T09
  source_chapter: §9.1.1–9.1.2 pp.321–328；尤其pp.325,328关于Mf,k与RM信息集
  source_quote: "the matrix obtained by selecting those columns of G corresponding to the elements of the support of f has full rank"
  summary: 按次数d列出平方自由单项式，在f=1及f=0的输入上分别求评估矩阵核；最先出现非零核向量的d是AI。
  inputs: n、完整二进制f表、资源预算
  outputs: AI、零化目标f或f+1、非零零化子ANF、较低次数满秩证书
  steps: 从d=0向上增加；分别在两个支持集上构造单项式评估矩阵；求F2核；发现非零g后全点核验gf=0或g(f+1)=0；证明所有较低次数无核后才称精确AI。
  missing_conditions: 精确矩阵算法为原书评估秩判据的独立实现；书中不提供本项目具体资源上限。
  boundary: 必须检查f与f+1两侧；最优AI不保证抵抗快速代数攻击；balanced且n奇数时才可用p.328单侧优化。
  tags: [algebraic-immunity, annihilator, linear-algebra]
- id: f13
  title: 对称函数的简化向量与Krawtchouk谱
  type: procedure
  task: T10
  source_chapter: §10.1.1–10.1.3 pp.352–355，式(10.3)
  source_quote: "Its output depends then only on the Hamming weight of the input"
  summary: 使用长度n+1的重量值向量表述对称函数；二元子集变换得到简化ANF向量；Krawtchouk和给出各掩码重量的谱。
  inputs: n、简化值向量v[0..n]
  outputs: 简化ANF系数、代数次数、权重、按频率重量分组的Walsh谱
  steps: 计算epsilon_i=⊕_(r子掩码i)v_r；取最高非零i；用Σ_r v_r C(n,r)求重量；用Σ_r (-1)^v_r K_(n,r)(j)求重量j的Walsh值，并以C(n,j)为重数检验Parseval。
  missing_conditions: 无；式中越界二项式取0为实现约定。
  boundary: 对称性不等于旋转对称；n+1参数的族搜索不能证明所有布尔函数中的最优性；p.352明确指出系统使用可能引入特殊弱点。
  tags: [symmetric, krawtchouk, representation]
- id: f14
  title: Gold函数用归一化差分方程证明APN
  type: procedure
  task: T11/T14
  source_chapter: §11.5.2 pp.399–400；§11.4 p.394的Gold类；§14.5 pp.494–495
  source_quote: "since i and n are coprime"
  summary: 对F(x)=x^(2^i+1)，a≠0时令x=az，将导数方程归约为z^(2^i)+z=c；gcd(i,n)=1时核恰为F2，所以每个非空纤维有两个解。
  inputs: n、i、明确的F_(2^n)模型
  outputs: gcd条件、线性化导数证明、有限维DDT证书、置换性另验
  steps: 检查gcd(i,n)=1；展开F(x+a)+F(x)并作尺度变换；通过Frobenius固定域得到核大小2；枚举小维真值表独立核验DDT。
  missing_conditions: 当前开放性或新颖性不由本候选决定。
  boundary: 不把APN自动当成AB；不把幂函数表示不同当作CCZ不等价；n偶数时Gold APN通常不为置换。
  tags: [gold, apn, finite-field, proof]
- id: f15
  title: 阈值实现的正确性和非完备性构造
  type: procedure
  task: T12
  source_chapter: §12.1.4 pp.437–440；尤其p.439显式单项式分配流程
  source_quote: "This way guarantees both correctness and noncompleteness."
  summary: 对次数≤t的F，以t+1份输入分享替换每个输入变量并展开ANF；每个展开单项式缺少至少一种分享索引，将它分配给相应输出分享。
  inputs: F的ANF、t、t+1份分享规则
  outputs: 分享函数F_j、异或恢复正确性、各F_j缺失指定分享的非完备性、均匀性单独结果
  steps: 用分享异或代替输入；展开并约去重复项；把各单项式分配到不含其索引的输出分享；检验ΣF_j=F(Σ输入分享)及指定变量不出现；另行枚举合法输入分享的输出分布。
  missing_conditions: 只凭该分配法不能保证uniformity；实际电路glitch与组合安全也需独立条件。
  boundary: 不宣称由正确性和非完备性自动得到任意阶SCA安全；均匀性未证时只能报告结构核验。
  tags: [threshold-implementation, masking, bounded-procedure]
- id: f16
  title: 受限输入域上重新定义密码指标
  type: framework
  task: T12
  source_chapter: §12.2.2 pp.456–465，尤其pp.456,464–465
  source_quote: "the input to f has constant Hamming weight"
  summary: 先根据密码和攻击确定真实输入集E，再在E上重算平衡偏置、仿射逼近与零化子；不能用全空间指标替代切片上的性能。
  inputs: f、非空输入集合E或切片重量k、输入分布
  outputs: E的规格与大小、受限重量和NL、AI_E证书或矩阵秩界
  steps: 明确E与概率分布；在E上枚举仿射函数并求最小距离；AI_E检验零化条件时额外要求g在E上不恒零；用受限单项式评估矩阵核验。
  missing_conditions: 原书公式主要针对均匀E；非均匀分布需独立定义加权量，不冒称同一定理。
  boundary: 全域高AI可能在切片上降为0；受限AI也可能升高，不能无条件声称单调下降；E可能随攻击变化。
  tags: [restricted-domain, fhe, evaluation]
- id: f17
  title: 有限域商环运算、迹及二次方程的构造链
  type: procedure
  task: T14
  source_chapter: §14.2 pp.483–484；§14.3.1 p.489；§14.5 pp.494–495
  source_quote: "the usual addition and with the multiplication mod f(x)"
  summary: 用不可约多项式构造F2[X]/(p)，按Frobenius平方和计算绝对迹；x²+x=beta的可解性由迹0刻画。
  inputs: n、不可约模多项式、基及位编码、beta
  outputs: 加乘与迹表、迹值校验、方程解或无解证书
  steps: 检验模多项式次数及不可约性；异或加法与模约减乘法；tr(x)=Σ_(j=0..n-1)x^(2^j)；检验迹属于F2；若tr(beta)=1则无解，否则求一解并核验另一解为x+1。
  missing_conditions: 选primitive element仅在乘法指数表需要；不可约不等于本原。
  boundary: 域模型不同的整数真值表不能直接比较；迹配对与坐标内积的掩码对应需对偶基；书p.489的线性描述应以Fp线性为准，不解释为一般Fq线性。
  tags: [finite-field, trace, quadratic-equation]
- id: f18
  title: 研究路线的历史问题台账
  type: framework
  task: T13
  source_chapter: 第13章 pp.475–479
  source_quote: "we list open problems related to the main chapters of this book"
  summary: 把原书问题作为出版时研究入口，链接前文定义和已知构造；保留维数、等价关系和目标界作为后续文献核验条件。
  inputs: 选定问题、来源位置、拟研究维数与目标
  outputs: 原书问题规格、前提、已核查来源与日期、可检验子任务
  steps: 还原问题精确范围；链接相应正文；区分有限实验、猜想与全称证明；查新后才更新当前状态。
  missing_conditions: 本书不包含2021年之后的进展；联网查新不是原书提供的方法论。
  boundary: 本项适合研究参考台账，不应以引用历史问题承诺已完成当前开放性核查。
  tags: [research, historical-reference, open-problem]
```
