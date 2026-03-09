# competitive-ads-extractor

Extracts and analyzes competitor ads from ad libraries (Facebook, LinkedIn, etc.) to identify what messaging, creative approaches, and pain points are working.

## What it does

When invoked, this skill instructs Claude to scrape competitor ads from public ad libraries, capture screenshots, analyze messaging patterns, and produce a structured report with actionable insights for your own ad campaigns.

## When to use

- Researching competitor ad strategies before launching a campaign
- Finding inspiration and proven creative patterns
- Understanding how competitors position themselves in the market
- Identifying pain points and use cases competitors are targeting

## Example prompt

```
Extract all current ads from [Competitor] on Facebook Ad Library and tell me what messaging is working for them.
```

## How to use

1. Install the skill:
   ```powershell
   cp -r "competitive-ads-extractor/" "$HOME/.claude/skills/"
   ```
2. Restart VSCode or open a new terminal
3. In VSCode: type `/` in the Claude chat and select `competitive-ads-extractor`
4. In terminal: run `claude`, then `/competitive-ads-extractor`

Claude will also trigger this skill automatically when you ask about competitor ads.
