# Narrative_Discovery_Integration_Patch.md

**Version:** 1.0  
**Purpose:** Minimal repository changes required to activate the Narrative Discovery Record and Narrative Discovery Agent.

---

## 1. Artifact Registry Addition

Add this row to `Artifact_Registry.md`:

```markdown
| Narrative Discovery Record | Narrative Discovery | proposed→active→under_review→approved→locked |
```

The Narrative Discovery Agent is the sole owner. The Chapter Architect is the approver.

---

## 2. Repository Structure Addition

Add:

```text
book/
└── narrative_discovery/
```

Canonical filename:

```text
ndr-chapter-##-entrepreneur-slug.md
```

Required identifier:

```text
NDR-CH##-PER#####
```

---

## 3. Orchestrator Agent List Addition

Add:

```markdown
- Narrative Discovery Agent
```

The agent must be instantiated after sufficient research exists and before Chapter Brief approval.

---

## 4. Workflow Dependency Changes

Add these hard dependencies:

```yaml
chapter_brief_approved:
  requires:
    - narrative_discovery_record_approved

chapter_draft_started:
  requires:
    - narrative_discovery_record_approved
    - chapter_brief_approved

first_draft_approved:
  requires:
    - narrative_discovery_omission_audit_passed

final_chapter_approved:
  requires:
    - narrative_discovery_omission_audit_passed
    - fact_verification_passed
```

---

## 5. Approval Gate Changes

Do not add a new Project Owner approval gate.

The NDR is an internal quality gate:

```text
Narrative Discovery Agent creates
→ Chapter Architect approves
→ Orchestrator unlocks Chapter Brief approval
```

Escalate only disputed, sensitive, thesis-changing, or ethically consequential selections to the Project Owner.

---

## 6. Chapter Brief Requirement

Add a mandatory section to every Chapter Brief:

```markdown
## Narrative Discovery Requirements

- NDR ID:
- Astonishing fact:
- Required reveal window:
- Reader-retell sentence:
- Greatest risk:
- Defining decision:
- Human contradiction:
- Cedar Rapids consequence:
- Inheritance to next builder:
- Required secondary discoveries:
```

The brief may summarize the NDR but may not replace it.

---

## 7. Writer Input Contract

The Writer must load the approved NDR before drafting.

The Writer must explicitly report at completion:

```yaml
ndr_compliance:
  astonishing_fact_location:
  required_discoveries_present: true | false
  approved_exceptions: []
```

---

## 8. Editorial Review Addition

Every Developmental Editorial Review must include:

```markdown
## Narrative Discovery Audit

- Is the astonishing fact present?
- Is it revealed within the approved window?
- Is it prominent enough to be remembered?
- Is it accurately contextualized?
- Has editing weakened, buried, or sensationalized it?
- Are required secondary discoveries present?
- Does the chapter pass the reader-retell test?
```

---

## 9. QA Failure Conditions

Automatically fail a chapter when:

- the approved astonishing fact is absent;
- it appears outside the approved reveal window;
- it is vague when the evidence permits precision;
- its wording exceeds the evidence;
- a required discovery was removed without an approved exception;
- the omission audit is incomplete.

---

## 10. Existing Manuscript Backfill

Run the Narrative Discovery Agent across every existing chapter.

For each chapter:

1. Review all research and evidence.
2. Create an NDR.
3. Audit the current chapter.
4. Produce a bounded revision directive containing only identified omissions, buried discoveries, inaccuracies, and placement problems.
5. Do not automatically rewrite chapters.
6. Route revision directives to the existing Writer and Editor workflow.
7. Re-run fact verification and QA after changes.

This backfill is mandatory because the Sydney Rieckhoff omission proves the failure may exist elsewhere in the manuscript.

---

## 11. Activation Order

```text
1. Add Narrative_Discovery_Record.md to governance or schemas.
2. Add NARRATIVE_DISCOVERY_AGENT.md to agent specifications.
3. Update Artifact_Registry.md.
4. Add book/narrative_discovery/.
5. Update Orchestrator dependencies.
6. Add NDR fields to Chapter Brief and review templates.
7. Run manuscript-wide NDR backfill.
8. Revise only chapters with material findings.
9. Re-verify affected chapters.
```
