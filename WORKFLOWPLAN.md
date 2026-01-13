# Workflow plan for The Great Decoupling

Here is a concrete blueprint for building the "3 depths" site (visual, semantic, analytic) using your toolchain, anchored to the Great Decoupling structure and vibe you already have.

---

A. The product architecture

Depth 1: Visual (Infographic)

Purpose: grab attention, show the fracture clearly, minimal text.
Rules:
- Every number shown has a clickable source note.
- No causal claims in the visuals unless they are phrased as "associated with" or "coincided with."

Depth 2: Semantic (Narrative essay)

Purpose: the human story, Acts, psychological toll, meaning.
Rules:
- Interpretations must be labeled as interpretation.
- Every strong claim links to a "proof panel" in Depth 3.

Depth 3: Analytic (Technical brief)

Purpose: credibility armor. Definitions, methods, sources, caveats, alternative explanations.
Rules:
- Tables, footnotes, definitions, measurement choices, sensitivity checks.
- Explicit section titled "What this does NOT claim."

---

B. The workflow you described, made robust

1) Deep research → Brief (NotebookLM + validation pass)

Goal: create the “source of truth” dataset and claims ledger.

Deliverables from this step:
- Claim ledger (see below)
- Source pack (PDFs, links, screenshots)
- Methods notes (definitions of productivity, compensation, inflation index, time windows, etc.)

Then ChatGPT's job is not "write it," but:
- check internal consistency
- detect overclaims
- enforce wording discipline
- generate attack simulations (what critics will say)

2) Narrative essay (Claude)

Claude is great at voice and cohesion.
But Claude must write against a fixed constraint:
- It may only use claims that exist in the claim ledger
- Every paragraph should map to at least one ledger claim ID
- High heat phrases ("stolen," "weaponized," "designed") must be marked as interpretation, not measurement

3) Infographic (NotebookLM or build directly)

NotebookLM can help storyboard, but the final infographic should pull numbers directly from the claim ledger so the visual never drifts.

---

C. The key system that makes it airtight: a Claim Ledger

This is the spine. Without it, your narrative and visuals will diverge and critics will find the weak seams.

Recommended fields (minimum):
- Claim ID (ex: A1, B3, C7)
- Claim text (one sentence)
- Claim type (descriptive, causal, interpretive)
- Geography (US, OECD, etc.)
- Time window (1948–1973, 1973–2023, etc.)
- Metric definition (exact)
- Source(s) (primary)
- Confidence level (High, Medium, Low)
- Attack surface notes (what critics will challenge)
- Approved phrasing (the exact safe wording you will reuse)

Everything in the narrative and infographic must point back to Claim IDs.

---

D. Website UX: "3 depths" without feeling like 3 separate products

Keep the Great Decoupling scroll as the default experience. Then add a Depth toggle:
- Visual: charts, minimal prose
- Essay: the story fills in
- Brief: opens a side panel or separate route with citations, definitions, and tables

Implementation pattern that preserves your vibe:
- Main scroll remains identical
- The toggle changes what "expands" under each section
- Each chart and number has a "Source" button that opens a citation card

---

E. Quality control gates (what prevents credibility collapse)

Gate 1: Data integrity
- Numbers match sources
- Time windows match across all three layers
- Inflation adjustment method is consistent and named

Gate 2: Claim discipline
- Descriptive claims are not written as causal
- Interpretive claims are explicitly labeled
- No "this proves" language unless you truly have causal identification

Gate 3: Critic simulation

Before publish, run:
- "Economist skeptic"
- "Policy wonk"
- "Labor historian"
- "Left critic" and "right critic"

Your goal is not to satisfy them, it is to ensure they cannot win with cheap shots.