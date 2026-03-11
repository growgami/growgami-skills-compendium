# Growgami Skills

Claude Code skills built from real operational experience.

## Install

**One skill:**

```bash
git clone https://github.com/growgami/growgami-skills-compendium.git
cp -r growgami-skills-compendium/skills/org-map ~/.claude/skills/
```

**All skills:**

```bash
git clone https://github.com/growgami/growgami-skills-compendium.git
cp -r growgami-skills-compendium/skills/* ~/.claude/skills/
```

**With the install script:**

```bash
git clone https://github.com/growgami/growgami-skills-compendium.git
cd growgami-skills-compendium
./install.sh              # interactive picker
./install.sh org-map      # specific skill
./install.sh --all        # everything
```

## Skills

| Skill | What it does |
|---|---|
| [org-map](skills/org-map/) | Map your org's real operating model into a structured YAML ontology |
| [brand-guidelines](skills/brand-guidelines/) | Brand color and typography standards |
| [competitive-ads-extractor](skills/competitive-ads-extractor/) | Competitive ad intelligence extraction |
| [editor](skills/editor/) | Content editing |
| [frontend-design](skills/frontend-design/) | Frontend UI/UX design |
| [investor-materials](skills/investor-materials/) | Investor decks and materials |
| [lead-research-assistant](skills/lead-research-assistant/) | Lead research and qualification |
| [market-research-reports](skills/market-research-reports/) | Market research generation |
| [memory-management](skills/memory-management/) | Claude memory management |
| [neobank-lifecycle-sequence-generator](skills/neobank-lifecycle-sequence-generator/) | Neobank lifecycle sequences |
| [skill-creator](skills/skill-creator/) | Scaffold new Claude skills |

## Structure

```
skills/
  skill-name/
    SKILL.md        # skill definition (YAML frontmatter + prompt)
    references/     # optional supporting files
```

Compatible with vanilla Claude Code (`~/.claude/skills/`) and [skills.ws](https://skills.ws).
