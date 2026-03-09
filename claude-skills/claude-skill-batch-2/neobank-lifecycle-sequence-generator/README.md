# Neobank Lifecycle Sequence Generator

A Claude skill that generates complete 30-day lifecycle marketing sequences for crypto neobanks. Outputs ready-to-use email, push, and in-app messages for Day 0/1/3/7/14/30, each tied to a specific activation milestone.

## What it does

Takes 3-4 inputs and produces a full sequence covering every touchpoint a new user sees from signup to first activation milestone. Every message is grounded in real crypto neobank user language, not generic fintech copy.

## Quick Start

```bash
# Stablecoin sequence for Plasma targeting first deposit
uv run python scripts/generate_sequence.py \
  --company "Plasma" \
  --product-type stablecoin \
  --goal first-deposit

# Generic crypto card sequence for a client proposal
uv run python scripts/generate_sequence.py \
  --company generic \
  --product-type crypto-card \
  --goal first-spend \
  --voice casual

# Yield sequence saved to file
uv run python scripts/generate_sequence.py \
  --company "Nexo" \
  --product-type yield \
  --goal first-yield \
  --output nexo-activation.md
```

## Inputs

| Argument | Required | Options |
|----------|----------|---------|
| `--company` | Yes | Any neobank name or `generic` |
| `--product-type` | Yes | `stablecoin`, `crypto-card`, `yield`, `self-custody`, `remittance`, `super-app` |
| `--goal` | Yes | `first-deposit`, `first-spend`, `first-yield`, `kyc-complete` |
| `--voice` | No (default: `professional`) | `casual`, `professional`, `crypto-native` |
| `--output` | No (stdout) | file path |

## Output

A single Markdown file structured for direct import into Klaviyo, Customer.io, or Braze. For each of 7 touchpoints (Day 0, 1, 3, 7, 14, 30):

- **Email**: Subject line + full body (100-250 words) + CTA
- **Push notification**: Title + body (under 100 chars)
- **In-app message**: Headline + body + CTA button

Output includes `[bracketed tokens]` for product-specific values (APY rates, fee amounts, user counts) that you replace with real data before activating.

## Product Types

| Type | Primary Goal | Key Activation Barrier |
|------|-------------|------------------------|
| Stablecoin | first-deposit | Trust: "is this safe?" + network confusion |
| Crypto Card | first-spend | Card delivery wait + first decline fear |
| Yield / Earn | first-yield | Post-Celsius trust + yield source opacity |
| Self-Custody | first-deposit | Seed phrase anxiety + gas fee surprise |
| Remittance | first-deposit | Family safety fear + recipient setup complexity |
| Super-App | first-deposit | Feature overwhelm + switching inertia |

## Quality Standards

Every generated message is checked against:

1. **Competitor test**: Could any other neobank send this? If yes, too generic.
2. **Single CTA rule**: One job per touchpoint. No "also check out our features."
3. **Real language rule**: Copy mirrors user pain language, not marketing rewrites.
4. **Specificity rule**: Numbers over adjectives. `$0 in fees` over `no fees`.
5. **No slop rule**: No em-dashes, "seamless", "innovative", "we're thrilled."

## Reference Data

Built on:
- Crypto neobank app store review patterns (KYC rage cycle, trust test, yield mercenary, etc.)
- Activation benchmarks: 63% month-one churn, 72-hour critical window, drop-off rates per product type
- User language from real app store reviews across 15+ crypto neobanks
- Category-specific pain points and timing benchmarks

## Files

```
neobank-lifecycle-sequence-generator/
├── SKILL.md                              # Full skill documentation (Claude instructions)
├── README.md                             # This file
├── scripts/
│   └── generate_sequence.py              # CLI generator
└── references/
    ├── lifecycle-sequence-library.md     # Frameworks for 6 product types
    └── activation-milestones.md          # Timing benchmarks and drop-off rates
```

## Background

Part of Growgami's neobank skills suite. Companion skills:
- [App Store Intelligence](https://github.com/xkonjin/neobank-app-store-intelligence) — analyze user reviews for lifecycle insights
- [Positioning Engine](https://github.com/xkonjin/neobank-positioning-engine) — competitive messaging framework
- [TikTok Hook Generator](https://github.com/xkonjin/neobank-tiktok-hook-generator) — acquisition content for neobanks
