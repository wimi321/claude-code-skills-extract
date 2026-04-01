# Claude Code Skills Extraction Pack

This repository extracts reusable skill-worthy workflows from a local Claude Code source snapshot and republishes them as independent skills.

## Layout

- `skills/`: one publishable skill per directory
- `EXTRACTION_REPORT.md`: mapping from source modules to extracted skills and omitted modules

## Notes

- Skills were selected for cross-session or cross-agent reuse.
- Product toggles and entitlement-gated UI switches were intentionally excluded.
- Each skill includes a minimal `agents/openai.yaml` for agent-facing metadata.
