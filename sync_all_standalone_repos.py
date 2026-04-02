#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys
import yaml


OWNER = "wimi321"
BASE = Path("/Users/haoc/Developer/cc-mg55/standalone-repos")
TOPICS = ["skill", "claude-code", "agents", "automation", "developer-tools"]


def sh(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if check and proc.returncode != 0:
        print("FAILED:", " ".join(cmd), file=sys.stderr)
        if proc.stdout:
            print(proc.stdout, file=sys.stderr)
        if proc.stderr:
            print(proc.stderr, file=sys.stderr)
        raise SystemExit(proc.returncode)
    return proc


def description_for(repo_dir: Path) -> str:
    text = (repo_dir / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(text.split("---\n", 2)[1])
    return frontmatter["description"]


def ensure_repo_exists(repo: str, description: str) -> None:
    exists = sh(["gh", "repo", "view", f"{OWNER}/{repo}"], check=False)
    if exists.returncode != 0:
        print(f"creating {repo}")
        sh(["gh", "repo", "create", f"{OWNER}/{repo}", "--public", "--description", description])


def update_repo_metadata(repo: str, description: str) -> None:
    cmd = [
        "gh",
        "repo",
        "edit",
        f"{OWNER}/{repo}",
        "--default-branch",
        "main",
        "--description",
        description,
    ]
    for topic in TOPICS:
        cmd.extend(["--add-topic", topic])
    sh(cmd, check=False)


def sync_git_remote(repo_dir: Path, repo: str) -> None:
    if not (repo_dir / ".git").exists():
        sh(["git", "init"], cwd=repo_dir)
    sh(["git", "checkout", "-B", "main"], cwd=repo_dir)
    if sh(["git", "remote", "get-url", "origin"], cwd=repo_dir, check=False).returncode == 0:
        sh(["git", "remote", "remove", "origin"], cwd=repo_dir)
    sh(["git", "remote", "add", "origin", f"https://github.com/{OWNER}/{repo}.git"], cwd=repo_dir)


def commit_if_needed(repo_dir: Path) -> None:
    sh(["git", "add", "."], cwd=repo_dir)
    status = sh(["git", "status", "--short"], cwd=repo_dir)
    if status.stdout.strip():
        sh(["git", "commit", "-m", "Initial standalone skill release"], cwd=repo_dir, check=False)


def main() -> None:
    for repo_dir in sorted(BASE.iterdir()):
        if not repo_dir.is_dir():
            continue
        repo = repo_dir.name
        description = description_for(repo_dir)
        ensure_repo_exists(repo, description)
        update_repo_metadata(repo, description)
        sync_git_remote(repo_dir, repo)
        commit_if_needed(repo_dir)
        sh(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_dir)
        print(f"synced {repo}")


if __name__ == "__main__":
    main()
