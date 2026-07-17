# HERMES_DATA_FIRST_ADDENDUM.md

This document supplements `HERMES_ORCHESTRATOR.md`.

## Canonical Knowledge Rule

Hermes must treat records in `data/` as the factual source of truth.

Markdown in `views/` is generated and must not be edited as canonical data.

Governance Markdown remains authoritative for policy and editorial direction.

Manuscript prose remains authoritative only as approved prose, not as the master factual database.

## Required Agent Sequence

For research work:

1. Register or identify entities.
2. Register sources.
3. Create or update claims.
4. Create events, quotes, and relationships where applicable.
5. Validate records against schemas.
6. Generate human-readable views.
7. Permit synthesis or drafting only after validation.

## Prohibitions

Agents may not:

- store a material fact only in a narrative note,
- create duplicate canonical entities,
- cite a URL without a Source Record,
- insert an unsupported claim into a chapter,
- edit generated Markdown instead of its source record,
- silently resolve conflicting evidence.

## Chapter Gate Rule

Before a chapter brief can be approved, its Chapter Record must list the research questions and claims it depends on.

Before a first draft can be approved, every material factual assertion must map to claim IDs.

Before a final chapter can be locked, its claim map and quote records must pass verification.
