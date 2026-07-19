# DATA_FIRST_ARCHITECTURE.md

# Data-First Repository Architecture

**Project:** *Built Here: The Cedar Rapids Advantage*  
**Status:** v2.0  
**Migration rule:** Preserve prior artifacts as immutable history while allowing aggressive new manuscript versions.

## Core Principle

Structured records are canonical.

Markdown files remain essential for governance, editorial judgment, review, and manuscript prose, but factual project knowledge must be stored once in structured records and referenced everywhere else.

## Source of Truth Hierarchy

1. Approved governance documents
2. Canonical structured data in `data/`
3. Current project state in `project_state/`
4. Generated human-readable views in `views/`
5. Manuscript prose in `manuscript/`
6. Exports and presentation files

A generated view may never silently override canonical data.

## Repository Model

```text
BUILT HERE/
├── governance/             # Existing approved Markdown preserved
├── schemas/                # JSON Schemas for canonical records
├── data/                   # Canonical structured knowledge
│   ├── project/
│   ├── research_questions/
│   ├── sources/
│   ├── claims/
│   ├── entities/
│   ├── events/
│   ├── quotes/
│   ├── relationships/
│   ├── chapters/
│   ├── reviews/
│   └── decisions/
├── views/                  # Generated Markdown for humans
├── manuscript/             # Briefs, drafts, and approved prose
├── project_state/          # Current machine-readable state
├── workflows/              # Orchestration instructions
├── scripts/                # Validation and view-generation utilities
├── tests/                  # Fixtures and validation tests
├── logs/
├── exports/
└── archive/
```

## Canonical Record Types

### Source
Describes one source and its provenance.

### Claim
Represents one material factual or interpretive assertion.

### Entity
Represents one person, company, organization, or place.

### Event
Represents one dated or date-bounded occurrence.

### Quote
Stores exact quoted language with source location and permission status.

### Relationship
Represents a typed connection between entities, claims, events, or sources.

### Research Question
Tracks one bounded investigative question and its status.

### Chapter
Tracks chapter purpose, evidence dependencies, approval state, and manuscript paths.

### Review
Stores formal findings without overwriting the reviewed artifact.

### Decision
Records material human or orchestrator decisions and their rationale.

## Write Rules

Agents must write facts to structured records before relying on them in prose.

Agents may create Markdown synthesis only after referenced records exist.

Every material claim in a chapter must resolve to one or more claim IDs.

Every claim must resolve to supporting or contradicting source IDs.

Every quote must resolve to one source and a precise location.

Every entity reference should use a canonical entity ID.

## Generated Views

The system may generate:

- source catalogs
- claim ledgers
- entity dossiers
- timelines
- research-question dashboards
- chapter evidence maps
- contradiction reports
- unresolved issue reports

Generated files must contain a header stating that they are derived and naming the generator.

## Preservation Rule

All existing governance files remain in `governance/`.

Existing research Markdown should move to `archive/legacy_markdown/` only after its durable facts are migrated into canonical records.

Existing completed drafts remain untouched as prior versions. New versioned drafts may and should be rewritten aggressively once their factual boundaries and claim links are established.

## Migration Sequence

1. Copy the new directories and schemas into the existing repository.
2. Preserve the existing `governance/` folder.
3. Move old operational folders only when their contents have been mapped.
4. Initialize project metadata and ID counters.
5. Convert research questions into structured records.
6. Register existing sources and entities.
7. Generate human-readable views.
8. Update Hermes to use structured records as the factual source of truth.
9. Begin discovery.

## Failure Rule

When structured data and prose conflict:

- do not auto-correct silently,
- create an issue,
- identify the conflicting record,
- preserve both versions,
- require review when the conflict is material.

## Success Condition

The repository is data-first when:

- every source has a canonical source record,
- every material claim has a canonical claim record,
- entities are deduplicated,
- timelines are generated from event records,
- chapter evidence maps are generated from claim links,
- Hermes can resume work from repository state without relying on chat history.
