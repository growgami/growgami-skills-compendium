# Claude Skills

Internal staging repo for team-submitted `skills.md` and `tools.md` files before they are published to the public repository.

## Submitting a Skill

Each skill must follow this structure:

```
skill-name/
├── README.md     # Description of what the skill does
└── SKILL.md      # The skill definition itself
```

- The folder must be named after the skill (e.g. `code-review/`, `summarize-pr/`)
- `README.md` should describe the skill's purpose and usage
- `SKILL.md` contains the skill definition

## Using a Skill

### Prerequisites

Install the Claude Code CLI if you haven't already:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Then add it to your PATH: **System Properties → Environment Variables → Edit User PATH → New → `C:\Users\<you>\.local\bin`** and restart your terminal.

### Install a skill

Copy the skill folder to your personal Claude skills directory:

```powershell
cp -r "path/to/skill-name/" "$HOME/.claude/skills/"
```

Restart VSCode or open a new terminal session after copying.

### Use a skill in VSCode (Claude Code extension)

Type `/` in the Claude chat to see available skills, then select the skill from the menu. Claude will also trigger the skill automatically when your request matches its description.

### Use a skill in the terminal

Start a Claude session and invoke the skill by name:

```bash
claude
/skill-name
```

Or verify your skills are loaded with:

```bash
/skills
```
