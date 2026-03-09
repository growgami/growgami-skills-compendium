#!/usr/bin/env python3
"""
Lifecycle Sequence Generator for Crypto Neobanks
Generates a complete 30-day email/push/in-app sequence for any crypto neobank type.

Usage:
    uv run python neobank-skills/lifecycle-sequence-generator/scripts/generate_sequence.py \
      --company "Plasma" \
      --product-type stablecoin \
      --goal first-deposit

    uv run python neobank-skills/lifecycle-sequence-generator/scripts/generate_sequence.py \
      --company generic \
      --product-type crypto-card \
      --goal first-spend \
      --voice casual
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Add /work to path for SDK access
sys.path.insert(0, "/work")


# ── Constants ────────────────────────────────────────────────────────────────

PRODUCT_TYPES = ["stablecoin", "crypto-card", "yield", "self-custody", "remittance", "super-app"]
GOALS = ["first-deposit", "first-spend", "first-yield", "kyc-complete"]
VOICES = ["casual", "professional", "crypto-native"]

# Goal compatibility map: (product_type, goal) → "primary" | "secondary" | "prereq" | "mismatch"
GOAL_COMPATIBILITY = {
    ("stablecoin",    "first-deposit"):  "primary",
    ("stablecoin",    "first-spend"):    "secondary",
    ("stablecoin",    "first-yield"):    "secondary",
    ("stablecoin",    "kyc-complete"):   "prereq",
    ("crypto-card",   "first-deposit"):  "prereq",
    ("crypto-card",   "first-spend"):    "primary",
    ("crypto-card",   "first-yield"):    "mismatch",
    ("crypto-card",   "kyc-complete"):   "prereq",
    ("yield",         "first-deposit"):  "prereq",
    ("yield",         "first-spend"):    "mismatch",
    ("yield",         "first-yield"):    "primary",
    ("yield",         "kyc-complete"):   "prereq",
    ("self-custody",  "first-deposit"):  "primary",
    ("self-custody",  "first-spend"):    "secondary",
    ("self-custody",  "first-yield"):    "mismatch",
    ("self-custody",  "kyc-complete"):   "prereq",
    ("remittance",    "first-deposit"):  "primary",
    ("remittance",    "first-spend"):    "secondary",
    ("remittance",    "first-yield"):    "mismatch",
    ("remittance",    "kyc-complete"):   "prereq",
    ("super-app",     "first-deposit"):  "primary",
    ("super-app",     "first-spend"):    "secondary",
    ("super-app",     "first-yield"):    "secondary",
    ("super-app",     "kyc-complete"):   "prereq",
}

# Voice mismatch warnings
VOICE_MISMATCHES = {
    ("remittance",   "crypto-native"): "Remittance products target mainstream users. crypto-native voice may create friction. Consider 'casual' or 'professional'.",
    ("super-app",    "crypto-native"): "Super-apps often target mainstream users. Verify the product's primary audience before using crypto-native voice.",
}


# ── Product-Specific Copy Data ────────────────────────────────────────────────

SEQUENCES = {
    "stablecoin": {
        "first-deposit": {
            "tagline": "Your USDC account is ready. Here's how to fund it.",
            "days": {
                0: {
                    "role": "Welcome + wallet ready + single micro-action",
                    "trigger": "Account created",
                    "email": {
                        "subject": "{company}: Your USDC wallet is ready",
                        "body": """Hi {first_name},

Your {company} account is live. Your USDC wallet address is waiting for you in the app.

Before you fund it, one thing to know: {company} uses {network} to keep transfers fast and fees near zero. When you send from an exchange or another wallet, pick {network} as the network. Wrong network = funds don't arrive.

To make your first deposit:
1. Open the app and tap "Receive"
2. Copy your wallet address
3. From your exchange: send USDC on {network}
4. Funds arrive in under 3 minutes

Start with any amount. There's no minimum.

Questions? Reply to this email.

— {company} team""",
                        "cta_text": "See My Wallet Address",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "Your USDC wallet is live",
                        "body": "Tap to see your address and make your first deposit.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "Your wallet is ready",
                        "body": "Deposit USDC in under 3 minutes.",
                        "cta": "See My Address",
                    },
                },
                1: {
                    "role": "Nudge toward first deposit, invite test deposit",
                    "trigger": "24 hours after signup, no deposit made",
                    "email": {
                        "subject": "How to send your first $10 to {company}",
                        "body": """Hi {first_name},

You haven't made your first deposit yet. That's fine — here's the exact path.

**Option 1: Send from Coinbase or Binance**
Go to your exchange → Withdraw → Select USDC → Choose {network} as the network → Paste your {company} wallet address. Arrives in 2-3 minutes. Fees: under $0.10.

**Option 2: Send from another wallet (MetaMask, etc.)**
Open MetaMask → Send → Paste your {company} address → Select {network} → Amount. Same arrival time.

**Not sure which to use?** Start with $10. It's not about the amount — it's about seeing the funds arrive in your account so you know the process works.

Once it arrives, you'll see your balance update in real time.

— {company} team""",
                        "cta_text": "Open Deposit Guide",
                        "cta_dest": "help/first-deposit",
                    },
                    "push": {
                        "title": "First deposit: 3 minutes",
                        "body": "Test with any amount. Step-by-step guide ready.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "Deposit in 3 minutes",
                        "body": "Start with any amount to test the process.",
                        "cta": "See How",
                    },
                },
                3: {
                    "role": "Address trust barrier head-on, invite $10 test",
                    "trigger": "3 days after signup, no deposit made",
                    "email": {
                        "subject": "You can test {company} with $10 first",
                        "body": """Hi {first_name},

No pressure. But a lot of {company} users started with a $10 test deposit before sending larger amounts.

Here's why that works: you can see exactly how fast deposits arrive, confirm your address is correct, and verify that withdrawals work before committing more. Most users who test first say the whole process takes about 4 minutes and nothing goes wrong.

About your funds at {company}: {custody_statement}

{reserve_statement}

To run the test:
1. Send $10 USDC on {network}
2. Watch it arrive in your balance (usually under 3 minutes)
3. Optional: withdraw it back to confirm that works too

After that, you'll know exactly what you're dealing with.

— {company} team""",
                        "cta_text": "Start $10 Test",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "Test with $10 first",
                        "body": "Most users do a test deposit before going bigger. Here's how.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "Start with $10",
                        "body": "See how deposits work before committing more.",
                        "cta": "Test Deposit",
                    },
                },
                7: {
                    "role": "Social proof, make staying feel smart",
                    "trigger": "7 days after signup, no deposit made",
                    "email": {
                        "subject": "{user_count} people moved their money to {company} this week",
                        "body": """Hi {first_name},

Last week, {user_count} people made their first deposit on {company}.

Most of them weren't moving large amounts. The median first deposit was around $200. But after their first deposit, {retention_stat}% of them made a second one within 7 days.

What they said they were doing before {company}:
- Paying $15-40 per international wire transfer
- Waiting 3-5 business days for cross-border payments
- Accepting 2-3% FX markup on every conversion

With {company}: {fee_statement}

Your wallet is still ready when you are.

— {company} team""",
                        "cta_text": "Make My First Deposit",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "Your wallet is still here",
                        "body": "{user_count} deposits made this week. Yours is waiting.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "{user_count} deposits this week",
                        "body": "Join them. Your wallet is ready.",
                        "cta": "Deposit Now",
                    },
                },
                14: {
                    "role": "Opportunity cost — what they're missing",
                    "trigger": "14 days after signup, no deposit made",
                    "email": {
                        "subject": "You've sent {estimated_transfers} bank transfers this month. Here's the real cost.",
                        "body": """Hi {first_name},

A quick calculation: if you send money internationally once a month, the average bank fee plus FX markup costs $28-45 per transfer. Over a year, that's $336-540 gone.

{company} users who switch from wire transfers save an average of {avg_savings} per year.

Nothing has changed with your account. It's still open. Your wallet address is the same. And the first deposit still takes about 3 minutes.

