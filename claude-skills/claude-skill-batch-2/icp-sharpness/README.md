# icp-sharpness

Test how well you actually know your audience. Scores your Ideal Customer Profile across four dimensions, tells you where it's vague, rewrites it sharper, and — if you pass a URL — checks whether your website actually speaks to that audience.

**Modified by Growgami** — removed hardcoded Web3 default, added auto-detect industry context, and added website alignment evaluation mode.

---

## What it does

- Accepts either a written ICP description or a website URL
- Auto-detects the industry from your input (no manual setting required)
- Scores across 4 dimensions: WHO, WHEN, WHY, WHO NOT
- Returns a classification: Sharp / Partially Sharp / Vague / Fundamentally Unclear
- Rewrites your ICP sharper, including a ≤20-word succinct version
- If a URL is provided: fetches the page and checks whether the site actually reflects the ICP

---

## Installation

**Windows**
```bash
copy "icp-sharpness.md" "%USERPROFILE%\.claude\skills\icp-sharpness.md"
```

**macOS / Linux**
```bash
cp icp-sharpness.md ~/.claude/skills/icp-sharpness.md
```

Restart Claude Code after installing. The skill is then available globally across all Claude Code sessions.

---

## Usage

**Text input — evaluate a written ICP:**
```
/icp-sharpness We target fintech and neobank companies that need tech and marketing support
```

**URL input — evaluate a website's implied ICP:**
```
/icp-sharpness https://growgami.com
```

**Detailed input:**
```
/icp-sharpness Head of Marketing at a Series A neobank, 6–12 months post-launch, struggling to convert paid traffic because their landing pages don't match their product's actual audience — not for pre-launch teams or enterprise banks
```

---

## Scoring

| Dimension | What it checks |
|---|---|
| WHO | Is there a named person or role with agency? |
| WHEN | Is there a trigger or moment of urgency? |
| WHY | Is there a concrete pain — not just a benefit? |
| WHO NOT | Is there an exclusion? Who is this NOT for? |

| Score | Classification |
|---|---|
| 80–100 | Sharp |
| 40–79 | Partially Sharp |
| 15–39 | Vague |
| 0–14 | Fundamentally Unclear |

**Hard rule**: Cannot be Sharp without WHO NOT, regardless of score.

---

## Website Alignment (URL mode only)

When you pass a URL, Claude fetches the page and adds a **Website Alignment** section:

- Does the site name the right audience?
- Does it surface the pain point?
- Does it signal who it's NOT for?
- Verdict: does the site speak to the ICP or drift from it?

---

## Tips

- Run this before `lead-research-assistant` — a sharp ICP produces better leads
- Run it on competitor websites to find their positioning gaps
- The 20-word succinct version is useful for pitch decks, LinkedIn bios, and one-pagers
- If the site can't be fetched, paste the page content directly and it will analyze that instead
