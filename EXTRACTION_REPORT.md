# Extraction Report

## Extracted Skills

- `batch-migration-orchestrator` <- `src/skills/bundled/batch.ts`
- `claude-api-builder` <- `src/skills/bundled/claudeApi.ts`
- `chrome-web-automation` <- `src/skills/bundled/claudeInChrome.ts`
- `session-debug-log-investigator` <- `src/skills/bundled/debug.ts`
- `keybindings-customizer` <- `src/skills/bundled/keybindings.ts`
- `recurring-loop-runner` <- `src/skills/bundled/loop.ts`
- `memory-landscape-review` <- `src/skills/bundled/remember.ts`
- `remote-agent-scheduler` <- `src/skills/bundled/scheduleRemoteAgents.ts`
- `code-simplifier` <- `src/skills/bundled/simplify.ts`
- `workflow-skillify` <- `src/skills/bundled/skillify.ts`
- `stuck-session-diagnosis` <- `src/skills/bundled/stuck.ts`
- `claude-settings-editor` <- `src/skills/bundled/updateConfig.ts`
- `runtime-verifier` <- `src/skills/bundled/verify.ts`
- `git-commit-workflow` <- `src/commands/commit.ts`
- `git-commit-pr-workflow` <- `src/commands/commit-push-pr.ts`
- `pull-request-reviewer` <- `src/commands/review.ts`
- `security-review-workflow` <- `src/commands/security-review.ts`
- `claude-md-initializer` <- `src/commands/init.ts`
- `verifier-skill-generator` <- `src/commands/init-verifiers.ts`
- `statusline-setup` <- `src/commands/statusline.tsx`

## Omitted Modules

- `src/commands/advisor.ts`: Primarily a product/account model toggle, not a reusable cross-agent workflow.
- `src/commands/brief.ts`: UI/runtime mode toggle with entitlement gating; low standalone reuse as a published skill.
- `src/skills/bundled/loremIpsum.ts`: Synthetic filler text generation is niche and not a strong reusable agent capability.
