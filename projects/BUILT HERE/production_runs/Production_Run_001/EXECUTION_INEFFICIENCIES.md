# Production Run 001 — Execution Inefficiency Log

**Purpose:** Record execution inefficiencies observed during the baseline implementation of Publishing Operating System v2.0.

**Control:** Observations are recorded during production but are not remediated in this run. Runtime redesign and Publishing Operating System changes are out of scope. Recommendations will be consolidated only after Production Run 001 completes.

## EI-001 — Runtime stage-model mismatch

- **Observed:** The executable runtime models Specification, Research, Draft, Citation/Interpretation, Editing, and Assembly, while the frozen POS requires Character Brief, Narrative Discovery Record, Chapter Intent, Narrative Enrichment, Reader Review, and Editorial Approval as distinct stages.
- **Production effect:** Run-specific stages require manual artifact orchestration and tracker updates outside the executable runtime state machine.
- **Disposition:** Record only; do not redesign during production.

## EI-002 — Global drafting-gate ambiguity

- **Observed:** A production instruction to complete all upstream coverage before drafting was interpreted as a manuscript-wide hard gate, although the POS and executable runtime support per-chapter progression after book-level architecture approval.
- **Production effect:** Draft-ready chapters were temporarily blocked by unrelated late-chapter evidence gaps.
- **Disposition:** Resume controlled streaming under the validated architecture; defer engine-policy recommendations to the final report.

## EI-003 — Narrative dependencies are not execution dependencies

- **Observed:** `Book_Backlog.yaml` records sequential narrative dependencies, but the executable scheduler checks only hard dependencies.
- **Production effect:** Continuity readiness must be coordinated manually during drafting packets.
- **Disposition:** Record only; do not modify scheduler behavior during production.

## EI-004 — Research-provider failure and fallback overhead

- **Observed:** The configured web-search/extraction provider repeatedly returned HTTP 432 or no useful entity matches. Workers used direct browser inspection, official pages, Internet Archive and Google Books OCR, publisher APIs, and RSS discovery instead.
- **Production effect:** Research packets consumed more calls and some workers reached iteration ceilings before writing artifacts.
- **Disposition:** Continue evidence-safe fallbacks; do not redesign tool configuration during production.

## EI-005 — Oversized research packets

- **Observed:** A five-chapter Research packet exhausted its iteration budget after discovery but before artifact creation.
- **Production effect:** Chapters 23–27 required a second, narrowly scoped write-and-validate dispatch.
- **Disposition:** Continue bounded packets without changing the runtime; retain this observation for the final report.

## EI-006 — Flat artifact naming complicates immutable revisions

- **Observed:** Run-specific Character Briefs use unversioned filenames. George Greene’s completed brief was scoped to Chapter 2 and explicitly excluded the later railroad decision, while the validated architecture also assigns Greene to Chapter 5.
- **Production effect:** The existing immutable brief cannot be overwritten and requires a separately versioned successor for complete entrepreneur coverage.
- **Disposition:** Preserve the original and create a run-specific successor artifact; defer naming/version-policy optimization.

## EI-007 — Runtime state and run-specific tracker are separate authorities

- **Observed:** The executable runtime state reports the prior 35-chapter manuscript assembled and complete, while Production Run 001 is tracked separately in `production_runs/Production_Run_001/PROGRESS.md`.
- **Production effect:** Current execution eligibility and completion must be reconstructed manually from run-specific artifacts rather than the runtime state.
- **Disposition:** Record only; do not reconcile or redesign runtime state during production.

## EI-008 — Requested filename propagated an unverified protagonist name

- **Observed:** A Character Brief packet requested `john-r-witwer.md`, while the frozen architecture and controlling Chapter 14 Research identify the protagonist as Weaver Witwer and do not establish that John R. Witwer is the same person.
- **Production effect:** The generated brief preserved a warning but still used an unsupported filename and heading, requiring rejection and a separately preserved corrected artifact.
- **Disposition:** Preserve the rejected file, create `weaver-witwer.md` from the controlling Research record, and defer identity-validation and packet-generation improvements to the final report.

## EI-009 — Worker input discovery can miss valid differently named artifacts

- **Observed:** The Chapter 18 NDR worker reported that no standalone George T. Ronk Character Brief existed even though the accepted artifact was present as `character_briefs/george-ronk.md`.
- **Production effect:** The NDR was grounded in the same controlling Research and architecture and later verified against the existing brief, but the worker's preflight summary overstated an input gap.
- **Disposition:** Accept the verified NDR; defer artifact-manifest and identity-resolution improvements to the final report.

## EI-010 — Untracked production tree limits Git-based mutation verification

- **Observed:** The enclosing `production_runs/` tree is untracked, so normal Git diff and target-scoped status cannot distinguish individual newly created run artifacts from earlier run files or prove protected-file immutability.
- **Production effect:** Workers and the orchestrator must rely on explicit target inventories, content validation, and SHA-256 baselines instead of ordinary tracked diffs.
- **Disposition:** Continue target-scoped verification during the baseline run; defer repository-tracking recommendations until the Execution Lessons Learned report.

## EI-011 — Evidence resolution lacks a first-class nonblocking queue

- **Observed:** Research failures were represented only as chapter-stage `Blocked` statuses, which made isolated evidence gaps appear equivalent to manuscript-wide execution blockers.
- **Production effect:** The Project Owner had to designate an explicit Evidence Resolution Queue and clarify that ready drafting and review lanes must continue.
- **Disposition:** Maintain `EVIDENCE_QUEUE.md` manually for this run; do not redesign runtime states or scheduling during production.

## EI-012 — Canonical-root-relative and run-root-relative paths can diverge

- **Observed:** A qualified NDR packet named `narrative_discovery/...` outputs while describing the project root as canonical. Workers created ten files at the project-level directory rather than the active Production Run 001 directory used by prior run artifacts.
- **Production effect:** Outputs required target reconciliation into `production_runs/Production_Run_001/narrative_discovery/` before validation and downstream use.
- **Disposition:** Reconcile the ten artifacts without changing their contents; defer explicit run-root manifest and packet-path validation recommendations to the final report.
