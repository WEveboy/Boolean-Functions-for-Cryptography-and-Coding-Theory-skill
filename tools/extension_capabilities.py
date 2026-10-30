"""v0.2 capability definitions and source anchors; consumed by build_bundle.py."""
DATA=[
('boomerang','BCT与boomerang均匀度','T03/T11','§3.4.1 pp.141–142，式(3.42)',
 '只在置换上计算逆函数BCT，最大值排除两个零差分轴。','BCT、boomerang、回旋镖、S盒',
 '输入n<=8和长度2^n的置换表。构造逆表，按BCT[a,b]=#{x:F^-1(F(x)+b)+F^-1(F(x+a)+b)=a}求完整表；取a!=0,b!=0最大值，输出达到最大值的(a,b)与全部解。零行零列值为2^n，用于校验但不计均匀度。',
 '合成演练：2位恒等置换，完整BCT每项4，boomerang均匀度4。',
 '重复输出时拒绝逆函数BCT；该参数不一般保持EA/CCZ不变，不把delta相同当BCT相同。单盒指标不证明多轮攻击复杂度。',
 'CLI operation=boomerang；research_extensions.boomerang(table,n)。'),
('field-trace-dual','绝对迹与多项式基对偶基','T14','§14.3.1 p.489；§14.2 pp.483–484',
 '固定不可约模多项式和多项式基，用迹配对恢复坐标内积。','绝对迹、dual basis、对偶基、trace、域掩码',
 '输入n<=8和次数n的不可约二元模多项式。先验证域，计算Tr(x)=Σ_{i=0}^{n-1}x^(2^i)全表；以alpha_i=X^i为基，求beta_j使Tr(alpha_i*beta_j)=delta_ij。输出迹表、基、对偶基、配对矩阵和单位核验矩阵。坐标掩码b对应域元素a=Σ b_i*beta_i，满足b·x=Tr(a*x)。',
 '合成演练：GF(4)取mod=7（X²+X+1），多项式基[1,2]，对偶基[3,1]，迹表[0,0,1,1]。',
 '只支持所声明多项式基；不可约不等于本原。Tr为F2线性，不能照抄原书p.489的Fq线性措辞冲突。不同模多项式必须先建立域同构才能比较整数标签。',
 'CLI operation=field-trace；research_extensions.trace_and_dual(n,mod)。'),
('equivalence-certificate','给定EA与CCZ等价证书','T01/T11','§2.1 pp.28–30，Definition 5',
 '验证给定可逆仿射变换的逐点等式，不把失败证书当成不等价证明。','EA证书、CCZ证书、graph affine、等价验证',
 '输入n<=8,m<=8,n+m<=16，两份表F/G和矩阵行掩码。EA验证G(x)=Aout(F(Ain(x))) XOR L(x)，输入/输出线性部分满秩；offset以整数向量表示，add_rows允许非满秩。CCZ把图编码z=x+(F(x)<<n)，用可逆(n+m)维仿射矩阵映射，核验输入投影无重复且输出等于G的新图。输出true和点数，或false与第一个失败见证；矩阵格式/秩不合法则报输入错误。',
 '合成演练：GF(8)的x³是置换，把图的输入输出两块交换，逐点得到其逆函数，构成CCZ证书。',
 '矩阵第i行的内积给第i输出位，与原书行向量形式需转置。只有所给证书失败，不能推出EA/CCZ不等价；没有未知变换搜索、全分类或新颖性证明。',
 'CLI operation=ea-certificate或ccz-certificate；参数格式见usage.md。'),
('higher-order-distance','预算内精确高阶非线性度','T02/T04','§3.1.3 pp.79–84；§4.1.6 pp.157–158',
 '将高阶非线性度落实到RM码的有限精确距离，先核枚举规模。','高阶非线性度、NL_r、二阶距离、RM距离',
 '输入n<=8、标量表和0<=r<=n。若ANF次数<=r，则以成员资格证书返回距离0，不作枚举。否则计算K=Σ_{i=0}^r C(n,i)，仅K<=16时枚举2^K个RM码字；用Gray码每次异或一个单项式评价行，取最小Hamming距离并保留最近多项式ANF掩码。输出r、距离、实际枚举数和最近码字。',
 '合成演练：n=3，f=x0*x1*x2到RM(2,3)距离1；次数<=2的函数距离0。',
 '超出K<=16即拒绝精确枚举，不能把未完成结果记最优；距离0的成员资格分支不受枚举维数限制。一次给定函数到码的距离不是覆盖半径。',
 'CLI operation=higher-order，字段r；research_extensions.higher_order(table,n,r)。'),
('function-code','函数生成码、秩门与重量分布','T04/T11','§4.2 p.160；§2.3.6 pp.71–73',
 '先计算实际生成矩阵秩，再枚举不同码字；退化参数不套满秩距离公式。','函数生成码、重量分布、rank gate、few-weight code',
 '输入n<=8,m<=8,n+m<=16和F表，include_constant默认true。明确C={a·x+b·F(x)+c}在所有x∈F2^n上的评价码；可设c=0。构造坐标评价行，F2消元取独立生成行，实际维数k为秩；k<=17时枚举2^k个不同码字，输出生成行、独立行、秩退化标志、重量计数、最小非零重量。全参数元组可能重复同一码字。',
 '合成演练：F为2位恒等，含常数时参数数5、实际秩3，重量分布{0:1,2:6,4:1}；向量NL=0而码最小距离2。',
 '原书p.160的维数n+m+1及d=NL需要F无仿射分量。缺满秩时只报告实际码参数；不把不同(a,b,c)的次数当不同码字数。没有一般码分类或译码算法。',
 'CLI operation=function-code；research_extensions.function_code(table,n,m,include_constant=True)。')]

ANCHORS={
'boomerang':('the so-called boomerang uniformity','p.141，式(3.42)'),
'field-trace-dual':('an Fp-linear form over the space Fq','§14.3.1 p.489；数学下标用纯文本转写'),
'equivalence-certificate':('for some affine automorphism L','§2.1 Definition 5(4)(5) p.28；输入投影条件p.29'),
'higher-order-distance':('this distance is called the r-th order nonlinearity of f','§4.1.6 p.157；RM基与维数pp.151–152'),
'function-code':('having no affine component (i.e., having strictly positive nonlinearity)','§4.2.1 p.160')}

EXAMPLES={
'bct-identity':{'operation':'boomerang','n':2,'table':[0,1,2,3]},
'trace-gf4':{'operation':'field-trace','n':2,'modulus':7},
'nl2-cubic':{'operation':'higher-order','n':3,'r':2,'table':[0,0,0,0,0,0,0,1]},
'code-identity':{'operation':'function-code','n':2,'m':2,'table':[0,1,2,3]},
'ccz-inverse-gf8':{'operation':'ccz-certificate','n':3,'m':3,'table':[0,1,3,4,5,6,7,2],
                   'target':[0,1,7,2,3,4,5,6],'graph_rows':[8,16,32,1,2,4]},
'ea-identity':{'operation':'ea-certificate','n':2,'m':2,'table':[0,1,3,2],'target':[0,1,3,2],
               'input_rows':[1,2],'output_rows':[1,2]}}
