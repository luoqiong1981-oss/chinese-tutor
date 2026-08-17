# P0-2 数据契约验收报告

验收日期：2026-08-16  
工程根目录：`D:/1_Link-KnowledgeBase/1.北京语文AI辅导/beijing_chinese_ai/`

## 1. 创建的 Schema

共创建 9 个 JSON Schema，均通过 Draft 2020-12 合法性检查：

1. `schemas/ability_catalog.schema.json`
2. `schemas/subskills.schema.json`
3. `schemas/evidence_sources.schema.json`
4. `schemas/claims.schema.json`
5. `schemas/student_profile.schema.json`
6. `schemas/skill_state.schema.json`
7. `schemas/learning_event.schema.json`
8. `schemas/session.schema.json`
9. `schemas/task.schema.json`

结果：**9/9 PASS**

## 2. 主数据数量

- `data/master/ability_catalog.v1.1.json`：39 项能力。
- `data/master/master_data_version.json`：已记录 Schema 版本、能力目录版本、冻结状态和破坏性变更策略。
- 能力 ID 被声明为永久主键；废弃时只能标记 `deprecated`，不得删除、重新编号、回收或改变含义。

## 3. 39 项能力检查

- 能力数量：39/39 PASS
- 固定 ID 集合：PASS
- 重复 ID：0，PASS
- 第 40 项：不存在，PASS
- `domain_code` 与能力 ID 前缀一致：PASS
- BA、LU、RD、CL、PO、WR、OC、MC 为 `operational_domain`：PASS
- WB01—WB03 为 `cross_domain_module`：PASS

## 4. 引用完整性检查

校验器会递归检查 `ability_id`、`ability_ids`、`target_ability_ids`、`next_review_ability_ids`、`primary_ability_id` 和 `secondary_ability_ids`。

当前主数据及运行数据中不存在无效能力引用。测试已确认 `ZZ99` 等不存在的引用会导致失败。

结果：**PASS**

## 5. baseline_status 检查

允许值固定为：

- `unknown`
- `in_progress`
- `established`

默认值为 `unknown`。学生初始化时不得用能力状态替代基线诊断进度。

结果：**PASS**

## 6. skill_state 检查

S0—S6 定义已从既有 V1.1 研究报告提取并写入 `docs/specifications/student_state_rules.md`。`skill_state` Schema 要求 `evidence_count >= 1`，自动校验器还要求存在同一 `student_id + ability_id` 的真实 `learning_event`。

`baseline_status = unknown` 时写入任何 `skill_state`，包括 S0，都会失败。

结果：**PASS**

## 7. 隐私规则检查

- `student_id` 必须匹配 `STU-` 开头的假名化标识格式。
- `student_profile` 禁止未声明字段，未提供 `real_name` 字段。
- 未创建真实学生数据。
- 匿名 mock 数据仅位于 `tests/fixtures/`。

结果：**PASS**

## 8. 自动测试结果

执行命令：

```text
python scripts/validate_v1_1.py
python -m unittest discover -s tests -v
```

结果：

- 自动校验器：15/15 PASS
- 自动测试：9 passed / 0 failed
- 当前 Python 环境未安装 pytest，按任务要求使用标准库 `unittest`，未强制安装额外依赖。

已覆盖：39 项完整性、删除能力、增加第 40 项、重复 ID、WB 类型错误、RD 类型错误、`unknown` 合法性、未测试 S0 初始化失败、无效跨表引用失败。

## 9. 尚未解决的问题

以下内容因现有资料不足以形成可审计的结构化冻结值，按规则保留为 `null`，没有猜测补全：

- 17 项能力的 `definition` 待人工确认：CL02、CL04、PO01—PO04、WR02—WR06、OC01—OC03、MC01—MC03。
- 39 项能力的 `assessment_focus` 待人工确认。
- 39 项能力的 `evidence_requirements` 待人工确认。
- 研究资料能识别 RD08-A—D、WR06-A—F、OC03-A—G 共 17 个子技能名称，但其完整定义与可观察行为尚未全部冻结，因此本阶段只创建了子技能 Schema，未编造子技能主数据。
- 证据来源与系统结论映射本阶段只冻结 Schema，尚未创建正式主数据行。
- 较早 V1.1 报告曾使用“9 个操作领域”的历史措辞；后续《工程化验收补充研究》已明确修正为当前冻结的“8 个操作领域 + 1 个跨领域模块”。工程数据采用后者，原研究 PDF 保持原样。

所有 39 项记录均通过 `needs_review: true` 明示以上人工复核需求。本阶段不存在未定义的 S0—S6 状态，即无 `PENDING_DEFINITION` 状态项。

## 10. 下一阶段建议

1. 由人工依据研究母稿确认 17 项缺失定义及 39 项评估焦点、证据要求。
2. 冻结 17 个子技能的主数据及外键关系。
3. 建立证据来源和系统结论映射主数据，并加入 source/claim 跨表引用验收。
4. 在数据契约稳定后，再进入真实诊断任务与辅导记录建设。

## 最终结论

允许为空的未决字段均已显式标记，没有生成虚构学生数据、训练题或研究结论；全部硬性工程检查与自动测试通过。

**P0-2 DATA CONTRACT = PASS**
