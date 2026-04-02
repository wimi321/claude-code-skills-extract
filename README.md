# Claude Code Skills Extract

A production-ready collection of standalone skills extracted from reusable Claude Code workflows and repackaged as public skills for agent ecosystems.

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

Every extracted skill is also prepared as an independent GitHub repository under `wimi321`, using the naming convention `claude-code-<skill-slug>`.

| Skill | Independent Repo |
|---|---|
| `batch-migration-orchestrator` | [claude-code-batch-migration-orchestrator](https://github.com/wimi321/claude-code-batch-migration-orchestrator) |
| `chrome-web-automation` | [claude-code-chrome-web-automation](https://github.com/wimi321/claude-code-chrome-web-automation) |
| `claude-api-builder` | [claude-code-claude-api-builder](https://github.com/wimi321/claude-code-claude-api-builder) |
| `claude-md-initializer` | [claude-code-claude-md-initializer](https://github.com/wimi321/claude-code-claude-md-initializer) |
| `claude-settings-editor` | [claude-code-claude-settings-editor](https://github.com/wimi321/claude-code-claude-settings-editor) |
| `code-simplifier` | [claude-code-code-simplifier](https://github.com/wimi321/claude-code-code-simplifier) |
| `git-commit-pr-workflow` | [claude-code-git-commit-pr-workflow](https://github.com/wimi321/claude-code-git-commit-pr-workflow) |
| `git-commit-workflow` | [claude-code-git-commit-workflow](https://github.com/wimi321/claude-code-git-commit-workflow) |
| `keybindings-customizer` | [claude-code-keybindings-customizer](https://github.com/wimi321/claude-code-keybindings-customizer) |
| `memory-landscape-review` | [claude-code-memory-landscape-review](https://github.com/wimi321/claude-code-memory-landscape-review) |
| `pull-request-reviewer` | [claude-code-pull-request-reviewer](https://github.com/wimi321/claude-code-pull-request-reviewer) |
| `recurring-loop-runner` | [claude-code-recurring-loop-runner](https://github.com/wimi321/claude-code-recurring-loop-runner) |
| `remote-agent-scheduler` | [claude-code-remote-agent-scheduler](https://github.com/wimi321/claude-code-remote-agent-scheduler) |
| `runtime-verifier` | [claude-code-runtime-verifier](https://github.com/wimi321/claude-code-runtime-verifier) |
| `security-review-workflow` | [claude-code-security-review-workflow](https://github.com/wimi321/claude-code-security-review-workflow) |
| `session-debug-log-investigator` | [claude-code-session-debug-log-investigator](https://github.com/wimi321/claude-code-session-debug-log-investigator) |
| `statusline-setup` | [claude-code-statusline-setup](https://github.com/wimi321/claude-code-statusline-setup) |
| `stuck-session-diagnosis` | [claude-code-stuck-session-diagnosis](https://github.com/wimi321/claude-code-stuck-session-diagnosis) |
| `verifier-skill-generator` | [claude-code-verifier-skill-generator](https://github.com/wimi321/claude-code-verifier-skill-generator) |
| `workflow-skillify` | [claude-code-workflow-skillify](https://github.com/wimi321/claude-code-workflow-skillify) |

## Published to ClawHub

ClawHub publish progress is tracked in [CLAWHUB_PUBLISH_STATUS.md](./CLAWHUB_PUBLISH_STATUS.md).

Already published:

- `claude-code-batch-migration-orchestrator`
- `claude-code-chrome-web-automation`
- `claude-code-claude-api-builder`
- `claude-code-claude-md-initializer`
- `claude-code-claude-settings-editor`

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
