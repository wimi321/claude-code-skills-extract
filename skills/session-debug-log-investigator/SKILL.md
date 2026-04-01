---
name: "session_debug_log_investigator"
description: "Use when diagnosing a failing or confusing Claude Code session by enabling debug logging, tailing recent logs, and explaining warnings or errors."
---

# Session Debug Log Investigator

Use this skill to diagnose runtime issues in an agent session.

## Workflow
1. Enable debug logging if it is not already active.
2. Read the latest portion of the debug log instead of the whole file.
3. Search for warnings, errors, and repeated failure patterns.
4. Cross-check config files that can explain the behavior.
5. Summarize likely causes and next reproduction steps.

## Guardrails
- Tail logs instead of loading giant files.
- Separate configuration issues from product/runtime bugs.
- If logging was just enabled, ask for reproduction before concluding too much.

## Source Provenance
Derived from `src/skills/bundled/debug.ts`.
