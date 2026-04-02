# Claude Code Skills Extract

A production-ready collection of standalone skills extracted from reusable Claude Code workflows and repackaged as public skills for agent ecosystems.

English | [简体中文](./README.zh-CN.md)

## Why This Project Exists

Claude Code contains many strong internal workflows that are useful far beyond a single product surface. This repository turns the best of those workflows into standalone, documented, distributable skills that can be:

- installed locally in compatible agent runtimes
- published through registries such as ClawHub
- maintained as independent GitHub projects
- reused across repositories, teams, and automation setups

The goal is not to dump prompts. The goal is to ship public-quality skill artifacts with clear contracts, provenance, and distribution paths.

## What You Get

- `20` extracted standalone skills
- one collection repository for discovery and governance
- one independent GitHub repository per skill
- local generation scripts for rebuilding standalone repositories
- ClawHub publishing automation for registry rollout
- provenance mapping back to the analyzed Claude Code source snapshot

## Skill Families

| Family | Skills |
|---|---|
| Planning and Orchestration | `batch-migration-orchestrator`, `workflow-skillify`, `verifier-skill-generator` |
| Coding and Git | `code-simplifier`, `git-commit-workflow`, `git-commit-pr-workflow`, `pull-request-reviewer`, `security-review-workflow` |
| Runtime and Diagnostics | `runtime-verifier`, `session-debug-log-investigator`, `stuck-session-diagnosis` |
| Browser and API | `chrome-web-automation`, `claude-api-builder` |
| Agent Ops and Config | `claude-md-initializer`, `claude-settings-editor`, `keybindings-customizer`, `memory-landscape-review`, `recurring-loop-runner`, `remote-agent-scheduler`, `statusline-setup` |

## Standalone Skill Repositories

Every extracted skill is also prepared as an independent GitHub repository under `wimi321`, using the naming convention `<skill-slug>-skill`.

| Skill | Independent Repo |
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

## Published to ClawHub

ClawHub publish progress is tracked in [CLAWHUB_PUBLISH_STATUS.md](./CLAWHUB_PUBLISH_STATUS.md).

Already published:

- `batch-migration-orchestrator`
- `chrome-web-automation`
- `claude-api-builder`
- `claude-md-initializer`
- `claude-settings-editor`

The remaining skills are queued behind the current ClawHub new-skill rate limit and are being resumed automatically.

## Repository Structure

- `skills/`: canonical extracted skill set
- `docs/CATALOG.md`: public catalog with repository links
- `docs/PUBLISHING.md`: publishing workflow and operational notes
- `EXTRACTION_REPORT.md`: source-module to skill mapping
- `CLAWHUB_PUBLISH_STATUS.md`: publish progress and automation status
- `generate_skills.py`: deterministic generator for the current skill set
- `build_standalone_repos.py`: builds standalone repository copies locally
- `sync_all_standalone_repos.py`: creates, syncs, and pushes independent repos
- `publish_clawhub.sh`: full registry publish script
- `resume_clawhub_publish.sh`: resume script for rate-limited follow-up publishes
- `auto_resume_publish.sh`: unattended retry loop for ClawHub publishing

## Quality Standard

Each public skill is shipped as a maintained artifact, not a raw prompt snippet.

Every skill includes:

- clean YAML frontmatter
- `agents/openai.yaml` metadata for agent UIs
- clear trigger description and workflow guidance
- example requests
- explicit inputs and outputs
- success criteria and non-goals
- provenance back to the analyzed Claude Code source module
- a standalone repository with its own README and license
- bilingual English and Simplified Chinese documentation

## How To Use

### Use from the collection

Copy any skill directory from `skills/<slug>/` into a compatible local skill workspace.

### Use as a standalone repository

Clone the independent repository for the skill you want and use the repository root as the skill root.

If you want to regenerate all standalone repositories locally from this collection, use `build_standalone_repos.py`.

### Publish through ClawHub

Run:

```bash
./publish_clawhub.sh
```

If ClawHub rate-limits new skill creation:

```bash
./resume_clawhub_publish.sh
```

For unattended retries:

```bash
./auto_resume_publish.sh
```

## Source and Provenance

These skills were derived by reading a local Claude Code source snapshot and extracting only the modules that map cleanly onto standalone public skills.

See [EXTRACTION_REPORT.md](./EXTRACTION_REPORT.md) for the exact mapping and [docs/CATALOG.md](./docs/CATALOG.md) for the public-facing skill inventory.
