# Activation Milestones for Crypto Neobanks

Timing benchmarks, drop-off rates, and event definitions for the 4 activation goals. Used by the lifecycle sequence generator to calibrate when each message fires and what the copy must address.

---

## The Activation Problem

63% of fintech users churn within month one. For crypto neobanks, the problem compounds: users face multiple friction points before they reach the first value moment (the moment they realize the product actually works for them).

Most neobanks lose users in the gap between signup and first value moment. The lifecycle sequence exists to bridge that gap.

---

## The 4 Activation Goals

### 1. `kyc-complete`

**Definition:** User has passed identity verification and is fully approved to use the product.

**Why it matters:** KYC is the most common early drop-off point for crypto neobanks. 40-60% of signups never complete KYC. The marketing sequence for this goal must acknowledge the friction and reduce it.

**Typical KYC flow:**
1. Signup (email + password)
2. Personal details (name, DOB, address)
3. ID document upload (passport, driver's license)
4. Selfie / liveness check
5. Review period (instant to 72 hours)
6. Approval notification

**Timing benchmarks:**
| Stage | Typical Drop-Off | Notes |
|-------|-----------------|-------|
| Signup → ID upload | 25-35% | Users balk at uploading documents |
| ID upload → liveness check | 15-20% | Technical failures, camera issues |
| Liveness → pending | 5-10% | Users who complete liveness usually wait |
| Pending → approved | 10-20% abandonment | Long waits cause forgetting or competitor switch |

**Message timing for kyc-complete goal:**
- Day 0: Welcome + "Start KYC now, takes 3 minutes" CTA
- Day 1: If KYC not started — "Your account is ready, one step missing" nudge
- Day 3: If KYC stuck in review — "We're checking your details, here's what happens next" expectation setter
- Day 7: If KYC still pending — support escalation offer
- Day 14: If still not complete — re-engagement with a friction reduction hook
- Day 30: Final attempt or graceful handoff

**Real user language around KYC pain:**
- "I don't know if my verification actually went through"
- "The app just says 'pending' with no update"
- "My selfie kept failing and I don't know why"
- "I submitted documents 5 days ago and heard nothing"
- "It asked for my ID 3 times and kept rejecting it"

---

### 2. `first-deposit`

**Definition:** User's first successful fund deposit (crypto or fiat) into their account.

**Why it matters:** First deposit signals intent. Users who deposit are 4-8x more likely to become active long-term users than users who only complete KYC. For stablecoin and yield products, this is the primary value moment.

**Typical deposit flow (stablecoin example):**
1. KYC complete
2. View account/wallet address
3. Add funding source (bank account, crypto wallet, exchange)
4. Initiate transfer
5. Wait for confirmation (seconds for crypto, 1-3 days for bank)
6. Funds appear in account
7. First value moment: see balance, explore features

**Timing benchmarks:**
| Stage | Typical Drop-Off | Notes |
|-------|-----------------|-------|
| KYC complete → viewed deposit screen | 30-40% | Users don't know next step |
| Viewed deposit → initiated transfer | 25-35% | Fear: "Is this safe? What if I lose it?" |
| Initiated → confirmed | 5-10% | Technical issues, wrong network |
| First deposit → second deposit | 40-50% don't return | First deposit is too small to generate value |

**Message timing for first-deposit goal:**
- Day 0: Welcome + "See your wallet address" or "Connect your first account" CTA
- Day 1: If no deposit — "Here's exactly how to make your first deposit" with specific steps
- Day 3: If no deposit — Address the trust barrier head-on ("test with $10 first" or "your funds are FDIC/fully backed")
- Day 7: If no deposit — Social proof: "X users deposited in the last 7 days" or a specific success story
- Day 14: If no deposit — Different angle: focus on what they're missing (yield earned, fee saved, etc.)
- Day 30: If no deposit — Final re-engagement or graceful offboarding

**Critical: The Test Deposit Psychology**
Many users want to "test" the product before committing real funds. The Day 3 message should explicitly invite this: "Start with $10 to see how it works." This converts fence-sitters into depositors. A user who deposits $10 and sees it work smoothly will often return with $500.

**Real user language around first-deposit barriers:**
- "I wasn't sure if it was safe to send real money"
- "I didn't understand if I needed to use a specific network"
- "I sent crypto to the address but it didn't show up"
- "I was worried about losing my money if the app crashed"
- "I wanted to test with a small amount first but wasn't sure how"

---

### 3. `first-spend`

**Definition:** User's first successful transaction using the neobank's card or payment feature.

**Why it matters:** For crypto card products, the first tap of the card is the proof-of-concept moment. Users who spend at least once in month one are 3-5x more likely to reach month three.

**Typical first-spend flow (crypto card example):**
1. KYC complete
2. Fund account
3. Order card (physical or request virtual card)
4. Card delivery / virtual card activation
5. Add to Apple/Google Pay or use card number online
6. First tap at point of sale or online checkout
7. See transaction in app (confirmation this actually works)

**Timing benchmarks:**
| Stage | Typical Drop-Off | Notes |
|-------|-----------------|-------|
| Funded → card ordered | 30-40% | Users don't realize ordering is a separate step |
| Card ordered → activated | 20-30% | Physical card delivery takes days/weeks |
| Activated → first use | 25-35% | Card sits in wallet unused |
| First use → second use | 30-40% don't return | No habit formed from one-time use |

**Physical vs virtual card timing:**
- Virtual card: available minutes after funding; first use possible same day
- Physical card: 5-14 business days delivery; activation required
- This is a major lifecycle split — virtual card users need different Day 3 messaging than physical card waiters

**Message timing for first-spend goal:**
- Day 0: Welcome + "Activate your virtual card in 2 minutes" CTA (or "Your card is on its way" status if physical)
- Day 1: If not activated — "Your virtual card is waiting" or "Your physical card ships in X days"
- Day 3: If no spend yet — Address the spend barrier: "Here's 5 places to test your card today"
- Day 7: If still no spend — Show what they're missing: "You earned 0 cashback this week. Here's what [X] users earned."
- Day 14: If no spend — Re-engage with a specific spend incentive or spend challenge
- Day 30: Graduation (first spend) or final push (no spend)

**Real user language around first-spend barriers:**
- "The card was declined at my first transaction"
- "I didn't realize I had to activate it separately"
- "I added it to Apple Pay but the first tap failed"
- "I don't know which merchants accept it"
- "The conversion rate at the register wasn't what I expected"

---

### 4. `first-yield`

**Definition:** User's first earned yield or interest payment posted to their account.

**Why it matters:** For yield/earn products, the moment users see actual money earned (not just a projected APY) is the "aha" moment. Users who see their first yield payment are dramatically more likely to maintain or increase their balance.

**Typical first-yield flow:**
1. KYC complete
2. Fund account
3. Enable/opt into yield (some require explicit opt-in)
4. Yield accrual period (hourly, daily, or weekly depending on product)
5. First yield payment visible in account
6. "Aha" moment: "This is actually working"

**Timing benchmarks:**
| Stage | Typical Drop-Off | Notes |
|-------|-----------------|-------|
| Funded → yield enabled | 20-30% | Users don't realize yield requires opt-in |
| Yield enabled → first payment | Depends on product | Daily products: 24hrs. Weekly: 7 days. |
| First payment → increased deposit | 40-50% stay flat | First yield is too small on small balances |
| Month 1 → Month 3 | 30-40% churn | Yield mercenaries leave for higher APY |

**The Yield Anxiety Pattern:**
Users often ask: "Where does the yield come from?" before they feel comfortable depositing meaningful amounts. If the product doesn't explain the yield source, users assume risk they can't quantify. The Day 1 and Day 3 messages for yield products must answer this question.

Post-Celsius/BlockFi: Trust in yield products is near-zero for many users. The Day 3 message must address this directly without being defensive.

**Message timing for first-yield goal:**
- Day 0: Welcome + "Your funds start earning as soon as you deposit" (set expectation for the first-yield moment)
- Day 1: If no deposit — "You're missing earnings right now. Here's where your yield comes from." (transparency first)
- Day 3: If deposit made but yield not enabled — "One step to start earning: [specific action]"
- Day 7: If yield enabled — Show the real numbers: "At your current balance, you'd earn $X per month"
- Day 14: If yield enabled — Deepen the habit: "Your account has earned $X so far. Here's how to earn more."
- Day 30: Graduation: show total yield earned. Non-activated: show the opportunity cost of not depositing.

**Real user language around first-yield barriers:**
- "I don't understand where the yield actually comes from"
- "I'm nervous after what happened to Celsius"
- "The APY looked great but I didn't realize it required locking up my funds"
- "The 8% they advertised dropped to 3% after the first month"
- "I'm earning fractions of a cent and it doesn't feel worth the risk"

---

## Activation Timing by Product Type

| Product Type | Median Time to First Value | Top Drop-Off Stage |
|-------------|---------------------------|-------------------|
| Stablecoin | 3-5 days | KYC to first deposit |
| Crypto Card | 7-14 days | Card activation to first spend |
| Yield/Earn | 1-3 days (if funded) | Signup to first deposit |
| Self-Custody | 5-10 days | Onboarding to first transaction |
| Remittance | 2-4 days | KYC to first send |
| Super-App | 10-21 days | Signup to any single feature activation |

---

## The Critical Window

For crypto neobanks, the activation window is roughly 72 hours from signup. After 72 hours without activation, churn probability exceeds 60%. After 7 days without any action, churn probability exceeds 80%.

This means:
- Day 0 and Day 1 messages are the most important in the sequence
- Day 3 is the last good chance to prevent early churn
- Day 7 onward is recovery mode for users who didn't activate

The lifecycle sequence must treat Day 0-3 as the primary activation window and Days 7-30 as the recovery window.

---

## Product-Goal Compatibility Matrix

Not all goals fit all product types. Use this matrix to flag mismatches:

| Product Type | first-deposit | first-spend | first-yield | kyc-complete |
|-------------|:---:|:---:|:---:|:---:|
| stablecoin | ✓ primary | | ✓ secondary | ✓ prereq |
| crypto-card | ✓ prereq | ✓ primary | | ✓ prereq |
| yield | ✓ prereq | | ✓ primary | ✓ prereq |
| self-custody | ✓ primary | ✓ secondary | | ✓ prereq |
| remittance | ✓ primary | ✓ secondary | | ✓ prereq |
| super-app | ✓ primary | ✓ secondary | ✓ secondary | ✓ prereq |

✓ primary = ideal goal for this product
✓ secondary = valid but not optimal
✓ prereq = this goal is a precursor to activation, not the activation itself
