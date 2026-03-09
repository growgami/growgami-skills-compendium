# frontend-design

Build production-grade web interfaces that look genuinely designed, not AI-generated. Commits to a bold visual direction, outputs a Design Context block to keep revisions consistent, and offers 4 explicit revision options after every generation.

**Modified by Growgami** — added intake brief, Design Context block, and A/B/C/D revision loop.
**Original license**: Apache 2.0

---

## What it does

- Asks two quick questions before building: aesthetic direction and tech constraints
- Picks a bold, specific visual style and commits to it
- Outputs a Design Context block (colors, fonts, motion) so every revision stays on-theme
- After every generation, offers 4 revision paths: change palette, layout, typography, or full rebuild

---

## Installation

**Windows**
```bash
copy "SKILL.md" "%USERPROFILE%\.claude\skills\frontend-design.md"
```

**macOS / Linux**
```bash
cp SKILL.md ~/.claude/skills/frontend-design.md
```

Restart Claude Code after installing. The skill is then available globally across all sessions.

---

## Usage

Invoke from any Claude Code chat:

```
/frontend-design Build a landing page for a fintech SaaS product
```

```
/frontend-design Create a dashboard component showing real-time signal data in React
```

```
/frontend-design Design a skill marketplace listing card in plain HTML
```

After generating, Claude will output a **Design Context** block and offer revision options A–D. Pick one to iterate.

---

## Tips

- Say "just build it" if you want Claude to pick the direction without asking
- Reference a site or screenshot for a specific aesthetic: "something like stripe.com but darker"
- Use option D to start fresh with a completely different visual direction
- Works with any framework — React, Vue, plain HTML/CSS. Specify in your prompt or Claude will choose based on context