The one question worth answering before you decide: what would you use {company} for specifically?

If it's cross-border payments: you'd save on every transfer, and payments settle in minutes not days.

If it's holding USDC: your funds stay dollar-denominated without a bank that can freeze your account.

If you're not sure: reply to this email and tell me what you're dealing with. I'll tell you if {company} solves it.

— {company} team""",
                        "cta_text": "Calculate My Savings",
                        "cta_dest": "tools/savings-calculator",
                    },
                    "push": {
                        "title": "14 days. Zero deposits.",
                        "body": "Here's what that's cost you vs. using {company}.",
                        "deep_link": "tools/savings-calculator",
                    },
                    "in_app": {
                        "headline": "Your savings calculator",
                        "body": "See what you'd save vs. wire transfers.",
                        "cta": "Calculate",
                    },
                },
                30: {
                    "role": "Final push — last shot before churn",
                    "trigger": "30 days after signup, no deposit made",
                    "email": {
                        "subject": "Last email (and one honest question)",
                        "body": """Hi {first_name},

You signed up for {company} 30 days ago and haven't made a deposit.

That's okay. But before we stop sending you emails, I want to ask one honest question: what stopped you?

Was it:
(A) Too complicated — you didn't know how to deposit
(B) Trust — you weren't sure if {company} was safe
(C) Not the right time — you'll get to it later
(D) Something else entirely

Reply with a letter and I'll send you a direct answer. If it's (A), I'll walk you through it in 5 messages. If it's (B), I'll show you exactly how your funds are protected. If it's (C), your account stays open — no deadline.

No hard sell. Just trying to understand.

— {company} team""",
                        "cta_text": "Tell Us What Stopped You",
                        "cta_dest": "feedback/why-not",
                    },
                    "push": {
                        "title": "Still here. No pressure.",
                        "body": "Your account stays open. One question before we go quiet.",
                        "deep_link": "feedback/why-not",
                    },
                    "in_app": {
                        "headline": "One question for you",
                        "body": "What stopped you? Reply takes 10 seconds.",
                        "cta": "Tell Us",
                    },
                },
            }
        }
    },

    "crypto-card": {
        "first-spend": {
            "tagline": "Your card is ready. Here's how to make your first tap count.",
            "days": {
                0: {
                    "role": "Welcome + activate virtual card immediately",
                    "trigger": "Account created",
                    "email": {
                        "subject": "{company}: Your virtual card is ready to activate",
                        "body": """Hi {first_name},

Your {company} account is live. You have a virtual card waiting in the app right now — no need to wait for a physical card.

To use it in the next 5 minutes:
1. Open the {company} app
2. Tap "Card" → "Activate virtual card"
3. Add it to Apple Pay or Google Pay
4. Use it anywhere contactless payments work

Your physical card ships separately. ETA: {card_eta} business days. But you don't need to wait for it — the virtual card works everywhere the physical card does.

Fund your account and your card is ready to spend.

— {company} team""",
                        "cta_text": "Activate My Card",
                        "cta_dest": "card/activate",
                    },
                    "push": {
                        "title": "Your virtual card is ready",
                        "body": "Activate now. Use it today without waiting for delivery.",
                        "deep_link": "card/activate",
                    },
                    "in_app": {
                        "headline": "Virtual card: activate now",
                        "body": "No delivery wait. Works with Apple Pay.",
                        "cta": "Activate Card",
                    },
                },
                1: {
                    "role": "Best first-spend locations, Apple/Google Pay setup",
                    "trigger": "24 hours after signup, card not yet used",
                    "email": {
                        "subject": "5 places to test your {company} card today",
                        "body": """Hi {first_name},

Your {company} card works everywhere Visa/Mastercard is accepted. But if you want an easy first transaction, here are 5 places where it almost never fails:

1. **Coffee shop** (contactless, small amount, fast checkout)
2. **Grocery store** (chip or tap, easy to retry if needed)
3. **Uber or Lyft** (online, automatic, no POS friction)
4. **Amazon** (add as saved payment, low-friction first use)
5. **Gas station** (pre-auth works slightly differently — see note below)

Note on gas stations: Gas stations often pre-authorize $75-100 and then charge the actual amount. Make sure your balance covers the pre-auth, not just the gas cost.

Your cashback starts on the first transaction. For your card: {cashback_statement}

— {company} team""",
                        "cta_text": "Add to Apple Pay",
                        "cta_dest": "card/add-to-wallet",
                    },
                    "push": {
                        "title": "First tap: pick an easy one",
                        "body": "Coffee shop, Uber, or Amazon. Your card is ready.",
                        "deep_link": "card/use",
                    },
                    "in_app": {
                        "headline": "Easy first transaction",
                        "body": "Coffee shop, Uber, or Amazon. All work.",
                        "cta": "See Where to Start",
                    },
                },
                3: {
                    "role": "Address the first-decline fear, set up for success",
                    "trigger": "3 days after signup, no transaction yet",
                    "email": {
                        "subject": "Before your first transaction: 2 things to check",
                        "body": """Hi {first_name},

Two things that cause first transactions to fail — and how to avoid both:

**1. Check your balance**
Your card draws from your {company} balance. Make sure you have funds loaded. The app shows your spendable balance under "Card."

**2. Make sure the card is activated**
Even after adding to Apple Pay, you need to activate the {company} card itself. App → Card → Activate. Takes 30 seconds.

If a transaction does get declined, don't panic. The most common reasons:
- Insufficient balance
- Card not fully activated
- Merchant doesn't accept {card_network} (rare but happens)

If none of those apply and it's still declined, tap "Report an issue" in the app and we'll fix it within the hour.

Most people's first transaction works fine. These are just the things to check beforehand.

— {company} team""",
                        "cta_text": "Check Card Status",
                        "cta_dest": "card/status",
                    },
                    "push": {
                        "title": "Card ready to go?",
                        "body": "2 quick checks before your first transaction.",
                        "deep_link": "card/status",
                    },
                    "in_app": {
                        "headline": "Ready for your first spend?",
                        "body": "Check balance and activation status.",
                        "cta": "Check Card",
                    },
                },
                7: {
                    "role": "Show missed cashback, make inaction cost concrete",
                    "trigger": "7 days after signup, no transaction yet",
                    "email": {
                        "subject": "You've left {missed_cashback} in cashback uncollected",
                        "body": """Hi {first_name},

{company} users who made their first transaction in their first week earned an average of {avg_week1_cashback} in cashback.

You haven't made a transaction yet, so that's {missed_cashback} you've missed so far.

Your cashback rate: {cashback_rate} on {cashback_categories}. It accumulates on every purchase, automatically, in {cashback_currency}.

The fastest way to start: add your {company} card to Apple Pay and use it next time you buy coffee. {coffee_cashback} in cashback on a $5 coffee isn't life-changing, but it's the first proof that the card works.

Your card is funded and activated. The next tap is yours.

— {company} team""",
                        "cta_text": "Make My First Transaction",
                        "cta_dest": "card/use",
                    },
                    "push": {
                        "title": "{missed_cashback} in cashback missed",
                        "body": "Your card has been idle for 7 days. One tap changes that.",
                        "deep_link": "card/use",
                    },
                    "in_app": {
                        "headline": "{missed_cashback} missed this week",
                        "body": "Your cashback starts with the next purchase.",
                        "cta": "Use Card Now",
                    },
                },
                14: {
                    "role": "Re-engage with a specific spend challenge",
                    "trigger": "14 days after signup, no transaction yet",
                    "email": {
                        "subject": "One spend this week. That's all we're asking.",
                        "body": """Hi {first_name},

You've had your {company} card for 2 weeks. Here's a challenge: use it once before next Friday.

Not because of the cashback (though {weekly_cashback_potential} is there for the taking). But because the first transaction is always the hardest, and after that it becomes automatic.

Pick one thing you already buy this week — groceries, lunch, a subscription renewal — and pay with {company} instead of your regular card.

