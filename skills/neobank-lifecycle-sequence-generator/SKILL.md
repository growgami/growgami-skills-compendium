---
name: lifecycle-sequence-generator
description: Generate full lifecycle marketing sequences for crypto neobanks. Outputs ready-to-use email, push, and in-app messages for Day 0/1/3/7/14/30 tied to activation milestones. Use when building onboarding flows, activation campaigns, or retention sequences for neobank clients.
---

# Lifecycle Sequence Generator for Crypto Neobanks

Generates a complete 30-day lifecycle sequence for any crypto neobank type. Every touchpoint (email, push, in-app) is tied to a specific activation milestone and written in real user language, not marketing jargon.

Not a generic email template builder. Every sequence is grounded in crypto neobank churn data ($150-500 CAC, 63% month-one churn), real activation barriers (KYC rage cycles, trust tests, yield anxiety), and the specific language users use in app store reviews.

## Trigger

- `generate lifecycle sequence for [company]`
- `build onboarding emails for [neobank]`
- `lifecycle marketing for [product type]`
- `activation campaign for [neobank name]`

## Quick Start

```bash
# Full sequence with company name
uv run python neobank-skills/lifecycle-sequence-generator/scripts/generate_sequence.py \
  --company "Plasma" \
  --product-type stablecoin \
  --goal first-deposit

# Generic sequence for client proposals
uv run python neobank-skills/lifecycle-sequence-generator/scripts/generate_sequence.py \
  --company generic \
  --product-type crypto-card \
  --goal first-spend \
  --voice casual

# Full options with file output
uv run python neobank-skills/lifecycle-sequence-generator/scripts/generate_sequence.py \
  --company "KAST" \
  --product-type crypto-card \
  --goal first-spend \
  --voice crypto-native \
  --output sequences/kast-activation.md
```

| Arg | Required | Options |
|-----|----------|---------|
| `--company` | Yes | Any neobank name or "generic" |
| `--product-type` | Yes | stablecoin, crypto-card, yield, self-custody, remittance, super-app |
| `--goal` | Yes | first-deposit, first-spend, first-yield, kyc-complete |
| `--voice` | No (default: professional) | casual, professional, crypto-native |
| `--output` | No (default: stdout) | file path |

## Workflow

### Step 1: Load Context

Before generating, the script loads:
- Category pain points and user language from `references/lifecycle-sequence-library.md`
- Activation timing benchmarks from `references/activation-milestones.md`
- If company is not "generic": checks for app store review data at `neobank-skills/app-store-intelligence/output/{slug}-reviews.json`

If review data exists, the Day 3 message pulls real user complaint language directly from reviews. If not, it falls back to category-level pain language. The output header states which was used.

### Step 2: Build the Sequence

For each of the 7 touchpoints (Day 0, 1, 3, 7, 14, 30), three channels are generated:

| Channel | Output |
|---------|--------|
| Email | Subject line + full body (100-250 words) + visual recommendation |
| Push notification | Title + body (under 100 chars total) |
| In-app message | Headline + CTA (under 60 chars) |

**What each touchpoint does:**

- **Day 0**: Welcome. Set expectations. Reduce fear. Drive one micro-action (email confirm or KYC start).
- **Day 1**: Nudge toward activation goal. Remind them why they signed up. Address the most likely hesitation.
- **Day 3**: Directly address the #1 drop-off barrier for this product type. No selling. Solve the problem.
- **Day 7**: Social proof. Real numbers. Make staying feel smart, not just easy.
- **Day 14**: Re-engage fence-sitters. One specific value proof point. One clear action.
- **Day 30**: Graduation (activated) or hard reset (not activated, different CTA, different tone).

Day 0 and Day 1 are always sent. Days 3, 7, 14, 30 are conditional on activation status — the script generates both the activated and non-activated variants.

### Step 3: Apply Quality Filters

Every message is checked against five rules before output:

