# /org-map

A Claude Code skill that walks you through mapping your organization into a structured YAML ontology.

The pitch version: it extracts the intelligence layer -- the structured knowledge about how your org actually operates that makes any AI system dramatically more useful. The honest version: it is a 90-minute guided interview that asks the questions a good consultant would ask in their first week, and produces a machine-readable file instead of a slide deck.

## Install

Via the Growgami skill marketplace:
```
/plugin marketplace add growgami/growgami-skills-compendium
/plugin install org-map
```

Or copy manually:
```bash
git clone https://github.com/growgami/growgami-skills-compendium.git
cp -r growgami-skills-compendium/plugins/org-map/skills/org-map ~/.claude/skills/
```

## Usage

```
/org-map              # Start fresh
/org-map --resume     # Continue from existing org-ontology.yaml
/org-map --audit      # Score and gap-analyze an existing ontology
/org-map --schema     # View the output format
/org-map --export md  # Export to markdown, json, prompt, or onboarding
```

## What it does

Runs a structured interview across five phases:

**Foundation** -- what the org does, team shape, tool stack, how decisions actually get made.

**Process Architecture** -- the 3-5 core workflows that drive the org. For each one: triggers, steps, decisions, exceptions, handoffs, bus factor. The skill probes for the real variants, not the documented happy path.

**Decision Architecture** -- who decides what, using which criteria, with what authority. Historical patterns, escalation paths, failure modes.

**Knowledge Flows** -- how information moves through the org, where it gets stuck, what is tribal, what breaks when someone leaves.

**Synthesis** -- compiles everything into `org-ontology.yaml` + `org-summary.md` with honest completeness scores and a gap analysis.

## What the output looks like

```yaml
processes:
  - id: feature-development
    owner: head-of-product
    trigger:
      type: request
      description: "Product decides to build -- roadmap, customer request, or sales pressure"
    decisions:
      - id: scope-feasibility
        owner: cto
        criteria: [engineering-effort, team-capacity, technical-debt-impact]
        historical_pattern: "Pushes back on ~30% of features. Prioritizes reliability over speed."
    exceptions:
      - condition: "Urgent enterprise escalation"
        frequency: "~2x/month"
        override: "Skip PRD. CTO approves directly."
    bus_factor: 2
    new_hire_gotcha: "No staging env. PRs go straight to production after merge."
```

See `skills/org-map/references/example-saas.yaml` for a full worked example.

## What it draws from

The interview protocol borrows from Wardley mapping (value chain positioning), Team Topologies (interaction modes between teams), Jobs to Be Done (outcome-first process framing), RACI (decision ownership clarity), ADRs (structured decision capture), and Conway's Law (org-system alignment). None of these are cited during the interview -- they just make the questions better.

Nine documented anti-patterns -- the ways org mapping typically fails -- are built into the skill as guardrails. See `references/anti-patterns.md`.

## Files

```
skills/org-map/
  SKILL.md                        # The interview protocol
  references/
    schema.yaml                   # Full output schema, annotated
    example-saas.yaml             # Realistic example (45-person B2B SaaS)
    anti-patterns.md              # 9 failure modes and how the skill avoids them
```
