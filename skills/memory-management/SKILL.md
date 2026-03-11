---
name: memory-management
description: >
  File-based persistent memory system for Claude. Stores client context, skill patterns, and signal insights across sessions using native Read/Write/Edit tools. Use when you need to remember something across conversations, look up past decisions, or build a shared knowledge base.
  Use when: storing client context, saving successful skill patterns, recording high-signal topics, sharing knowledge across sessions.
  Skip when: ephemeral one-off tasks, external data sources already available, no learning needed.
---

# Memory Management Skill

## Purpose

Give Claude persistent memory across sessions using native file-based storage — no external CLI or dependencies required. Memory is stored as structured markdown files and searched semantically by reading and reasoning over them.

## Memory Structure

Memory lives in a `memory/` folder at the root of your current workspace:

```
memory/
  clients.md
  skill-patterns.md
  signals.md
```

Three namespaces:

| File | What Goes In It |
|------|----------------|
| `memory/clients.md` | Client names, ICPs, preferences, past work, tone |
| `memory/skill-patterns.md` | What worked when building or running skills, reusable patterns |
| `memory/signals.md` | High-scoring topics from monitoring, trending skill gaps |

## When to Use

**Before starting any task:**
- Read the relevant memory file(s)
- Check if there's existing context that applies

**After completing any task:**
- Store what worked (pattern, decision, insight)
- Update existing entries rather than duplicating

## How to Store a Memory

**First time using a namespace?** Use the `Write` tool to create the file. After that, use `Edit` to append new entries.

If a file doesn't exist yet, create it with a header:
```markdown
# [Namespace Name]
```
Then add entries below.

Use the `Edit` tool to append to an existing file. Format:

```markdown
## [Topic or Client Name]
- [Key fact or pattern]
- [Date added: YYYY-MM-DD]
```

**Example — client context:**
```markdown
## Acme Corp
- ICP: B2B SaaS CTOs at Series A companies replacing legacy tools
- Preferred tone: direct, no buzzwords
- Past work: lead research for their DevOps product (March 2026)
- Date added: 2026-03-09
```

**Example — skill pattern:**
```markdown
## Lead Research — What Works
- Always use WebSearch, never generate companies from training data
- CSV export at the end increases session value significantly
- Mode selector (own business vs client) reduces back-and-forth
- Date added: 2026-03-09
```

**Example — signal pattern:**
```markdown
## High-Signal Topics (March 2026)
- "Code review automation" trending on Twitter, 3 weeks consistent
- "Proposal writing assistant" gap confirmed — no skillsmp match
- Date added: 2026-03-09
```

## How to Search Memory

Read the relevant file and reason over it:

```
Read memory/clients.md → find entries matching the current client or project
Read memory/skill-patterns.md → find patterns relevant to the current task type
Read memory/signals.md → find recent signal trends relevant to the current topic
```

**If the file doesn't exist or is empty**: proceed without memory — nothing to apply yet. This is expected on first use.

## Decision Logic

```
START TASK
  → Read relevant memory file
  → Apply any matching context or patterns
  → Proceed with task

END TASK
  → Did you learn something reusable?
    YES → Append to the relevant memory file
    NO  → Skip
```

## Best Practices

1. Check memory before starting — avoid re-learning what's already known
2. Store after completing — one line is enough if that's all there is
3. Update existing entries rather than creating duplicates
4. Keep entries concise — memory files should be scannable, not essays
5. Use the `signals.md` file to feed insights back into the skill pipeline
