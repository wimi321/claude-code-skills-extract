#!/usr/bin/env python3

from pathlib import Path
import shutil
import yaml


ROOT = Path("/Users/haoc/Developer/cc-mg55")
SKILLS_ROOT = ROOT / "skills"
OUT_ROOT = ROOT / "standalone-repos"
LICENSE_TEXT = (ROOT / "LICENSE").read_text(encoding="utf-8")
PARENT_REPO = "https://github.com/wimi321/claude-code-skills-extract"


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


def first_title(body: str, fallback: str) -> str:
    return next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), fallback)


def non_empty_lines(text: str, fallback: list[str]) -> list[str]:
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    return lines or fallback


def bulletize(text: str, fallback: list[str]) -> str:
    lines = non_empty_lines(text, fallback)
    output: list[str] = []
    for line in lines:
        if line.startswith(("- ", "* ", "1. ", "2. ", "3. ", "4. ", "5. ")):
            output.append(line)
        else:
            output.append(f"- {line}")
    return "\n".join(output)


def numbered(text: str, fallback: list[str]) -> str:
    lines = non_empty_lines(text, fallback)
    output: list[str] = []
    for index, line in enumerate(lines, start=1):
        if line[:3] == f"{index}. ":
            output.append(line)
        else:
            output.append(f"{index}. {line.lstrip('-* ').strip()}")
    return "\n".join(output)


def zh_lines(text: str, fallback: list[str]) -> str:
    lines = non_empty_lines(text, fallback)
    return "\n".join(f"- {line.lstrip('-* ').strip()}" for line in lines)


def readme_for_skill(
    repo_name: str,
    title: str,
    description: str,
    short_description: str,
    sections: dict[str, str],
) -> str:
    repo_url = f"https://github.com/wimi321/{repo_name}"
    examples = bulletize(
        sections.get("Example Requests", ""),
        ["See `SKILL.md` for request patterns and invocation examples."],
    )
    workflow = numbered(
        sections.get("Workflow", ""),
        ["Inspect the task and confirm the real scope before acting."],
    )
    inputs = bulletize(
        sections.get("Inputs", ""),
        ["Task-specific context, constraints, and verification expectations."],
    )
    outputs = bulletize(
        sections.get("Outputs", ""),
        ["A reproducible, agent-ready outcome documented in `SKILL.md`."],
    )
    success = bulletize(
        sections.get("Success Criteria", ""),
        ["The workflow produces a high-signal result with clear boundaries and validation."],
    )
    non_goals = bulletize(
        sections.get("Non-Goals", ""),
        ["Use a different skill when the request does not match this workflow."],
    )
    provenance = sections.get("Source Provenance", "Derived from local Claude Code source analysis.")

    return f"""# {title}

[![Repo](https://img.shields.io/badge/github-{repo_name}-181717?logo=github)]({repo_url})
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Collection](https://img.shields.io/badge/collection-claude--code--skills--extract-blue)]({PARENT_REPO})

{description}

English | [简体中文](./README.zh-CN.md)

## Why This Skill Exists

{title} packages a reusable Claude Code workflow as a standalone public skill repository. It is designed for agent teams that want a well-documented, installable, and maintainable capability rather than an internal prompt fragment.

## Highlights

- Focused, reusable workflow with a clear trigger boundary
- Standalone skill root that works well in agent workspaces
- Agent metadata in `agents/openai.yaml`
- Public provenance back to the extracted Claude Code source
- Bilingual documentation for English and Chinese readers

## What It Is Good At

- {short_description}
- Running the workflow described in `SKILL.md` with explicit boundaries
- Producing repeatable outputs for operators and agent runtimes

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

## Installation

### Use as a standalone skill

Clone this repository and place the repository root in a compatible skill directory.

### Use from a larger collection

This skill is also included in the parent collection:

- [claude-code-skills-extract]({PARENT_REPO})

## Repository Layout

- `SKILL.md`: canonical skill instructions
- `README.md`: English project overview
- `README.zh-CN.md`: Simplified Chinese project overview
- `agents/openai.yaml`: UI-facing metadata for agent runtimes
- `references/`: provenance and support notes
- `LICENSE`: repository license

## Provenance

{provenance}

## Related Projects

- Parent collection: [claude-code-skills-extract]({PARENT_REPO})
- GitHub repository: [{repo_name}]({repo_url})
"""


