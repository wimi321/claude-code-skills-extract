# Publishing Notes

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
