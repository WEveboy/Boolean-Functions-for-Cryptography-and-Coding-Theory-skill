# 术语候选池

提取方式：检索式回查原书明确术语定义及邻接段落，结合 framework 全14章逐页机制扫描。没有词法索引，采用正文页标记定位；无chunk_id。src-carlet-2021，印刷页p=PDF第p+15页。author_definition为忠实中文释义，非逐字引文。27项均作为reference候选，具体定义、区分和页码收录于../GLOSSARY.md，不晋级独立能力。

```yaml
- {id: g01, term: 布尔与向量函数, type: term, source_chapter: '§1.3–1.4 pp.17–26', author_definition: '从F2^n到F2或F2^m的映射', key_distinction: '变量数n、输出m和表长2^n不同', why_it_matters: '统一输入规格', tags: [term, representation]}
- {id: g02, term: ANF, type: term, source_chapter: '§2.2.1 pp.30–37', author_definition: 'F2上唯一平方自由多项式', key_distinction: '不同于整数NNF及域单变量表达', why_it_matters: '决定异或运算与次数', tags: [term, representation]}
- {id: g03, term: 代数次数, type: term, source_chapter: '§2.2.1 pp.36–41', author_definition: '最高非零ANF单项式次数', key_distinction: '向量最大坐标次数不同于最小分量次数', why_it_matters: '防止错误套攻击条件', tags: [term, algebra]}
- {id: g04, term: 绝对迹, type: term, source_chapter: '§14.3.1 p.489', author_definition: 'Frobenius共轭之和形成Fp线性形式', key_distinction: '二进制域上是F2线性而非一般扩域线性', why_it_matters: '域模型和掩码对应', tags: [term, finite-field]}
- {id: g05, term: Walsh变换, type: term, source_chapter: '§2.3 pp.53–61', author_definition: '符号函数与全部线性字符的未归一化内积', key_distinction: '不同于对0/1函数直接Fourier变换', why_it_matters: 'NL与Parseval数值口径', tags: [term, spectrum]}
- {id: g06, term: 分量, type: term, source_chapter: '§2.3.6 pp.71–73', author_definition: '非零输出掩码b对应b·F', key_distinction: '坐标只是分量的一部分', why_it_matters: '向量最弱掩码不遗漏', tags: [term, vectorial]}
- {id: g07, term: 平衡, type: term, source_chapter: '§3.2.1 pp.112–113', author_definition: '全部输出等频', key_distinction: '坐标平衡不足以保证向量平衡', why_it_matters: '独立核查原像分布', tags: [term, balancedness]}
- {id: g08, term: 非线性度, type: term, source_chapter: '§3.1.3 p.79', author_definition: '到所有仿射函数的最小Hamming距离', key_distinction: '不等于代数次数或非线性门数', why_it_matters: '正确衡量线性逼近', tags: [term, nonlinearity]}
- {id: g09, term: Reed-Muller码, type: term, source_chapter: '§4.1 pp.151–154', author_definition: '次数至多r的函数真值表组成的线性码', key_distinction: '码维数不是函数变量数', why_it_matters: '参数及高阶距离', tags: [term, code]}
- {id: g10, term: 高阶非线性度与覆盖半径, type: term, source_chapter: '§4.1.6 pp.157–159', author_definition: '到RM码的距离及其对全空间的最大值', key_distinction: '不同于码内部最小距离', why_it_matters: '避免最小与最大量混淆', tags: [term, distance]}
- {id: g11, term: EA等价, type: term, source_chapter: '§2.1 pp.27–30', author_definition: '仿射输入输出置换及额外仿射项', key_distinction: '证书验证不是未知变换搜索', why_it_matters: '新颖性边界', tags: [term, equivalence]}
- {id: g12, term: CCZ等价, type: term, source_chapter: '§2.1 pp.28–30', author_definition: '函数图像在联合空间中的仿射等价', key_distinction: '比EA广且不保留所有代数指标', why_it_matters: '不变量需匹配关系', tags: [term, equivalence]}
- {id: g13, term: 导数, type: term, source_chapter: '§2.2.1 pp.38–39', author_definition: 'f(x)+f(x+a)', key_distinction: '异或差分不是实数极限', why_it_matters: '传播与次数分析', tags: [term, derivative]}
- {id: g14, term: 自相关, type: term, source_chapter: '§2.3 pp.61–63', author_definition: '导数符号和', key_distinction: '零方向为平凡值', why_it_matters: '传播测试排除a=0', tags: [term, correlation]}
- {id: g15, term: SAC与PC, type: term, source_chapter: '第8章 pp.318–320', author_definition: '规定低重量方向上的导数平衡', key_distinction: 'SAC仅重量1且order k另有含义', why_it_matters: '防止多位传播误报', tags: [term, propagation]}
- {id: g16, term: bent, type: term, source_chapter: '§6.1 pp.190–192', author_definition: '偶数维平坦Walsh幅度函数', key_distinction: '必不平衡', why_it_matters: '应用条件相容性', tags: [term, bent]}
- {id: g17, term: bent对偶, type: term, source_chapter: '§6.1.6 pp.197–199', author_definition: 'Walsh符号定义的布尔函数', key_distinction: '不是逻辑否定', why_it_matters: '构造与双对偶校验', tags: [term, dual]}
- {id: g18, term: plateaued, type: term, source_chapter: '§6.2.2 pp.258–261', author_definition: '谱至多一个非零绝对值', key_distinction: '不等于partially-bent且不要求三个值均出现', why_it_matters: '谱分类条件', tags: [term, spectrum]}
- {id: g19, term: 二次极化秩, type: term, source_chapter: '§5.2 pp.170–175', author_definition: '二次函数关联交错双线性型的秩', key_distinction: '高次数不能直接套秩公式', why_it_matters: '谱幅与核的计算', tags: [term, quadratic]}
- {id: g20, term: 相关免疫与韧性, type: term, source_chapter: '第7章 pp.284–317', author_definition: '低重量频点消失及额外平衡条件', key_distinction: '相关免疫不含平衡要求', why_it_matters: '阶数判定', tags: [term, resilience]}
- {id: g21, term: 代数免疫, type: term, source_chapter: '§9.1 pp.321–328', author_definition: 'f或f+1非零零化子的最小次数', key_distinction: '不等于f的次数', why_it_matters: '两侧线性系统', tags: [term, immunity]}
- {id: g22, term: 快速代数攻击与FAI, type: term, source_chapter: '§9.1 pp.321–324', author_definition: '低次乘子产生低次乘积的关系', key_distinction: '最优AI仍不足，FAI具体定义需核对', why_it_matters: '不误报抵抗代数攻击', tags: [term, attack]}
- {id: g23, term: 差分均匀度, type: term, source_chapter: '§3.4.1 pp.134–137', author_definition: '全部非零输入差导数方程最大解数', key_distinction: '概率需除以2^n且a=0不纳入', why_it_matters: 'DDT的正确最大值', tags: [term, differential]}
- {id: g24, term: APN, type: term, source_chapter: '§3.4.1 p.137', author_definition: 'n到n函数差分均匀度2', key_distinction: '不必置换或AB', why_it_matters: '设计目标不混同', tags: [term, apn]}
- {id: g25, term: AB, type: term, source_chapter: '§3.2.3 pp.118–121；§11.3', author_definition: '奇数维达到SCV非线性界的向量函数', key_distinction: 'AB蕴含APN，反向一般不成立', why_it_matters: '全分量谱判定', tags: [term, ab]}
- {id: g26, term: 对称与旋转对称, type: term, source_chapter: '§10.1–10.2 pp.352–362', author_definition: '任意置换不变或仅循环移位不变', key_distinction: '后者是更广的类', why_it_matters: '族搜索覆盖范围', tags: [term, symmetry]}
- {id: g27, term: 受限输入指标, type: term, source_chapter: '§12.2.2 pp.456–465', author_definition: '在实际输入集E上定义密码指标', key_distinction: '零化子必须在E上不恒零', why_it_matters: '不能用全域参数替代切片', tags: [term, restricted-domain]}
```
