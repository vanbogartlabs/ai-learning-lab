# Production Repository Structure

**Project:** *Built Here: The Cedar Rapids Advantage*  
**Status:** v1.0  
**Purpose:** Define the operational filesystem Hermes and all specialist agents must use.

## Governing Rule

Every durable project output must be stored in the repository.  
Chat history, temporary context, and agent memory are not authoritative.

## Directory Tree

```text
built-here-repository/
├── governance/
├── project_state/
├── research/
│   ├── questions/
│   ├── companies/
│   ├── founders/
│   ├── institutions/
│   ├── industries/
│   ├── peer_cities/
│   ├── timelines/
│   └── themes/
├── evidence/
│   ├── sources/
│   ├── claims/
│   └── citations/
├── entities/
│   ├── people/
│   ├── companies/
│   ├── places/
│   └── organizations/
├── book/
│   ├── architecture/
│   ├── briefs/
│   ├── drafts/
│   ├── final/
│   ├── front_matter/
│   └── back_matter/
├── reviews/
│   ├── developmental/
│   ├── fact_check/
│   ├── continuity/
│   └── style/
├── decisions/
├── logs/
│   ├── agent_runs/
│   └── errors/
├── exports/
└── archive/
    └── superseded/
```

## Folder Responsibilities

### `governance/`
Contains approved governing artifacts. These files change rarely and control all downstream work.

### `project_state/`
Contains the current machine-readable and human-readable state of the project, including active phase, blocked work, approval status, and next actions.

### `research/questions/`
One file per approved research question. These are the primary work units Hermes schedules.

### `research/*`
Stores topic-specific research synthesis. These files summarize evidence but do not replace source or claim records.

### `evidence/sources/`
One source record per source. Each record must comply with `Source_Record.schema.md`.

### `evidence/claims/`
One claim record per material claim. Claims link sources, research questions, entities, and chapters.

### `evidence/citations/`
Citation maps and formatted citation outputs derived from source and claim records.

### `entities/`
Canonical records for people, companies, places, and organizations. Duplicate entities are prohibited.

### `book/architecture/`
Thesis assessments, narrative architecture, part structure, table of contents, and chapter dependency maps.

### `book/briefs/`
Approved and provisional chapter briefs.

### `book/drafts/`
First drafts and active revisions.

### `book/final/`
Approved, locked chapter files.

### `book/front_matter/`
Title page, introduction materials, acknowledgements, AI disclosure, and other front matter.

### `book/back_matter/`
Notes, bibliography, appendices, index inputs, and end matter.

### `reviews/`
Formal editorial and verification reports. Reviews never overwrite the artifact being reviewed.

### `decisions/`
Material human and orchestrator decisions, including rationale and downstream impact.

### `logs/`
Operational logs, agent execution records, failures, retries, and recovery data.

### `exports/`
Generated manuscript packages and publication files. These are derived outputs, not sources of truth.

### `archive/superseded/`
Replaced artifacts preserved for traceability.

## Naming Conventions

Use lowercase kebab-case for filenames except approved governing documents.

Examples:

```text
rq-001-is-the-premise-true.md
person-howard-hall.yaml
company-collins-radio.yaml
claim-clm-0001.yaml
chapter-01-brief.md
chapter-01-draft-v01.md
chapter-01-final.md
decision-dec-0001.md
review-chapter-01-fact-check-v01.md
```

## Required Identifiers

- Research questions: `RQ-###`
- Sources: `SRC-#####`
- Claims: `CLM-#####`
- People: `PER-#####`
- Companies: `COM-#####`
- Organizations: `ORG-#####`
- Places: `PLC-#####`
- Decisions: `DEC-#####`
- Reviews: `REV-#####`
- Agent runs: `RUN-YYYYMMDD-####`

Identifiers are permanent and may not be reused.

## Artifact Lifecycle

Every operational artifact moves through:

```text
proposed
→ active
→ under_review
→ approved
→ locked
```

Optional terminal states:

```text
rejected
superseded
archived
```

### Rules

- `proposed`: created but not yet accepted into active work.
- `active`: currently in use or being developed.
- `under_review`: awaiting automated or human review.
- `approved`: accepted for downstream use.
- `locked`: authoritative and change-controlled.
- `rejected`: failed review and cannot be used.
- `superseded`: replaced by a newer artifact.
- `archived`: retained only for history.

No artifact may skip a required human approval gate.

## Versioning Rules

- Use Git for all version history.
- Do not encode versions in canonical filenames unless multiple active review copies are required.
- Final approved files use stable filenames.
- Superseded versions move to `archive/superseded/` only when needed for operational clarity.
- Never silently overwrite a rejected or reviewed artifact.

## Ownership Rules

Each artifact must identify:

- artifact ID
- artifact type
- owner role
- status
- created date
- modified date
- dependencies
- source links
- approval requirements

One role owns an artifact at a time. Multiple agents may contribute, but ownership must remain explicit.

## Hermes Operating Rules

Hermes must:

1. Validate this structure at boot.
2. Create missing required directories.
3. Refuse to store durable work outside the correct folder.
4. Update `project_state/project-status.yaml` after material work.
5. Preserve failed outputs and review records.
6. Stop at required human approval gates.
7. Commit coherent batches of work to Git.
8. Resume from repository state rather than chat memory.

## Minimum State Files

The repository must always contain:

- `project_state/project-status.yaml`
- `project_state/work-queue.yaml`
- `project_state/approval-gates.yaml`
- `project_state/open-issues.yaml`

## Completion Standard

The repository is operational when Hermes can:

- determine the current phase,
- identify ready work,
- assign agents,
- locate governing rules,
- trace claims to sources,
- locate chapter status,
- stop at approval gates,
- and resume after interruption without relying on conversation history.
