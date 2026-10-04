# 人类通信

## 两条通信线

| 文件 | 层面 | 用途 |
|---|---|---|
| `inbox.md` | 业务面 | 人类补充 Goal、Story 优先级、资源和边界 |
| `questions.md` | 业务面 | Story 需要人类做业务判断 |
| `escalations.md` | 管控面 | 权限、认证、网络、磁盘、进程、配额或基础设施异常 |

人类输入由 Project Supervisor 在下一次激活时吸收。处理后保留原文，并写清处理时间、采取的动作、影响的 Story 和优先级变化。

## Questions

需要人类做业务决定时，先把 Story 现场保存到对应 `stories/<story-id>.md`，再写入 `questions.md`。每个问题必须包括：

- Story ID、标题以及它与长期 Goal 的关系；
- 已完成内容和可信证据；
- 为什么 Agent 不能自行决定；
- 可选方案、权衡和建议；
- 不回答会造成什么影响；
- 人类只需要回复的最小问题；
- 回答后如何恢复 Story。

写完 Question 后把 Story 标记为 `waiting`、`waiting_on: human`，关闭当前 Story 实际创建的角色和 Story Supervisor session。人类回复被吸收后，将 Story 改回 `ready`，使用新的 session 和 `team.md` 当前启用的角色继续同一个 Story。

## Escalations

环境、权限、认证、网络、磁盘、进程、配额或基础设施阻塞时写入 `escalations.md`。同样关联 Story ID，说明发生了什么、影响、证据、已尝试的安全恢复、人类需要做什么和恢复验证。

写入 Escalation 前保存 Story 正文，标记 `waiting_on: control` 并关闭 Story session。不要在异常现场无上限重试或自动改变认证、模型和系统配置。

## 外部等待

等待 CI、review、数据发布或外部服务时，把 Story 标记为 `waiting_on: external`，正文写清等待对象、最近检查时间、恢复条件和下一步。长期等待不保留 TUI session。
