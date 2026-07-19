# Built Here Version 1.5 Release Report

**Release date:** July 19, 2026  
**Release:** Built Here Version 1.5 — constitutional narrative rewrite  
**Primary manuscript:** `manuscript/final/Built_Here_Manuscript_V1.5.md`

## Release Summary

Version 1.5 is a complete beginning-to-end rewrite of the 35-chapter Version 1 assembled manuscript. It preserves the available historical record while replacing the prior civic-history and evidence-ledger structure with entrepreneur-centered narrative nonfiction.

The manuscript contains 35 chapters and 54,443 words including front matter. The chapter text contains 54,202 words. Version 1 contained 115,839 words; Version 1.5 removes 61,396 words, a 53.0 percent reduction. The reduction is deliberate: repeated context, source-trace appendices, timeline exposition, process language, academic caveats, and accuracy-only paragraphs were cut rather than carried forward.

## Repository Audit and Changes

The startup audit examined the active writing prompts, editorial prompts, agent specifications, workflow guidance, governance hierarchy, data-first architecture, and chapter validation contracts. Instructions that treated chronology, institutions, the city, or historical exposition as the narrative center were revised.

Changes include:

- Established `The_Promise_of_Built_Here.md`, `Writing_Constitution_v2.md`, `Chapter_Contract_v2.md`, and `Narrative_Test.md` as the highest editorial authority.
- Revised the book charter, editorial vision, first principles, development workflow, and Hermes orchestrator guidance so the book—not the repository—is the controlling objective.
- Clarified that research timelines are factual infrastructure and may never become a chapter outline or narrative spine.
- Preserved completed Version 1 artifacts as immutable history while authorizing aggressive new versioned drafts.
- Kept structured records and prior research as the factual boundary for the rewrite.

No Version 1 chapter or release artifact was overwritten.

## Prompt Changes

The runtime Writer and Editor prompts now load the four constitutional documents before worker identity, operating rules, job packets, and output contracts.

Writer instructions now require:

- one entrepreneur as protagonist;
- an immediate documented business problem, risk, decision, or opportunity;
- business as plot;
- conflict, stakes, pivotal decision, consequence, legacy, emotional movement, takeaway, and chapter bridge;
- elimination of timeline structure, civic exposition, encyclopedia prose, academic overqualification, and inert factual passages.

Editor instructions now authorize aggressive structural revision while preserving established facts. They explicitly reject chapters centered on a city, institution, company, or timeline and require every edited chapter to satisfy the constitutional narrative contract.

## Agent Changes

Updated agent specifications include:

- Hermes Orchestrator
- Chapter Architect
- Chapter Writer
- Developmental Editor
- Continuity Editor
- Timeline Researcher

The Orchestrator is now accountable for the finished book rather than acting only as project manager. The Chapter Architect and Writer must build stories around entrepreneurs and decisions. Developmental and continuity review now test entrepreneurial prominence, emotional movement, chapter bridges, whole-book momentum, and opening-to-ending payoff. The Timeline Researcher is explicitly barred from prescribing chronological manuscript structure.

## Architectural Changes

Version 1.5 introduces a separate versioned manuscript path:

- Chapter drafts: `manuscript/drafts/v1.5/Chapters/`
- Assembled manuscript: `manuscript/final/Built_Here_Manuscript_V1.5.md`

The production architecture remains evidence-first, but evidence no longer dictates an evidence-ledger reading experience. Structured records and prior research constrain factual claims; narrative architecture determines how supported material reaches the reader.

The final manuscript was assembled reproducibly from 35 numbered chapter files. Each chapter file has one H1, is nonempty, and contains no source-trace appendix, inline numeric citation marker, TODO, TBD, or placeholder. No duplicate full paragraphs were detected across chapters.

## Manuscript Changes

Version 1.5 changes the center of gravity from Cedar Rapids history to the people who made consequential choices there.

Major changes include:

- New person-led openings throughout the book.
- One named builder carrying each chapter's narrative.
- Business problems and decisions replacing dates as the structural engine.
- Stronger attention to risk, uncertainty, failure, capital, operations, markets, labor, scale, and reinvention.
- Cedar Rapids revealed through what each builder needed from the city and what each left behind.
- Explicit handoffs between chapters to create one cumulative book rather than 35 isolated essays.
- A rewritten opening centered on Nicholas B. Brown while preserving the contested Indigenous and political history of the land on which his opportunity depended.
- A rewritten conclusion centered on Sydney Rieckhoff's move from a NewBo booth to a storefront, completing the book's argument that builders leave usable capabilities for the builders who follow.

## Verification

The assembled manuscript passed the following deterministic checks:

- 35 of 35 chapter files present and nonempty.
- 35 chapter H1 headings in the assembled manuscript.
- Exactly one H1 in every source chapter file.
- No source-trace sections or inline numeric citation markers.
- No TODO, TBD, or placeholder markers.
- No duplicate full paragraphs across chapters.
- Final manuscript SHA-256: `81a2d5a58620541b6ea9cd19b6eca33ea925fc6d8141b43a608d071b4585a04d`.

Repository runtime validation reported:

- `STRUCTURE VALID`
- `EXECUTION READY`

## Remaining Weaknesses

Version 1.5 is a narrative rewrite, not a fresh primary-source research campaign or publication certification pass.

The surviving record is uneven. Several chapters have rich company evidence but thin personal evidence, limiting scene reconstruction and interior emotional detail. A few protagonists are best understood as creative, institutional, labor, or corporate builders rather than conventional company founders. That choice preserves the existing 35-chapter arc without inventing founder stories the evidence cannot support.

The rewrite changes factual phrasing and emphasis across every chapter. The prior Version 1 citation status therefore cannot certify Version 1.5 sentence by sentence. All 35 chapters require a fresh claim map and citation review before publication.

At 54,443 words, Version 1.5 is substantially leaner than the Version 1 assembled manuscript. Expansion should occur only where new evidence supports richer human scenes, decisions, setbacks, relationships, and consequences—not to restore removed exposition.

## Recommendations Before Version 2.0

1. Build a fresh claim map for every Version 1.5 chapter and run claim-level citation review against the actual rewritten prose.
2. Conduct targeted primary-source research for the personal stakes and business decisions of thinly documented protagonists.
3. Resolve whether creative, labor, institutional, and corporate builders remain within the final editorial definition of entrepreneur.
4. Interview living entrepreneurs and knowledgeable participants where permission and verification allow.
5. Run an independent historical-integrity, legal-sensitivity, and reputational-risk review.
6. Perform a full-book line edit after evidence revisions, preserving the new person-led structure and momentum.
7. Build the normalized bibliography, notes apparatus, acknowledgements, AI disclosure, index inputs, and publication design.
8. Obtain final human approval only after the publication candidate's hash, citations, and supporting apparatus are complete.

## Release Assessment

Built Here Version 1.5 fulfills the constitutional rewrite mission as a complete narrative manuscript. It is materially more human, entrepreneurial, selective, and forward-moving than Version 1. It should be treated as the narrative foundation for Version 2.0—not yet as a citation-certified or publication-approved edition.
