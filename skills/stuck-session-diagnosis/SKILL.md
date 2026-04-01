---
name: "stuck_session_diagnosis"
description: "Use when another Claude Code session appears frozen, stuck, or abnormally slow and needs process-level diagnosis and reporting."
---

# Stuck Session Diagnosis

Use this skill to investigate slow or frozen local agent sessions.

## Workflow
1. List candidate agent processes.
2. Check CPU, RSS, state, uptime, and child processes.
3. Sample suspicious processes again to confirm sustained issues.
4. Inspect related debug logs when possible.
5. Produce a concise diagnosis and escalation-ready report.

## Guardrails
- Diagnostic only: do not kill or signal processes unless asked.
- Confirm suspicious metrics are sustained, not transient.
- Keep the final report focused on actionable symptoms.

## Source Provenance
Derived from `src/skills/bundled/stuck.ts`.
