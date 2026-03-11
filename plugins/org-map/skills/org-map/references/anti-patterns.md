# Ontology Anti-Patterns

These are the ways org mapping goes wrong. Each one is something we have seen repeatedly, and each has a corresponding guardrail built into the interview protocol.

## 1. The Happy Path Problem

SOPs describe the ideal scenario. In practice, people execute 5-12 undocumented variants -- workarounds, escalation shortcuts, informal paths. An AI system trained on the documented process hits these exceptions on day one and has no idea what to do.

Example: "Our support process is ticket, triage, resolve or escalate." The reality: 30% of issues get resolved in Slack DMs before a ticket exists. Enterprise customers call the support lead directly. "Escalation" means four different things depending on severity, customer tier, and who is online.

The interview probes for exceptions and variants on every single process.

## 2. Org Chart as Ontology

Titles and reporting lines are the least valuable information you can capture. "VP of Engineering, reports to CTO, manages 15 engineers" tells an AI system almost nothing.

What matters: the VP approves architecture decisions, escalates vendor purchases over $50k, holds tribal knowledge about the 2024 database migration, and is a bus factor of 1 for incident response on weekends.

The interview extracts authority, actions, and tribal knowledge for every role -- not just where they sit on the chart.

## 3. Tools Mistaken for Processes

"We use Jira" is not a process description. How tickets flow through Jira -- who creates them, what criteria drive prioritization, where they stall, what happens when the process breaks -- that is a process description.

The interview requires actor, action, system, and output for every step. The system is context, not content.

## 4. Read-Only Ontology

A knowledge graph full of nouns -- roles, systems, documents -- is a glossary. It can answer "what exists?" but not "what can be done?" AI agents need typed actions with permissions to operate autonomously.

Knowing "Support Lead manages tickets" vs knowing "Support Lead can resolve tickets, escalate to engineering, issue refunds under $500, create bug reports, update knowledge base articles." The second version is an operating model.

The interview captures verbs for every entity. What can this role approve, create, escalate, override?

## 5. False Completeness

Every section filled in, everything marked "complete," and the hard parts papered over with generalities. "Decision criteria: team evaluates options and picks the best one." That sentence contains zero information.

Useful version: "Tends toward proven technology over cutting-edge. PostgreSQL over NoSQL. Will tolerate known pain over unknown risk. Last three architecture decisions took two-plus weeks because the CTO wanted production metrics before committing."

Completeness scores must be honest. A section with real gaps at 0.5 is worth more than platitudes at 1.0.

## 6. The Documentation Sprint

The org plans a big push to document everything before deploying AI. Subject matter experts are too busy. Quality degrades under deadline pressure. The sprint stalls. The AI deployment gets blocked on an asset that was never going to be ready.

Knowledge capture works at the moment of execution -- when someone handles an exception, solves a novel problem, or makes a judgment call. Retrospective documentation three months later loses the nuance.

The interview is designed to run in 90 minutes, not 90 days. It captures knowledge conversationally, from the people who hold it, while the context is fresh.

## 7. No Drift Plan

The ontology is accurate on day one. Three months later the team has reorganized, two tools swapped, and three new processes exist. The file silently becomes fiction. AI outputs degrade and nobody connects it to the stale ontology.

Every output includes a MAINTENANCE.md with drift indicators, review cadence, and which sections decay fastest. The --resume and --audit modes exist for ongoing maintenance.

## 8. The Dark Knowledge Problem

80% of operational knowledge is undocumented. This is not laziness -- much of it is tacit, transferred conversationally between experienced people, never needing to be written down because humans handle ambiguity well enough.

AI cannot consume what was never articulated. An org that skips extraction gets AI that performs at industry average, because it was trained on public (industry-average) knowledge, not the org-specific knowledge that actually differentiates.

The interview explicitly probes for tribal knowledge in every phase. "What does your most experienced person know that nobody else does?"

## 9. Retrieval Confused with Reasoning

Dumping docs into a vector database and adding search does not produce organizational understanding. RAG retrieves relevant paragraphs. It does not reason about relationships between entities, trace decision authority, or navigate exception paths.

The YAML ontology provides semantic structure. Feed it as system context. Use RAG for the details. The ontology is the map; RAG is the encyclopedia.