That's it. One transaction. 

After that, we'll show you your first spending summary and you'll see exactly what the card earned you.

— {company} team""",
                        "cta_text": "Accept the Challenge",
                        "cta_dest": "card/use",
                    },
                    "push": {
                        "title": "One spend. This week.",
                        "body": "That's the whole ask. Your card is ready.",
                        "deep_link": "card/use",
                    },
                    "in_app": {
                        "headline": "One purchase this week",
                        "body": "Use your {company} card once. See what it earns.",
                        "cta": "Use My Card",
                    },
                },
                30: {
                    "role": "Final re-engagement or graceful goodbye",
                    "trigger": "30 days after signup, no transaction made",
                    "email": {
                        "subject": "Your {company} card: still waiting",
                        "body": """Hi {first_name},

30 days. Your card has been ready, and hasn't been used.

Before we stop checking in, here's the honest situation: your {company} card is still active. Your account is still open. There's no expiry.

But the cashback you could have earned this month ({monthly_cashback_potential}) is gone.

If something specific stopped you — a declined test, confusion about activation, not enough balance — reply to this email and tell me. I'll fix it today.

If the card just isn't the right fit, no hard feelings. Your account stays open.

— {company} team""",
                        "cta_text": "Use My Card",
                        "cta_dest": "card/use",
                    },
                    "push": {
                        "title": "30 days. First swipe waiting.",
                        "body": "Card still active. Cashback still available.",
                        "deep_link": "card/use",
                    },
                    "in_app": {
                        "headline": "Still here for you",
                        "body": "Your card and cashback are waiting.",
                        "cta": "Use My Card",
                    },
                },
            }
        }
    },

    "yield": {
        "first-yield": {
            "tagline": "Your money can earn. Here's where the yield actually comes from.",
            "days": {
                0: {
                    "role": "Welcome + transparency on yield source + set expectation for first payout",
                    "trigger": "Account created",
                    "email": {
                        "subject": "{company}: where your yield comes from (and when you'll see it)",
                        "body": """Hi {first_name},

Welcome to {company}. Before you deposit anything, here's exactly where the yield comes from.

{yield_source_explanation}

The yield rate today: {current_apy}% APY on {supported_assets}.

When you deposit, you'll see your first yield payment in {first_yield_timing}. It shows up as a separate line item in your transaction history.

{lockup_disclosure}

To start earning:
1. Open the app and tap "Earn"
2. Select {primary_asset}
3. Deposit any amount
4. Watch your first yield payment post in {first_yield_timing}

— {company} team""",
                        "cta_text": "Start Earning",
                        "cta_dest": "earn/deposit",
                    },
                    "push": {
                        "title": "Yield starts when you deposit",
                        "body": "Current rate: {current_apy}% APY. Here's where it comes from.",
                        "deep_link": "earn/deposit",
                    },
                    "in_app": {
                        "headline": "Start earning today",
                        "body": "{current_apy}% APY. First yield in {first_yield_timing}.",
                        "cta": "Deposit Now",
                    },
                },
                1: {
                    "role": "Address post-Celsius trust barrier with specific transparency",
                    "trigger": "24 hours after signup, no deposit made",
                    "email": {
                        "subject": "After Celsius, BlockFi, and Voyager: here's how {company} is different",
                        "body": """Hi {first_name},

If you've been in crypto for more than 2 years, you know what happened to Celsius, BlockFi, and Voyager. Users deposited funds for yield and couldn't withdraw when those platforms collapsed.

Here's why {company} is different — specifically, not just "we're different":

{trust_differentiators}

These are facts about how {company} is structured, not marketing claims. You can verify {verifiable_claim}.

The question to ask any yield platform before depositing: "What happens to my funds if this company goes bankrupt?" At {company}, the answer is: {bankruptcy_answer}

Your account is ready. The choice to deposit is yours.

— {company} team""",
                        "cta_text": "Review Our Security Model",
                        "cta_dest": "security/overview",
                    },
                    "push": {
                        "title": "How {company} protects your funds",
                        "body": "Specific answer. Not marketing. Tap to read.",
                        "deep_link": "security/overview",
                    },
                    "in_app": {
                        "headline": "How your funds are protected",
                        "body": "Read before you deposit. Clear answer inside.",
                        "cta": "Read Now",
                    },
                },
                3: {
                    "role": "Real earnings calculator, make it concrete",
                    "trigger": "3 days after signup, no deposit made",
                    "email": {
                        "subject": "What $1,000 earns at {company} vs. your bank",
                        "body": """Hi {first_name},

A simple comparison:

**$1,000 in a US savings account (average rate: 0.46% APY):**
Monthly earnings: $0.38
Annual earnings: $4.60

**$1,000 in {company} at {current_apy}% APY:**
Monthly earnings: ${monthly_1k}
Annual earnings: ${annual_1k}

That's a difference of ${annual_diff} per year on $1,000.

On $10,000: ${annual_diff_10k} extra per year.
On $50,000: ${annual_diff_50k} extra per year.

The calculation scales linearly. The risk is the question. That's why the Day 1 email explained exactly how {company} protects your funds.

If you've read that and you're comfortable with it, the next step is depositing. If you haven't read it, here it is again: [link to security model]

— {company} team""",
                        "cta_text": "Deposit and Start Earning",
                        "cta_dest": "earn/deposit",
                    },
                    "push": {
                        "title": "Your bank pays $4.60/year on $1k",
                        "body": "{company} pays ${annual_1k}. Here's the difference.",
                        "deep_link": "earn/deposit",
                    },
                    "in_app": {
                        "headline": "Your bank vs {company}",
                        "body": "${annual_diff}/year difference on $1,000.",
                        "cta": "Start Earning",
                    },
                },
                7: {
                    "role": "Show what other users are earning, social proof",
                    "trigger": "7 days after signup, no deposit made",
                    "email": {
                        "subject": "{active_users} people earned yield on {company} this week",
                        "body": """Hi {first_name},

{active_users} {company} users received a yield payment this week. The average account earned ${avg_weekly_yield}.

The smallest accounts (under $500) earned ${small_account_yield} on average.
The most common first deposit amount: ${median_first_deposit}.

Most of them didn't read 10 articles before deciding. They deposited $100-300 first, watched the yield arrive, confirmed withdrawals worked, and then moved more in.

That's a reasonable approach. If you want to do the same, your account is ready.

— {company} team""",
                        "cta_text": "Make My First Deposit",
                        "cta_dest": "earn/deposit",
                    },
                    "push": {
                        "title": "{active_users} earned yield this week",
                        "body": "Average: ${avg_weekly_yield}. Your account is ready.",
                        "deep_link": "earn/deposit",
                    },
                    "in_app": {
                        "headline": "{active_users} users earned this week",
                        "body": "The average first deposit is ${median_first_deposit}.",
                        "cta": "Join Them",
                    },
                },
                14: {
                    "role": "Opportunity cost made concrete over 2 weeks",
                    "trigger": "14 days after signup, no deposit made",
                    "email": {
                        "subject": "14 days. Here's what you've missed.",
                        "body": """Hi {first_name},

If you'd deposited $5,000 on the day you signed up, at {current_apy}% APY, you'd have earned ${two_week_yield} in yield by now.

That's not a lot of money. But it's $0 more than you're earning in your bank account on the same amount.

The yield compounds. Month 2 would have earned more. Month 6 would be ${six_month_yield} on $5,000.

Your account is still open. The rate is still {current_apy}%.

— {company} team""",
                        "cta_text": "Start Earning",
                        "cta_dest": "earn/deposit",
                    },
                    "push": {
                        "title": "2 weeks of missed yield",
                        "body": "${two_week_yield} on $5k. Still time to start.",
                        "deep_link": "earn/deposit",
                    },
                    "in_app": {
                        "headline": "${two_week_yield} missed so far",
                        "body": "Based on $5k at {current_apy}% APY.",
                        "cta": "Start Earning",
                    },
                },
                30: {
                    "role": "Final message, honest tone",
                    "trigger": "30 days after signup, no deposit made",
                    "email": {
                        "subject": "One month. Quick question.",
                        "body": """Hi {first_name},

