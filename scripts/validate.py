#!/usr/bin/env python3
"""Validate the guarded-domain-modeling plugin package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "domain-modeling"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
PLUGIN_JSON = ROOT / "plugin.json"
MARKETPLACE_JSON = ROOT / ".agents" / "plugins" / "marketplace.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


class ValidationError(Exception):
    """Raised when a package invariant is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict), f"{path.relative_to(ROOT)} must contain an object")
    return data


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict), f"{path.relative_to(ROOT)} must contain a mapping")
    return data


def validate_skill() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")

    frontmatter = yaml.safe_load(match.group(1))
    require(isinstance(frontmatter, dict), "SKILL.md frontmatter must be a mapping")
    require(frontmatter.get("name") == "domain-modeling", "Unexpected skill name")
    require(isinstance(frontmatter.get("description"), str), "Skill description is required")
    require(frontmatter.get("license") == "MIT", "Skill license must be MIT")
    require("[TODO:" not in text, "SKILL.md contains an unfinished TODO")
    require("agent-skills:documentation-and-adrs" in text, "ADR delegation is missing")
    require("ADR-FORMAT" not in text, "Obsolete ADR template reference remains")
    require(not (SKILL_DIR / "ADR-FORMAT.md").exists(), "Obsolete ADR template still exists")

    for target in re.findall(r"\]\((\./[^)#]+)", text):
        require((SKILL_DIR / target).resolve().is_file(), f"Missing skill reference: {target}")


def validate_skill_metadata() -> None:
    metadata = load_yaml(OPENAI_YAML)
    require(isinstance(metadata.get("interface"), dict), "openai.yaml interface is required")
    require(
        metadata.get("policy", {}).get("allow_implicit_invocation") is False,
        "domain-modeling must remain explicit-only",
    )


def validate_plugin() -> None:
    plugin = load_json(PLUGIN_JSON)
    require(plugin.get("name") == "guarded-domain-modeling", "Unexpected plugin name")
    version = plugin.get("version")
    require(isinstance(version, str) and SEMVER.fullmatch(version), "Invalid plugin version")
    require(plugin.get("repository") == "https://github.com/rlapoele/codex-skills", "Unexpected repository URL")
    require(plugin.get("license") == "MIT", "Plugin license must be MIT")
    require(SKILL_DIR.is_dir(), "skills/domain-modeling is missing")

    marketplace = load_json(MARKETPLACE_JSON)
    require(marketplace.get("name") == "rlapoele-codex-skills", "Unexpected marketplace name")
    entries = marketplace.get("plugins")
    require(isinstance(entries, list) and len(entries) == 1, "Marketplace must expose exactly one plugin")
    entry = entries[0]
    require(entry.get("name") == plugin["name"], "Marketplace plugin name does not match")
    require(entry.get("version") == version, "Marketplace and plugin versions do not match")
    require(entry.get("source") == {"source": "local", "path": "./"}, "Unexpected marketplace source")


def validate_attribution() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    require("Spencer Schneidenbach" in license_text, "Upstream Spencer Schneidenbach notice is missing")
    require("Matt Pocock" in license_text, "Upstream Matt Pocock notice is missing")
    require("Renaud Lapoële" in license_text, "Modification copyright notice is missing")

    upstream = (ROOT / "UPSTREAM.md").read_text(encoding="utf-8")
    require(
        "0da27f7c38d44d2b38755cdafdce19d8a5b7b6c1" in upstream,
        "Pinned upstream source revision is missing",
    )


def main() -> int:
    try:
        validate_skill()
        validate_skill_metadata()
        validate_plugin()
        validate_attribution()
    except (OSError, json.JSONDecodeError, yaml.YAMLError, ValidationError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
