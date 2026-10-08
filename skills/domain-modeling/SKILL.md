---
name: domain-modeling
description: Explicitly guided domain modeling for sharpening project terminology, bounded contexts, and domain relationships.
license: MIT
---

# Domain Modeling

Actively sharpen a project's domain model by challenging terminology, probing edge cases, and reconciling the stated model with the code. Use this as an explicit working mode, not as a prerequisite for ordinary coding or for merely reading existing domain documentation.

## Responsibility boundary

- Explicit user instructions and repository-local instructions take precedence over this skill.
- Existing repository terminology, file locations, and documentation conventions take precedence over this skill's fallback guidance.
- Treat discussion as exploratory by default. Do not create or modify domain documentation merely because a term appears resolved.
- Persist glossary changes only when the user has requested documentation changes or confirms the proposed change and location.
- This skill owns domain analysis and glossary proposals. It does not own ADR file operations.

## Discover the existing model

Before proposing or persisting changes, inspect the relevant repository instructions, existing `CONTEXT.md` or equivalent glossary, any `CONTEXT-MAP.md`, existing ADRs, and the code that implements the concepts under discussion.

Do not introduce a parallel glossary, context map, ADR directory, numbering scheme, or template. If existing evidence conflicts, surface the conflict and ask the user to resolve it.

If no domain glossary exists and the user wants the model documented, propose an appropriate location. Create it only after the user requests documentation or confirms that location. Use [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) only as a fallback when the repository has no established glossary format.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the established language, call out the mismatch and ask which meaning is intended.

### Sharpen fuzzy language

When a term is vague or overloaded, identify the competing meanings and propose a precise canonical term. Do not silently choose one when the distinction affects behavior or scope.

### Discuss concrete scenarios

Stress-test domain relationships with specific scenarios, especially edge cases that expose unclear ownership, lifecycle, identity, invariants, or boundaries between concepts.

### Cross-reference with code

When the user states how the domain works, check whether the code and existing documentation agree. Surface contradictions and preserve the distinction between intended behavior, documented behavior, and implemented behavior.

### Maintain the glossary deliberately

When persistence is authorized, update the existing glossary in the smallest relevant change. Keep it focused on domain language rather than implementation details, feature specifications, or session notes.

If no write is authorized, summarize resolved terminology and proposed glossary changes in the response instead of editing files.

## ADR qualification and handoff

Offer an ADR only when all three conditions are met:

1. **Hard to reverse**: changing the decision later would have meaningful cost.
2. **Surprising without context**: a future reader would reasonably ask why this approach was chosen.
3. **A real trade-off**: credible alternatives existed and were rejected for specific reasons.

If any condition is missing, do not propose an ADR.

When an ADR action is warranted, this skill prepares the decision material but must not create, modify, move, rename, or delete ADR files directly. Prepare a handoff containing:

- the decision context and constraints;
- the chosen option;
- alternatives considered and why they were rejected;
- expected positive and negative consequences;
- affected bounded contexts and glossary terms;
- the requested lifecycle action: create, clarify, accept, deprecate, supersede, or remove a draft.

Then explicitly use the available `agent-skills:documentation-and-adrs` skill as the sole ADR-writing workflow. That skill must inspect and follow repository conventions before making changes. Do not combine its workflow with a separate ADR template from this skill.

If `agent-skills:documentation-and-adrs` is unavailable, or if repository conventions conflict, stop and explain the issue instead of editing ADR files directly.

### ADR lifecycle guardrails

- Do not delete an accepted, deprecated, or superseded ADR; it is historical evidence.
- Do not rewrite an accepted ADR to describe a materially different decision. Create a new ADR that supersedes it.
- Direct edits to an accepted ADR are limited to corrections, non-substantive clarifications, links, and lifecycle status changes that preserve the original decision.
- Remove an ADR only when it is an unaccepted draft or accidental duplicate and the user explicitly requests removal.
- Use one ADR workflow per task: `agent-skills:documentation-and-adrs` owns all ADR filesystem operations.
