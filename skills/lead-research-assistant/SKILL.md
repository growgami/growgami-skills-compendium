---
name: lead-research-assistant
description: Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. Perfect for sales, business development, and marketing professionals.
---

# Lead Research Assistant

This skill helps you identify and qualify potential leads by analyzing your product/service, understanding your ideal customer profile, and providing actionable outreach strategies — with live web-searched company data and a CRM-ready export.

## When to Use This Skill

- Finding potential customers or clients for your product/service
- Building a list of companies to reach out to for partnerships
- Identifying target accounts for sales outreach
- Researching companies that match your ideal customer profile
- Preparing for business development activities

## Instructions

### Step 1: Mode — Who Is This For?

Ask the user: **"Is this research for your own business, or for a client?"**

- **Own business**: Gather context directly from the user or their codebase
- **Client**: Ask for the client's product description and ICP before proceeding

This affects how facts are sourced and how the output is framed.

### Step 2: Understand the Product/Service

- If in a code directory, analyze the codebase to understand the product
- Ask clarifying questions about the value proposition if needed
- Identify key features, benefits, and the problem being solved

### Step 3: Define Ideal Customer Profile

Confirm or gather:
- Target industries and sectors
- Company size ranges
- Geographic preferences
- Key pain points the product solves
- Any technology requirements or stack signals

### Step 4: Research and Identify Leads — Use Live Web Search

**CRITICAL**: Use the `WebSearch` tool to find real companies. Do NOT generate company names from training data alone.

Run searches like:
- `"[industry] companies using [relevant tech] site:linkedin.com"`
- `"[industry] startups [location] [pain point keyword]"`
- `"[competitor] customers [industry] [company size]"`
- Look for job postings, press releases, and LinkedIn signals as evidence of fit

For each candidate company, mark confidence level:
- ✅ **Verified** — found via live search with a source URL
- ⚠️ **Inferred** — plausible match based on known context, not directly confirmed

### Step 5: Prioritize and Score

Create a fit score (1–10) for each lead. Consider:
- Alignment with ICP
- Signals of immediate need (job postings, funding, recent news)
- Budget availability
- Competitive landscape
- Timing indicators

### Step 6: Structured Output

For each lead, provide:

```markdown
## Lead [N]: [Company Name]

**Website**: [URL]
**Priority Score**: [X/10] — [one-sentence reason]
**Industry**: [Industry]
**Size**: [Employee count / revenue range]
**Confidence**: ✅ Verified / ⚠️ Inferred

**Why They're a Good Fit**:
[2–3 specific reasons based on their business]

**Target Decision Maker**: [Role/Title]
**LinkedIn**: [URL if found]

**Value Proposition for Them**:
[Specific benefit for this company]

**Outreach Strategy**:
[Personalized approach — mention specific pain points, recent news, or relevant context]

**Conversation Starters**:
- [Specific point 1]
- [Specific point 2]
```

### Step 7: CRM Export

After listing all leads, always offer a CSV export. Format:

```
Company,Website,Fit Score,Target Role,LinkedIn,Value Prop,Conversation Starters,Confidence
[Company],[URL],[X/10],[Role],[LinkedIn URL],[Value prop sentence],[First line of outreach],[Verified/Inferred]
```

Ask: "Would you like me to format this as a CSV for CRM import?"

### Step 8: Next Steps

Offer:
- Draft personalized outreach emails for top 3 leads
- Deeper research on a specific company
- Export to CSV for CRM import (HubSpot, Notion, etc.)

## Tips for Best Results

- **Be specific** about your product and its unique value
- **Run from your codebase** if applicable for automatic context
- **Provide context** about your ideal customer profile
- **Specify constraints** like industry, location, or company size
- **Request follow-up** research on promising leads for deeper insights
