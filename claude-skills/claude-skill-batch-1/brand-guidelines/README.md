# brand-guidelines

Applies Growgami's official brand colors and typography to any artifact.

## What it does

When invoked, this skill instructs Claude to apply Growgami's visual identity — grayscale color palette and Geist Mono typography — to documents, slides, designs, or any other output that benefits from consistent brand styling.

## When to use

- Creating or styling any visual artifact for Growgami
- Ensuring brand consistency across documents and presentations
- Applying correct colors and fonts to new or existing content

## How to use

1. Install the skill:
   ```powershell
   cp -r "brand-guidelines/" "$HOME/.claude/skills/"
   ```
2. Restart VSCode or open a new terminal
3. In VSCode: type `/` in the Claude chat and select `brand-guidelines`
4. In terminal: run `claude`, then `/brand-guidelines`

Claude will also trigger this skill automatically when you ask about brand styling or design.

## Brand at a glance

- **Font**: Geist Mono (Medium for headlines, Regular for sub-heads)
- **Dark palette**: `#080808` → `#333333`
- **Light palette**: `#D6D6D6` → `#F9F9F9`
