# Evidence Expansion Applied — Chapters 8 and 10 — Pass 001

## Scope and result

This application pass implements exactly the ten `REWRITE` decisions in `evidence_expansion/chapters-01-12-pass-001.md` that apply to Chapters 8 and 10. It creates immutable successors only. It does not edit the queue, architecture, progress records, predecessor artifacts, or any other chapter.

Chapter 8 incorporates only what the inspected November 3, 1897 *Pokrok západu* publication establishes: Josef Žbánek, Alois Bláha, and Hynek Breuer are the three named signatories/incorporators; the president, secretary, and treasurer constitute the executive committee; Bláha is the initial secretary; and the principal office is in Cedar Rapids. Every successor preserves Žbánek/Breuer co-agency and withholds sole founding, individual reserve or claim authority, personal guarantee, accepted downside, and attributable consequence.

Chapter 10 changes one reader-facing sentence only: the terminal `EIQ-10-C15` inheritance. The successor removes the implication that the source or legal control of project funds is proved. All other Chapter 10 manuscript prose is byte-identical to `drafts/chapter-10-fortunes-obligations-v002.md`.

## Exact REWRITE-ID disposition

| Rewrite ID | Disposition | Applied bounded change | Residual boundary retained |
|---|---|---|---|
| `EIQ-08-C01` | **APPLIED** | Opening truth now begins with the 1897 three-signatory incorporation record and Bláha's initial secretary office, then carries the 1899 and 1917 anchors. | No uninterrupted tenure, sole control, specific financial decision, or consequence. |
| `EIQ-08-C03` | **APPLIED** | Institutional mechanism now states the Cedar Rapids principal office, three-officer executive committee, and initial secretary role. | Structure does not prove Bláha's sole control. |
| `EIQ-08-C04` | **APPLIED** | Authority boundary now identifies Bláha as one of three incorporator-signatories and initial secretary. | No sole founding, rule authorship, benefit design, reserve control, individual claim approval, guarantee, or location-selection authority. |
| `EIQ-08-C08` | **APPLIED** | Personal-risk boundary now acknowledges Bláha's executive-committee office. | No officer bond, compensation, personal liability, control of particular funds, or specific reserve or claim decision. |
| `EIQ-08-C10` | **APPLIED** | Title-to-authority boundary now links the 1917 title to the 1897 secretary office and executive structure. | Later discretion, tenure, signature practice, and legal or personal consequence remain unresolved. |
| `EIQ-08-C11` | **APPLIED** | Cedar Rapids section now states that the 1897 articles place the principal office there. | The source does not establish who selected Cedar Rapids or why. |
| `EIQ-08-C12` | **APPLIED** | Continuity synthesis now includes the 1897 incorporation structure alongside the 1899, 1908, and 1917 anchors. | No uninterrupted tenure, particular reserve or claim decision, personal exposure, or Bláha-caused outcome. |
| `EIQ-08-C13` | **APPLIED** | Late authority boundary now recognizes co-incorporator and initial-secretary status. | No recovered Bláha-specific reserve, claim, building-finance, personal-guarantee, or consequence record. |
| `EIQ-08-C14` | **APPLIED** | Exact Chapter 8 outgoing condition now carries the 1897 incorporation structure and initial secretary role. | Specific person-level financial control and consequence remain unresolved. |
| `EIQ-10-C15` | **APPLIED** | Exact terminal inheritance now names Caroline's documented purchase, commissioning, architect replacement, oversight, occupancy, and completed residence. | Source and legal control of project funds and personal downside remain unresolved. |

**Disposition arithmetic:** 10 expected; 10 applied; 0 deferred; 0 omitted; 0 extra claims authorized.

## Exact transitions and EIQ linkage

- Chapter 8 incoming condition remains exactly: **a neighborhood with recurring household commerce and obligations but without a person-level claim about who created or controlled a durable mechanism for pooling death, credit, or institutional risk**.
- Chapter 8 outgoing condition is synchronized byte-for-byte across the Research successor, Character Brief successor, NDR successor, Intent successor, evidence-improved draft, and claim-map entry: **documented collective mutual-aid capacity grounded in the 1897 incorporation structure, Bláha’s initial secretary role, later convention participation, national office, and institutional administration, while specific person-level financial control and consequence remain unresolved**.
- `EIQ-08-01` remains the nonblocking umbrella marker in the Chapter 8 Research, Character Brief, NDR, Intent, and all fourteen claim-map entries.
- Chapter 10 incoming condition and all prose before the final inherited condition remain unchanged.
- Chapter 10 outgoing condition is: **a substantial residence completed through Caroline Sinclair’s documented purchase, commissioning, architect replacement, oversight, and occupancy, while the source and legal control of the project funds and any personal downside remain unresolved**.
- `EIQ-10-01` remains the umbrella marker in every Chapter 10 map entry, and the terminal sentence remains linked to hidden marker `EIQ-10-C15`.

## Source identity and SHA-256 hashes

### Newly inspected 1897 primary source payloads

| Source payload | Retrieval identity | Bytes | SHA-256 |
|---|---|---:|---|
| LOC item API JSON | `https://www.loc.gov/resource/sn83045348/1897-11-03/ed-1/?sp=10&fo=json` | 50,131 | `1970911b4e24cc22ee9de435f47dd260d8a9a7ba7a4955ccfaeb9c60ad1086ee` |
| LOC full-text service response | segment `/service/ndnp/nbu/batch_nbu_froelichiafloridana_ver01/data/sn83045348/00279527173/1897110301/0908.xml`, `format=alto_xml&full_text=1` | 24,367 | `3e21bddc9005ab03d7d6c9cbec60496e651a2c9856d410e11af03c4b2d2976bf` |
| LOC IIIF page-image JPEG inspected at `pct:6.25` | image service path ending `1897110301:0899/full/pct:6.25/0/default.jpg` | 29,945 | `d0792dfe6a66ad4576915f443ae9d7d66743cd8e33ec827fdf26f3fa2f366926` |

