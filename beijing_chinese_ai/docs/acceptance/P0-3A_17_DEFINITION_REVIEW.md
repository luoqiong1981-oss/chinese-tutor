# P0-3A-1：17 项候选定义人工审校表

## 审校前提

- `definition = null` 的能力总数：**17**。
- ability_id 清单：CL02、CL04、PO01、PO02、PO03、PO04、WR02、WR03、WR04、WR05、WR06、OC01、OC02、OC03、MC01、MC02、MC03。
- 使用的研究资料：
  - `docs/research/北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`，第 8—12 页。
  - `docs/research/北京语文小初高贯通完整能力研究 V1.1：补章、补字段、补证据与 SKILL 落地.pdf`，第 5—8 页。
- 本轮未修改正式能力表 `data/master/ability_catalog.v1.1.json`，也未修改 `master_data_version.json`。
- 本轮所有 definition、assessment_focus 和 evidence_requirements 均为候选内容，不能视为正式冻结值。
- 17 项正式记录的 `needs_review` 均继续为 `true`。

## 17 项总览

| ability_id | ability_name | 候选定义状态 | 依据类型 | 可信度 | 主要风险 | 人工结论 |
|---|---|---|---|---|---|---|
| CL02 | 虚词句法与特殊句式识别 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 BA03、CL03 的句法处理边界 | PENDING |
| CL04 | 内容主旨、人物态度与课内外迁移 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 RD04、RD05、RD06 的解释能力重叠 | PENDING |
| PO01 | 朗读节奏、字词与画面建构 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 PO02 的情感解释边界 | PENDING |
| PO02 | 意象情感主旨证据化 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 RD05、PO03 的证据解释边界 | PENDING |
| PO03 | 炼字手法与表达效果 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 RD08 高度相似 | PENDING |
| PO04 | 比较阅读与诗文互证 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 RD03 的多材料比较边界 | PENDING |
| WR02 | 立意与问题意识 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 WR01、RD06、WR06 的边界 | PENDING |
| WR03 | 选材细节与真实性 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 WR02、WR05 的素材/表达边界 | PENDING |
| WR04 | 结构组织与段落推进 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 LU02、RD07 的结构能力重叠 | PENDING |
| WR05 | 叙事描写与个性表达 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 WR03、RD08 的细节/语言边界 | PENDING |
| WR06 | 观点证据论证与修改责任 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | MEDIUM | 包含 6 个子技能，范围较宽 | PENDING |
| OC01 | 倾听、复述、提问与对话 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 RD01 的信息辨识边界 | PENDING |
| OC02 | 说明、发言、演讲、讨论与合作 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 LU01、WR06 的口头表达边界 | PENDING |
| OC03 | 信息搜集核验、调查与跨学科呈现 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | MEDIUM | 包含 7 个子技能，范围较宽 | PENDING |
| MC01 | 计划预习与任务分解 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 WR01、WB01 的计划边界 | PENDING |
| MC02 | 自我监控、错因诊断与修订 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | HIGH | 与 LU03、RD05 的修订边界 | PENDING |
| MC03 | Feynman 式复述、间隔复测与迁移 | COMPLETE_CANDIDATE | RESEARCH_SYNTHESIS | MEDIUM | 多机制复合，且易与 S4—S6 混淆 | PENDING |

## CL02 虚词句法与特殊句式识别

