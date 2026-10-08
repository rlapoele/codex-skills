# Upstream provenance

This repository contains a modified version of the `domain-modeling` skill from:

- Repository: https://github.com/schneidenbach/skills
- Source revision: `0da27f7c38d44d2b38755cdafdce19d8a5b7b6c1`
- Original path: `skills/domain-modeling`

The upstream work credits Matt Pocock's skills collection as its original inspiration.

## Modifications

- Made invocation explicit-only.
- Made repository-local conventions authoritative.
- Prevented documentation writes during exploratory discussion.
- Added authorization requirements for glossary creation and modification.
- Delegated all ADR filesystem operations to `agent-skills:documentation-and-adrs`.
- Added ADR lifecycle and deletion guardrails.
- Removed the competing ADR template.
- Packaged the skill as a portable Codex plugin with a repository marketplace.
