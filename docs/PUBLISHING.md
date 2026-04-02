# Publishing Notes

This project publishes extracted skills across two surfaces:

- GitHub for standalone repositories
- ClawHub for installable registry distribution

## GitHub

Primary collection repository:

- [claude-code-skills-extract](https://github.com/wimi321/claude-code-skills-extract)

Standalone repositories are generated locally, then synced one-by-one to GitHub under the `<skill-slug>-skill` naming convention.

### Generate standalone repositories

```bash
python3 build_standalone_repos.py
```

### Sync all standalone repositories

```bash
python3 -u sync_all_standalone_repos.py
```

The sync script will:

- create missing public repositories
- set the default branch to `main`
- apply repository description and topics
- commit repository contents when needed
- push each repository to GitHub

## ClawHub

This project now targets concise ClawHub slugs such as `batch-migration-orchestrator`, `runtime-verifier`, and `workflow-skillify`.

When a bare short slug is already owned by another publisher, this project falls back to the shortest available alternative slug rather than returning to the old long prefix.

Current exceptions:

- `code-simplifier` publishes as `code-simplify`
- `pull-request-reviewer` publishes as `pr-audit`

An earlier publish pass used a legacy `claude-code-` prefix. Those legacy slugs may remain published because the current CLI does not provide an in-place slug rename command.

### Publish the current queue

```bash
./publish_clawhub.sh
```

### Resume after rate limiting

```bash
./resume_clawhub_publish.sh
```

The resume script now skips short slugs that are already owned by `wimi321` and continues with only the remaining unpublished skills.

### Unattended retry loop

```bash
./auto_resume_publish.sh
```

## Rate Limits

ClawHub currently limits this account to `5` new skills per hour.

When the queue is blocked:

1. wait for the next publish window
2. run `./resume_clawhub_publish.sh`
3. update `CLAWHUB_PUBLISH_STATUS.md`

## Operational Files

- [CLAWHUB_PUBLISH_STATUS.md](/Users/haoc/Developer/cc-mg55/CLAWHUB_PUBLISH_STATUS.md): current registry progress
- [docs/CATALOG.md](/Users/haoc/Developer/cc-mg55/docs/CATALOG.md): public skill catalog and repo links
- [EXTRACTION_REPORT.md](/Users/haoc/Developer/cc-mg55/EXTRACTION_REPORT.md): extraction lineage
