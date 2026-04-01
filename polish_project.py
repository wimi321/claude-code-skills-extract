from pathlib import Path
import json

root = Path('/Users/haoc/Developer/cc-mg55')
skills_root = root / 'skills'
(root / 'docs').mkdir(exist_ok=True)

catalog = {
    'batch-migration-orchestrator': {
        'title': 'Batch Migration Orchestrator',
        'examples': ['Migrate this monorepo from Jest to Vitest in parallel.', 'Split this bulk API rename into independently shippable work units.'],
        'inputs': ['Migration goal', 'Affected modules or directories', 'Verification expectations', 'Branch or PR policy'],
        'outputs': ['Work decomposition plan', 'Parallel worker prompts', 'Status tracking summary', 'PR or patch rollup'],
        'success': ['Every unit has a clear scope.', 'No worker write conflicts exist.', 'Each unit includes verification.'],
        'non_goals': ['One-off tiny edits', 'Tightly coupled refactors that must land as one patch'],
    },
    'chrome-web-automation': {
        'title': 'Chrome Web Automation',
        'examples': ['Open the current Chrome session and reproduce this checkout bug.', 'Fill the form, capture screenshots, and show me where validation breaks.'],
        'inputs': ['Target site or current tab context', 'Desired browser actions', 'Artifacts to capture'],
        'outputs': ['Browser interaction transcript', 'Screenshots or evidence', 'Reproduction notes'],
        'success': ['The correct tab or page was inspected.', 'Interactions were completed against fresh page state.', 'Useful artifacts were captured when needed.'],
        'non_goals': ['Synthetic browser testing unrelated to the user browser context'],
    },
    'claude-api-builder': {
        'title': 'Claude API Builder',
        'examples': ['Add Anthropic streaming support to this TypeScript app.', 'Help me implement tool use with the Python Anthropic SDK.'],
        'inputs': ['Project language', 'Anthropic API feature needed', 'Performance or UX constraints'],
        'outputs': ['Recommended API pattern', 'Implementation guidance', 'SDK-specific caveats'],
        'success': ['The guidance matches Anthropic APIs specifically.', 'The selected pattern fits the use case and language.', 'Fast-moving API details are called out clearly.'],
        'non_goals': ['General LLM vendor-neutral advice', 'Non-Anthropic SDK design by default'],
    },
    'claude-md-initializer': {
        'title': 'CLAUDE MD Initializer',
        'examples': ['Analyze this repo and produce a strong CLAUDE.md for future agent sessions.', 'Upgrade the existing CLAUDE.md so future coding agents onboard faster.'],
        'inputs': ['Repository structure', 'Existing docs and config', 'Important commands and conventions'],
        'outputs': ['New or improved CLAUDE.md', 'Optional follow-up recommendations'],
        'success': ['Repo-specific commands are captured correctly.', 'Architecture notes are practical, not generic.', 'The file helps future agents move faster.'],
        'non_goals': ['Generic engineering advice', 'Invented commands or undocumented workflows'],
    },
    'claude-settings-editor': {
        'title': 'Claude Settings Editor',
        'examples': ['Update project hooks without breaking existing settings.', 'Change Claude permissions and MCP toggles in the right settings file.'],
        'inputs': ['Requested configuration change', 'Desired scope', 'Existing settings state'],
        'outputs': ['Validated JSON config edits', 'Scope explanation', 'Risk notes for sensitive changes'],
        'success': ['Only the intended file was changed.', 'JSON remains valid.', 'Unrelated settings were preserved.'],
        'non_goals': ['Blind full-file rewrites', 'Silent permission broadening'],
    },
    'code-simplifier': {
        'title': 'Code Simplifier',
        'examples': ['Review my diff for duplicate logic and unnecessary complexity.', 'Clean up this changed code before I ship it.'],
        'inputs': ['Relevant diff or changed files', 'Optional focus area'],
        'outputs': ['Concrete cleanup changes', 'Short summary of improvements'],
        'success': ['Duplication or awkward abstractions were reduced.', 'Performance regressions were checked.', 'No unnecessary churn was introduced.'],
        'non_goals': ['Massive style-only rewrites', 'Review of untouched code with no link to the change'],
    },
    'git-commit-pr-workflow': {
        'title': 'Git Commit PR Workflow',
        'examples': ['Commit this work, push it, and open a PR.', 'Take the current changes to a polished PR with a test plan.'],
        'inputs': ['Current git state', 'Default branch', 'Optional user instructions'],
        'outputs': ['New commit', 'Pushed branch', 'Created or updated PR'],
        'success': ['The right files were committed.', 'The branch was pushed safely.', 'The PR body accurately reflects the diff.'],
        'non_goals': ['Force-push workflows by default', 'Interactive git rebases'],
    },
    'git-commit-workflow': {
        'title': 'Git Commit Workflow',
        'examples': ['Make one clean commit from the current working tree.', 'Stage the right files and create a proper commit message.'],
        'inputs': ['Current diff', 'Branch state', 'Recent commit style'],
        'outputs': ['One non-amended commit', 'Accurate commit message'],
        'success': ['Only relevant changes were committed.', 'No empty commit was created.', 'Hooks and safety rules were respected.'],
        'non_goals': ['Amend flows unless explicitly asked', 'Committing secrets or unrelated changes'],
    },
    'keybindings-customizer': {
        'title': 'Keybindings Customizer',
        'examples': ['Rebind the external editor shortcut.', 'Add a chord to toggle todos without overwriting my keybindings file.'],
        'inputs': ['Requested key changes', 'Existing keybindings file', 'OS or terminal constraints'],
        'outputs': ['Merged keybinding config', 'Conflict explanations'],
        'success': ['The file was merged, not clobbered.', 'Reserved shortcuts were handled correctly.', 'Schema and docs fields remain intact.'],
        'non_goals': ['Whole-file replacement for a small binding change'],
    },
    'memory-landscape-review': {
        'title': 'Memory Landscape Review',
        'examples': ['Review my auto-memory and tell me what belongs in durable memory.', 'Find duplicate or conflicting instructions across memory layers.'],
        'inputs': ['Repo memory files', 'Auto-memory state', 'User preference for shared vs local memory'],
        'outputs': ['Promotion proposals', 'Conflict cleanup report', 'No-change recommendations'],
        'success': ['Durable memory candidates are identified clearly.', 'Duplicates and stale entries are surfaced.', 'No edits happen before approval.'],
        'non_goals': ['Silently editing memory files', 'Guessing personal vs shared intent when ambiguous'],
    },
    'pull-request-reviewer': {
        'title': 'Pull Request Reviewer',
        'examples': ['Review PR #123 for correctness and risk.', 'List the biggest problems in this open PR.'],
        'inputs': ['PR number or selection', 'GitHub diff', 'Repo conventions'],
        'outputs': ['Ordered review findings', 'Risk summary', 'Improvement suggestions'],
        'success': ['The review is grounded in the actual diff.', 'Findings are actionable.', 'Risky changes are prioritized.'],
        'non_goals': ['Generic praise-only review', 'Reviewing without reading the diff'],
    },
    'recurring-loop-runner': {
        'title': 'Recurring Loop Runner',
        'examples': ['Check the deploy every 15 minutes.', 'Run this slash-command hourly and execute it once now.'],
        'inputs': ['Requested cadence', 'Prompt or command to repeat'],
        'outputs': ['Scheduled recurring task', 'Immediate first execution', 'Cancellation details'],
        'success': ['The interval is parsed correctly.', 'The task is both scheduled and run once immediately.', 'The user knows how to stop it later.'],
        'non_goals': ['One-off commands with no repeating behavior'],
    },
    'remote-agent-scheduler': {
        'title': 'Remote Agent Scheduler',
        'examples': ['Create a nightly remote agent to summarize repo health.', 'Update this cloud trigger to use a different environment and cron.'],
        'inputs': ['Desired action', 'Repo source', 'Environment and connector context', 'Cron schedule'],
        'outputs': ['Trigger definition', 'Run or update confirmation', 'Operational notes'],
        'success': ['The action type is clear.', 'Remote environment assumptions are explicit.', 'Auth and repo blockers are surfaced.'],
        'non_goals': ['Local cron setup', 'Ambiguous cloud-vs-local scheduling'],
    },
    'runtime-verifier': {
        'title': 'Runtime Verifier',
        'examples': ['Actually run the app and prove this change works.', 'Verify this endpoint or CLI flow in a live environment.'],
        'inputs': ['Verification target', 'Expected runtime behavior', 'Environment startup instructions'],
        'outputs': ['Verification plan', 'Pass/fail evidence', 'Cleanup summary'],
        'success': ['The behavior was exercised in a live runtime.', 'Evidence is explicit.', 'Started processes were cleaned up.'],
        'non_goals': ['Stopping at unit tests only', 'Vague confidence statements with no evidence'],
    },
    'security-review-workflow': {
        'title': 'Security Review Workflow',
        'examples': ['Review this branch only for concrete security bugs.', 'Find high-confidence vulnerabilities in the current diff and ignore noise.'],
        'inputs': ['Diff against base', 'Changed files', 'Relevant security context'],
        'outputs': ['High-signal security findings', 'Severity and exploit path', 'Fix recommendations'],
        'success': ['Only concrete issues are reported.', 'False positives are aggressively filtered.', 'Each finding is actionable.'],
        'non_goals': ['General style review', 'Speculative low-confidence security commentary'],
    },
    'session-debug-log-investigator': {
        'title': 'Session Debug Log Investigator',
        'examples': ['Help me understand why this Claude Code session is misbehaving.', 'Turn on debug logging and diagnose this issue from the latest logs.'],
        'inputs': ['Issue description', 'Current log availability', 'Relevant settings files'],
        'outputs': ['Error or warning analysis', 'Likely causes', 'Suggested reproduction or next steps'],
        'success': ['Recent logs were interpreted correctly.', 'The diagnosis distinguishes config vs runtime issues.', 'Follow-up steps are specific.'],
        'non_goals': ['Reading giant logs in full without need', 'Pretending to diagnose pre-log activity that was never captured'],
    },
    'statusline-setup': {
        'title': 'Statusline Setup',
        'examples': ['Set up Claude statusline to match my shell prompt.', 'Tune the statusline UI from current shell config.'],
        'inputs': ['Existing shell prompt context', 'Current Claude settings'],
        'outputs': ['Updated statusline-related settings', 'Refinement notes'],
        'success': ['The shell context was inspected first.', 'Settings changes stayed minimal.', 'User preferences were preserved.'],
        'non_goals': ['Blind statusline config rewrites'],
    },
    'stuck-session-diagnosis': {
        'title': 'Stuck Session Diagnosis',
        'examples': ['Find out why another Claude session on this machine is frozen.', 'Inspect local agent processes and tell me if one is hung.'],
        'inputs': ['Observed symptom', 'Process state', 'Optional target PID'],
        'outputs': ['Diagnosis summary', 'Evidence from process inspection', 'Escalation-ready report'],
        'success': ['Suspicious sessions were confirmed rather than guessed.', 'Supporting process data was captured.', 'The report is concise and actionable.'],
        'non_goals': ['Killing processes by default', 'Reporting transient blips as confirmed hangs'],
    },
    'verifier-skill-generator': {
        'title': 'Verifier Skill Generator',
        'examples': ['Generate verifier skills for this frontend and API.', 'Inspect the project and create runtime verifier skills the Verify agent can find.'],
        'inputs': ['Project layout', 'Detected stacks', 'Verification tooling availability'],
        'outputs': ['One or more verifier skill folders', 'Project-specific setup guidance'],
        'success': ['Relevant project areas were detected correctly.', 'Generated verifiers match web, CLI, or API needs.', 'Each verifier is discoverable and reusable.'],
        'non_goals': ['Unit-test-only verification setup', 'Generic verifier templates with no project specifics'],
    },
    'workflow-skillify': {
        'title': 'Workflow Skillify',
        'examples': ['Turn this successful session into a reusable skill.', 'Capture the process we just followed as a formal skill.'],
        'inputs': ['Session history', 'User corrections', 'Desired save scope'],
        'outputs': ['Reusable SKILL.md', 'Trigger and argument guidance'],
        'success': ['The resulting skill captures the real workflow.', 'User corrections are preserved as rules.', 'The saved skill is specific and reusable.'],
        'non_goals': ['Over-interviewing simple workflows', 'Saving a vague process with no triggers or success criteria'],
    },
}

