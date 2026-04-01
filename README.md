# Claude Code Skills

A production-ready collection of standalone skills extracted from reusable Claude Code workflows and repackaged as public skills for agent ecosystems.

## What This Is

This project turns high-value Claude Code capabilities into individually publishable skills that can be reused outside the original product context.

The extraction focuses on workflows that are:
- repeatable across sessions and repositories
- useful to multiple agent runtimes
- strong enough to justify a dedicated public skill
- safer as standalone capabilities than as hidden product internals

## Included Skill Families

| Family | Skills |
|---|---|
| Planning and Orchestration | `batch-migration-orchestrator`, `workflow-skillify`, `verifier-skill-generator` |
| Coding and Git | `code-simplifier`, `git-commit-workflow`, `git-commit-pr-workflow`, `pull-request-reviewer`, `security-review-workflow` |
| Runtime and Diagnostics | `runtime-verifier`, `session-debug-log-investigator`, `stuck-session-diagnosis` |
| Browser and API | `chrome-web-automation`, `claude-api-builder` |
| Agent Ops and Config | `claude-md-initializer`, `claude-settings-editor`, `keybindings-customizer`, `memory-landscape-review`, `recurring-loop-runner`, `remote-agent-scheduler`, `statusline-setup` |

## Published to ClawHub

Current publish state lives in [`CLAWHUB_PUBLISH_STATUS.md`](./CLAWHUB_PUBLISH_STATUS.md).

Already published:
- `claude-code-batch-migration-orchestrator`
- `claude-code-chrome-web-automation`
- `claude-code-claude-api-builder`
- `claude-code-claude-md-initializer`
- `claude-code-claude-settings-editor`

## Repository Structure

- `skills/`: one skill per directory
- `docs/CATALOG.md`: quick reference catalog for all extracted skills
- `EXTRACTION_REPORT.md`: source-module to skill mapping
- `CLAWHUB_PUBLISH_STATUS.md`: publish progress and remaining queue
- `generate_skills.py`: deterministic generator for the current skill set
- `publish_clawhub.sh`: full publish script
- `resume_clawhub_publish.sh`: resume script for rate-limited follow-up publishes

## Quality Bar

This repository treats each skill as a public artifact, not a private prompt snippet.

Every shipped skill includes:
- clean YAML frontmatter
- agent-facing metadata in `agents/openai.yaml`
- explicit workflows and guardrails
- example requests
- clear input and output expectations
- success criteria and non-goals
- provenance back to the analyzed Claude Code source module

## Selection Policy

Included:
- reusable workflows
- operator-facing or agent-facing capabilities
- repeatable review, verification, planning, and automation patterns

Excluded:
- entitlement-gated UI toggles
- account-specific product settings with weak reuse outside the original app
- novelty helpers that do not justify standalone public maintenance

## Use the Skills Locally

Install or copy any individual skill directory into a compatible agent workspace, or publish and install through ClawHub.

For local experimentation, each skill is already self-contained under `skills/<slug>/`.

## Publish to ClawHub

Publish everything from the current queue:

```bash
./publish_clawhub.sh
```

If ClawHub rate-limits new skill creation, resume later with:

```bash
./resume_clawhub_publish.sh
```

## Source and Intent

These skills were derived by reading a local Claude Code source snapshot and extracting only the modules that map cleanly onto standalone public skills.

See [`EXTRACTION_REPORT.md`](./EXTRACTION_REPORT.md) for the exact mapping.
