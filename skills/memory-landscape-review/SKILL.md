---
name: "memory_landscape_review"
description: "Use when the user wants to review auto-memory, promote durable instructions into CLAUDE.md or local memory, and clean up duplicates or conflicts."
---

# Memory Landscape Review

Use this skill to review project memory, local memory, and auto-memory together.

## Workflow
1. Gather repo memory files and current auto-memory context.
2. Classify each entry as repo-wide, personal, team-wide, or temporary.
3. Detect duplicates, conflicts, and outdated instructions.
4. Present a grouped report before making any changes.
5. Only apply promotions or cleanup after explicit approval.

## Guardrails
- Propose first, edit second.
- Do not guess when an instruction might be personal vs shared.
- Keep transient notes out of durable memory files.

## Source Provenance
Derived from `src/skills/bundled/remember.ts`.