- domain_code：CL
- 当前 definition：`null`
- 当前已有字段：`ability_name=虚词句法与特殊句式识别`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 8 页，“文言文”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表将其发展描述为“常见虚词→结合语境判断功能→复杂长句逻辑分析”，训练观察包括找谓语、判断连接关系和还原省略，达标表现为能够用句法解释判断。
- 候选 definition：**能够在文言语句中结合上下文和句法关系，判断常见虚词的功能，识别特殊句式，并说明句内成分的连接与逻辑关系。**
- 候选 assessment_focus：是否依据语境与句法判断虚词功能；是否能找出核心谓语和连接成分；是否能还原省略并解释判断依据，而非机械套用虚词意义表。
- 候选 evidence_requirements：同一虚词在不同语句中的比较判断；陌生文言句的结构分析；能够用句法关系说明判断理由。
- 与相邻能力的边界：相邻 ability_id 为 BA03、CL01、CL03。相似点是都调用句法或词义分析；CL02 保留的核心边界是文言虚词功能与特殊句式识别，BA03 是通用语法标点基础，CL01 是实词推义，CL03 是断句、翻译与完整语义复原。需人工确认“特殊句式”的具体覆盖范围是否另行列举。
- 可信度：HIGH
- 风险或疑问：候选定义中的“特殊句式”沿用能力名称，但研究表未在本页穷举其类型。
- needs_review：`true`
- 人工审核结论：PENDING

## CL04 内容主旨、人物态度与课内外迁移

- domain_code：CL
- 当前 definition：`null`
- 当前已有字段：`ability_name=内容主旨、人物态度与课内外迁移`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 8 页，“文言文”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从说清人物事件发展到依据原文评价，再到分析立场、论证与历史条件；训练链为事实、因果、观点证据和比较，达标要求是在陌生文言中独立解释与评价。
- 候选 definition：**能够在文言文本中依据人物事件、原文证据和因果关系，解释内容主旨、人物态度或作者立场，并将课内形成的理解方法迁移到陌生文本。**
- 候选 assessment_focus：是否以原文事实和因果关系支撑解释；是否区分人物态度、作者立场与主旨；是否能在陌生文本中使用方法而非复述课内结论。
- 候选 evidence_requirements：陌生文言文本的独立解释；与结论直接相关的原文证据；课内外文本或不同条件下的比较说明。
- 与相邻能力的边界：相邻 ability_id 为 CL03、RD04、RD05、RD06。相似点是均涉及内容理解、证据和推断；CL04 的核心边界是文言文本中的高层解释及课内外迁移，CL03 负责语义复原，RD04 面向现代文人物与主旨，RD05/06 是跨材料的证据与推断机制。需人工确认“作者立场”是否始终包含在本能力范围内。
- 可信度：HIGH
- 风险或疑问：能力名称同时包含内容、人物、态度和迁移，范围较宽，正式定义需避免成为文言阅读的兜底能力。
- needs_review：`true`
- 人工审核结论：PENDING

## PO01 朗读节奏、字词与画面建构

- domain_code：PO
- 当前 definition：`null`
- 当前已有字段：`ability_name=朗读节奏、字词与画面建构`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 8 页，“古诗词”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求由景物情境形成连贯画面，并进一步处理时空跳转与复杂意境；训练观察为朗读、圈出景物和动作并复原基本情境，达标时不依赖作者标签。
- 候选 definition：**能够依据古诗词的朗读节奏、关键字词、景物与动作信息，复原作品的基本情境，建构连贯画面并辨明其中的时空变化。**
- 候选 assessment_focus：能否从字词、景物、动作和时空信息复原情境；画面是否连贯；是否脱离背诵译文和作者标签独立理解。
- 候选 evidence_requirements：陌生诗词的基本情境复原；对关键字词、景物、动作和时空关系的文本指认；能够说明画面建构依据。
- 与相邻能力的边界：相邻 ability_id 为 BA04、PO02。相似点是都调用语言积累或作品理解；PO01 的核心边界是建立字面情境与画面，PO02 才进入情感、主旨及其证据解释。需人工确认“朗读节奏”在正式定义中是输入线索还是独立结果。
- 可信度：HIGH
- 风险或疑问：画面建构与“意境”容易越界到 PO02/PO03，候选定义暂限于基本情境和时空关系。
- needs_review：`true`
- 人工审核结论：PENDING

## PO02 意象情感主旨证据化