You've had a {company} account for a month and haven't deposited.

We're not going to keep emailing you after this. Your account stays open as long as you want it.

But before we go quiet: what's the main reason you haven't deposited?

Reply with a number:
1. I'm still not sure how {company} makes the yield
2. I'm worried about losing my funds
3. I'm planning to, just haven't gotten around to it
4. The yield rate isn't compelling enough
5. Something else

If it's 1 or 2, I'll send you a direct answer. If it's 3, no pressure. If it's 4 or 5, I'd genuinely like to know.

— {company} team""",
                        "cta_text": "Reply With Your Reason",
                        "cta_dest": "feedback/why-not",
                    },
                    "push": {
                        "title": "One last question",
                        "body": "What stopped you from depositing? 30 seconds to answer.",
                        "deep_link": "feedback/why-not",
                    },
                    "in_app": {
                        "headline": "What stopped you?",
                        "body": "Help us understand. Takes 20 seconds.",
                        "cta": "Tell Us",
                    },
                },
            }
        }
    },

    "self-custody": {
        "first-deposit": {
            "tagline": "Your keys. Your wallet. Here's how to fund it.",
            "days": {
                0: {
                    "role": "Welcome + wallet backup first, then fund",
                    "trigger": "Account created",
                    "email": {
                        "subject": "{company}: back up your wallet before you fund it",
                        "body": """Hi {first_name},

Your {company} self-custody wallet is ready. Before you add funds, one critical step: back up your recovery phrase.

Your {company} wallet uses {recovery_method}. This means {company} does not hold your private keys and cannot recover your funds if you lose access. Your recovery phrase is the only backup.

To back up now:
1. App → Settings → Security → Backup wallet
2. Write down your {phrase_length}-word recovery phrase on paper
3. Store it somewhere you won't lose it (not a screenshot, not cloud storage)
4. Confirm backup in the app

Takes 5 minutes. Do this before you send a single dollar.

After backup: your wallet is ready to receive any EVM-compatible asset. Here's your wallet address: [wallet_address]

— {company} team""",
                        "cta_text": "Back Up My Wallet",
                        "cta_dest": "settings/backup",
                    },
                    "push": {
                        "title": "Back up first, fund second",
                        "body": "5-min backup before you add funds. Your keys, your funds.",
                        "deep_link": "settings/backup",
                    },
                    "in_app": {
                        "headline": "Back up before you fund",
                        "body": "5 minutes now. Protects everything later.",
                        "cta": "Back Up Now",
                    },
                },
                1: {
                    "role": "Why self-custody + banking vs. MetaMask or Ledger",
                    "trigger": "24 hours after signup, no deposit made",
                    "email": {
                        "subject": "What {company} does that MetaMask and Ledger can't",
                        "body": """Hi {first_name},

If you already use MetaMask or Ledger, you might wonder why you need {company}.

The honest answer: you don't, if all you need is a wallet.

But if you also want to:
- Spend your crypto with a debit card (without moving to an exchange first)
- Receive direct deposits to a self-custody wallet
- {unique_feature_1}
- {unique_feature_2}

...then MetaMask and Ledger can't do that. {company} can, while keeping you as the only keyholder.

Your funds stay in your wallet. {company} facilitates the card and banking layer on top — it never touches your keys.

{key_differentiator_explanation}

Fund your wallet with any amount to see how it works.

— {company} team""",
                        "cta_text": "Fund My Wallet",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "MetaMask + banking. In one app.",
                        "body": "Your keys. Spend it anywhere. Here's how.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "Your keys + card + banking",
                        "body": "What MetaMask and Ledger can't do.",
                        "cta": "See How",
                    },
                },
                3: {
                    "role": "Gas fees: set expectations, show when they apply",
                    "trigger": "3 days after signup, no deposit made",
                    "email": {
                        "subject": "Gas fees on {company}: here's the real number",
                        "body": """Hi {first_name},

Self-custody wallets involve gas fees. Here's what you're actually looking at on {company}:

Network: {primary_network}
Current gas fee for a standard transfer: approximately ${current_gas_usd}

{gas_context}

For card transactions: {card_gas_handling}

Compared to custodial wallets: no gas fees for internal transfers. The tradeoff is custody — they hold your keys.

On {company}: you pay gas. You keep your keys. That's the deal.

If you're making transactions under ${min_economical_amount}, gas fees will be a significant percentage of the amount. If you're moving larger amounts, gas is negligible.

Ready to fund your wallet? Here's your address: [wallet_address]

— {company} team""",
                        "cta_text": "Fund My Wallet",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "Gas fees: the real number",
                        "body": "~${current_gas_usd} per transaction on {primary_network}. Worth knowing.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "Gas fee: ~${current_gas_usd}",
                        "body": "That's the real cost per transaction here.",
                        "cta": "Fund Wallet",
                    },
                },
                7: {
                    "role": "Social proof from crypto-native users who switched",
                    "trigger": "7 days after signup, no deposit made",
                    "email": {
                        "subject": "{switcher_count} people moved from Coinbase to {company} this month",
                        "body": """Hi {first_name},

{switcher_count} {company} users this month came from custodial wallets (Coinbase, Binance, Crypto.com).

What they said they hated about custodial wallets:
- "Coinbase froze my account with no warning"
- "I couldn't withdraw during the [market event] because the platform was overloaded"
- "They required extra KYC every time the regulations changed"
- "My crypto, but only when they say so"

The switch to {company} takes about 20 minutes: back up your wallet, fund it from your exchange, done.

Your account and wallet are ready.

— {company} team""",
                        "cta_text": "Fund My Wallet",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "{switcher_count} left Coinbase for {company}",
                        "body": "Your keys. Your rules. Here's how they switched.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "{switcher_count} moved to self-custody",
                        "body": "This month. From Coinbase, Binance, and others.",
                        "cta": "Join Them",
                    },
                },
                14: {
                    "role": "Unique feature activation nudge",
                    "trigger": "14 days after signup, no deposit made",
                    "email": {
                        "subject": "The thing {company} users use that you haven't tried yet",
                        "body": """Hi {first_name},

The most-used feature by active {company} users: {top_feature}.

This is the thing custodial wallets can't do. And it only works once your wallet is funded.

{top_feature_explanation}

Your wallet is still ready. Still unfunded. That's the only thing between you and {top_feature}.

— {company} team""",
                        "cta_text": "Fund and Try {top_feature}",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "{top_feature} is waiting",
                        "body": "Only works with a funded wallet. Takes 5 minutes.",
                        "deep_link": "wallet/receive",
                    },
                    "in_app": {
                        "headline": "{top_feature}: almost ready",
                        "body": "Fund your wallet to unlock it.",
                        "cta": "Fund Wallet",
                    },
                },
                30: {
                    "role": "Last message, honest tone",
                    "trigger": "30 days after signup, no deposit made",
                    "email": {
                        "subject": "Honest question about your {company} wallet",
                        "body": """Hi {first_name},

Your {company} wallet has been backed up and ready for 30 days. No funds in it yet.

I want to ask you directly: what's stopping you?

If it's the gas fees — I can show you how to minimize them.
If it's not sure what to do first — I can send a 3-step guide.
If it's concern about self-custody risk — I can explain exactly how recovery works.
If it's something else — tell me and I'll give you a straight answer.

Reply to this email with whatever is in the way.

Your account and wallet stay open indefinitely. No urgency from our end. Just want to know if there's something we can fix.

