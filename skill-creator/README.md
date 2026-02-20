# skill-creator

Guides Claude through creating a new skill from scratch — from understanding requirements to packaging a distributable `.skill` file.

## What it does

When invoked, this skill turns Claude into a skill-building assistant. It walks through the full skill creation process: gathering examples, planning reusable resources (scripts, references, assets), writing the SKILL.md, and packaging the final output.

## When to use

- Creating a brand new Claude skill
- Updating or improving an existing skill
- Learning how to structure a skill correctly

## Example prompts

```
Create a new skill that helps Claude write LinkedIn posts in our brand voice.
```

```
Help me build a skill for summarizing customer support tickets.
```

## How to use

1. Install the skill:
   ```powershell
   cp -r "skill-creator/" "$HOME/.claude/skills/"
   ```
2. Restart VSCode or open a new terminal
3. In VSCode: type `/` in the Claude chat and select `skill-creator`
4. In terminal: run `claude`, then `/skill-creator`

Claude will also trigger this skill automatically when you ask to create or update a skill.
