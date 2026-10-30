# 反例与失败模式提取

来源：Claude Carlet (2021)，用户指定PDF。印刷页p对应PDF第p+15页（1起算）。本文件依 `counter-example-extractor.md` 提取已定位的数学限制，不把理论反例写成作者个人失败。全书14章按否定/条件/错误/例外锚点检索，并回查下列命中页及邻页；这是代表性边界清单，不是全书勘误全集。

## ce01 同书算例位序不同

- type: counter-example
- source_chapter: §2.2.1，p.31例题与p.35表2.1；p.56表2.2
- source_quote: “an ordering ... being chosen”（p.30对真值表定义的限定；省略的是定义域符号）
- failure_mode：把本书所有十六进制索引都当同一坐标序。p.31的001对应1（x1最高位），表2.1的1000对应1（x1最低位）。
- mechanism：坐标次序改变时，相同字符串代表不同函数的标号；ANF掩码或有符号谱可能错配。
- warning_signs：未记录x_i与整数位的对应；照抄某表而采用另一表的变量序。
- bound_to: representation; scalar-spectrum
- 修正：这是两种合法枚举约定，不指控原书数学矛盾；导入时显式转换。

## ce02 普通Fourier与符号Walsh不能混用

- type: counter-example
- source_chapter: §2.3.2，pp.54–57，公式(2.32)
- source_quote: “fχ being equal to 1−2f”
- failure_mode：把0/1表直接做Hadamard后套非线性度公式。
- mechanism：Walsh作用于(−1)^f，而普通Fourier可作用于f；W_f=2^nδ_0−2f^，零频和其余频都有转换因子。
- warning_signs：Walsh Parseval平方和不是2^(2n)；零频不能恢复权重。
- bound_to: scalar-spectrum; representation

## ce03 CCZ不保持代数次数

- type: counter-example
- source_chapter: §2.1，p.29命题1证明；pp.29–30特殊子类的例外
- source_quote: “EA equivalence preserves algebraic degree ... CCZ equivalence does not.”
- failure_mode：看到次数不同就宣布两向量映射CCZ不等价，或把所有CCZ等价都当EA等价。
- mechanism：CCZ是图上的仿射变换，可以混合输入与输出；EA的次数不变量不能直接迁移。
- warning_signs：没写明EA/CCZ口径；把一般函数与书中列出的特殊子类混为一谈。
- bound_to: representation; research-triage
- 限定：EA的次数保持在次数>1的条件下表述；本书p.30指出标量等特殊情形CCZ与EA一致。

## ce04 坐标平衡不够

- type: counter-example
- source_chapter: §3.2.1，命题35，pp.112–113；向量非线性§3.2 pp.116–117
- source_quote: “balanced if and only if its component functions are balanced”
- failure_mode：只检验m个坐标函数，把其平衡或高NL推广为整个向量映射性质。
- mechanism：攻击者可取所有非零输出线性组合；输出分布均匀等价于每个非零分量平衡，向量NL由最弱分量决定。
- warning_signs：结果只有m行，没有2^m−1个非零输出掩码；没有最弱掩码见证。
- bound_to: vector-metrics; resilience
- 合成演练（不是原书实例）：F(x)=(x0,x0)，两个坐标均平衡，但输出掩码11的分量恒0。

## ce05 Bent与平衡冲突

- type: counter-example
- source_chapter: §6.1，p.191
- source_quote: “Bent Boolean functions are not balanced.”
- failure_mode：将最大NL的bent函数直接当平衡流密码组合函数，或宣称存在平衡bent。
- mechanism：bent的零频绝对值2^(n/2)不为0，权重为2^(n−1)±2^(n/2−1)。
- warning_signs：同时报告所有绝对谱值等于2^(n/2)与W(0)=0。
- bound_to: bent-construction; scalar-spectrum; model-review

## ce06 MM构造的等长条件不能丢

- type: counter-example
- source_chapter: §6.1.15，命题77与脚注8，p.209
- source_quote: “bentness is then obviously not characterized by the bijectivity of π.”
- failure_mode：把x,y不等长的广义拼接构造也用“π双射当且仅当bent”判断。
- mechanism：原始MM把输入分成两个k维块，单原像保证谱幅度；不等长时映射维数及原像数改变。
- warning_signs：x、y长度不同仍机械调用k变量置换构造。
- bound_to: bent-construction

## ce07 高AI与高NL互不等同

- type: counter-example
- source_chapter: §9.1，p.331；majority例p.335
- source_quote: “high algebraic immunity does not imply high nonlinearity”
- failure_mode：AI达ceil(n/2)就停止检查非线性度、快速代数攻击或平衡性。
- mechanism：AI控制低次零化子；Walsh最大值控制仿射逼近，两个优化目标不同。Majority最优AI但低NL和FAA抵抗差。
- warning_signs：把“最优AI”写成“全指标最优”；没有零化子证书和完整谱。
- bound_to: algebraic-immunity; scalar-spectrum; model-review

## ce08 APN不是置换条件，偶数维Gold尤其需要单独检查