- domain_code：PO
- 当前 definition：`null`
- 当前已有字段：`ability_name=意象情感主旨证据化`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 9 页，“古诗词”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求由诗句支持情感判断，进一步解释情感变化、复合情绪与多义；典型观察是比较两种情感候选及其证据，避免用作者标签套固定情感。
- 候选 definition：**能够依据诗词中的意象、关键字词和诗句证据，判断并解释作品的情感、情感变化与主旨，同时处理复合情绪或多种可能解释。**
- 候选 assessment_focus：情感或主旨判断是否有诗句证据；是否解释证据与结论的关系；能否比较候选解释、识别反例并避免作者标签化。
- 候选 evidence_requirements：明确的情感或主旨结论；与结论相关的关键字词或诗句；对至少两个候选解释的证据比较；在同意象不同作品中的迁移表现。
- 与相邻能力的边界：相邻 ability_id 为 PO01、PO03、RD05。相似点是都使用文本证据；PO02 的核心边界是诗词情感与主旨的证据化解释，PO01 停留在情境画面，PO03 解释语言形式效果，RD05 提供跨领域的一般证据机制。需人工确认“主旨”与“情感”是否应在子字段中分开观察。
- 可信度：HIGH
- 风险或疑问：复合情绪和多义解释可能使候选 assessment_focus 过宽，需审校最低充分证据标准。
- needs_review：`true`
- 人工审核结论：PENDING

## PO03 炼字手法与表达效果

- domain_code：PO
- 当前 definition：`null`
- 当前已有字段：`ability_name=炼字手法与表达效果`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 9 页，“古诗词”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求通过换词感受差异，结合语境解释并评价审美选择；达标表现是不依赖模板完成“形式—意义”解释，而非堆砌术语。
- 候选 definition：**能够结合诗词语境，通过比较替换等方式辨析关键字词或表达手法带来的意义差异，并解释其对整体表达和审美效果的作用。**
- 候选 assessment_focus：能否指出具体语言形式；能否说明替换前后的意义差异；能否把局部形式与整体表达效果连接起来，而非只报手法名称。
- 候选 evidence_requirements：原表达与可比替换的差异说明；对关键字词或手法的语境证据；完整的“形式—意义—整体作用”解释。
- 与相邻能力的边界：相邻 ability_id 为 PO02、RD08。相似点是都解释语言和审美效果；PO03 的核心边界是古诗词中的炼字与手法，RD08 是跨现代文材料的语言鉴赏、比较评价与审美解释，PO02 处理情感主旨证据。需人工确认 PO03 与 RD08 是否按文体分域，还是另有认知动作差异。
- 可信度：HIGH
- 风险或疑问：与 RD08 的语义高度相似，是本轮明显能力边界风险之一。
- needs_review：`true`
- 人工审核结论：PENDING

## PO04 比较阅读与诗文互证

- domain_code：PO
- 当前 definition：`null`
- 当前已有字段：`ability_name=比较阅读与诗文互证`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 9 页，“古诗词”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从简单同异发展到按统一维度比较，再分析立场和条件差异；训练要求对两个文本对称取证，达标覆盖诗—诗与诗—文迁移。
- 候选 definition：**能够在诗—诗或诗—文阅读中确定共同的比较维度，分别提取对应证据，解释作品在内容、情感、表达或立场上的异同及其条件。**
- 候选 assessment_focus：比较维度是否统一；是否对两个文本对称取证；是否解释异同而非分别复述；能否说明立场或条件差异。
- 候选 evidence_requirements：明确的共同比较维度；来自双方文本的对应证据；基于证据的异同解释；诗—诗及诗—文材料中的迁移表现。
- 与相邻能力的边界：相邻 ability_id 为 PO02、PO03、RD03。相似点是都可能整合多份证据；PO04 的核心边界是含诗词的对称比较与诗文互证，RD03 是一般多材料关系建模，PO02/03 提供单篇情感和语言解释基础。需人工确认“内容、情感、表达、立场”是否作为开放维度而非固定全选项。
- 可信度：HIGH
- 风险或疑问：若不限定含诗词材料，定义会与 RD03 重复。
- needs_review：`true`
- 人工审核结论：PENDING

