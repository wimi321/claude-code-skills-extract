#!/bin/zsh
set -euo pipefail

OWNER='wimi321'
ROOT='/Users/haoc/Developer/cc-mg55/skills'

entries=(
  'code-simplify|Code Simplifier|code-simplifier'
  'git-commit-pr-workflow|Git Commit PR Workflow|git-commit-pr-workflow'
  'git-commit-workflow|Git Commit Workflow|git-commit-workflow'
  'keybindings-customizer|Keybindings Customizer|keybindings-customizer'
  'memory-landscape-review|Memory Landscape Review|memory-landscape-review'
  'pr-audit|Pull Request Reviewer|pull-request-reviewer'
  'recurring-loop-runner|Recurring Loop Runner|recurring-loop-runner'
  'remote-agent-scheduler|Remote Agent Scheduler|remote-agent-scheduler'
  'runtime-verifier|Runtime Verifier|runtime-verifier'
  'security-review-workflow|Security Review Workflow|security-review-workflow'
  'session-debug-log-investigator|Session Debug Log Investigator|session-debug-log-investigator'
  'statusline-setup|Statusline Setup|statusline-setup'
  'stuck-session-diagnosis|Stuck Session Diagnosis|stuck-session-diagnosis'
  'verifier-skill-generator|Verifier Skill Generator|verifier-skill-generator'
  'workflow-skillify|Workflow Skillify|workflow-skillify'
)

already_owned() {
  local slug="$1"
  local out
  if ! out=$(clawhub inspect "$slug" --json 2>/dev/null); then
    return 1
  fi
  local owner
  owner=$(printf '%s' "$out" | jq -r '.owner.handle // .publisher.handle // .author.handle // .creator.handle // empty' 2>/dev/null)
  [[ "$owner" == "$OWNER" ]]
}

for entry in "${entries[@]}"; do
  slug=${entry%%|*}
  rest=${entry#*|}
  name=${rest%%|*}
  dir=${rest##*|}

  if already_owned "$slug"; then
    echo "Skipping already published: $slug"
    continue
  fi

  echo "Publishing $slug"
  if clawhub publish "$ROOT/$dir" --slug "$slug" --name "$name" --version 1.0.0 --changelog 'Initial extraction from local Claude Code source' --tags latest,claude-code,extracted; then
    echo "Published $slug"
    continue
  fi

  echo "Failed on $slug" >&2
  exit 1
done

echo 'Publish queue finished'
