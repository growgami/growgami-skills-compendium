# memory-management

Give Claude persistent memory across sessions using plain markdown files in your workspace. Stores client context, skill patterns, and signal trends — and knows to check them before starting a task and update them after.

**Modified by Growgami** — completely rewritten to remove `@claude-flow/cli` dependency and replace with native file-based memory using Claude Code's built-in Read/Write/Edit tools.

---

## What it does

- Stores memory in 3 files inside a `memory/` folder in your workspace:
  - `memory/clients.md` — client ICPs, tone preferences, past work
  - `memory/skill-patterns.md` — what worked when building or running skills
  - `memory/signals.md` — trending topics and confirmed skill gaps
- Checks memory before starting any task
- Saves useful patterns after completing a task
- No external tools, no CLI, no setup — works out of the box

---

## Installation

**Windows**
```bash
copy "memory-management\SKILL.md" "%USERPROFILE%\.claude\skills\memory-management.md"
```

**macOS / Linux**
```bash
cp memory-management/SKILL.md ~/.claude/skills/memory-management.md
```

Restart Claude Code after installing.

The `memory/` folder will be created automatically the first time you store something, relative to whatever workspace you're working in.

---

## Usage

Claude applies this skill automatically when it's installed — no slash command needed. It will:

1. Read relevant memory files at the start of each session
2. Apply any matching context to the task at hand
3. Offer to store new patterns after completing work

You can also prompt it directly:

```
Store this client's ICP in memory: [client name], targeting CTOs at Series A fintechs
```

```
Check memory for any patterns related to lead research before we start
```

```
Save this pattern: the brainstorming skill works best when complexity is classified upfront
```

---

## Memory structure

Files live at `memory/` relative to your current workspace root:

```
your-project/
  memory/
    clients.md
    skill-patterns.md
    signals.md
```

Each entry follows this format:
```markdown
## [Topic or Client Name]
- [Key fact or pattern]
- [Date added: YYYY-MM-DD]
```

---

## Tips

- Memory is per-workspace — each project has its own `memory/` folder
- Keep entries short and scannable — one line is enough if that's all there is
- Use `signals.md` to log trending topics from the claude-md-monitor pipeline
- If a file doesn't exist yet, Claude will create it on first write