for slug, meta in catalog.items():
    path = skills_root / slug / 'SKILL.md'
    txt = path.read_text(encoding='utf-8')
    parts = txt.split('---\n', 2)
    frontmatter = '---\n' + parts[1] + '---\n\n'
    body = parts[2]
    body_no_prov, prov = body.split('## Source Provenance\n', 1)
    extra = []
    extra.append('## Example Requests\n' + '\n'.join(f'- {x}' for x in meta['examples']))
    extra.append('## Inputs\n' + '\n'.join(f'- {x}' for x in meta['inputs']))
    extra.append('## Outputs\n' + '\n'.join(f'- {x}' for x in meta['outputs']))
    extra.append('## Success Criteria\n' + '\n'.join(f'- {x}' for x in meta['success']))
    extra.append('## Non-Goals\n' + '\n'.join(f'- {x}' for x in meta['non_goals']))
    new_body = body_no_prov.rstrip() + '\n\n' + '\n\n'.join(extra) + '\n\n## Source Provenance\n' + prov.lstrip()
    path.write_text(frontmatter + new_body, encoding='utf-8')

readme = '''# Claude Code Skills

A production-ready collection of standalone skills extracted from reusable Claude Code workflows and repackaged as public skills for agent ecosystems.

## What This Is

This project turns high-value Claude Code capabilities into individually publishable skills that can be reused outside the original product context.

The extraction focuses on workflows that are:
- repeatable across sessions and repositories
- useful to multiple agent runtimes
- strong enough to justify a dedicated public skill
- safer as standalone capabilities than as hidden product internals

## Included Skill Families

| Family | Skills |
|---|---|
| Planning and Orchestration | `batch-migration-orchestrator`, `workflow-skillify`, `verifier-skill-generator` |
| Coding and Git | `code-simplifier`, `git-commit-workflow`, `git-commit-pr-workflow`, `pull-request-reviewer`, `security-review-workflow` |
| Runtime and Diagnostics | `runtime-verifier`, `session-debug-log-investigator`, `stuck-session-diagnosis` |
| Browser and API | `chrome-web-automation`, `claude-api-builder` |
| Agent Ops and Config | `claude-md-initializer`, `claude-settings-editor`, `keybindings-customizer`, `memory-landscape-review`, `recurring-loop-runner`, `remote-agent-scheduler`, `statusline-setup` |

## Published to ClawHub

Current publish state lives in [`CLAWHUB_PUBLISH_STATUS.md`](./CLAWHUB_PUBLISH_STATUS.md).

Already published:
- `claude-code-batch-migration-orchestrator`
- `claude-code-chrome-web-automation`
- `claude-code-claude-api-builder`
- `claude-code-claude-md-initializer`
- `claude-code-claude-settings-editor`

## Repository Structure

- `skills/`: one skill per directory
- `docs/CATALOG.md`: quick reference catalog for all extracted skills
- `EXTRACTION_REPORT.md`: source-module to skill mapping
- `CLAWHUB_PUBLISH_STATUS.md`: publish progress and remaining queue
- `generate_skills.py`: deterministic generator for the current skill set
- `publish_clawhub.sh`: full publish script
- `resume_clawhub_publish.sh`: resume script for rate-limited follow-up publishes

## Quality Bar

This repository treats each skill as a public artifact, not a private prompt snippet.

Every shipped skill includes:
- clean YAML frontmatter
- agent-facing metadata in `agents/openai.yaml`
- explicit workflows and guardrails
- example requests
- clear input and output expectations
- success criteria and non-goals
- provenance back to the analyzed Claude Code source module

## Selection Policy

Included:
- reusable workflows
- operator-facing or agent-facing capabilities
- repeatable review, verification, planning, and automation patterns

Excluded:
- entitlement-gated UI toggles
- account-specific product settings with weak reuse outside the original app
- novelty helpers that do not justify standalone public maintenance

## Use the Skills Locally

Install or copy any individual skill directory into a compatible agent workspace, or publish and install through ClawHub.

For local experimentation, each skill is already self-contained under `skills/<slug>/`.

## Publish to ClawHub

Publish everything from the current queue:

```bash
./publish_clawhub.sh
```

If ClawHub rate-limits new skill creation, resume later with:

```bash
./resume_clawhub_publish.sh
```

## Source and Intent

These skills were derived by reading a local Claude Code source snapshot and extracting only the modules that map cleanly onto standalone public skills.

See [`EXTRACTION_REPORT.md`](./EXTRACTION_REPORT.md) for the exact mapping.
'''
(root / 'README.md').write_text(readme, encoding='utf-8')