- type: counter-example
- source_chapter: §11.5.2，p.400；§2.3.6 p.72幂函数置换判据
- source_quote: “whatever is the parity of n”
- failure_mode：证明Gold的APN后自动宣称其为置换或AB。
- mechanism：APN约束差分方程解数；幂函数置换需要gcd(d,2^n−1)=1；AB在本书框架要求奇数n。Gold APN证明不要求奇数n。
- warning_signs：只报告delta=2，没有输出去重；偶数维继承奇数维AB结论。
- bound_to: field-power; vector-metrics
- 合成实例化：GF(16)上的x³是Gold APN，但gcd(3,15)=3，非置换。不是书中列出的具体真值表。

## ce09 逆函数的奇偶维差分分支

- type: counter-example
- source_chapter: §11.5.2，pp.400–401
- source_quote: “admits four solutions (the elements of F4) if b=1”
- failure_mode：把奇数维乘法逆的APN结论用于偶数维AES类逆映射。
- mechanism：在0映到0约定下，导数步长1的b=1分支，偶数维还出现GF(4)中的额外根，解数4。
- warning_signs：未处理0,1端点；用1/x表达却没定义x=0。
- bound_to: field-power; vector-metrics

## ce10 Boomerang均匀度不是EA/CCZ不变量

- type: counter-example
- source_chapter: §3.4，p.141及后页，公式(3.42)
- source_quote: “it is not EA invariant ... and therefore not CCZ invariant.”
- failure_mode：把差分均匀度与boomerang均匀度共同当EA或CCZ分类不变量。
- mechanism：boomerang统计额外涉及逆函数组合；原书仅给仿射等价与取逆的不变性。
- warning_signs：用EA变换后不重新算BCT；把S盒各指标不变量表合并成一栏。
- bound_to: vector-metrics; representation; research-triage

## ce11 传播性质不能由某个高NL构造自动继承

- type: counter-example
- source_chapter: §8.1，p.319
- source_quote: “cannot produce functions satisfying PC(l) with l≥n/2”
- failure_mode：认为Dobbertin平衡高NL构造自然有任意高阶传播性质。
- mechanism：指定半空间内平方谱和为0，与命题129的PC必要条件矛盾。
- warning_signs：只看NL，没有导数或平方谱和证书。
- bound_to: propagation; bent-construction
- 限定：仅针对原书该构造，不是否定所有函数。

## ce12 受限域AI不具有单调下降性

- type: counter-example
- source_chapter: §12.2，p.464
- source_quote: “but it may also increase the algebraic immunity”
- failure_mode：把完整域AI当限制域AI的统一上界，或把全空间非零零化子当限制域合法零化子。
- mechanism：限制域减弱乘积恒零条件，同时加强“g在E上非零”的条件；二者效应竞争。原书f'(x,0)=f(x),f'(x,1)=0有整体AI=1，限制到E=F2^(n−1)×{0}则AI_E≥2。
- warning_signs：零化子在E上恒0却仍计为证书；没输出域E。
- bound_to: symmetry; algebraic-immunity; model-review

## ce13 大距离线性码不直接解决对抗故障检测

- type: counter-example
- source_chapter: §12.1.6，p.447
- source_quote: “The worst error-masking probability being then equal to 1”
- failure_mode：从自然低重量错误纠正能力直接推出对任意攻击者选定故障的检测安全。
- mechanism：攻击者若可注入非零码字作为错误，线性码的合法码字被映到另一个合法码字，校验必然漏检。
- warning_signs：仍假设攻击者故障低重量；不定义故障分布及攻击能力。
- bound_to: reed-muller; model-review
- 限定：不是所有编码防护都无效，而是目标必须匹配最坏漏检概率与相应模型。

## ce14 TI取逆不能机械继承

- type: counter-example
- source_chapter: §12.1，p.444
- source_quote: “function F−1 is not necessarily a t-mask TI of F−1.”
- failure_mode：函数的共享实现满足t-mask TI后，直接把逆实现也认定为同阶TI。
- mechanism：non-completeness的输入共享独立性条件在取逆、输入输出交换后并不等价。
- warning_signs：只核正确性或可逆性，未重新核non-completeness与uniformity。
- bound_to: model-review

## ce15 部分bent同名近邻不应合并

- type: counter-example
- source_chapter: §6.2，p.258
- source_quote: “Partially-bent functions must not be mistaken for partial bent functions”
- failure_mode：把partially-bent与partial bent两种性质翻译成同一标签，按同一个谱定义测试。
- mechanism：原书后者涉及对0/1函数的Fourier值及partial difference sets，前者有另一组导数和Walsh结构。
- warning_signs：只有中文“部分bent”，没有英文术语及变换定义。
- bound_to: bent-construction; representation

## ce16 搜索域最优与全空间最优不同

- type: counter-example
- source_chapter: §10.2，pp.360–361；§3.5.2 p.143；第13章 pp.475–479
- source_quote: “This is a quality ... but also a drawback” （p.143对结构性构造的限定）
- failure_mode：从受限对称族的穷举、若干小维样本、构造实例，宣称全空间最优或新无限族。
- mechanism：构造或轨道限制只覆盖全函数空间的一部分；书中9变量旋转对称241与更大搜索类242展示域的差别。第13章将更大范围问题单独列为待研究。
- warning_signs：没记录搜索空间、等价关系和预算；“未找到”被写成“不存在”。
- bound_to: symmetry; research-triage

## 下游使用

每条反例仅作为能力卡B段依据；来源充分性、实际执行及任务收益需要主流程分别验证。位序差异是实现接口问题，不是作者心理矛盾。当前开放状态及现代实现安全需实时一手材料，不能仅由2021年书籍回答。