## WR02 立意与问题意识

- domain_code：WR
- 当前 definition：`null`
- 当前已有字段：`ability_name=立意与问题意识`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 9 页，“写作”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从围绕中心发展到由经历提炼认识，再发现矛盾、条件并形成观点；典型任务是对同一材料提出多个立意，达标要求立意可被全文材料持续支撑。
- 候选 definition：**能够从写作任务、材料或经历中提炼值得表达的问题，识别其中的矛盾与条件，形成范围适当且能被全文材料持续支撑的中心认识或观点。**
- 候选 assessment_focus：是否从任务或材料中提出真实问题；立意是否避免口号化、绝对化；范围是否适当；全文材料能否持续支撑中心。
- 候选 evidence_requirements：同一材料的多个候选立意及取舍理由；立意与材料之间的支撑关系；换材料或条件后重新限定观点的表现。
- 与相邻能力的边界：相邻 ability_id 为 WR01、RD06、WR06。相似点是都处理任务、条件或观点；WR02 的核心边界是生成写作中心和问题意识，WR01 识别任务约束，RD06 判断推断边界，WR06 负责展开和修订论证。需人工确认叙事类“中心认识”和议论类“观点”是否采用同一字段表达。
- 可信度：HIGH
- 风险或疑问：若把完整论证纳入 definition，会侵入 WR06；候选定义只保留立意生成与可支撑性。
- needs_review：`true`
- 人工审核结论：PENDING

## WR03 选材细节与真实性

- domain_code：WR
- 当前 definition：`null`
- 当前已有字段：`ability_name=选材细节与真实性`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 10 页，“写作”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从具体经历中选择和取舍细节，并权衡真实性、典型性与原创性；训练筛选维度为相关、具体、新鲜、可证，达标要求换立意后重新评估素材。
- 候选 definition：**能够依据写作目的和立意，选择、取舍并组织真实、相关且具体的素材与细节，同时判断其典型性、原创性和可验证边界。**
- 候选 assessment_focus：素材是否支撑立意；细节是否具体、真实和可证；是否存在万能素材、虚构细节或失去相关性的堆砌；立意变化后能否重新取舍。
- 候选 evidence_requirements：候选素材的筛选与取舍理由；素材真实性及来源说明；具体细节与立意的对应关系；换立意后的重新评估记录。
- 与相邻能力的边界：相邻 ability_id 为 BA04、WR02、WR05。相似点是都涉及材料调用或细节；WR03 的核心边界是写作素材的选择、真实性与取舍，BA04 是文化语言材料积累，WR02 决定立意，WR05 负责把选定素材转化为叙事描写和个性语言。需人工确认“原创性”是素材属性还是写作责任的一部分。
- 可信度：HIGH
- 风险或疑问：真实性与原创性可能与 WR06 的事实/原创责任交叉，需按叙事素材和论证来源区分。
- needs_review：`true`
- 人工审核结论：PENDING

## WR04 结构组织与段落推进