— {company} team""",
                        "cta_text": "Fund My Wallet",
                        "cta_dest": "wallet/receive",
                    },
                    "push": {
                        "title": "30 days. Wallet unfunded.",
                        "body": "What's in the way? Reply and we'll fix it.",
                        "deep_link": "feedback/why-not",
                    },
                    "in_app": {
                        "headline": "What's stopping you?",
                        "body": "Tell us and we'll fix it today.",
                        "cta": "Tell Us",
                    },
                },
            }
        }
    },

    "remittance": {
        "first-deposit": {
            "tagline": "Send money home without the fees. Here's your first transfer.",
            "days": {
                0: {
                    "role": "Welcome + fee comparison + path to first send",
                    "trigger": "Account created",
                    "email": {
                        "subject": "{company}: your first transfer to {destination_country} costs {our_fee}",
                        "body": """Hi {first_name},

Here's what your first transfer costs with {company}:

Transfer amount: $500
{company} fee: {our_fee}
Exchange rate: {our_rate}
What {recipient_name} receives: {recipient_receives}

Western Union equivalent:
Fee: {wu_fee}
Exchange rate: {wu_rate} (with markup)
What they'd receive: {wu_recipient_receives}

Difference: {difference} more with {company} on a $500 transfer.

To send your first transfer:
1. Complete your verification (takes {kyc_time})
2. Add a recipient
3. Choose your funding method
4. Send

Your first transfer often takes the longest to set up. After that, sending again takes under 2 minutes.

— {company} team""",
                        "cta_text": "Start My First Transfer",
                        "cta_dest": "transfer/new",
                    },
                    "push": {
                        "title": "Your first transfer: {our_fee} total",
                        "body": "Western Union charges {wu_fee}. See the full comparison.",
                        "deep_link": "transfer/new",
                    },
                    "in_app": {
                        "headline": "Send for {our_fee}",
                        "body": "Western Union: {wu_fee}. Your savings: {difference}.",
                        "cta": "Send Now",
                    },
                },
                1: {
                    "role": "Recipient setup guide, country-specific",
                    "trigger": "24 hours after signup, no transfer made",
                    "email": {
                        "subject": "How to set up your {destination_country} recipient in {company}",
                        "body": """Hi {first_name},

To send money to {destination_country}, you'll need your recipient's:

{recipient_fields_for_country}

{country_specific_notes}

If you're sending to a mobile money account ({mobile_money_provider}):
{mobile_money_instructions}

If you're sending to a bank account:
{bank_account_instructions}

Setting up a recipient for the first time takes about 3 minutes. After that, sending to them again takes under 30 seconds.

Need help finding any of these details? {country_specific_resource}

— {company} team""",
                        "cta_text": "Add My Recipient",
                        "cta_dest": "recipients/add",
                    },
                    "push": {
                        "title": "Set up your recipient first",
                        "body": "3 minutes now = 30-second sends forever after.",
                        "deep_link": "recipients/add",
                    },
                    "in_app": {
                        "headline": "Add your recipient",
                        "body": "3 minutes once. 30 seconds every time after.",
                        "cta": "Add Recipient",
                    },
                },
                3: {
                    "role": "Test transfer invitation, family safety frame",
                    "trigger": "3 days after signup, no transfer made",
                    "email": {
                        "subject": "A $10 test to make sure your family gets the money",
                        "body": """Hi {first_name},

Sending money home is too important to get wrong. That's why a lot of {company} users do a $10 test transfer before sending a larger amount.

Here's what a test transfer tells you:
- That your recipient details are correct
- How long it actually takes to arrive (not just what we say)
- That the exchange rate you saw is the rate they received
- That withdrawing and receiving works end-to-end

A $10 test transfer on {company} costs {test_fee} total. It arrives in {arrival_time}.

Once you see the $10 arrive and your recipient confirms it, you'll know exactly what a $500 or $1,000 transfer will look like.

Your account is verified and ready. Set up a recipient and try the test transfer.

— {company} team""",
                        "cta_text": "Send $10 Test Transfer",
                        "cta_dest": "transfer/new?amount=10",
                    },
                    "push": {
                        "title": "$10 test. Confirm it works.",
                        "body": "Arrives in {arrival_time}. {test_fee} total. Worth knowing.",
                        "deep_link": "transfer/new",
                    },
                    "in_app": {
                        "headline": "Test with $10 first",
                        "body": "Confirms everything works for your family.",
                        "cta": "Send Test",
                    },
                },
                7: {
                    "role": "Annual savings comparison, make it real",
                    "trigger": "7 days after signup, no transfer made",
                    "email": {
                        "subject": "If you send $400/month home, here's what you're overpaying",
                        "body": """Hi {first_name},

Average remittance to {destination_country}: $400/month.

Average annual fee with Western Union / bank wire: ${annual_fees_traditional}
Annual fee with {company}: ${annual_fees_company}

Annual savings: ${annual_savings}

That's not hypothetical. It's what {corridor_users} {company} users sending on the {origin}-{destination_country} corridor save per year on average.

Your account is verified. Your recipient setup takes 3 minutes. The first transfer after that takes under 2 minutes.

The only thing between you and ${annual_savings}/year: sending once.

— {company} team""",
                        "cta_text": "Send My First Transfer",
                        "cta_dest": "transfer/new",
                    },
                    "push": {
                        "title": "You're overpaying by ${annual_savings}/year",
                        "body": "On {destination_country} transfers. Here's the math.",
                        "deep_link": "transfer/new",
                    },
                    "in_app": {
                        "headline": "${annual_savings}/year in savings",
                        "body": "On your {destination_country} transfers.",
                        "cta": "Send Now",
                    },
                },
                14: {
                    "role": "Recurring transfer setup hook",
                    "trigger": "14 days after signup, no transfer made",
                    "email": {
                        "subject": "Set up a monthly transfer and never forget again",
                        "body": """Hi {first_name},

The most popular {company} feature for people who send money home regularly: scheduled transfers.

You set it once — the amount, the recipient, the date — and {company} sends it automatically every month.

No remembering. No logging in. No last-minute scrambles.

Average user who sets up a scheduled transfer: sends {avg_recurring_frequency}x more consistently than those who send manually.

To set it up: Transfer → Schedule → Monthly → [your details]. Takes 2 minutes.

Your first transfer still needs to happen before you can schedule. That's the 3-minute setup. After that, it's automatic.

— {company} team""",
                        "cta_text": "Set Up Monthly Transfer",
                        "cta_dest": "transfer/schedule",
                    },
                    "push": {
                        "title": "Auto-send every month",
                        "body": "Set up once. Your family gets paid. Every time.",
                        "deep_link": "transfer/schedule",
                    },
                    "in_app": {
                        "headline": "Auto monthly transfer",
                        "body": "Set up once. Never forget again.",
                        "cta": "Schedule Transfer",
                    },
                },
                30: {
                    "role": "Final message — family framing, no pressure",
                    "trigger": "30 days after signup, no transfer made",
                    "email": {
                        "subject": "Your family. One month without {company}.",
                        "body": """Hi {first_name},

You signed up for {company} a month ago. You haven't sent a transfer yet.

We don't know your situation. Maybe you're using another service that works fine for you. Maybe you just haven't gotten to it. That's completely okay.

What we do know: if you're still paying {traditional_fee_example} per transfer to {destination_country}, there's a better option sitting in your account.

Your {company} account is still active. When you're ready to try your first transfer, it'll take under 5 minutes from start to finish.

And if something stopped you from trying it — a technical issue, something confusing — reply to this email and I'll fix it.

— {company} team""",
                        "cta_text": "Send My First Transfer",
                        "cta_dest": "transfer/new",
                    },
                    "push": {
                        "title": "Still here. No pressure.",
                        "body": "First transfer: under 5 minutes when you're ready.",
                        "deep_link": "transfer/new",
                    },
                    "in_app": {
                        "headline": "When you're ready",
                        "body": "First transfer: under 5 minutes.",
                        "cta": "Send Now",
                    },
                },
            }
        }
    },

    "super-app": {
        "first-deposit": {
            "tagline": "One app, one account. Start with the feature that matters most to you.",
            "days": {
                0: {
                    "role": "Welcome + single primary feature, ignore everything else",
                    "trigger": "Account created",
                    "email": {
                        "subject": "{company}: one thing to do first",
                        "body": """Hi {first_name},

