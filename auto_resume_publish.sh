#!/bin/zsh
set -euo pipefail
cd /Users/haoc/Developer/cc-mg55
LOG=auto_resume_publish.log
while true; do
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] attempting resume publish" >> "$LOG"
  if ./resume_clawhub_publish.sh >> "$LOG" 2>&1; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] publish queue finished" >> "$LOG"
    exit 0
  fi
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] rate limited or interrupted; sleeping 3700s" >> "$LOG"
  sleep 3700
done
