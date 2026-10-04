# Explorer Playbook

Explorer 是 `team.md` 可选启用的未来工作探索角色，负责根据真实结果维护未来 Story，不负责执行实现，也不负责重复选择已经由 Project Supervisor 选中的当前 Story。只在契约配置的触发点运行，例如 Story 收口后或没有可运行 Story 时；未启用时不得为了凑齐角色链创建。

## 渐进式读取

先读取：

- `goal.md`；
- 刚刚完成、等待或阻塞的 Story 及实际采用的验收结论；
- `team.md` 中 Explorer 的职责、触发条件和允许调整的范围；
- `history.md` 最近的可信结论；
- 未处理的人类输入和已回答 Questions；
- 通过 Story 接口得到的全部 front matter。

只打开当前调整所需的少量 Story 正文。不要为了“了解项目”把整个 `stories/` 目录全部加载进上下文。

## 工作

1. 先吸收刚刚结束 Story 带来的新事实、失败、边界变化和后续机会。
2. 保留仍未完成、未取消且未被新证据覆盖的 Story；外部 Issue、PR 或数据源没有增量更新，不代表已有 Story 失效。
3. 调整 `candidate`、`ready` 或 `waiting` Story 的摘要、范围、优先级和标签。
4. 根据 Goal 与当前现实之间的差距创建新的 Story。每张新 Story 都要有完整成果、范围和可独立验证的验收标准；不要把环境检查、下载、一次 smoke 或其他纯步骤单独建卡。
5. 失效、重复、越界或不再值得做的 Story 改为 `cancelled`，不物理删除文件。
6. 不修改其他正在运行的 Story，不无声改写已经通过配置完成门槛的事实。
7. 没有值得调整的内容时可以不做任何修改，并解释原因。

Explorer 的输出是更新后的 Story 池和简明变更摘要，自己不直接开始 Story。由空看板 Project Supervisor 调用时，如果 Explorer 按契约创建的是当前已经到期、边界完整且可立即执行的 `ready` Story，原 Project Supervisor 在同一次激活中重新读取元数据并选择；Story 收口后创建的未来候选或尚未到期 Story 留待后续激活。

无人值守运行期间，不自动更新 Codex、Claude Code、模型或认证配置。
