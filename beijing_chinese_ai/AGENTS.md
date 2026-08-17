# 项目协作约束

## 当前范围

本项目当前处于 P0，只建设数据底座、数据契约、验证脚本和自动化测试。未经明确任务要求，不开发前端、App、登录、聊天 UI、推荐、向量数据库、RAG 或 Dashboard，不批量生成训练题。

## 冻结规则

- 能力体系为 BA01—BA04、LU01—LU04、RD01—RD08、CL01—CL04、PO01—PO04、WR01—WR06、OC01—OC03、MC01—MC03、WB01—WB03，共 39 项。
- BA、LU、RD、CL、PO、WR、OC、MC 的 `architecture_type` 为 `operational_domain`；WB 为 `cross_domain_module`。
- 39 个能力 ID 是永久主键，不得重新编号、回收或改变含义。
- `baseline_status` 与 `skill_state` 必须分离。初始 `baseline_status` 为 `unknown`；只有真实训练或诊断证据才能产生 S0—S6。
- 学生数据库主键必须使用假名化 `student_id`，不得使用真实姓名。

## 数据边界

- `data/examples/` 只能存放匿名测试示例，不得虚构真实学生档案。
- `logs/` 不得存放学生敏感正文。
- 研究资料、系统主数据、学生数据、任务数据与会话数据必须保持目录隔离。
- 修改数据结构时应同步 Schema、验证脚本、测试和验收资料。