1. **Competitor test**: Could Revolut, Coinbase, or any other neobank send this exact message? If yes, rewrite it.
2. **Single CTA rule**: Every touchpoint has one job and one CTA. No "also check out our features."
3. **Real language rule**: Copy mirrors user pain language, not marketing reframes.
4. **Specificity rule**: Numbers over adjectives. "$0 in fees" over "no fees". "Under 3 seconds" over "instant."
5. **No slop rule**: No em-dashes, no "seamless", no "we're excited/thrilled", no "innovative", no "cutting-edge."

### Step 4: Output Format

Output is a single Markdown file structured for direct paste into Klaviyo, Customer.io, or Braze:

```markdown
# Lifecycle Sequence: [Company] — [Product Type] — Goal: [Goal]
Generated: [date] | Voice: [voice] | Review data: yes/no

---

## Day 0 — Welcome

**Activation Goal:** [goal]
**Trigger:** Account created
**Send:** Immediately on signup

### Email
**Subject:** [subject line]

[Email body]

**CTA button:** [text] → [destination]

**Visual:** [specific visual recommendation — what to show, the format (hero image / GIF / screenshot / illustration), and why it works for this touchpoint's goal]

### Push Notification
**Title:** [title]
**Body:** [body]
**Deep link:** [screen]

### In-App Message
**Headline:** [headline]
**Body:** [body]
**CTA:** [button text]
```

## Quality Standards

**The Specificity Test**
Every message must answer: could any other neobank in this category send this exact message? If yes, rewrite it. A stablecoin sequence must not read like a generic fintech onboarding. A self-custody sequence must not read like a yield product sequence.

**The Activation Linkage Test**
Every message has ONE goal. Day 1 email has one CTA. Push has one tap destination. In-app has one button. Diluted messages produce diluted activation rates.

**The Real Language Test**
Pull from user pain language in `references/lifecycle-sequence-library.md`. Real users write "the app froze during KYC" not "I experienced technical difficulties during identity verification." Copy should mirror the user's language, not reframe it in brand voice.

**The Zero-Slop Test**
Banned: em-dashes (—), seamless, innovative, we're thrilled/excited, next-gen, cutting-edge, revolutionize. These are auto-rewrites, not style preferences.

## Examples

**User says:** "Generate lifecycle sequence for Plasma, stablecoin, goal: first-deposit"

Actions:
1. Load stablecoin sequence framework from `references/lifecycle-sequence-library.md`
2. Check for Plasma app store review data at `neobank-skills/app-store-intelligence/output/plasma-reviews.json`
3. Map activation milestones: signup to KYC to wallet connection to first USDC deposit
4. Generate 7 touchpoints, each tied to first-deposit milestone
5. Apply crypto-native voice appropriate for Plasma's stablecoin product
6. Output Markdown ready to paste into Klaviyo

**User says:** "Build onboarding emails for a generic crypto card neobank"

Actions:
1. Load crypto-card framework from library
2. No company data — use category pain language and benchmarks
3. Map activation milestones: card order, card activation, first tap, first month spend
4. Generate with professional voice (default)
5. Include `[Company Name]` placeholder tokens throughout for client customization

## Edge Cases

- **No app store data**: Falls back to category pain language from the library. Output header notes this clearly.
- **Goal mismatch with product**: `first-yield` for `crypto-card` is flagged. Script suggests the correct goal and asks to confirm before continuing.
- **Super-app product type**: Has multiple possible goals. Generates sequence for the stated goal, adds a note about secondary activation goals to consider.
- **crypto-native voice + remittance or super-app**: Flag raised in output. These products target mainstream users and crypto-native tone may create friction. Script recommends `casual` or `professional` voice instead but continues.
- **Brand "generic"**: All company-specific references use `[Company Name]`, `[Product Name]` tokens. Ready for white-label delivery to clients.

## Files

| Path | Purpose |
|------|---------|
| `scripts/generate_sequence.py` | Main CLI generator: inputs to full sequence output |
| `references/lifecycle-sequence-library.md` | Pre-built sequence frameworks for 6 neobank types |
| `references/activation-milestones.md` | Activation events, timing benchmarks, drop-off rates |
