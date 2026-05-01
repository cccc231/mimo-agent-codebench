# MiMo Agent CodeBench

MiMo Agent CodeBench is an open-source multi-agent workflow for automated software engineering tasks. It focuses on GitHub issue understanding, repository-level code search, patch generation, test execution, evaluation reporting, and reproducible agent logs.

The project is designed to evaluate how AI coding agents perform on real-world software maintenance tasks, including bug fixing, test generation, refactoring, documentation updates, and performance optimization.

## 核心定位

- 面向中大型开源代码库的多 Agent 自动化研发与评测平台。
- 解决 issue 理解、代码检索、修复规划、代码修改、测试验证、报告沉淀流程中的高成本与低复现问题。
- 支持可审计实验：自动保存 Prompt、补丁、测试结果、日志与评测结论。

## Core Workflow

1. Parse GitHub issues and extract requirements
2. Search and summarize relevant code files
3. Generate repair or refactoring plans
4. Apply code changes through an agentic workflow
5. Run unit tests and static checks
6. Generate structured evaluation reports
7. Save prompts, logs, patches, and metrics for review

## 多 Agent 协作流水线

- 需求理解 Agent：解析 issue，识别目标、约束与验收标准。
- 代码检索 Agent：结合仓库结构进行相关文件定位与上下文摘要。
- 修复规划 Agent：输出分步修复方案与风险评估。
- 代码修改 Agent：按计划实施补丁并保持最小改动面。
- 测试验证 Agent：执行单测/静态检查并定位失败根因。
- 报告生成 Agent：沉淀评测记录、复盘信息与 PR 总结。

## Why Token Plan Is Needed

The project requires large-scale token usage for long-context repository understanding, multi-agent reasoning, repeated patch generation, test failure analysis, and cross-model evaluation. The 1.6B token plan will be used to run reproducible experiments across multiple open-source repositories and publish benchmark results.

## 16 亿 Token 使用规划

- Issue 解析与仓库检索：4 亿
- 长链推理与补丁生成：6 亿
- 测试迭代与失败复盘：3 亿
- 多模型对比评测：2 亿
- 日志沉淀与报告生成：1 亿

## AI 开发 / Agent 工具（可填）

- Cline：开源 IDE 编程 Agent。
- LangGraph：用于构建可控的 Agent 图工作流。
- SWE-agent：面向 GitHub issue 自动修复。
- OpenHands：开源 AI 软件开发 Agent，可作为技术参考与依赖。
- 兼容生态：Claude Code、Codex、Cursor 等。

## 仓库结构

```text
docs/
  architecture.png
  workflow.md
prompts/
  issue_triage.md
  code_repair.md
  test_generation.md
scripts/
  run_agent.py
  run_eval.py
  collect_logs.py
examples/
  demo_issue.md
  demo_report.md
logs/
  sample_run.md
```

## 材料清单

1. 项目架构图与 Agent 工作流图。
2. README、Prompt 模板、评测脚本与样例日志。
3. 终端运行日志：展示从 issue 解析、代码检索、补丁生成到测试验证的闭环流程。
4. 持续提交真实仓库修复案例、评测报告与失败案例复盘。
