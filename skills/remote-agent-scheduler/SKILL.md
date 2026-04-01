---
name: "remote_agent_scheduler"
description: "Use when the user wants to create, inspect, update, or run scheduled remote agents in the cloud rather than local cron jobs."
---

# Remote Agent Scheduler

Use this skill for recurring remote agent jobs that run in isolated cloud environments.

## Workflow
1. Determine whether the user wants to create, list, update, or run a trigger.
2. Collect repo source, environment, connectors, schedule, and prompt payload.
3. Build or inspect the trigger definition.
4. Confirm authentication, environment, and connector assumptions.
5. Return the trigger details and next management steps.

## Guardrails
- Distinguish remote cloud runs from local cron jobs.
- Keep repo URL, environment ID, and schedule explicit.
- Surface setup blockers like missing auth or repo access early.

## Source Provenance
Derived from `src/skills/bundled/scheduleRemoteAgents.ts`.
