# Guarded Domain Modeling for Codex

An explicit-only domain-modeling skill for Codex. It sharpens project terminology, bounded contexts, and domain relationships while keeping documentation changes authorized and repository conventions authoritative.

## Key behavior

- Activates only when explicitly invoked as `$domain-modeling`.
- Treats discussion as exploratory unless documentation changes are requested or confirmed.
- Uses existing glossary and ADR conventions rather than creating parallel structures.
- Qualifies architecture decisions, but delegates every ADR file operation to `agent-skills:documentation-and-adrs`.
- Preserves accepted ADRs as historical evidence; materially changed decisions supersede them.

## Prerequisite

ADR operations require the `documentation-and-adrs` skill from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills):

```bash
codex plugin marketplace add addyosmani/agent-skills
codex plugin add agent-skills@agent-skills
```

If that skill is unavailable, `$domain-modeling` stops rather than editing ADR files directly.

## Install as a native Codex plugin

Install the stable production channel:

```bash
codex plugin marketplace add rlapoele/codex-skills --ref releases
codex plugin add guarded-domain-modeling@rlapoele-codex-skills
```

For a reproducible installation, replace `releases` with a release tag such as `v0.1.0`.

Start a new Codex session after installation, then invoke:

```text
$domain-modeling
```

Do not install this plugin alongside another global skill named `domain-modeling`; duplicate skill identities can make discovery ambiguous.

## Branches and releases

- `dev`: development, experiments, and validation.
- `releases`: validated production work and the supported plugin marketplace channel.
- `main`: backup of the latest released commit.
- Annotated tags such as `v0.1.0`: immutable release points.

Release commits are promoted from `dev` to `releases`, tagged, and then fast-forwarded to `main` so all three release pointers share the same validated history.

## Development

Install validation dependencies and run the repository checks:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

## Provenance

This skill is derived from [`schneidenbach/skills`](https://github.com/schneidenbach/skills) and ultimately credits Matt Pocock's skills collection. See [UPSTREAM.md](./UPSTREAM.md) for the source revision and modification summary.

## License

MIT. See [LICENSE](./LICENSE).
