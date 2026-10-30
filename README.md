# Carlet Boolean Research Skill

基于Claude Carlet《Boolean Functions for Cryptography and Coding Theory》（2021）的研究技能。仿照已有Boolean Vector Research项目，使用cangjie-skill v2.5完成来源提取、能力分流和Bundle编译。新入口为`carlet-boolean-research`，避免覆盖旧技能。

当前版本 **0.2.0**：18张能力卡连接ANF、Walsh、RM、bent、APN、BCT、迹/对偶基、给定EA/CCZ证书、精确高阶距离与函数码重量分布。Python标准库工具提供预算内精确计算和批量执行；旧版JSON输入保持可用。详见[更新日志](CHANGELOG.md)与[使用合同](skills/carlet-boolean-research/resources/usage.md)。

## 开始使用

将仓库中的整个`skills/carlet-boolean-research`目录复制到你的Codex技能目录（如`~/.codex/skills/`），保留references和resources；重新开启聊天后调用：

```text
$carlet-boolean-research 用GF(8)中x^3作例子，写清模多项式，核验全部分量和DDT，并区分实验与族证明。
```

独立运行计算器：

```text
python skills/carlet-boolean-research/resources/research_core.py examples/quadratic-bent.json --out output/result.json
python skills/carlet-boolean-research/resources/research_core.py examples/trace-gf4.json --out output/trace.json
python skills/carlet-boolean-research/resources/research_core.py examples/ccz-inverse-gf8.json --out output/ccz.json
python skills/carlet-boolean-research/resources/research_core.py examples/batch-mixed.json --out output/batch.json
python -m unittest discover -s tools -p "test_*.py" -v
```

## 阅读与复现

- [整书骨架](books/carlet-2021/BOOK_OVERVIEW.md)、[精华长文](books/carlet-2021/DIGEST.md)、[术语](books/carlet-2021/GLOSSARY.md)。
- [覆盖审计](books/carlet-2021/coverage-audit.md)、[三重验证](books/carlet-2021/verified.md)、[0.2版验证](docs/VALIDATION-0.2.0.md)、[0.1版历史记录](docs/VALIDATION.md)。
- 唯一编译源为`books/carlet-2021/.cangjie/capabilities/verified.yaml`与同目录cards/resources；最终skills为生成目录，不手改。编译需cangjie-skill v2.5及其PyYAML等作者端依赖；计算器本身无第三方依赖。
- [上传与维护流程](docs/UPLOAD_WORKFLOW.md)。没有把cangjie工具本体复制进仓库。

本仓库不分发原书PDF、整章文本或本机私人路径。原书版权归原权利人；短引文只用于定位与校验。项目原创代码和原创说明采用[MIT许可](LICENSE)，该许可不覆盖原书或上游仓颉工具。第13章记录的是出版时开放问题，不代表2026年状态；数学指标不证明系统安全。

项目需求与维护：WEveboy。技能整理、独立计算实现、验证及文档由Codex协助完成。
