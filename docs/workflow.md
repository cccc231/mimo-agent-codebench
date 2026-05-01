# Agent Workflow

## 目标

构建一个可复现、可审计、可扩展的多 Agent 软件工程自动化流程。

## 流程阶段

1. **Issue Intake**：读取 GitHub issue（标题、正文、标签、复现信息）。
2. **Repository Recon**：分析目录结构、语言栈、测试框架与关键模块。
3. **Context Retrieval**：检索相关代码片段并生成任务上下文。
4. **Patch Planning**：生成修复计划与执行步骤。
5. **Patch Execution**：进行最小可行补丁修改。
6. **Validation**：执行单元测试和静态检查。
7. **Reporting**：输出评测报告、日志索引、失败复盘与 PR 摘要。

## 输入输出

- 输入：issue 文本、仓库路径、运行配置。
- 输出：补丁、测试结果、评测报告、日志与复盘记录。
