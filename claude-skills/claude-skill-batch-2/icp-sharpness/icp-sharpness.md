# ICP Sharpness Test

## Description
Tests how well YOU know your own audience. Evaluates an Ideal Customer Profile across four dimensions (WHO, WHEN, WHY, WHO NOT), scores it, and returns a structured report with a sharpened version and concrete actions. Can evaluate either a written ICP or a live website URL.

**TRIGGER when**: the user invokes `/icp-sharpness` followed by their ICP text or a URL.

---

## Instructions

### Step 1: Parse the Input

The user's input (everything after `/icp-sharpness`) is either:
- **A URL** — if it starts with `http://`, `https://`, or `www.`
- **ICP text** — everything else

### Step 2: Handle URL Input (if applicable)

If the input is a URL:
1. Use the **WebFetch** tool to retrieve the page content
2. From the fetched content, extract: page title, tagline, headings, product descriptions, value propositions, and any explicit audience mentions
3. Treat the extracted content as the source for ICP analysis — evaluate the *implied* ICP from the company's website positioning
4. Also evaluate: **does the website actually speak to this ICP?** (see Step 6 — Website Alignment section)
5. If WebFetch fails, respond: "I couldn't fetch that URL. Please paste the relevant page content directly and I'll analyze it."

### Step 3: Auto-Detect Industry Context

Do NOT default to any industry. Infer from the input:

- Look for: product category, audience language, use cases, pricing signals, technical terminology
- Common signals:
  - "series A", "SaaS", "MRR", "churn" → B2B SaaS
  - "wallet", "chain", "protocol", "DAO" → Web3/crypto
  - "patients", "HIPAA", "EHR" → Healthcare
  - "merchants", "checkout", "GMV" → E-commerce/fintech
  - "engineers", "PRs", "deploy", "CI" → Developer tooling

State the detected industry before scoring: "Detected context: **B2B SaaS / developer tooling**"

If industry is ambiguous, state the assumption and ask for confirmation.

### Step 4: Apply the Evaluation Framework

Evaluate the ICP across four dimensions:

#### WHO (buyer or primary user)
Does the ICP name a real person or user type with agency?
- **Strong** B2B: "Head of Engineering", "Founder at a Series A infra startup", "Head of Compliance at a licensed exchange"
- **Strong** B2C: "Retail traders on centralized exchanges", "Non-technical users holding stablecoins"
- **Weak**: "Teams", "companies", "Users" (without context), "businesses"
- **Missing**: No person or role referenced at all

#### WHEN (trigger or situation)
Is there a moment when the product becomes urgent?
- **Strong**: "when moving from testnet to mainnet", "after raising a Series A", "when failed transactions cause churn", "when compliance blocks expansion"
- **Weak**: "who want to grow", "who want better UX", "looking to scale"
- **Missing**: No trigger or situational context

#### WHY (acute pain)
Does it name a concrete problem — not a benefit?
- **Strong**: "failed transactions causing loss of trust", "compliance blocking expansion", "engineers spending 40% of time on manual work"
- **Weak**: "inefficiency", "innovation", "scalability", "they want growth"
- **Missing**: No pain mentioned, only benefits or features described

#### WHO NOT (exclusions)
Does it clearly or implicitly say who this is NOT for?
- **Strong**: "not pre-product teams", "not professional traders", "not companies without a legal entity"
- **Weak**: "anyone can use it", no exclusions mentioned, audience is too broad
- **Missing**: Zero exclusion signals

#### Anti-Signals (apply automatic downgrade)

Downgrade the score sharply if the ICP includes:
- Category-first language ("tech companies", "businesses that need X")
- Feature-led descriptions instead of user-led ("a platform that does X")
- Multiple unrelated audiences mashed together
- Buzzword-dense vision statements ("disrupting", "revolutionizing", "next-gen")
- No implied buyer, user, or urgency whatsoever

### Step 5: Score and Classify

Calculate `overall_score` (0–100):
- Each dimension scored "**strong**" = **25 points**
- Each dimension scored "**weak**" = **10 points**
- Each dimension scored "**missing**" = **0 points**

Apply anti-signal penalties as judgment calls (–5 to –20 pts per signal).

Classify based on total score:
| Score | Classification |
|-------|---------------|
| 80–100 | **Sharp** |
| 40–79 | **Partially Sharp** |
| 15–39 | **Vague** |
| 0–14 | **Fundamentally Unclear** |

> **Hard rule**: An ICP **cannot** be classified as "Sharp" unless it includes WHO NOT (explicit or very strong implicit exclusions). Downgrade to "Partially Sharp" if WHO NOT is weak or missing, regardless of score.

### Step 6: Output the Report

```
## ICP Sharpness Report

**Classification**: [Sharp / Partially Sharp / Vague / Fundamentally Unclear]
**Overall Score**: XX/100
**Detected Industry**: [Industry context]

**Summary**: [2–3 sentence executive summary. Be specific about what makes it work or not work. Reference their actual ICP language.]

---

### Dimension Analysis

| Dimension | Score   | Found                              | Recommendation                        |
|-----------|---------|------------------------------------|---------------------------------------|
| WHO       | [Strong / Weak / Missing] | [Quote or describe what was found] | [Specific suggestion] |
| WHEN      | [Strong / Weak / Missing] | [Quote or describe what was found] | [Specific suggestion] |
| WHY       | [Strong / Weak / Missing] | [Quote or describe what was found] | [Specific suggestion] |
| WHO NOT   | [Strong / Weak / Missing] | [Quote or describe what was found] | [Specific suggestion] |

---

### Key Observations
- [First specific observation — tied to their exact language]
- [Second observation]
- [Third observation]

### Action Items
1. [First concrete action — specific, not generic]
2. [Second action]
3. [Third action]

---

### Sharpened ICP Example
> [A rewritten 2–3 sentence ICP that improves on the user's input. Add the missing dimensions, especially WHO NOT. Use their actual product context.]

### Succinct ICP (≤20 words)
> [Single punchy sentence: WHO + WHEN + WHY. Example: "Series A SaaS CTOs replacing legacy billing before their next enterprise deal."]

---

[ONLY INCLUDE THIS SECTION IF INPUT WAS A URL]
### Website Alignment

**Does your website reflect this ICP?**

| Signal | Found on site | Assessment |
|---|---|---|
| WHO is addressed | [Yes/No — quote] | [Clear / Implied / Missing] |
| Pain point named | [Yes/No — quote] | [Clear / Implied / Missing] |
| WHO NOT excluded | [Yes/No — quote] | [Clear / Implied / Missing] |

**Verdict**: [1–2 sentences on whether the site speaks to the ICP or drifts from it. Name the specific lines that help or hurt.]
```

---

## Tone

Be senior, observant, and direct. This is a test of how well the user knows their own audience — not a cheerleading exercise. If the ICP is weak, say so clearly and explain exactly why. Tie every observation and recommendation to what was actually provided.

Frame the output as: "Here's how clearly you know who you're building for."
