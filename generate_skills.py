from pathlib import Path
import json

root = Path('/Users/haoc/Developer/cc-mg55')
skills_root = root / 'skills'
skills_root.mkdir(parents=True, exist_ok=True)

skills = [
    {
        'slug': 'batch-migration-orchestrator',
        'name': 'batch_migration_orchestrator',
        'display': 'Batch Migration Orchestrator',
        'description': 'Use when the user wants a large, mechanical change split into many independent units and executed in parallel with isolated workers and PRs.',
        'short': 'Plan and parallelize broad codebase migrations',
        'default_prompt': 'Break this large migration into isolated work units, define verification, and run the units in parallel.',
        'provenance': 'src/skills/bundled/batch.ts',
        'body': '''# Batch Migration Orchestrator

Use this skill for sweeping refactors, migrations, bulk renames, or repetitive codebase-wide edits.

## Goal
Turn one large request into a safe parallel rollout with independent units, validation, and mergeable outputs.

## Workflow
1. Inspect the repo to find every affected area, convention, and dependency.
2. Split the change into independent units by module, directory, or subsystem.
3. Define an end-to-end verification recipe for each unit.
4. Launch workers in parallel only when their write scopes do not overlap.
5. Track completion, collect PRs or patches, and summarize failures.

## Guardrails
- Do not parallelize tightly coupled work.
- Do not let workers edit the same files.
- Require each worker to validate its own unit.
- Prefer worktree or isolated branch execution when git is available.

## Inputs
- Migration target
- Scope boundaries
- Verification method
- Branch/PR expectations

## Source Provenance
Derived from Claude Code bundled skill logic in `src/skills/bundled/batch.ts`.
'''
    },
    {
        'slug': 'claude-api-builder',
        'name': 'claude_api_builder',
        'display': 'Claude API Builder',
        'description': 'Use when code imports Anthropic SDKs or the user asks to build with the Claude API, Agent SDK, tool use, streaming, files, or batches.',
        'short': 'Build apps on the Claude API and Agent SDK',
        'default_prompt': 'Help me implement this feature with the Claude API and choose the right Anthropic SDK pattern.',
        'provenance': 'src/skills/bundled/claudeApi.ts',
        'body': '''# Claude API Builder

Use this skill when the task is specifically about Anthropic or Claude API integration.

## Trigger Signals
- Imports like `anthropic`, `@anthropic-ai/sdk`, or Agent SDK packages
- Requests about streaming, tool use, prompt caching, file uploads, or Claude batch jobs
- Questions about choosing Anthropic API patterns for an app

## Workflow
1. Detect the project language and SDK surface.
2. Choose the smallest fitting pattern: simple messages, streaming, tools, batches, or files.
3. Prefer official docs and SDK-native examples.
4. Keep model names, error handling, and retries explicit.
5. Explain when to browse live docs for fast-moving API details.

## Guardrails
- Do not pivot to non-Anthropic SDKs unless the user asks.
- Prefer primary documentation over memory for model/API specifics.
- Separate one-shot prompts from stateful agent workflows.

## Source Provenance
Derived from `src/skills/bundled/claudeApi.ts` and the bundled Claude API references.
'''
    },
    {
        'slug': 'chrome-web-automation',
        'name': 'chrome_web_automation',
        'display': 'Chrome Web Automation',
        'description': 'Use when the user wants browser automation in an existing Chrome session: click, fill, inspect tabs, capture screenshots, or debug web flows.',
        'short': 'Drive Chrome for browser-based tasks',
        'default_prompt': 'Open the active Chrome context, inspect tabs, and automate this browser flow step by step.',
        'provenance': 'src/skills/bundled/claudeInChrome.ts',
        'body': '''# Chrome Web Automation

Use this skill before any browser interaction that depends on the user\'s live Chrome session.

## Workflow
1. Start by inspecting current tabs and browser context.
2. Navigate or select the right tab.
3. Snapshot the page before interacting.
4. Click, type, submit, and screenshot using stable references.
5. Re-snapshot after navigation or large DOM updates.

## Best Fits
- Web app debugging
- Form filling
- Screenshot capture
- Console or tab inspection
- Reproducing UI issues in a user browser session

## Guardrails
- Re-snapshot when element references go stale.
- Do not assume current tab state without checking.
- Prefer explicit browser actions over ambiguous natural-language leaps.

## Source Provenance
Derived from `src/skills/bundled/claudeInChrome.ts`.
'''
    },
    {
        'slug': 'session-debug-log-investigator',
        'name': 'session_debug_log_investigator',
        'display': 'Session Debug Log Investigator',
        'description': 'Use when diagnosing a failing or confusing Claude Code session by enabling debug logging, tailing recent logs, and explaining warnings or errors.',
        'short': 'Inspect and interpret session debug logs',
        'default_prompt': 'Turn on session debugging if needed, read the latest log tail, and diagnose this Claude Code issue.',
        'provenance': 'src/skills/bundled/debug.ts',
        'body': '''# Session Debug Log Investigator

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
'''
    },
    {
        'slug': 'keybindings-customizer',
        'name': 'keybindings_customizer',
        'display': 'Keybindings Customizer',
        'description': 'Use when the user wants to customize Claude Code keybindings, rebind shortcuts, add chords, or edit `~/.claude/keybindings.json` safely.',
        'short': 'Safely edit Claude keybinding config',
        'default_prompt': 'Update my Claude Code keybindings without clobbering the existing file.',
        'provenance': 'src/skills/bundled/keybindings.ts',
        'body': '''# Keybindings Customizer

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
'''
    },
    {
        'slug': 'recurring-loop-runner',
        'name': 'recurring_loop_runner',
        'display': 'Recurring Loop Runner',
        'description': 'Use when the user wants a prompt or command to run on a recurring interval, such as checking deploys, polling status, or repeating a slash-command.',
        'short': 'Schedule recurring prompts and checks',
        'default_prompt': 'Schedule this prompt on a recurring interval and run it immediately once.',
        'provenance': 'src/skills/bundled/loop.ts',
        'body': '''# Recurring Loop Runner

Use this skill when a task should repeat on a time interval.

## Workflow
1. Parse the interval from the user request.
2. Normalize human phrasing into a valid cadence.
3. Create the recurring schedule.
4. Confirm the cadence, identifier, and expiry behavior.
5. Execute the task once immediately so the user gets instant feedback.

## Guardrails
- Do not trigger for one-off requests.
- If the cadence is ambiguous or uneven, round and explain the rounding.
- Make cancellation or update instructions easy to find.

## Source Provenance
Derived from `src/skills/bundled/loop.ts`.
'''
    },
    {
        'slug': 'memory-landscape-review',
        'name': 'memory_landscape_review',
        'display': 'Memory Landscape Review',
        'description': 'Use when the user wants to review auto-memory, promote durable instructions into CLAUDE.md or local memory, and clean up duplicates or conflicts.',
        'short': 'Review and reorganize memory layers',
        'default_prompt': 'Audit my memory layers and propose what should move into durable repo or personal memory.',
        'provenance': 'src/skills/bundled/remember.ts',
        'body': '''# Memory Landscape Review

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
'''
    },
    {
        'slug': 'remote-agent-scheduler',
        'name': 'remote_agent_scheduler',
        'display': 'Remote Agent Scheduler',
        'description': 'Use when the user wants to create, inspect, update, or run scheduled remote agents in the cloud rather than local cron jobs.',
        'short': 'Schedule isolated remote agent runs',
        'default_prompt': 'Help me create or update a scheduled remote agent with the right repo, environment, and cron.',
        'provenance': 'src/skills/bundled/scheduleRemoteAgents.ts',
        'body': '''# Remote Agent Scheduler

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
'''
    },
    {
        'slug': 'code-simplifier',
        'name': 'code_simplifier',
        'display': 'Code Simplifier',
        'description': 'Use when changed code should be reviewed for reuse, code quality, and efficiency, then cleaned up before finalizing.',
        'short': 'Review and simplify changed code',
        'default_prompt': 'Inspect the changed files for duplication, awkward abstractions, and inefficiencies, then fix what you find.',
        'provenance': 'src/skills/bundled/simplify.ts',
        'body': '''# Code Simplifier

Use this skill after making changes and before wrapping up.

## Workflow
1. Inspect the relevant diff or latest modified files.
2. Review for existing utilities that should be reused.
3. Review for code smell: parameter sprawl, copy-paste, leaky abstractions, or unnecessary comments.
4. Review for efficiency problems: repeated work, unnecessary reads, event churn, and hot-path bloat.
5. Fix confirmed issues and summarize what changed.

## Guardrails
- Prefer concrete fixes over broad stylistic churn.
- Keep attention on changed code, not the whole codebase.
- If no issue exists, say so explicitly.

## Source Provenance
Derived from `src/skills/bundled/simplify.ts`.
'''
    },
    {
        'slug': 'workflow-skillify',
        'name': 'workflow_skillify',
        'display': 'Workflow Skillify',
        'description': 'Use when a successful session or repeatable process should be captured as a reusable skill with steps, arguments, and invocation guidance.',
        'short': 'Turn a session into a reusable skill',
        'default_prompt': 'Extract the repeatable workflow from this session and write a reusable skill specification.',
        'provenance': 'src/skills/bundled/skillify.ts',
        'body': '''# Workflow Skillify

Use this skill at the end of a repeatable process to capture it as a standalone skill.

## Workflow
1. Summarize the session and extract user-visible goals, corrections, and constraints.
2. Identify inputs, outputs, artifacts, and success criteria.
3. Interview for missing details only where the workflow is ambiguous.
4. Write a clean `SKILL.md` with trigger conditions, steps, and optional arguments.
5. Save the skill in the appropriate repo-level or personal location.

## Guardrails
- Capture the user\'s corrections, not just the first draft of the process.
- Keep the resulting skill concrete and execution-oriented.
- Do not over-question simple workflows.

## Source Provenance
Derived from `src/skills/bundled/skillify.ts`.
'''
    },
    {
        'slug': 'stuck-session-diagnosis',
        'name': 'stuck_session_diagnosis',
        'display': 'Stuck Session Diagnosis',
        'description': 'Use when another Claude Code session appears frozen, stuck, or abnormally slow and needs process-level diagnosis and reporting.',
        'short': 'Diagnose frozen or slow agent sessions',
        'default_prompt': 'Inspect this machine for stuck Claude sessions and prepare a clear diagnosis report.',
        'provenance': 'src/skills/bundled/stuck.ts',
        'body': '''# Stuck Session Diagnosis

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
'''
    },
    {
        'slug': 'claude-settings-editor',
        'name': 'claude_settings_editor',
        'display': 'Claude Settings Editor',
        'description': 'Use when the user wants to update Claude settings, hooks, permissions, MCP server toggles, or other JSON config safely and with scope awareness.',
        'short': 'Edit Claude settings and hook config',
        'default_prompt': 'Help me update Claude settings with the right file scope and valid JSON structure.',
        'provenance': 'src/skills/bundled/updateConfig.ts',
        'body': '''# Claude Settings Editor

Use this skill for `settings.json`, local overrides, and hook configuration.

## Workflow
1. Choose the correct settings file by scope: user, project, or local.
2. Read the current file before editing.
3. Apply the smallest valid JSON change.
4. Keep permissions, hooks, plugins, and MCP configuration syntactically valid.
5. Explain scope, precedence, and any risky config changes.

## Guardrails
- Do not replace a config file wholesale unless necessary.
- Preserve unrelated user settings.
- Warn before widening permissions or changing automation hooks broadly.

## Source Provenance
Derived from `src/skills/bundled/updateConfig.ts`.
'''
    },
    {
        'slug': 'runtime-verifier',
        'name': 'runtime_verifier',
        'display': 'Runtime Verifier',
        'description': 'Use when a code change must be verified by actually running the app, endpoint, or CLI flow instead of relying only on unit tests.',
        'short': 'Verify changes against running software',
        'default_prompt': 'Create and execute a concrete verification plan that proves the change works in a live runtime.',
        'provenance': 'src/skills/bundled/verify.ts',
        'body': '''# Runtime Verifier

Use this skill to verify that a change behaves correctly in a running system.

## Workflow
1. Translate the request into a concrete verification plan.
2. Start the needed app, server, or CLI environment.
3. Execute the runtime checks exactly as planned.
4. Report pass/fail per step with evidence.
5. Clean up any processes or sessions you started.

## Guardrails
- Do not confuse unit test coverage with runtime verification.
- Prefer observable outcomes over vague confidence statements.
- Update the verifier instructions if the environment changed and the failure is instruction drift, not product breakage.

## Source Provenance
Derived from `src/skills/bundled/verify.ts`.
'''
    },
    {
        'slug': 'git-commit-workflow',
        'name': 'git_commit_workflow',
        'display': 'Git Commit Workflow',
        'description': 'Use when the user wants a single clean commit created from current changes with safe staging, message drafting, and non-interactive git usage.',
        'short': 'Stage and create one safe commit',
        'default_prompt': 'Review the current diff, stage the right files, and create one well-formed commit without amending.',
        'provenance': 'src/commands/commit.ts',
        'body': '''# Git Commit Workflow

Use this skill when the task is to create one commit from current work.

## Workflow
1. Inspect git status, diff, branch, and recent commit style.
2. Stage only relevant changes.
3. Draft a concise commit message that reflects why the change exists.
4. Create a new commit non-interactively.
5. Report the resulting commit summary.

## Guardrails
- Never amend unless explicitly asked.
- Never bypass hooks unless explicitly asked.
- Avoid staging secrets or unrelated files.
- Do not create an empty commit.

## Source Provenance
Derived from `src/commands/commit.ts`.
'''
    },
    {
        'slug': 'git-commit-pr-workflow',
        'name': 'git_commit_pr_workflow',
        'display': 'Git Commit PR Workflow',
        'description': 'Use when the user wants the full git workflow: branch creation if needed, commit, push, and PR create or update with a concise summary and test plan.',
        'short': 'Commit, push, and open or update a PR',
        'default_prompt': 'Take the current branch state to a ready PR with safe git operations and a crisp PR body.',
        'provenance': 'src/commands/commit-push-pr.ts',
        'body': '''# Git Commit PR Workflow

Use this skill for end-to-end git delivery from working tree to pull request.

## Workflow
1. Inspect branch state, diff against default branch, and existing PR state.
2. Create a feature branch if still on the default branch.
3. Stage and commit the relevant changes.
4. Push the branch.
5. Create or update the PR with a short title, summary bullets, and test plan.

## Guardrails
- No destructive git commands unless explicitly requested.
- No force push to default branches.
- Keep PR titles short and bodies structured.
- Avoid committing secrets or unrelated changes.

## Source Provenance
Derived from `src/commands/commit-push-pr.ts`.
'''
    },
    {
        'slug': 'pull-request-reviewer',
        'name': 'pull_request_reviewer',
        'display': 'Pull Request Reviewer',
        'description': 'Use when the user wants a local review of a GitHub pull request based on its diff, risks, quality, performance, tests, and security implications.',
        'short': 'Review a PR from its GitHub diff',
        'default_prompt': 'Inspect this pull request diff and produce a concise but thorough review with risks and improvement suggestions.',
        'provenance': 'src/commands/review.ts',
        'body': '''# Pull Request Reviewer

Use this skill for code review of an existing GitHub PR.

## Workflow
1. Resolve the target PR number or list open PRs if needed.
2. Read PR metadata and full diff.
3. Review correctness, conventions, performance, test coverage, and security-sensitive changes.
4. Prioritize concrete findings over generic praise.
5. Return a structured review with suggested follow-up.

## Guardrails
- Base the review on the actual diff, not assumptions.
- Findings first, summary second.
- Keep comments actionable and specific.

## Source Provenance
Derived from `src/commands/review.ts`.
'''
    },
    {
        'slug': 'security-review-workflow',
        'name': 'security_review_workflow',
        'display': 'Security Review Workflow',
        'description': 'Use when the current branch or PR needs a focused security review that minimizes false positives and only reports concrete, exploit-relevant issues.',
        'short': 'Run a high-signal security review on diffs',
        'default_prompt': 'Review this branch diff strictly for concrete security vulnerabilities and filter out low-confidence noise.',
        'provenance': 'src/commands/security-review.ts',
        'body': '''# Security Review Workflow

Use this skill for focused security review of branch or PR changes.

## Workflow
1. Collect git status, changed files, commit list, and full diff against the target base.
2. Research the codebase\'s existing security patterns.
3. Inspect only newly introduced attack surfaces in the diff.
4. Filter out speculative, low-signal, or excluded finding classes.
5. Report only concrete, actionable findings with file, severity, exploit path, and recommendation.

## Guardrails
- Minimize false positives aggressively.
- Ignore general code review comments that are not security issues.
- Prefer fewer high-confidence findings over noisy coverage.

## Source Provenance
Derived from `src/commands/security-review.ts`.
'''
    },
    {
        'slug': 'claude-md-initializer',
        'name': 'claude_md_initializer',
        'display': 'CLAUDE MD Initializer',
        'description': 'Use when onboarding a repository into Claude Code by creating or improving CLAUDE.md, and optionally identifying useful skills, hooks, and verifier setup.',
        'short': 'Bootstrap repo guidance for future agents',
        'default_prompt': 'Analyze this repository and create a practical CLAUDE.md with architecture, commands, and agent guidance.',
        'provenance': 'src/commands/init.ts',
        'body': '''# CLAUDE MD Initializer

Use this skill when a repo needs onboarding documentation for future agent sessions.

## Workflow
1. Read the repository structure, README, existing instructions, and tooling config.
2. Identify key build, test, and run commands.
3. Summarize the high-level architecture and important conventions.
4. Create or improve `CLAUDE.md` without stuffing it with generic advice.
5. Suggest follow-on skills, hooks, or verifier setup if they materially help.

## Guardrails
- Do not invent commands or conventions.
- Focus on repo-specific knowledge, not generic coding advice.
- Keep the file practical for future agent sessions.

## Source Provenance
Derived from `src/commands/init.ts`.
'''
    },
    {
        'slug': 'verifier-skill-generator',
        'name': 'verifier_skill_generator',
        'display': 'Verifier Skill Generator',
        'description': 'Use when a project needs one or more verifier skills for web, CLI, or API runtime checks that the Verify agent can discover automatically.',
        'short': 'Generate project-specific verifier skills',
        'default_prompt': 'Inspect this project and generate verifier skills for the relevant web, CLI, or API surfaces.',
        'provenance': 'src/commands/init-verifiers.ts',
        'body': '''# Verifier Skill Generator

Use this skill to create project-specific verifier skills.

## Workflow
1. Detect project areas and application types.
2. Decide whether each area needs web, CLI, or API verification.
3. Identify available automation tools and setup gaps.
4. Ask only the project-specific questions needed to finalize each verifier.
5. Generate verifier skill folders in the repo so verification can be repeated later.

## Guardrails
- Focus on functional verification, not unit tests or type checks.
- Use names discoverable by downstream verification tooling.
- Include setup, authentication, cleanup, and self-update behavior in each verifier.

## Source Provenance
Derived from `src/commands/init-verifiers.ts`.
'''
    },
    {
        'slug': 'statusline-setup',
        'name': 'statusline_setup',
        'display': 'Statusline Setup',
        'description': 'Use when the user wants to configure Claude Code statusline UI by inspecting shell prompt configuration and updating the relevant settings.',
        'short': 'Set up Claude statusline UI',
        'default_prompt': 'Inspect my shell prompt setup and configure Claude Code statusline to match it.',
        'provenance': 'src/commands/statusline.tsx',
        'body': '''# Statusline Setup

Use this skill to configure Claude Code\'s statusline UI from an existing shell prompt setup.

## Workflow
1. Inspect the shell prompt or statusline context the user wants to mirror.
2. Read existing Claude settings that control statusline behavior.
3. Adjust the settings with minimal changes.
4. Explain what changed and how to refine it further.

## Guardrails
- Inspect current config before editing.
- Make the smallest possible settings change.
- Preserve unrelated user preferences.

## Source Provenance
Derived from `src/commands/statusline.tsx`.
'''
    },
]

