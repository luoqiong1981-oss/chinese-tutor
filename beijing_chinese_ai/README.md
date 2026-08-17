# 北京语文 AI 辅导系统

本项目用于建设北京语文小初高贯通的 AI 辅导数据底座，为后续诊断、训练与真实辅导提供稳定、可校验的数据契约。

## 当前版本

当前处于 **P0 数据底座阶段**：

- P0-1 Scaffold：**PASS**
- P0-2 Data Contract：**PASS**

本阶段只建设数据底座，不开发 Web 前端、App、登录系统、大模型聊天 UI、推荐系统、向量数据库、RAG 或数据可视化 Dashboard，也不批量生成训练题。

研究完成不等于系统建成。当前工程正在建立以下可验证闭环：

`研究 → 数据契约 → 自动验收 → 诊断 → 辅导 → 学情 → 复测`

## 目录

- `docs/research/`：政策、考试、课程标准及小初高贯通研究成果。
- `docs/specifications/`：系统蓝图、数据字典、版本规范及能力模型工程规范。
- `docs/acceptance/`：各阶段验收标准与验收报告。
- `data/master/`：能力、子技能、证据来源、核心结论映射等稳定主数据。
- `data/students/`：以假名化 `student_id` 管理的学生长期学情数据。
- `data/tasks/`：诊断题、训练题、迁移题等任务数据。
- `data/sessions/`：真实辅导产生的会话记录。
- `data/examples/`：仅用于 Schema 和程序测试的匿名示例数据。
- `schemas/`：JSON Schema 数据契约。
- `scripts/`：数据验证、迁移、索引与检查脚本。
- `tests/`：自动化测试。
- `skills/beijing-chinese-tutor/`：正式辅导 Skill。
- `logs/`：程序运行、数据校验与版本迁移日志；不得存放学生敏感正文。

## 冻结约束

能力体系固定为 8 个操作领域（BA、LU、RD、CL、PO、WR、OC、MC）与 1 个跨领域模块（WB），共 39 项能力。能力 ID 是永久主键。`baseline_status` 与 `skill_state` 必须分离；未测试时 `baseline_status = unknown`，不得据此写入 `skill_state = S0`。

## 下一阶段

人工确认当前标记为 `needs_review` 的能力字段，并在进入真实诊断前继续冻结子技能、证据来源和系统结论映射主数据。
