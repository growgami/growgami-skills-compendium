# editor

Professional editing and proofreading for any written content — improves clarity, grammar, style, and readability.

## What it does

When invoked, this skill turns Claude into a professional editor that can proofread, copy edit, line edit, or developmentally edit any text. It identifies and fixes grammar, wordiness, passive voice, weak verbs, and unclear structure, then explains every change made.

## When to use

- Proofreading documents before sending or publishing
- Improving clarity and conciseness of any written content
- Fixing grammar, punctuation, or tone
- Refining style for professional or marketing copy

## Example prompts

```
Edit this paragraph for clarity and conciseness: [paste text]
```

```
Proofread this email and fix any grammar issues: [paste text]
```

```
Rewrite this in a more confident, active voice: [paste text]
```

## How to use

1. Install the skill:
   ```powershell
   cp -r "editor/" "$HOME/.claude/skills/"
   ```
2. Restart VSCode or open a new terminal
3. In VSCode: type `/` in the Claude chat and select `editor`
4. In terminal: run `claude`, then `/editor`

Claude will also trigger this skill automatically when you ask it to edit, proofread, improve, or revise text.