The API identifies page/image 10 and the full-text segment used in the evidence-expansion report. The text-service response and IIIF image are official LOC derivatives. The listed hashes are of the retrieved payload bytes used for this application verification; they are not hashes of an underlying Iowa Secretary of State filing, which was not inspected.

### Controlling application source

| Path | SHA-256 |
|---|---|
| `evidence_expansion/chapters-01-12-pass-001.md` | `a5c640712440e71c81b3f63dfcfa09d4d0cc451584f310eb6c4f5dec715e2ec4` |

### Preserved predecessor inputs

| Path | SHA-256 |
|---|---|
| `research/chapter-08-alois-blaha-v002.md` | `784d0431ab9293491f61e3dd3db8e0c90909b41d6a45df1387414540149cedc9` |
| `character_briefs/alois-blaha.md` | `439e5c71071913dd669725f87b42fb6e525da8bfc2a92c7df59c8176f3a5d7f1` |
| `narrative_discovery/ndr-chapter-08-alois-blaha.md` | `e2d2ff5331a223525c48aa609023d4edbea21fac54494c82d39a4f9c04d87df2` |
| `chapter_intents/chapter-08-alois-blaha.md` | `de5d5722ddba790dd3036fb1f79b9aa1304b0fb5d7d29e27ac6ae195edb20419` |
| `drafts/chapter-08-mutual-aid-credit-trust-v002.md` | `da1bf3a9d8e282bd8c7d1b10e551bb3d48030779faf747d4bcee6db94ca64be3` |
| `claim_maps/chapter-08-v002.md` | `af4dff124fb9db825e09ee01b3f48375083a220502414d9351fa63e0c1e0b7f1` |
| `research/chapter-10-caroline-sinclair-v003.md` | `c57ca80605cb50677ed272722161f3abc216bfa177b7dc1b84f82347f149c634` |
| `chapter_intents/chapter-10-caroline-sinclair-v002.md` | `22d27be89a52a1ef4ed778ca88a7fe795f4b7c96f6db3b184eafc898602fc534` |
| `drafts/chapter-10-fortunes-obligations-v002.md` | `f816d3b728d5c10d041a5d985ee1e289306377fce8707317a2059b4e33154a70` |
| `claim_maps/chapter-10-v002.md` | `c229f05a67a2c4a1147a8518f3ec7b2e5baa56859c62bde1eebfd8523670ff7a` |

### Created successor artifact hashes

| Path | SHA-256 |
|---|---|
| `research/chapter-08-alois-blaha-v003.md` | `6c282f43c0f1f101a2429862cdac48b4c23ed5dd0f599e1904beb540501a7ada` |
| `character_briefs/alois-blaha-v002.md` | `60b85757de6847d423eb19cf9e7eb4b02ed7bf75a0e5f13ffe641e2562267c69` |
| `narrative_discovery/ndr-chapter-08-alois-blaha-v002.md` | `d3b6a89a195186a1c699449224ef33b2199dd1c96dc61033ccde5074e9366958` |
| `chapter_intents/chapter-08-alois-blaha-v002.md` | `4a57f1202f59843db95787f1aa7e7d883f7fd1aa6ffd7a4faa08e7b7fa34d812` |
| `evidence_improved/chapter-08-mutual-aid-credit-trust-v001.md` | `726c33a97da6fd9ff7a3ec7576ec9336c82a3f69e8401b752750720e46e1cf4f` |
| `evidence_improved_claim_maps/chapter-08-v001.md` | `d78c61ab30a42f22d20426f19035ee73f919961c5779b688e608d3a43d2359e0` |
| `evidence_improved/chapter-10-fortunes-obligations-v001.md` | `6a6f3ef3b5ab3a7fd1281531591b4f6faa84f5acf1ee2486fbb7930018910d24` |
| `evidence_improved_claim_maps/chapter-10-v001.md` | `472d82fff857054f0dbfa97fdb022ee066df849bd5bf0d01afd398a4a17b2560` |

## Validation result

- Exact authorized output set exists and every file is nonempty.
- Chapter 8 draft/map parity: 14 unique hidden markers and 14 map entries, in exact order.
- Chapter 10 draft/map parity: 15 unique hidden markers and 15 map entries, in exact order.
- Chapter 8 opening One Truth appears byte-for-byte in the evidence-improved draft and within its first ten percent.
- Chapter 8 and Chapter 10 exact outgoing sentences are the final nonblank manuscript lines, immediately preceded by their respective hidden markers.
- Chapter 8 incoming condition is unchanged and the outgoing successor condition is synchronized across the full successor chain.
- Chapter 10 manuscript diff against its predecessor contains exactly one changed reader-facing line.
- Every map entry retains its chapter umbrella EIQ linkage.
- No placeholders, trailing whitespace, malformed UTF-8, or newline defects were found; every output ends with exactly one newline.
- Publication prose preserves co-agency and does not introduce sole founding, individual reserve or claim authority, personal guarantee, accepted downside, consequence, or proven source/legal control of funds.

This application does not claim that historical research is complete.
