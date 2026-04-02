# ClawHub Publish Status

## Published

- `claude-code-batch-migration-orchestrator`
- `claude-code-chrome-web-automation`
- `claude-code-claude-api-builder`
- `claude-code-claude-md-initializer`
- `claude-code-claude-settings-editor`

## Pending

Blocked by ClawHub new-skill rate limit: max 5 new skills per hour.

- `code-simplifier`
- `git-commit-pr-workflow`
- `git-commit-workflow`
- `keybindings-customizer`
- `memory-landscape-review`
- `pull-request-reviewer`
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

The first 5 skills were already published with a legacy `claude-code-` prefix in the registry slug.

The remaining 15 pending skills have been switched to short slugs with no prefix.

## Monitor

- Active background publisher session: `tmux attach -t clawhub-publish`
- Resume script: `./resume_clawhub_publish.sh`
