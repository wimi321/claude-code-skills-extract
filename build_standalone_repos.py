#!/usr/bin/env python3

from pathlib import Path
import shutil
import yaml


ROOT = Path("/Users/haoc/Developer/cc-mg55")
SKILLS_ROOT = ROOT / "skills"
OUT_ROOT = ROOT / "standalone-repos"
LICENSE_TEXT = (ROOT / "LICENSE").read_text(encoding="utf-8")


def parse_skill(skill_dir: Path) -> tuple[dict, dict[str, str], str]:
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    parts = skill_text.split("---\n", 2)
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]

    sections: dict[str, str] = {}
    current = None
    buffer: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
        elif current is not None:
            buffer.append(line)
    if current is not None:
        sections[current] = "\n".join(buffer).strip()

    return frontmatter, sections, body


def readme_for_skill(title: str, description: str, sections: dict[str, str]) -> str:
    examples = sections.get("Example Requests", "- See `SKILL.md` for usage patterns.")
    workflow = sections.get("Workflow", "See `SKILL.md`.")
    inputs = sections.get("Inputs", "See `SKILL.md`.")
    outputs = sections.get("Outputs", "See `SKILL.md`.")
    success = sections.get("Success Criteria", "See `SKILL.md`.")
    non_goals = sections.get("Non-Goals", "See `SKILL.md`.")
    provenance = sections.get("Source Provenance", "Derived from local Claude Code source analysis.")

    return f"""# {title}

{description}

## Overview

This repository packages **{title}** as a standalone public skill repository. The repository root is the skill root, so it can be used directly in agent workspaces, mirrored into other skill collections, or published through registries such as ClawHub.

## Why This Exists

This project is part of the broader Claude Code skill extraction effort: reusable Claude Code workflows are being upgraded into independently maintained, public-facing skills with clearer contracts, stronger documentation, and standalone distribution.

## Example Requests

{examples}

## Workflow

{workflow}

## Inputs

{inputs}

## Outputs

{outputs}

## Success Criteria

{success}

## Non-Goals

{non_goals}

## Repository Layout

- `SKILL.md`: the skill definition
- `agents/openai.yaml`: agent-facing metadata
- `references/`: supporting provenance notes
- `LICENSE`: repository license

## Installation

Copy this repository root into a compatible skill directory, or publish/install it through your preferred skill registry workflow.

## Provenance

{provenance}

## Related

- Parent collection: [claude-code-skills-extract](https://github.com/wimi321/claude-code-skills-extract)
"""


def build_repo(skill_dir: Path) -> None:
    repo_name = f"claude-code-{skill_dir.name}"
    repo_dir = OUT_ROOT / repo_name

    if repo_dir.exists():
        shutil.rmtree(repo_dir)
    repo_dir.mkdir(parents=True)

    shutil.copy2(skill_dir / "SKILL.md", repo_dir / "SKILL.md")
    shutil.copytree(skill_dir / "agents", repo_dir / "agents")
    shutil.copytree(skill_dir / "references", repo_dir / "references")
    (repo_dir / "LICENSE").write_text(LICENSE_TEXT, encoding="utf-8")
    (repo_dir / ".gitignore").write_text(".DS_Store\n.clawhub/\n", encoding="utf-8")

    frontmatter, sections, body = parse_skill(skill_dir)
    title = next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), skill_dir.name)
    readme = readme_for_skill(title, frontmatter["description"], sections)
    (repo_dir / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    OUT_ROOT.mkdir(exist_ok=True)
    count = 0
    for skill_dir in sorted(SKILLS_ROOT.iterdir()):
        if skill_dir.is_dir():
            build_repo(skill_dir)
            count += 1
    print(f"generated {count} standalone repos in {OUT_ROOT}")


if __name__ == "__main__":
    main()