- domain_code：WR
- 当前 definition：`null`
- 当前已有字段：`ability_name=结构组织与段落推进`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 10 页，“写作”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从基本顺序发展到详略照应和复杂叙事/论证层级；训练使用段落功能和关系箭头，达标要求全文持续推进并能解释每段功能。
- 候选 definition：**能够围绕中心安排内容顺序、详略、照应和层级关系，使各段承担明确功能并推动叙事、说明或论证持续展开。**
- 候选 assessment_focus：段落是否服务中心；段与段之间是否存在推进关系；详略、照应和层级是否合理；是否能解释每段不可替代的功能。
- 候选 evidence_requirements：全文或提纲中的段落功能标注；段落关系说明；删除、换序或重组后的影响判断；能够解释全文如何持续推进。
- 与相邻能力的边界：相邻 ability_id 为 LU02、RD07、WR02、WR03。相似点是都处理逻辑或结构；WR04 的核心边界是写作生成过程中的全文组织，LU02 偏句段衔接，RD07 分析既有文本结构，WR02/03 提供中心与素材。需人工确认“段落推进”是否覆盖篇章内句群组织。
- 可信度：HIGH
- 风险或疑问：与 RD07 近似，但一项是生成结构、一项是分析结构；正式定义应保留这一方向差异。
- needs_review：`true`
- 人工审核结论：PENDING

## WR05 叙事描写与个性表达

- domain_code：WR
- 当前 definition：`null`
- 当前已有字段：`ability_name=叙事描写与个性表达`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 10 页，“写作”能力表及其后 AI 写作责任说明。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求由写清楚和具体细节发展到用细节表现变化，再控制视角、节奏与风格；达标表现是具有个人观察和可辨识语言，常见风险是形容词堆砌和“AI 腔”。
- 候选 definition：**能够运用具体动作、环境和感官等细节呈现人物、事件或情绪变化，并通过视角、节奏和语言选择形成基于个人观察的叙事与表达风格。**
- 候选 assessment_focus：是否以可观察细节代替抽象标签；细节是否推动人物或事件变化；视角和节奏是否稳定；语言是否具有个人观察而非套话或 AI 腔。
- 候选 evidence_requirements：一段以具体细节呈现变化的叙事文本；对视角、节奏或语言选择的解释；删除套话后的修订对比；跨题材仍能保持真实观察。
- 与相邻能力的边界：相邻 ability_id 为 WR03、WR04、RD08。相似点是都涉及细节、语言和效果；WR05 的核心边界是生成叙事描写和个性语言，WR03 选择真实素材，WR04 组织篇章，RD08 分析他人文本的语言效果。需人工确认“个性表达”是否也覆盖非叙事文体。
- 可信度：HIGH
- 风险或疑问：能力名称以“叙事描写”为主，但“个性表达”可能被解释为跨文体，范围需人工确认。
- needs_review：`true`
- 人工审核结论：PENDING

## WR06 观点证据论证与修改责任

