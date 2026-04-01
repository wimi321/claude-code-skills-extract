---
name: "keybindings_customizer"
description: "Use when the user wants to customize Claude Code keybindings, rebind shortcuts, add chords, or edit `~/.claude/keybindings.json` safely."
---

# Keybindings Customizer

Use this skill for shortcut rebinding, unbinding, or chord creation.

## Workflow
1. Read the current keybindings file first.
2. Merge changes instead of replacing the entire file.
3. Keep schema and docs fields intact.
4. Validate against reserved and non-rebindable shortcuts.
5. Explain any conflicts or terminal-level limitations.

## Guardrails
- Never overwrite the full file blindly.
- Preserve unrelated existing bindings.
- Flag OS or terminal-reserved shortcuts before saving.

## Source Provenance
Derived from `src/skills/bundled/keybindings.ts`.