catalog_md = ['# Skill Catalog', '', '| Skill | Focus | Source |', '|---|---|---|']
focus = {
    'batch-migration-orchestrator': 'Parallel planning for broad migrations',
    'chrome-web-automation': 'Live browser automation in Chrome',
    'claude-api-builder': 'Anthropic API and Agent SDK implementation',
    'claude-md-initializer': 'Repository onboarding documentation',
    'claude-settings-editor': 'Claude settings and hook configuration',
    'code-simplifier': 'Reuse, quality, and efficiency cleanup',
    'git-commit-pr-workflow': 'Commit, push, and PR lifecycle',
    'git-commit-workflow': 'Single safe git commit flow',
    'keybindings-customizer': 'Shortcut and chord customization',
    'memory-landscape-review': 'Memory promotion and cleanup',
    'pull-request-reviewer': 'Diff-grounded PR review',
    'recurring-loop-runner': 'Recurring prompts and checks',
    'remote-agent-scheduler': 'Cloud trigger scheduling for remote agents',
    'runtime-verifier': 'Live verification of behavior',
    'security-review-workflow': 'High-signal security review',
    'session-debug-log-investigator': 'Session debug log diagnosis',
    'statusline-setup': 'Statusline configuration',
    'stuck-session-diagnosis': 'Frozen or slow session diagnosis',
    'verifier-skill-generator': 'Project-specific verifier generation',
    'workflow-skillify': 'Turn a session into a skill',
}
for slug, meta in catalog.items():
    catalog_md.append(f"| `{slug}` | {focus[slug]} | `{slug}` |")
(root / 'docs' / 'CATALOG.md').write_text('\n'.join(catalog_md) + '\n', encoding='utf-8')

publishing = '''# Publishing Notes

## ClawHub

This project publishes each skill under a `claude-code-` prefixed slug to avoid collisions with existing public skills.

## Rate Limits

ClawHub currently limits this account to 5 new skills per hour.

When the queue is blocked:
1. wait for the next publish window
2. run `./resume_clawhub_publish.sh`
3. update `CLAWHUB_PUBLISH_STATUS.md`

## GitHub

Primary repository: https://github.com/wimi321/claude-code-skills-extract
'''
(root / 'docs' / 'PUBLISHING.md').write_text(publishing, encoding='utf-8')

license_text = '''MIT License

Copyright (c) 2026 haoc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
(root / 'LICENSE').write_text(license_text, encoding='utf-8')
print('polished repo and skills')