- domain_code：WR
- 当前 definition：`null`
- 当前已有字段：`ability_name=观点证据论证与修改责任`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`；`北京语文小初高贯通完整能力研究 V1.1：补章、补字段、补证据与 SKILL 落地.pdf`
- 页码或章节：前者第 10 页“写作”能力表；后者第 5 页 WR06-A—F 子技能。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求构成“观点—证据—解释”，进一步处理反例、条件、证据质量与来源，并在新主题中独立论证、承担事实和原创责任。V1.1 将其拆为观点限定、证据相关性、推理链、反例修正、来源核验和 AI 辅助写作责任 6 个子技能。
- 候选 definition：**能够提出范围适当的观点，选择并核验相关证据，建立清晰的推理链，回应反例与条件限制，并在修订和 AI 辅助过程中对事实准确性与原创表达承担责任。**
- 候选 assessment_focus：观点是否有边界；证据是否真实、相关且充分；推理是否连接观点与证据；是否处理反例和条件；是否核验来源并保留自主修改责任。
- 候选 evidence_requirements：陌生主题下的独立短论证；观点、证据和推理的可追踪对应；反例或条件处理；来源核验记录；初稿到修订稿的修改记录及原创责任说明。
- 与相邻能力的边界：相邻 ability_id 为 RD05、RD06、RD07、OC03、WR02。相似点是都涉及观点、证据、推断或来源；WR06 的核心边界是在写作成品中整合论证并承担修改责任，RD05/06/07 分别提供阅读中的证据、推断与论证链分析，OC03 提供资料核验，WR02 生成立意。需人工确认 6 个子技能是否允许在一个主能力定义中全部并列。
- 可信度：MEDIUM
- 风险或疑问：范围较宽，存在把多个可独立失败的动作合并为单一状态的风险；正式定义需与子技能状态分开。
- needs_review：`true`
- 人工审核结论：PENDING

## OC01 倾听、复述、提问与对话

- domain_code：OC
- 当前 definition：`null`
- 当前已有字段：`ability_name=倾听、复述、提问与对话`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 11 页，“口语交际与综合性学习”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求准确复述口头信息，区分事实与观点并追问，进一步识别前提、歧义与信息缺口；常见错误是把复述变成评价，达标要求对陌生口头材料提出有效问题。
- 候选 definition：**能够准确倾听并复述口头信息，区分事实与观点，识别其中的前提、歧义或信息缺口，并据此提出有效问题、参与对话。**
- 候选 assessment_focus：复述是否准确完整且不夹带评价；能否区分事实和观点；问题是否针对真实信息缺口；对话回应是否基于对方实际表达。
- 候选 evidence_requirements：陌生口头材料的要点复述；事实与观点区分；针对前提、歧义或缺口提出的问题；后续对话中的有效回应。
- 与相邻能力的边界：相邻 ability_id 为 RD01、OC02。相似点是都处理信息和回应；OC01 的核心边界是口头输入的准确接收、复述和追问，RD01 主要处理阅读材料的信息定位，OC02 负责较完整的口头说明、发言和协作。需人工确认“对话”是否仅指基于倾听的追问与回应。
- 可信度：HIGH
- 风险或疑问：若把完整立场表达纳入“对话”，会侵入 OC02。
- needs_review：`true`
- 人工审核结论：PENDING

## OC02 说明、发言、演讲、讨论与合作

- domain_code：OC
- 当前 definition：`null`
- 当前已有字段：`ability_name=说明、发言、演讲、讨论与合作`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`
- 页码或章节：第 11 页，“口语交际与综合性学习”能力表。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从有顺序说明发展到“观点+证据+回应”，再到现场调整和处理异议；达标表现是倾听、回应并共同形成结论。
- 候选 definition：**能够根据对象和目的组织口头说明、发言或演讲，以观点和证据参与讨论，准确回应他人意见，并根据现场反馈调整表达、协作形成结论。**
- 候选 assessment_focus：口头表达是否有目的和结构；观点是否有证据；是否准确复述并回应他人；能否处理异议、现场调整并参与共同结论形成。
- 候选 evidence_requirements：结构清楚的口头说明或立场发言；观点与证据的对应；讨论中对他人意见的准确回应；根据反馈调整表达或共同形成结论的记录。
- 与相邻能力的边界：相邻 ability_id 为 LU01、OC01、WR06。相似点是都涉及对象、表达和论证；OC02 的核心边界是现场口头表达与合作，LU01 侧重语言得体选择，OC01 侧重倾听复述追问，WR06 侧重书面论证与修改责任。需人工确认演讲与讨论是否共享同一最低证据要求。
- 可信度：HIGH
- 风险或疑问：能力名称覆盖多种口语场景，正式 assessment_focus 可能需要按独白和互动任务分层。
- needs_review：`true`
- 人工审核结论：PENDING

## OC03 信息搜集核验、调查与跨学科呈现