omitted = [
    ('src/commands/advisor.ts', 'Primarily a product/account model toggle, not a reusable cross-agent workflow.'),
    ('src/commands/brief.ts', 'UI/runtime mode toggle with entitlement gating; low standalone reuse as a published skill.'),
    ('src/skills/bundled/loremIpsum.ts', 'Synthetic filler text generation is niche and not a strong reusable agent capability.'),
]

for skill in skills:
    d = skills_root / skill['slug']
    (d / 'agents').mkdir(parents=True, exist_ok=True)
    (d / 'references').mkdir(parents=True, exist_ok=True)
    skill_md = (
        '---\n'
        f"name: {json.dumps(skill['name'])}\n"
        f"description: {json.dumps(skill['description'])}\n"
        '---\n\n'
        + skill['body'].rstrip()
        + '\n'
    )
    (d / 'SKILL.md').write_text(skill_md, encoding='utf-8')
    openai_yaml = (
        'interface:\n'
        f"  display_name: {json.dumps(skill['display'])}\n"
        f"  short_description: {json.dumps(skill['short'])}\n"
        f"  default_prompt: {json.dumps(skill['default_prompt'])}\n"
    )
    (d / 'agents' / 'openai.yaml').write_text(openai_yaml, encoding='utf-8')
    provenance = (
        '# Provenance\n\n'
        f"- Skill slug: `{skill['slug']}`\n"
        f"- Source module: `{skill['provenance']}`\n"
        '- Extracted from local Claude Code source analysis\n'
    )
    (d / 'references' / 'provenance.md').write_text(provenance, encoding='utf-8')

(root / 'README.md').write_text(
    '# Claude Code Skills Extraction Pack\n\n'
    'This repository extracts reusable skill-worthy workflows from a local Claude Code source snapshot and republishes them as independent skills.\n\n'
    '## Layout\n\n'
    '- `skills/`: one publishable skill per directory\n'
    '- `EXTRACTION_REPORT.md`: mapping from source modules to extracted skills and omitted modules\n\n'
    '## Notes\n\n'
    '- Skills were selected for cross-session or cross-agent reuse.\n'
    '- Product toggles and entitlement-gated UI switches were intentionally excluded.\n'
    '- Each skill includes a minimal `agents/openai.yaml` for agent-facing metadata.\n',
    encoding='utf-8',
)

report = ['# Extraction Report', '', '## Extracted Skills', '']
for skill in skills:
    report.append(f"- `{skill['slug']}` <- `{skill['provenance']}`")
report.extend(['', '## Omitted Modules', ''])
for mod, reason in omitted:
    report.append(f"- `{mod}`: {reason}")
(root / 'EXTRACTION_REPORT.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
(root / '.gitignore').write_text('.DS_Store\n.clawhub/\n', encoding='utf-8')

print(f'Generated {len(skills)} skills under {skills_root}')
