# Claude Code Skills Extract

从 Claude Code 可复用工作流中提取出来的独立 skill 合集，面向公开分发、独立维护和多智能体复用。

[English](./README.md) | 简体中文

## 这个项目是什么

这个仓库把 Claude Code 中高价值、可重复使用的工作流整理成独立 skill，并以公开项目标准进行打磨：

- 每个 skill 都可以独立作为 GitHub 项目维护
- 每个 skill 都可以作为智能体能力单独安装和分发
- 每个 skill 都保留来源说明、能力边界和质量标准
- 每个 skill 都提供中英文 README，方便国际化使用

## 你会得到什么

- `20` 个独立 skill
- 一个总览型合集仓库，便于发现、治理和批量生成
- 每个 skill 对应一个独立 GitHub 仓库，命名为 `<skill-slug>-skill`
- ClawHub 发布脚本与自动续发机制
- 提取来源映射和公开目录页

## 独立 Skill 仓库

| Skill | GitHub |
|---|---|
| `batch-migration-orchestrator` | [batch-migration-orchestrator-skill](https://github.com/wimi321/batch-migration-orchestrator-skill) |
| `chrome-web-automation` | [chrome-web-automation-skill](https://github.com/wimi321/chrome-web-automation-skill) |
| `claude-api-builder` | [claude-api-builder-skill](https://github.com/wimi321/claude-api-builder-skill) |
| `claude-md-initializer` | [claude-md-initializer-skill](https://github.com/wimi321/claude-md-initializer-skill) |
| `claude-settings-editor` | [claude-settings-editor-skill](https://github.com/wimi321/claude-settings-editor-skill) |
| `code-simplifier` | [code-simplifier-skill](https://github.com/wimi321/code-simplifier-skill) |
| `git-commit-pr-workflow` | [git-commit-pr-workflow-skill](https://github.com/wimi321/git-commit-pr-workflow-skill) |
| `git-commit-workflow` | [git-commit-workflow-skill](https://github.com/wimi321/git-commit-workflow-skill) |
| `keybindings-customizer` | [keybindings-customizer-skill](https://github.com/wimi321/keybindings-customizer-skill) |
| `memory-landscape-review` | [memory-landscape-review-skill](https://github.com/wimi321/memory-landscape-review-skill) |
| `pull-request-reviewer` | [pull-request-reviewer-skill](https://github.com/wimi321/pull-request-reviewer-skill) |
| `recurring-loop-runner` | [recurring-loop-runner-skill](https://github.com/wimi321/recurring-loop-runner-skill) |
| `remote-agent-scheduler` | [remote-agent-scheduler-skill](https://github.com/wimi321/remote-agent-scheduler-skill) |
| `runtime-verifier` | [runtime-verifier-skill](https://github.com/wimi321/runtime-verifier-skill) |
| `security-review-workflow` | [security-review-workflow-skill](https://github.com/wimi321/security-review-workflow-skill) |
| `session-debug-log-investigator` | [session-debug-log-investigator-skill](https://github.com/wimi321/session-debug-log-investigator-skill) |
| `statusline-setup` | [statusline-setup-skill](https://github.com/wimi321/statusline-setup-skill) |
| `stuck-session-diagnosis` | [stuck-session-diagnosis-skill](https://github.com/wimi321/stuck-session-diagnosis-skill) |
| `verifier-skill-generator` | [verifier-skill-generator-skill](https://github.com/wimi321/verifier-skill-generator-skill) |
| `workflow-skillify` | [workflow-skillify-skill](https://github.com/wimi321/workflow-skillify-skill) |

## 质量标准

每个公开 skill 都至少包含：

- `SKILL.md`
- `agents/openai.yaml`
- 双语 README
- 输入、输出、成功标准和非目标
- 来源说明
- 独立许可证和可公开维护的仓库结构

## 重要文件

- [README.md](/Users/haoc/Developer/cc-mg55/README.md)
- [docs/CATALOG.md](/Users/haoc/Developer/cc-mg55/docs/CATALOG.md)
- [docs/PUBLISHING.md](/Users/haoc/Developer/cc-mg55/docs/PUBLISHING.md)
- [EXTRACTION_REPORT.md](/Users/haoc/Developer/cc-mg55/EXTRACTION_REPORT.md)
- [CLAWHUB_PUBLISH_STATUS.md](/Users/haoc/Developer/cc-mg55/CLAWHUB_PUBLISH_STATUS.md)

## 使用方式

### 作为合集使用

从 `skills/` 目录中挑选需要的 skill，安装到兼容的智能体环境中。

### 作为独立仓库使用

直接克隆对应的 `*-skill` 仓库，并将仓库根目录作为 skill 根目录使用。

### 发布到 ClawHub

使用：

```bash
./publish_clawhub.sh
```

限流后继续：

```bash
./resume_clawhub_publish.sh
```

后台自动重试：

```bash
./auto_resume_publish.sh
```
