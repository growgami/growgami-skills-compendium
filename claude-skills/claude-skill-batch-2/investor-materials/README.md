# investor-materials

Build pitch decks, one-pagers, and financial models that are consistent, credible, and tailored to the specific type of investor you're pitching. Everything stays in sync — no contradictions between your deck, model, and applications.

**Original author**: ECC
**Modified by Growgami** — added investor type selector, why-now narrative development flow, pre-revenue handling, and actionable frontend-design handoff.

---

## What it does

- Asks upfront: own company or client? And what type of investor?
- Adjusts tone, depth, and emphasis based on investor type (Angel / VC / Accelerator / Strategic)
- Forces a "why-now" narrative sentence before touching any numbers
- Handles pre-revenue companies — replaces traction slides with pipeline signals and milestone projections
- Keeps all documents consistent with a single source of truth
- Can hand off to the `frontend-design` skill to build a web-native deck

---

## Installation

**Windows**
```bash
copy "investor-materials\SKILL.md" "%USERPROFILE%\.claude\skills\investor-materials.md"
```

**macOS / Linux**
```bash
cp investor-materials/SKILL.md ~/.claude/skills/investor-materials.md
```

Restart Claude Code after installing.

---

## Usage

```
/investor-materials Build a pitch deck for angels. We're a B2B SaaS for fintech compliance teams.
```

```
/investor-materials My client needs a one-pager for their Series A. Here are their metrics: [paste metrics]
```

```
/investor-materials Create a financial model for a pre-revenue SaaS targeting neobanks.
```

```
/investor-materials Fill out this YC application question: "What are you building and why now?"
```

---

## Asset types supported

| Asset | Best for |
|---|---|
| Pitch deck | Angels, VCs, first meetings |
| One-pager / memo | Warm intros, follow-ups |
| Financial model | Due diligence, internal planning |
| Accelerator application | YC, Techstars, specific questions |

---

## Investor type guide

| Type | What Claude leads with |
|---|---|
| Angel | Story, team, why-now |
| VC | Metrics, market size, model |
| Accelerator | Exact answer to the question asked |
| Strategic | Synergy and partnership value |

---

## Tips

- Have your traction metrics, raise size, and use-of-funds ready before starting
- If you don't have a why-now sentence yet, Claude will help you build one
- Pre-revenue? Claude will substitute projections and pipeline for actuals
- Want a visual deck? Claude will hand off to `frontend-design` once the outline is approved
