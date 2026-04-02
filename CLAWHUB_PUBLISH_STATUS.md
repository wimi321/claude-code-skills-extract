# ClawHub Publish Status

## Published

- `batch-migration-orchestrator`
- `chrome-web-automation`
- `claude-api-builder`
- `claude-md-initializer`
- `claude-settings-editor`

## Pending

Blocked by ClawHub new-skill rate limit: max 5 new skills per hour.

- `code-simplify`
- `git-commit-pr-workflow`
- `git-commit-workflow`
- `keybindings-customizer`
- `memory-landscape-review`
- `pr-audit`
- `recurring-loop-runner`
- `remote-agent-scheduler`
- `runtime-verifier`
- `security-review-workflow`
- `session-debug-log-investigator`
- `statusline-setup`
- `stuck-session-diagnosis`
- `verifier-skill-generator`
- `workflow-skillify`

## Naming Note

GitHub repositories now use short repository names.

ClawHub uses the shortest available registry slug for each skill:

- most skills use the plain short slug
- `code-simplifier` uses `code-simplify` because `code-simplifier` was already taken
- `pull-request-reviewer` uses `pr-audit` because `pull-request-reviewer` was already taken

Legacy long-prefixed ClawHub slugs from the earlier publish pass may still exist as historical duplicates because the current CLI does not support in-place slug renames.

## Monitor

- Active background publisher session: `tmux attach -t clawhub-publish`
- Resume script: `./resume_clawhub_publish.sh`