- domain_code：OC
- 当前 definition：`null`
- 当前已有字段：`ability_name=信息搜集核验、调查与跨学科呈现`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`；`北京语文小初高贯通完整能力研究 V1.1：补章、补字段、补证据与 SKILL 落地.pdf`
- 页码或章节：前者第 11 页“口语交际与综合性学习”能力表；后者第 5—6 页 OC03-A—G 子技能。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求搜集、判断来源、整合信息并评估证据质量、偏差和不确定性，最后独立完成小研究和答辩。V1.1 将其拆为关键词设计、原始来源识别、来源分级与交叉核验、调查与数据采集、证据边界、成果呈现和答辩 7 个子技能。
- 候选 definition：**能够围绕真实问题设计检索或调查，识别并交叉核验原始来源，采集、整合和解释信息或数据及其边界，并以跨学科成果进行呈现和答辩。**
- 候选 assessment_focus：问题与检索设计是否匹配；能否找到原始来源并分级核验；数据解释是否承认偏差和不确定性；成果是否可追溯；能否回应质疑。
- 候选 evidence_requirements：检索关键词或调查设计；可追溯的原始来源与交叉核验记录；数据采集和边界说明；完整成果呈现；针对质疑的现场或书面回应。
- 与相邻能力的边界：相邻 ability_id 为 RD01、RD03、OC02、WR06。相似点是都涉及信息、整合、表达或来源；OC03 的核心边界是完成从问题、来源、调查到成果与答辩的综合研究流程，RD01/03 处理信息辨识与材料关系，OC02 处理口头交流，WR06 使用核验后的证据完成论证。需人工确认主能力定义是否应保留完整流程，还是仅定义统摄目标并由 7 个子技能承担细节。
- 可信度：MEDIUM
- 风险或疑问：范围最宽之一，且“跨学科”可能使能力边界扩张；不得把它表述为北京语文官方新增考点。
- needs_review：`true`
- 人工审核结论：PENDING

## MC01 计划预习与任务分解

- domain_code：MC
- 当前 definition：`null`
- 当前已有字段：`ability_name=计划预习与任务分解`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`；`北京语文小初高贯通完整能力研究 V1.1：补章、补字段、补证据与 SKILL 落地.pdf`
- 页码或章节：前者第 11 页“学习策略与元认知”能力表；后者第 6—7 页能力依赖与学习科学说明。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求设置小目标、预判难点、选择方法并动态调整策略；训练围绕目标、难点、方法、用时和可观察产出，达标要求在新领域自主选择策略。
- 候选 definition：**能够为学习任务设定可观察的目标，预判难点，选择适当策略，并将任务分解为可执行步骤和时间安排，再根据进展调整计划。**
- 候选 assessment_focus：目标是否具体可观察；是否识别难点并选择匹配方法；步骤和时间是否可执行；能否根据实际进展调整而非机械照表完成。
- 候选 evidence_requirements：包含目标、难点、方法、步骤和时间的计划；执行过程中的调整记录；复盘说明；在新领域中自主选择策略的表现。
- 与相邻能力的边界：相邻 ability_id 为 WR01、WB01、MC02。相似点是都涉及任务或计划；MC01 的核心边界是跨领域的学习过程规划，WR01 理解写作任务约束，WB01 规划整本书阅读进度，MC02 监控执行和诊断错误。需人工确认“预习”是否保留在名称中但不单独扩张定义。
- 可信度：HIGH
- 风险或疑问：若定义过于通用，可能难以形成语文学科内可观察证据；候选 evidence_requirements 需人工校准。
- needs_review：`true`
- 人工审核结论：PENDING

## MC02 自我监控、错因诊断与修订

