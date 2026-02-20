# market-research-reports

Generates comprehensive market research reports (50+ pages) in the style of top consulting firms like McKinsey, BCG, and Gartner.

## What it does

When invoked, this skill instructs Claude to produce a full professional-grade market research report with structured analysis, visual generation, and strategic recommendations. Reports are formatted in LaTeX and compiled to PDF.

**Includes:**
- Executive summary, market sizing (TAM/SAM/SOM), competitive landscape
- Porter's Five Forces, PESTLE, SWOT, BCG Matrix analysis
- 5–6 auto-generated diagrams and charts
- Implementation roadmap and investment thesis
- 50+ pages targeting consulting-firm quality

## When to use

- Creating market analysis for investment or strategic decisions
- Sizing a new market or evaluating a market entry opportunity
- Preparing competitive intelligence reports
- Building a business case for a new product or initiative

## Example prompts

```
Generate a full market research report on the B2B SaaS project management tools market.
```

```
Create a 50-page consulting-style report on the electric vehicle charging infrastructure market in Europe.
```

## Requirements

This skill depends on:
- **LaTeX** (XeLaTeX) for PDF compilation
- **Python 3** for visual generation scripts
- `scientific-schematics` and `generate-image` skills for diagrams

## How to use

1. Install the skill:
   ```powershell
   cp -r "market-research-reports/" "$HOME/.claude/skills/"
   ```
2. Restart VSCode or open a new terminal
3. In VSCode: type `/` in the Claude chat and select `market-research-reports`
4. In terminal: run `claude`, then `/market-research-reports`

Claude will also trigger this skill automatically when you ask for market research, industry analysis, or consulting-style reports.