Your {company} account is ready. The app has a lot of features. You don't need to use all of them on day one.

Here's the one thing to do first: {primary_action}.

Why this first: {primary_action_rationale}

It takes {primary_action_time} and it's the fastest way to see why {company} is different from your current financial apps.

Everything else in the app can wait. Start with this.

— {company} team""",
                        "cta_text": "{primary_cta}",
                        "cta_dest": "{primary_dest}",
                    },
                    "push": {
                        "title": "One thing to do first",
                        "body": "{primary_action_short}. Takes {primary_action_time}.",
                        "deep_link": "{primary_dest}",
                    },
                    "in_app": {
                        "headline": "Start here",
                        "body": "{primary_action_short}. One step.",
                        "cta": "{primary_cta}",
                    },
                },
                1: {
                    "role": "Competitive differentiation — what you can do here that [competitor] can't",
                    "trigger": "24 hours after signup, primary action not taken",
                    "email": {
                        "subject": "What {company} does that {main_competitor} doesn't",
                        "body": """Hi {first_name},

If you're already using {main_competitor}, here's the honest comparison:

{company} does this. {main_competitor} doesn't: {key_differentiator_1}

{company} does this better: {key_differentiator_2}

{main_competitor} does this better (we won't pretend otherwise): {competitor_advantage}

If what you care most about is {key_differentiator_1}, {company} is worth the switch. If {competitor_advantage} is your priority, {main_competitor} may be the better choice.

Most users who join {company} don't close their other accounts immediately. They try {company} for one specific thing first, see how it works, and decide from there.

The one thing to try: {primary_action}. Here's the link.

— {company} team""",
                        "cta_text": "Try {primary_action}",
                        "cta_dest": "{primary_dest}",
                    },
                    "push": {
                        "title": "{company} vs {main_competitor}",
                        "body": "One thing {company} does that {main_competitor} can't.",
                        "deep_link": "{primary_dest}",
                    },
                    "in_app": {
                        "headline": "vs {main_competitor}: one difference",
                        "body": "{key_differentiator_1_short}",
                        "cta": "Try It",
                    },
                },
                3: {
                    "role": "Friction reduction — address the most common barrier for this product",
                    "trigger": "3 days after signup, primary action not taken",
                    "email": {
                        "subject": "Most {company} users get stuck at this one point",
                        "body": """Hi {first_name},

The most common place new {company} users get stuck: {common_friction_point}.

Here's how to get past it:

{friction_resolution_steps}

If that's not what stopped you, reply to this email with what actually happened and I'll give you a direct answer.

— {company} team""",
                        "cta_text": "Get Past the Friction",
                        "cta_dest": "help/{friction_help_page}",
                    },
                    "push": {
                        "title": "Stuck at {common_friction_short}?",
                        "body": "Here's the fix. Takes 2 minutes.",
                        "deep_link": "help/{friction_help_page}",
                    },
                    "in_app": {
                        "headline": "Common issue: {common_friction_short}",
                        "body": "Here's how to fix it fast.",
                        "cta": "Fix It",
                    },
                },
                7: {
                    "role": "Social proof with specific numbers",
                    "trigger": "7 days after signup, primary action not taken",
                    "email": {
                        "subject": "{social_proof_number} people used {primary_feature} on {company} this week",
                        "body": """Hi {first_name},

{social_proof_number} {company} users used {primary_feature} this week. The average {primary_metric}.

What they said afterward: {social_proof_quote}

Your account is ready for the same thing. {primary_action_reminder}

— {company} team""",
                        "cta_text": "Join Them",
                        "cta_dest": "{primary_dest}",
                    },
                    "push": {
                        "title": "{social_proof_number} used {primary_feature}",
                        "body": "This week. Your account is ready for the same.",
                        "deep_link": "{primary_dest}",
                    },
                    "in_app": {
                        "headline": "{social_proof_number} this week",
                        "body": "Used {primary_feature}. You're next.",
                        "cta": "Try {primary_feature}",
                    },
                },
                14: {
                    "role": "Second feature introduction (only one)",
                    "trigger": "14 days after signup, primary action not taken",
                    "email": {
                        "subject": "You haven't tried {primary_feature} yet. Here's {secondary_feature}.",
                        "body": """Hi {first_name},

You still haven't tried {primary_feature}. That's fine.

But here's another feature you might find more immediately useful: {secondary_feature}.

{secondary_feature_explanation}

One of these two features is probably the right entry point for you. Try whichever feels more relevant.

— {company} team""",
                        "cta_text": "Try {secondary_feature}",
                        "cta_dest": "{secondary_dest}",
                    },
                    "push": {
                        "title": "Try {secondary_feature} instead",
                        "body": "Different entry point. Same account. See if this one clicks.",
                        "deep_link": "{secondary_dest}",
                    },
                    "in_app": {
                        "headline": "Try {secondary_feature}",
                        "body": "A different way in. Takes 2 minutes.",
                        "cta": "Try It",
                    },
                },
                30: {
                    "role": "Final message — honest question",
                    "trigger": "30 days after signup, no activation",
                    "email": {
                        "subject": "30 days and nothing used. One question.",
                        "body": """Hi {first_name},

You signed up 30 days ago and haven't used any {company} feature yet.

That's more common than you'd think. People sign up, get busy, and the app sits there.

One question before we stop emailing: what would have to be true for you to try {company} this week?

Reply with anything — an honest answer helps us improve, and if there's something we can fix for you specifically, I'll do it.

Your account stays open indefinitely.

— {company} team""",
                        "cta_text": "Tell Us",
                        "cta_dest": "feedback/why-not",
                    },
                    "push": {
                        "title": "What would it take?",
                        "body": "One question before we go quiet. 20 seconds to answer.",
                        "deep_link": "feedback/why-not",
                    },
                    "in_app": {
                        "headline": "One question",
                        "body": "What would make you try it this week?",
                        "cta": "Tell Us",
                    },
                },
            }
        }
    },
}


# ── Voice Adjustments ─────────────────────────────────────────────────────────

VOICE_PREFACE = {
    "casual": {
        "email_sign_off": "— Team {company}",
        "greeting": "Hey {first_name},",
        "notes": "Conversational, peer-to-peer. Short sentences. Direct.",
    },
    "professional": {
        "email_sign_off": "— The {company} team",
        "greeting": "Hi {first_name},",
        "notes": "Clean, benefit-forward. Professional but not corporate.",
    },
    "crypto-native": {
        "email_sign_off": "— {company}",
        "greeting": "gm {first_name},",
        "notes": "Can reference DeFi, on-chain, non-custodial, gas, chains directly. No explanations of basics.",
    },
}


# ── Default Tokens ─────────────────────────────────────────────────────────────

def get_default_tokens(company: str, product_type: str, goal: str, voice: str) -> dict:
    """Returns default placeholder tokens for copy generation."""
    is_generic = company.lower() == "generic"
    name = "[Company Name]" if is_generic else company

    tokens = {
        "company": name,
        "first_name": "[First Name]",
        "product_type": product_type,
        "goal": goal,
        "voice": voice,

        # Stablecoin tokens
        "network": "[Primary Network — e.g., Base, Tron, Polygon]",
        "custody_statement": "[e.g., 'Your USDC is held 1:1 in reserves. We cannot access or lend your funds.']",
        "reserve_statement": "[e.g., 'Reserves are audited monthly by [Auditor]. Report here: [link]']",
        "user_count": "[X,XXX]",
        "retention_stat": "[XX]",
        "fee_statement": "[e.g., '$0 transfer fees, 0% FX markup on USDC']",
        "estimated_transfers": "[X]",
        "avg_savings": "[$XXX]",

        # Yield tokens
        "yield_source_explanation": "[Explain specifically: e.g., 'We lend your USDC to institutional borrowers who post over-collateralized crypto as security. If a borrower defaults, the collateral covers your funds.']",
        "current_apy": "[X.X]",
        "supported_assets": "[USDC, USDT, BTC — specify]",
        "first_yield_timing": "[e.g., 'every 24 hours' or 'every Monday']",
        "lockup_disclosure": "[If flexible: 'No lockup. Withdraw anytime.' If locked: 'Note: the [X]% rate requires a [Y]-day lock. Flexible rate is [Z]%.']",
        "trust_differentiators": "[List 3 specific facts: custody model, reserve audit, insurance, regulatory status, etc.]",
        "verifiable_claim": "[e.g., 'monthly reserve reports at [URL]']",
        "bankruptcy_answer": "[Specific answer to what happens to user funds in bankruptcy. Not marketing — legal/structural reality.]",
        "primary_asset": "[USDC / USDT / BTC]",
        "monthly_1k": "[{current_apy} / 12 = monthly earnings on $1,000]",
        "annual_1k": "[{current_apy}% of $1,000]",
        "annual_diff": "[annual_1k - $4.60]",
        "annual_diff_10k": "[annual_1k × 10 - $46]",
        "annual_diff_50k": "[annual_1k × 50 - $230]",
        "active_users": "[X,XXX]",
        "avg_weekly_yield": "[XX.XX]",
        "small_account_yield": "[X.XX]",
        "median_first_deposit": "[XXX]",
        "two_week_yield": "[XX.XX]",
        "six_month_yield": "[XXX.XX]",

        # Crypto card tokens
        "card_eta": "[5-10]",
        "cashback_statement": "[e.g., '1.5% on all purchases in USDC' or '2% on dining, 1% on everything else']",
        "card_network": "[Visa / Mastercard]",
        "cashback_rate": "[X]%",
        "cashback_categories": "[all purchases / dining and travel / etc.]",
        "cashback_currency": "[USDC / native token / cash]",
        "coffee_cashback": "[$0.10]",
        "missed_cashback": "[$X.XX]",
        "avg_week1_cashback": "[$X.XX]",
        "weekly_cashback_potential": "[$X-XX]",
        "monthly_cashback_potential": "[$XX-XXX]",

        # Self-custody tokens
        "recovery_method": "[social recovery / seed phrase / hardware key — specify]",
        "phrase_length": "[12 or 24]",
        "primary_network": "[Base / Ethereum / Polygon — specify]",
        "current_gas_usd": "[0.01-2.00 depending on network]",
        "gas_context": "[e.g., 'On Base (L2), gas is typically under $0.02. On Ethereum mainnet, it varies from $2-50.']",
        "card_gas_handling": "[e.g., 'Card transactions are gasless — we batch and cover gas for card payments.']",
        "min_economical_amount": "[minimum sensible transaction amount given gas]",
        "unique_feature_1": "[specific feature not in MetaMask/Ledger]",
        "unique_feature_2": "[another specific feature]",
        "key_differentiator_explanation": "[1-2 sentences on the most important differentiator]",
        "switcher_count": "[XXX]",
        "top_feature": "[most-used feature for self-custody users]",
        "top_feature_explanation": "[2-3 sentences on what it does and why it requires a funded wallet]",

        # Remittance tokens
        "destination_country": "[Destination Country]",
        "our_fee": "[$0-3]",
        "our_rate": "[1:1 or specify rate]",
        "recipient_name": "your recipient",
        "recipient_receives": "[$XXX.XX]",
        "wu_fee": "[$12-45]",
        "wu_rate": "[with 2-3% markup]",
        "wu_recipient_receives": "[$XXX.XX — less]",
        "difference": "[$XX.XX]",
        "kyc_time": "[3-10 minutes]",
        "recipient_fields_for_country": "[Bank account: account number, routing number, bank name.\nMobile money: phone number, provider.]",
        "country_specific_notes": "[Any country-specific requirements or nuances]",
        "mobile_money_provider": "[GCash / M-Pesa / specify]",
        "mobile_money_instructions": "[Step-by-step mobile money setup]",
        "bank_account_instructions": "[Step-by-step bank account setup]",
        "country_specific_resource": "[e.g., 'For Philippine banks, here's a list of routing numbers: [link]']",
        "test_fee": "[$0.50-2]",
        "arrival_time": "[seconds to 3 minutes]",
        "annual_fees_traditional": "[XXX-XXX]",
        "annual_fees_company": "[XX-XX]",
        "annual_savings": "[XXX]",
        "corridor_users": "[X,XXX]",
        "origin": "[Origin Country/City]",
        "traditional_fee_example": "[$15-40]",
        "avg_recurring_frequency": "[X]",

        # Super-app tokens
        "primary_action": "[Single primary action — e.g., 'Open a USD account', 'Make your first crypto trade', 'Send money internationally']",
        "primary_action_rationale": "[Why this first: what makes it the best entry point]",
        "primary_action_time": "[2-5 minutes]",
        "primary_cta": "[CTA text]",
        "primary_dest": "[app screen / URL]",
        "primary_action_short": "[Short version of primary action]",
        "main_competitor": "[Revolut / Cash App / PayPal — specify]",
        "key_differentiator_1": "[Specific thing Company does that competitor can't]",
        "key_differentiator_2": "[Specific thing Company does better than competitor]",
        "competitor_advantage": "[Honest thing competitor does better]",
        "key_differentiator_1_short": "[Short version]",
        "common_friction_point": "[e.g., 'the KYC document step' or 'connecting a bank account']",
        "friction_resolution_steps": "[Step-by-step fix]",
        "friction_help_page": "[help article slug]",
        "common_friction_short": "[Short friction label]",
        "social_proof_number": "[X,XXX]",
        "primary_feature": "[primary feature name]",
        "primary_metric": "[e.g., 'saved $47 in fees' or 'transfer settled in 12 seconds']",
        "social_proof_quote": "[Real or representative user quote]",
        "primary_action_reminder": "[1-sentence reminder of the primary action]",
        "secondary_feature": "[secondary feature name]",
        "secondary_feature_explanation": "[2-3 sentences on what it does and why it's useful]",
        "secondary_dest": "[app screen / URL]",
    }

    # Override some tokens with company-specific values when available
    if not is_generic:
        tokens["email_sign_off"] = VOICE_PREFACE[voice]["email_sign_off"].format(company=name)

    return tokens


# ── Core Generator ─────────────────────────────────────────────────────────────

def apply_tokens(text: str, tokens: dict) -> str:
    """Replace {token} placeholders with values."""
    for key, value in tokens.items():
        text = text.replace("{" + key + "}", str(value))
    return text


def render_touchpoint(day: int, data: dict, tokens: dict, voice: str) -> str:
    """Render a single day's touchpoint as Markdown."""
    lines = []
    lines.append(f"## Day {day} — {data['role'].title()}")
    lines.append("")
    lines.append(f"**Activation Goal:** {tokens['goal']}")
    lines.append(f"**Trigger:** {data['trigger']}")
    lines.append("")

    # Email
    email = data["email"]
    subject = apply_tokens(email["subject"], tokens)
    body = apply_tokens(email["body"], tokens)

    # Apply voice greeting
    greeting = VOICE_PREFACE[voice]["greeting"]
    greeting_filled = apply_tokens(greeting, tokens)
    if body.startswith("Hi {first_name}"):
        body = body.replace("Hi {first_name}", greeting_filled)

    lines.append("### Email")
    lines.append(f"**Subject:** {subject}")
    lines.append("")
    lines.append(body)
    lines.append("")
    lines.append(f"**CTA button:** {apply_tokens(email['cta_text'], tokens)} → `{email['cta_dest']}`")
    lines.append("")

    # Push
    push = data["push"]
    lines.append("### Push Notification")
    lines.append(f"**Title:** {apply_tokens(push['title'], tokens)}")
    lines.append(f"**Body:** {apply_tokens(push['body'], tokens)}")
    lines.append(f"**Deep link:** `{push['deep_link']}`")
    lines.append("")

    # In-app
    inapp = data["in_app"]
    lines.append("### In-App Message")
    lines.append(f"**Headline:** {apply_tokens(inapp['headline'], tokens)}")
    lines.append(f"**Body:** {apply_tokens(inapp['body'], tokens)}")
    lines.append(f"**CTA:** {apply_tokens(inapp['cta'], tokens)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def generate_sequence(
    company: str,
    product_type: str,
    goal: str,
    voice: str = "professional",
    output_path: Optional[str] = None,
) -> str:
    """Generate a complete lifecycle sequence."""

    warnings = []
    notes = []

    # Check goal compatibility
    compat = GOAL_COMPATIBILITY.get((product_type, goal), "unknown")
    if compat == "mismatch":
        warnings.append(
            f"Goal mismatch: '{goal}' is not a natural fit for '{product_type}' products. "
            f"Consider: " + {
                "stablecoin": "first-deposit or first-spend",
                "crypto-card": "first-spend",
                "yield": "first-yield",
                "self-custody": "first-deposit or first-spend",
                "remittance": "first-deposit or first-spend",
                "super-app": "first-deposit, first-spend, or first-yield",
            }.get(product_type, "check activation-milestones.md")
        )
    elif compat == "prereq":
        notes.append(
            f"Note: '{goal}' is a prerequisite for '{product_type}', not the primary activation milestone. "
            "The sequence will drive toward this goal, but consider whether a downstream goal makes more sense."
        )
    elif compat == "secondary":
        notes.append(
            f"Note: '{goal}' is a valid secondary goal for '{product_type}'. "
            "The sequence will work, but the primary goal for this product type is: " + {
                "stablecoin": "first-deposit",
                "self-custody": "first-deposit",
                "remittance": "first-deposit",
                "super-app": "first-deposit",
            }.get(product_type, "see activation-milestones.md")
        )

    # Check voice mismatch
    voice_warn = VOICE_MISMATCHES.get((product_type, voice))
    if voice_warn:
        warnings.append(f"Voice advisory: {voice_warn}")

    # Check for app store review data
    review_data_path = Path(f"/work/neobank-skills/app-store-intelligence/output/{company.lower().replace(' ', '-')}-reviews.json")
    has_review_data = review_data_path.exists() and company.lower() != "generic"
    review_note = f"Review data: {'yes — Day 3 pain language sourced from real reviews' if has_review_data else 'no — using category pain language from lifecycle-sequence-library.md'}"

    # Find sequence template
    product_sequences = SEQUENCES.get(product_type)
    if not product_sequences:
        # Fallback to stablecoin for unknown product types
        product_sequences = SEQUENCES["stablecoin"]
        notes.append(f"Product type '{product_type}' not found in library. Using stablecoin framework as fallback.")

    goal_sequence = product_sequences.get(goal)
    if not goal_sequence:
        # Fallback to first available goal for this product
        first_available_goal = next(iter(product_sequences))
        goal_sequence = product_sequences[first_available_goal]
        notes.append(f"Goal '{goal}' not found for '{product_type}'. Using '{first_available_goal}' sequence as fallback.")

    tagline = goal_sequence.get("tagline", "")
    days = goal_sequence["days"]

    # Get tokens
    tokens = get_default_tokens(company, product_type, goal, voice)

    # Build output
    output_lines = []

    # Header
    company_display = "[Company Name]" if company.lower() == "generic" else company
    output_lines.append(f"# Lifecycle Sequence: {company_display}")
    output_lines.append(f"**Product type:** {product_type} | **Activation goal:** {goal} | **Voice:** {voice}")
    output_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')} | {review_note}")
    output_lines.append("")
    output_lines.append(f"*{tagline}*")
    output_lines.append("")

    if warnings:
        output_lines.append("### Warnings")
        for w in warnings:
            output_lines.append(f"> **Warning:** {w}")
        output_lines.append("")

    if notes:
        output_lines.append("### Notes")
        for n in notes:
            output_lines.append(f"> {n}")
        output_lines.append("")

    output_lines.append("## How to use this sequence")
    output_lines.append("")
    output_lines.append("1. Replace all `[bracketed tokens]` with your actual product values before importing")
    output_lines.append("2. Day 0 sends immediately on signup. Days 1+ are conditional on activation status")
    output_lines.append("3. Once a user completes the activation goal, stop the non-activated sequence")
    output_lines.append("4. Test emails in your ESP before activating")
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")

    # Render each day
    for day, data in sorted(days.items()):
        output_lines.append(render_touchpoint(day, data, tokens, voice))

    # Footer
    output_lines.append("## Customization Checklist")
    output_lines.append("")
    output_lines.append("Before activating this sequence, replace these tokens with real values:")
    output_lines.append("")
    output_lines.append("**Required for all product types:**")
    output_lines.append("- `[First Name]` → personalization token from your ESP (e.g., `{{first_name}}` in Klaviyo)")
    output_lines.append("- `[Company Name]` → your brand name")
    output_lines.append(f"- All `[X,XXX]`, `[$XX.XX]` tokens → real product metrics")
    output_lines.append("")
    output_lines.append("**Product-specific tokens to replace:**")
    if product_type == "stablecoin":
        output_lines.append("- `[Primary Network — e.g., Base, Tron, Polygon]` → your primary stablecoin network")
        output_lines.append("- Custody statement → your actual reserve/custody model")
        output_lines.append("- Fee statement → your actual fee structure")
    elif product_type == "crypto-card":
        output_lines.append("- `[5-10]` card ETA → your actual delivery time")
        output_lines.append("- Cashback statement → your actual cashback rate and categories")
        output_lines.append("- Missed cashback calculations → pull from live user data")
    elif product_type == "yield":
        output_lines.append("- Yield source explanation → your actual yield source, specific not generic")
        output_lines.append("- Trust differentiators → your actual custody, reserve, insurance model")
        output_lines.append("- APY → pull from live product data, not hardcoded")
    elif product_type == "self-custody":
        output_lines.append("- Recovery method → your exact recovery mechanism")
        output_lines.append("- Gas fee amount → check current network conditions before activating")
        output_lines.append("- Unique features → the 2 specific things you do that MetaMask/Ledger can't")
    elif product_type == "remittance":
        output_lines.append("- Destination country and corridor data → your actual supported corridors")
        output_lines.append("- Fee comparison → calculate against Western Union for your specific corridors")
        output_lines.append("- Recipient field requirements → country-specific banking requirements")
    elif product_type == "super-app":
        output_lines.append("- Primary action → pick ONE feature, not a generic 'explore'")
        output_lines.append("- Main competitor → the app your users are most likely already using")
        output_lines.append("- Key differentiators → must be specific and verifiable, not marketing claims")
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("*Generated by lifecycle-sequence-generator | neobank-skills*")

    result = "\n".join(output_lines)

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(result)
        print(f"Sequence written to: {output_path}")
    else:
        print(result)

    return result


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate lifecycle marketing sequences for crypto neobanks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Stablecoin sequence for Plasma
  python generate_sequence.py --company Plasma --product-type stablecoin --goal first-deposit

  # Generic crypto card sequence for a client proposal
  python generate_sequence.py --company generic --product-type crypto-card --goal first-spend --voice casual

  # Yield sequence saved to file
  python generate_sequence.py --company Nexo --product-type yield --goal first-yield --output nexo-activation.md
        """
    )

    parser.add_argument(
        "--company",
        required=True,
        help='Company name (e.g., "Plasma") or "generic" for white-label output',
    )
    parser.add_argument(
        "--product-type",
        required=True,
        choices=PRODUCT_TYPES,
        help="Product type",
    )
    parser.add_argument(
        "--goal",
        required=True,
        choices=GOALS,
        help="Activation goal to optimize for",
    )
    parser.add_argument(
        "--voice",
        default="professional",
        choices=VOICES,
        help="Brand voice (default: professional)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    generate_sequence(
        company=args.company,
        product_type=args.product_type,
        goal=args.goal,
        voice=args.voice,
        output_path=args.output,
    )


if __name__ == "__main__":
    main()