- domain_code：MC
- 当前 definition：`null`
- 当前已有字段：`ability_name=自我监控、错因诊断与修订`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`；`北京语文小初高贯通完整能力研究 V1.1：补章、补字段、补证据与 SKILL 落地.pdf`
- 页码或章节：前者第 12 页“学习策略与元认知”能力表；后者第 6—8 页能力依赖、首答—修订—迁移流程。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求从提示下找错发展到区分主要错因、自主修改，并监控证据和思维偏差；记录链为初答、错因、提示和修订，达标要求同一错因在换材料后显著减少。
- 候选 definition：**能够监控自己的理解与作答过程，依据初答和证据定位信息、证据、推理或表达等主要错因，并据此自主修订，在新材料中减少同类错误。**
- 候选 assessment_focus：是否保留并比较初答与修订；错因是否具体而非笼统归为“粗心”；修订是否针对主要原因；换材料后是否减少同类错误。
- 候选 evidence_requirements：可追踪的初答—错因—提示—修订记录；对主要错因的分类与理由；自主修订结果；陌生材料中同类错误减少的后续证据。
- 与相邻能力的边界：相邻 ability_id 为 LU03、RD05、MC01、MC03。相似点是都可能包含修改或证据检查；MC02 的核心边界是跨能力的自我监控和错因诊断，LU03 修订语言表达问题，RD05 检查证据解释，MC01 负责事前计划，MC03 负责延迟提取与迁移。需人工确认“思维偏差”是否需要独立观察字段。
- 可信度：HIGH
- 风险或疑问：同一修订行为可同时证明具体能力和 MC02，数据记录时必须区分“修订内容”与“自我诊断过程”。
- needs_review：`true`
- 人工审核结论：PENDING

## MC03 Feynman 式复述、间隔复测与迁移

- domain_code：MC
- 当前 definition：`null`
- 当前已有字段：`ability_name=Feynman 式复述、间隔复测与迁移`；`architecture_type=operational_domain`；`assessment_focus=null`；`evidence_requirements=null`；`version=1.1`；`status=active`。
- 来源文件：`北京语文小初高贯通完整能力研究与 AI 辅导实施框架（2026—2029）.pdf`；`北京语文小初高贯通完整能力研究 V1.1：补章、补字段、补证据与 SKILL 落地.pdf`
- 页码或章节：前者第 12 页“学习策略与元认知”能力表；后者第 7—8 页学习科学证据、复测流程和状态规则。
- 依据类型：RESEARCH_SYNTHESIS
- 关键依据摘要：研究表要求学生能说明“怎么做”，延迟后无提示完成同构陌生任务，并解释方法边界、跨领域迁移。V1.1 强调主动提取、分散复测和迁移，但明确固定复测日程及统一 Feynman 官方协议都不能由研究推出。
- 候选 definition：**能够用自己的话解释所学方法及其适用条件和边界，在间隔后主动提取该方法，并在无提示情况下将其迁移到陌生材料或不同情境。**
- 候选 assessment_focus：能否脱离题型名称解释方法；是否说明适用条件与边界；间隔后能否重新提取；是否在陌生材料或跨领域任务中独立使用，而非只完成同型练习。
- 候选 evidence_requirements：闭卷方法复述或教学式解释；间隔后的无提示复测；陌生材料的近迁移证据；不同情境或领域中的进一步迁移证据；对方法不适用情形的说明。
- 与相邻能力的边界：相邻 ability_id 为 MC02，以及状态 S4、S5、S6。相似点是都涉及修订、迁移、延迟稳定或方法边界；MC03 的核心边界是学生主动使用的自我解释、提取与迁移策略，S4—S6 是证据支持的能力状态等级，不是能力本身。需人工确认 MC03 是否应继续将三种机制合并为一项主能力。
- 可信度：MEDIUM
- 风险或疑问：“Feynman 式复述”不是统一官方科学协议；复测间隔必须自适应，不得把项目默认窗口写进定义。
- needs_review：`true`
- 人工审核结论：PENDING

## 汇总与人工处理建议

- COMPLETE_CANDIDATE：17
- PARTIAL_CANDIDATE：0
- INSUFFICIENT：0
- DIRECT_EXTRACT：0
- RESEARCH_SYNTHESIS：17
- HIGH：14
- MEDIUM：3
- LOW：0
- 明显能力边界风险：CL04、PO03、WR04、WR06、OC03、MC02、MC03。
- 未找到充分依据：无。

建议人工审核时逐项选择“接受、修改、退回补证”之一；只有审核结论不再是 `PENDING` 后，才进入正式能力主数据更新阶段。本文件本身不构成定义冻结。
