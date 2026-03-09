# lead-research-assistant

Find real companies that match your ideal customer using live web search — not training data guesses. Scores each lead by fit, marks confidence level, and ends with a CRM-ready CSV.

**Modified by Growgami** — added live WebSearch requirement, mode selector (own business vs client), confidence labeling, and CRM CSV export.

---

## What it does

- Asks upfront: is this for your own business or a client?
- Searches the web in real time to find matching companies (verified, not hallucinated)
- Scores each lead 1–10 by fit with explanation
- Labels each result as ✅ Verified or ⚠️ Inferred so you know what to double-check
- Ends with a CSV block ready to import into HubSpot, Notion, or any CRM

---

## Installation

**Windows**
```bash
copy "SKILL.md" "%USERPROFILE%\.claude\skills\lead-research-assistant.md"
```

**macOS / Linux**
```bash
cp SKILL.md ~/.claude/skills/lead-research-assistant.md
```

Restart Claude Code after installing.

---

## Usage

```
/lead-research-assistant Find 10 fintech companies in the UK that would benefit from a tech and marketing agency
```

```
/lead-research-assistant My client builds a code review automation tool for engineering teams. Find 15 leads.
```

```
/lead-research-assistant [run from your product's codebase directory]
Look at what I'm building and find 10 companies that would be a good fit.
```

---

## Output format

Each lead includes: company name, website, fit score, target decision-maker role, LinkedIn (if found), value proposition, and conversation starters.

At the end, Claude offers to format everything as a CSV:
```
Company, Website, Fit Score, Target Role, LinkedIn, Value Prop, Conversation Starters, Confidence
```

---

## Tips

- Run from your codebase directory for automatic product context
- Specify location, industry, or company size to narrow results
- Ask for follow-up research on your top 3 leads for deeper intel
- Request outreach email drafts for the highest-scored leads