def readme_zh_for_skill(
    repo_name: str,
    title: str,
    description: str,
    short_description: str,
    sections: dict[str, str],
) -> str:
    repo_url = f"https://github.com/wimi321/{repo_name}"
    examples = zh_lines(
        sections.get("Example Requests", ""),
        ["更多请求示例见 `SKILL.md`。"],
    )
    workflow = numbered(
        sections.get("Workflow", ""),
        ["先确认任务边界，再执行对应工作流。"],
    )
    inputs = zh_lines(
        sections.get("Inputs", ""),
        ["任务上下文、限制条件和验证要求。"],
    )
    outputs = zh_lines(
        sections.get("Outputs", ""),
        ["按 `SKILL.md` 约定生成可复用的技能输出。"],
    )
    success = zh_lines(
        sections.get("Success Criteria", ""),
        ["结果边界清晰、验证充分、可重复执行。"],
    )
    non_goals = zh_lines(
        sections.get("Non-Goals", ""),
        ["当请求不匹配本技能时，应切换到更合适的技能。"],
    )
    provenance = sections.get("Source Provenance", "来自本地 Claude Code 源码提取分析。")

    return f"""# {title}

[English](./README.md) | 简体中文

{description}

## 这个技能是做什么的

{title} 把 Claude Code 中可复用的一类工作流提取成独立 skill 仓库，方便在不同智能体环境里直接安装、复用和持续维护。

## 核心特点

- 聚焦单一能力边界，适合公开分发
- 仓库根目录就是 skill 根目录
- 内置 `agents/openai.yaml` 元数据
- 保留来源说明，便于追踪提取依据
- 提供中英文双语 README

## 擅长场景

- {short_description}
- 执行 `SKILL.md` 中定义的标准工作流
- 为智能体或操作者提供稳定、可复用的输出

## 示例请求

{examples}

## 工作流程

{workflow}

## 输入

{inputs}

## 输出

{outputs}

## 成功标准

{success}

## 不适用场景

{non_goals}

## 安装方式

### 作为独立 skill 使用

克隆本仓库，并将仓库根目录放入兼容的 skill 目录即可。

### 从合集仓库使用

该 skill 也收录在总仓库中：

- [claude-code-skills-extract]({PARENT_REPO})

## 仓库结构

- `SKILL.md`：技能主定义
- `README.md`：英文说明
- `README.zh-CN.md`：中文说明
- `agents/openai.yaml`：面向智能体 UI 的元数据
- `references/`：来源与补充说明
- `LICENSE`：开源许可证

## 来源说明

{provenance}

## 相关项目

- 总仓库：[claude-code-skills-extract]({PARENT_REPO})
- 当前仓库：[{repo_name}]({repo_url})
"""


def build_repo(skill_dir: Path) -> None:
    repo_name = f"{skill_dir.name}-skill"
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
    title = first_title(body, skill_dir.name)
    short_description = (
        yaml.safe_load((skill_dir / "agents" / "openai.yaml").read_text(encoding="utf-8"))
        .get("interface", {})
        .get("short_description", description_from(frontmatter))
    )
    readme = readme_for_skill(repo_name, title, description_from(frontmatter), short_description, sections)
    readme_zh = readme_zh_for_skill(repo_name, title, description_from(frontmatter), short_description, sections)
    (repo_dir / "README.md").write_text(readme, encoding="utf-8")
    (repo_dir / "README.zh-CN.md").write_text(readme_zh, encoding="utf-8")


def description_from(frontmatter: dict) -> str:
    return frontmatter["description"]


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
