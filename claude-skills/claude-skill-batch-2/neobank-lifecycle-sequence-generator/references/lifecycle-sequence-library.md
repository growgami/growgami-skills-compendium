# Lifecycle Sequence Library

Pre-built sequence frameworks for 6 crypto neobank product types. Each framework contains:
- The activation journey map (signup to first value moment)
- The top 3 drop-off barriers with real user language
- Touchpoint-by-touchpoint messaging strategy
- Voice and tone notes
- Copy building blocks (not final copy, but the raw material)

These frameworks are the source of truth when generating sequences. The generate_sequence.py script loads the relevant framework before producing any output.

---

## Framework 1: Stablecoin Banking

**Companies:** Plasma, PEXX, Infini, Copperx, Stables
**Core user need:** USD stability without traditional banking friction. Cross-border payments without fees.
**Primary activation goal:** first-deposit
**Typical user:** International professional, digital nomad, LatAm/SEA user escaping currency volatility, freelancer receiving USD payments

### Activation Journey

```
Signup → KYC (1-3 days) → Fund wallet (crypto or fiat) → First deposit confirmed
        ↓                  ↓                              ↓
   Drop-off 1:         Drop-off 2:                  Drop-off 3:
   KYC rejection or   "Is this safe?" fear           Network confusion
   wait anxiety       before sending funds           (wrong chain, wrong address)
```

### Top 3 Drop-Off Barriers

**1. KYC Wait Anxiety**
Users don't know how long approval takes, whether their documents were received, or if they need to do anything else. They abandon because they don't know what "pending" means.

User language:
- "I uploaded my passport 3 days ago and nothing happened"
- "I don't know if my KYC went through"
- "The app just says 'under review' with no timeline"
- "I gave up waiting and went with [competitor]"

Day 3 message must address this barrier directly.

**2. Trust Test Fear**
Users (especially post-FTX, post-Celsius) won't commit real money until they've "tested" the product. They want to do a small test send first but are afraid even that small amount will disappear.

User language:
- "I wanted to test with a small amount but wasn't sure if it was safe"
- "I didn't trust a new app with real money"
- "After what happened to FTX I'm careful with any new platform"
- "I needed to see that withdrawals actually work before depositing more"

Day 1 and Day 3 messages should explicitly invite test deposits.

**3. Network Confusion**
Stablecoin users often don't know which network (Ethereum, Tron, Solana, Polygon, etc.) to use when sending USDC/USDT. Wrong network = lost funds fear.

User language:
- "I didn't know which network to choose"
- "I sent USDC but chose the wrong chain"
- "There were 6 different networks and I didn't know which one was free"
- "I was scared I'd pick the wrong network and lose everything"

Day 1 message must include explicit network guidance for the primary stablecoin.

### Touchpoint Strategy

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + "your wallet is ready" + single-step action (view wallet address) | "Your USDC wallet is live. Here's your address." | "See your wallet → [button]" |
| 1 | How to make your first deposit: specific network, step by step. Invite test deposit. | "Send any amount to test. Start with $10." | "First deposit guide → [button]" |
| 3 | Address KYC status (if pending) or address trust barrier (if funded but no deposit) | "Funds take [X] mins on [network]. Your account is ready." | "Deposit now — 30-second guide" |
| 7 | Social proof: real users, real numbers. "$X deposited by [N] users this week." | "[N] people just made their first deposit. You're next." | "Join [N] users earning today" |
| 14 | Opportunity cost: what $X in stablecoins earns vs. bank account, plus what it costs to keep missing remittance fees | "You've been paying $X/month in transfer fees. There's a better way." | "Calculate your savings → [button]" |
| 30 | Graduation (deposited): show account summary + next feature to explore. Not activated: final re-engagement with a unique hook | "Last chance: [specific offer or unique value hook]" | "[One-line unique value prop]" |

### Voice Notes

**For casual/professional voice:** Lead with the practical benefit. Stablecoin users want USD, not crypto. Avoid "DeFi", "web3", "on-chain" language unless the product specifically targets crypto-native users. Talk about sending money, saving money, holding USD, not about blockchains.

**For crypto-native voice:** Can use network names (USDC on Base, USDT on Tron), yield rates, wallet terminology. Assumes user knows how to self-custody. Focus on fee savings and settlement speed vs. wire transfers.

### Copy Building Blocks

**Subject line formulas:**
- "[Company Name]: Your USDC wallet is ready" (Day 0)
- "How to send your first $10 to [Company Name]" (Day 1)
- "Still waiting? Here's what's happening with your account" (Day 3 - KYC)
- "You can test with any amount. Here's how." (Day 3 - trust)
- "[N] people moved their money here this week" (Day 7)
- "You're paying $X/month to send money you don't have to" (Day 14)

**Body language patterns:**
- "No wire fees. No exchange rate markup. Just USDC at 1:1."
- "Your first deposit is just a copy-paste. Here's the address."
- "Test with $10. If it doesn't work, we'll walk you through it."
- "Over [N] people have deposited since [date]. Here's what they said."
- "You're sending [X currency] home every month. Here's what the fees cost you per year."

---

## Framework 2: Crypto Card

**Companies:** KAST, Wirex, RedotPay, Gnosis Pay, BitPay, Crypto.com card
**Core user need:** Spend crypto in the real world without friction.
**Primary activation goal:** first-spend
**Typical user:** Crypto holder who wants to spend without converting to fiat first, international traveler, digital nomad, crypto-native who has most wealth in crypto

### Activation Journey

```
Signup → KYC → Fund account → Order card → Card delivery → Activate → First spend
        ↓         ↓              ↓            ↓               ↓
   Drop-off 1: Drop-off 2:  Drop-off 3:  Drop-off 4:   Drop-off 5:
   KYC friction  "What do    Card delivery Card just     "It got
                 I fund       takes 2 wks   sits there   declined"
                 with?"
```

Note: Virtual cards skip the delivery wait and unlock first-spend same day. The sequence must split on virtual vs. physical card.

### Top 3 Drop-Off Barriers

**1. Card Delivery Wait (Physical Card)**
Physical cards take 5-14 business days. During this wait, users forget about the product, have no engagement, and often sign up with a competitor.

User language:
- "I signed up but haven't heard anything about my card"
- "It's been 2 weeks and my card still hasn't arrived"
- "I gave up and got a Revolut card instead while waiting"
- "The card delivery took so long I forgot I'd signed up"

The Day 3-7 sequence for physical card users must bridge this dead time with engagement that doesn't require the card.

**2. First Transaction Decline**
The first card use is the proof-of-concept moment. If it fails, the user loses trust immediately. Card declines at first use are a major churn driver.

User language:
- "My card was declined at the register and it was embarrassing"
- "The first place I tried to use it didn't accept it"
- "I didn't know I needed to enable it before first use"
- "The crypto conversion didn't happen in time and the payment failed"

Day 1 message must set up the first use for success: pre-charge the card, confirm the balance, pick an easy first merchant.

**3. Cashback Confusion**
Many crypto card users signed up specifically for cashback rewards. If they don't understand how cashback works, when it pays out, or what they get it in, they feel deceived.

User language:
- "The cashback comes in [token] which keeps losing value"
- "I thought I'd get 2% but it was only on specific merchants"
- "I didn't know the cashback required staking to unlock"
- "The 'up to 5%' was only for the top tier that required $4,000 locked"

Day 7 message should clearly explain the cashback mechanics for this specific product.

### Touchpoint Strategy (Virtual Card)

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + "Activate your virtual card in 2 minutes" | "Your virtual card is waiting. Tap to activate." | "Activate card → [button]" |
| 1 | "Where to use your card first" — specific merchants, Apple/Google Pay setup | "Add to Apple Pay in 30 seconds. Here's how." | "Add to Apple Pay → [button]" |
| 3 | "Pick 3 places to use your card this week" — specific category and merchant recs | "Coffee, groceries, Uber — your card works at all 3." | "See where to use it → [button]" |
| 7 | Show cashback earned potential: "If you'd used the card this week, you'd have earned $X" | "You left $X in cashback on the table this week." | "Start earning cashback → [button]" |
| 14 | Re-engagement: "One tap to start earning on everyday spending" | "Your card hasn't been used. Let's change that." | "Use your card today" |
| 30 | Graduated: "Here's your month-one spending summary." Not activated: "What's stopping you? [one specific friction option]" | "[X] cashback waiting for your first swipe." | "First purchase = first reward" |

### Touchpoint Strategy (Physical Card)

Day 0-3 shifts to a waiting-room engagement strategy since the user can't spend yet:

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + card shipment confirmation + "While you wait: activate your virtual card" | "Your card ships in [X] days. Use virtual today." | "Virtual card ready now → [button]" |
| 1 | "Use your virtual card while your physical card ships" | "Don't wait for the physical card. Virtual is live." | "Virtual card: instant access" |
| 3 | Card tracking update + "Set up Apple Pay for day-one success" | "Your card arrives in ~[X] days. Get ready." | "Set up Apple Pay now → [button]" |
| 7 | "Your card may have arrived. Here's how to activate." | "Card arrived? Here's your 2-step activation." | "Activate card → [button]" |
| 14 | First spend coaching: "Your first swipe guide" | "3 easy places for your first transaction." | "First spend guide → [button]" |
| 30 | If no spend yet: "Your card has been active for [X] days. Here's what you're missing." | "Your first cashback is one swipe away." | "Use your card today" |

### Voice Notes

**Casual voice:** Conversational, peer-to-peer. "Your card is here. Tap it somewhere today." Uses everyday language, references real merchants (Starbucks, Uber, Amazon).

**Professional voice:** Clean, benefit-forward. "Your crypto card is ready for activation. Here's how to maximize your first month."

**Crypto-native voice:** Focuses on the DeFi angle (spending without converting, multi-chain support, non-custodial spend). Avoids explaining basics.

---

## Framework 3: Yield / Earn

**Companies:** Nexo, Crypto.com earn, Hi, Ledn, SwissBorg, Matrixport
**Core user need:** Make idle crypto or stablecoins earn passive income.
**Primary activation goal:** first-yield
**Typical user:** Crypto holder with idle assets, income-seekers, stablecoin holders who want more than 0% from sitting on USDC

### Activation Journey

```
Signup → KYC → Fund account → Enable yield → Accrual period → First payout posted
        ↓         ↓              ↓                ↓
   Drop-off 1: Drop-off 2:  Drop-off 3:      Drop-off 4:
   KYC friction "Where does  Lockup period    First payout
                yield come   surprise         too small to
                from?"                        feel meaningful
```

### Top 3 Drop-Off Barriers

**1. Yield Source Anxiety (Post-Celsius)**
After Celsius, BlockFi, and Voyager collapsed, users are scared to deposit funds into yield products. The #1 question is: "Where does the yield actually come from?" Products that don't answer this clearly lose users at the deposit stage.

User language:
- "I don't understand where the interest comes from"
- "After Celsius I don't trust any platform promising high yield"
- "What happens to my money if the company goes bankrupt?"
- "Is my money actually safe or is this just a Ponzi?"
- "They never explained the risk clearly"

Day 1 message MUST address this directly. Not defensively. Just clearly: "Here's exactly where your yield comes from."

**2. Lockup Surprise**
Many yield products require locking funds for 30, 60, or 90 days for higher rates. Users who don't realize this feel deceived when they try to withdraw.

User language:
- "I didn't know I couldn't withdraw for 30 days"
- "The lock-up period wasn't clear when I signed up"
- "I needed my money and couldn't access it"
- "The flexible rate was only 1% and I needed to lock for 60 days to get 8%"

Day 0 message must set expectations about lockup vs. flexible options upfront.

**3. Yield Mercenary Churn**
Users who came for a promoted APY will leave the moment a competitor offers more. These users have high CAC and low LTV. The sequence should target converting them to value-based retention, not just keeping them for the APY.

This is less of a drop-off barrier and more of a retention challenge for the Day 14-30 messages.

### Touchpoint Strategy

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + "Here's where your yield comes from" (transparency first) + "Start earning in 3 steps" | "Your yield starts the moment you deposit." | "Start earning → [button]" |
| 1 | "Your money is losing [X]% to inflation right now. Here's the alternative." — with specific yield source explanation | "Current rate: [X]% APY. Starts immediately." | "See your projected earnings → [button]" |
| 3 | Address the trust barrier: "Here's how your funds are protected" — specific: reserves, insurance, custody model | "Your funds: [custody model]. Protected by [specific safeguard]." | "How we protect your funds → [button]" |
| 7 | Real numbers: "If you deposited $1,000 today, here's what you'd earn this month" — with specific current APY | "Deposit $1,000 = $[X] this month at current rates." | "Calculate your earnings → [button]" |
| 14 | Show what similar users are earning. Social proof with numbers. | "[N] users earned over $[X] in yield last week." | "Join them → [button]" |
| 30 | Graduated: "You've earned $[actual amount] so far. Here's how to earn more." Not activated: "Opportunity cost: you've missed $[X] in yield." | "Your missed earnings: $[X]. Still time to start." | "Start earning today → [button]" |

### Voice Notes

**For crypto-native voice:** Can discuss DeFi yields, liquidity pools, lending mechanics. Assumes user understands APY, liquidation risk, and custody models.

**For professional/casual voice:** Focus on the savings account comparison. "Banks pay 0.01%. We pay [X]%. Here's why." Avoid DeFi jargon entirely.

**Yield products should NEVER use:** "guaranteed", "risk-free", "100% safe". These are legally problematic and destroy trust. Use: "protected by [specific mechanism]", "backed by [specific reserves]", "fully liquid with [specific notice period]."

---

## Framework 4: Self-Custody Banking

**Companies:** Bleap, Gnosis Pay, ether.fi Cash, Fiat24, Zengo
**Core user need:** Banking convenience (card, payments, fiat) without giving up custody of private keys.
**Primary activation goal:** first-deposit (wallet funding)
**Typical user:** Crypto-native who has self-custody experience, privacy-conscious user, anti-custodial ideologist, DeFi user who wants banking features

### Activation Journey

```
Signup → Wallet setup → Backup seed phrase → Fund wallet → Enable banking features → First transaction
        ↓               ↓                     ↓              ↓
   Drop-off 1:     Drop-off 2:           Drop-off 3:    Drop-off 4:
   Intimidated     Seed phrase           "I already      Gas fee
   by wallet       management            have a wallet"  surprise
   setup           anxiety
```

### Top 3 Drop-Off Barriers

**1. Seed Phrase Anxiety**
Many mainstream users have heard horror stories about lost seed phrases. Even crypto-native users are anxious about managing a new seed phrase for a new product. This is the biggest onboarding barrier for self-custody products.

User language:
- "I'm scared of losing my seed phrase and losing everything"
- "I've messed up with seed phrases before and can't risk it again"
- "The setup process was too complicated"
- "I didn't want to manage another set of private keys"
- "What happens if I lose my phone?"

Day 0 and Day 1 messages must reduce this anxiety with specific, credible safety measures (social recovery, hardware backup, guardian system, etc.).

**2. "I Already Have a Wallet" Resistance**
Self-custody users often already have a MetaMask, Ledger, or other wallet. They need a compelling reason to use a new one. Generic "banking for Web3" messaging doesn't convert them.

User language:
- "I already have MetaMask, why do I need another wallet?"
- "I don't want to move funds to a new wallet"
- "I've been using Ledger for years, why switch?"

Day 1 message must answer this objection directly: what does this product do that their existing wallet can't?

**3. Gas Fee Surprise**
Self-custody transactions involve gas fees. Users who don't expect this are shocked by their first transaction cost. This is especially true for small-balance users and users who came from custodial products.

User language:
- "I didn't realize gas fees would eat so much of my transaction"
- "My first transfer cost more in gas than the amount I was sending"
- "I can't make small payments because gas fees make it uneconomical"

Day 0 message should set explicit expectations: "Transactions cost [X] in gas fees on [network]." For L2-based products, this is a selling point.

### Touchpoint Strategy

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + "Your wallet is non-custodial: here's what that means and how backup works" | "Your keys. Your wallet. Backup takes 2 minutes." | "Back up your wallet → [button]" |
| 1 | "Why self-custody + banking? Here's what you can do that MetaMask can't." — specific features (card, direct deposit, etc.) | "Your card. Your keys. No permission needed." | "Explore banking features → [button]" |
| 3 | Address gas fees and network selection: "Here's the exact cost of your first transaction" | "First transaction: [gas cost] on [network]. Worth it." | "Send your first transaction → [button]" |
| 7 | Social proof: users who switched from custodial products. Focus on the "aha" moment. | "[N] users moved from Coinbase this month. Here's why." | "Why they switched → [button]" |
| 14 | Show what's unique: the specific thing they can do here that no custodial wallet offers | "Direct deposit to a self-custody wallet. No custodian." | "Try [specific feature] → [button]" |
| 30 | Graduated: "You've completed [X] transactions with full custody. Here's your account summary." Not activated: "Still haven't funded? Here's the 90-second setup." | "Your wallet. Unused. 90 seconds to first transaction." | "Fund wallet → [button]" |

### Voice Notes

**Self-custody products should ONLY use crypto-native voice** unless they're specifically targeting mainstream crossover users. This audience values technical accuracy over simplicity. Don't dumb it down. Do be specific.

"Your keys, your crypto" is a resonant phrase for this audience. Use it. Don't paraphrase it into "you control your funds."

---

## Framework 5: Remittance

**Companies:** PEXX, Bitso, Félix Pago, Yellow Card, Coins.ph
**Core user need:** Send money home (or cross-border) faster and cheaper than banks or Western Union.
**Primary activation goal:** first-deposit (to fund the first send)
**Typical user:** Immigrant worker in US/EU/UK sending money to LatAm, SEA, Africa, Philippines. Freelancer receiving international payment. Small business with cross-border payments.

### Activation Journey

```
Signup → KYC → Fund account → Enter recipient details → First send → Recipient receives funds
        ↓         ↓              ↓                          ↓
   Drop-off 1: Drop-off 2:  Drop-off 3:               Drop-off 4:
   KYC barriers "Is my      Setting up                 Recipient
   (immigration  family      recipient                  can't
   status fears) safe?"      info correctly             receive it
```

### Top 3 Drop-Off Barriers

**1. Family Safety Fear**
Remittance users aren't just transferring money — they're supporting family. The emotional stakes are higher than any other product type. If something goes wrong, it's not just financial loss; it's letting family down.

User language:
- "I was scared to use a new app to send money to my family"
- "What if the money doesn't arrive and my family is waiting for it?"
- "I've been burned by [app/service] before and I don't trust new platforms"
- "I wanted to test with a small amount first to make sure it worked"

Day 0 message must acknowledge this emotional weight and provide a clear path to a "test send."

**2. Recipient Setup Confusion**
Setting up a new recipient (bank account, mobile money, cash pickup) is often more complex than users expect. Errors in recipient details can cause failed transfers.

User language:
- "I didn't know what routing number my family's bank uses"
- "The recipient form asked for things I didn't have on hand"
- "I set it up but the money was rejected because of a name mismatch"
- "I couldn't figure out how to set up GCash / M-Pesa / mobile money"

Day 1 message should walk through recipient setup step by step.

**3. Fee Comparison Hesitation**
Remittance users are extremely fee-conscious. They've been burned by Western Union, MoneyGram, and bank wire fees. They want to see the fee comparison before committing. If the product doesn't show fees upfront and clearly, users assume hidden charges.

User language:
- "I wanted to see the total cost before sending, not after"
- "Western Union told me $4 and then charged $19"
- "I couldn't tell if the exchange rate had a markup built in"
- "I needed to compare with my current service before switching"

Day 0 and Day 1 must show specific, total fee comparison vs. traditional alternatives.

### Touchpoint Strategy

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + "Here's what your first transfer to [country] costs — and what Western Union charges" | "Your first transfer: $[fee]. Western Union: $[WU fee]." | "Send your first transfer → [button]" |
| 1 | "How to set up your first recipient in 4 steps" — country-specific guide | "Recipient ready? Send in 3 minutes." | "Add recipient → [button]" |
| 3 | "Here's how to do a $10 test send to make sure everything works" — specific, low-stakes path | "Test with $10. Arrives in [time]." | "Test transfer → [button]" |
| 7 | Real numbers: "Users who switch from Western Union save $[X]/month on average" with specific corridor data | "Average savings for [origin]-[destination] users: $[X]/month." | "Calculate your savings → [button]" |
| 14 | Scheduling hook: "Set up a recurring transfer and never forget to send money home" | "Set up monthly transfer. One time. Every month." | "Schedule transfer → [button]" |
| 30 | Graduated: "You've saved $[X] vs. traditional services this month." Not activated: "Your family is still waiting for a better way." | "First transfer: still available. Here's a shortcut." | "Send now → [button]" |

### Voice Notes

**Remittance products should NEVER use crypto-native voice.** The audience is mainstream consumers, often non-crypto-native. All crypto terminology must be invisible. Users should feel like they're using a money transfer app, not a crypto product.

**Regional specificity matters.** LatAm corridors (US to Mexico, US to Colombia): mention Peso, reference Oxxo or local pickup. SEA corridors (US to Philippines): mention GCash, Pag-IBIG, Philippine bank names. Africa corridors: reference M-Pesa, mobile money, specific country regulations.

**The emotional hook is family, not finance.** Copy should reference the recipient ("your family," "your parents," "back home") not just the transaction.

---

## Framework 6: Super-App

**Companies:** Revolut, Bybit MyBank, Hi, SoFi (crypto features), Crypto.com full suite
**Core user need:** One app for all financial needs — banking, crypto, investing, insurance, travel, spending.
**Primary activation goal:** variable (first-deposit most common, or whichever feature is the product's main hook)
**Typical user:** Millennial/Gen Z who wants to consolidate financial apps, frequent traveler, global professional, tech-forward mainstream user

### Activation Journey

Super-app activation is more complex because there are multiple possible "first value moments." The sequence must push toward ONE primary feature and ignore the others in activation messaging.

```
Signup → KYC → Primary feature activation → First use of primary feature
        ↓         ↓              ↓
   Drop-off 1: Drop-off 2:  Drop-off 3:
   KYC        Feature       Feature
   friction   overwhelm     paralysis
              ("too many    (which one
               options")     do I use?)
```

### Top 3 Drop-Off Barriers

**1. Feature Overwhelm**
Super-apps have too many features. New users don't know where to start. The onboarding sequence must pick ONE thing for the user to do first and ignore everything else.

User language:
- "There's so much in the app I didn't know where to start"
- "I signed up but never figured out how to use the main feature"
- "The app tried to sell me 10 things at once"
- "I downloaded it but never really got into using it"

Every Day 0-3 message must have ONE CTA. Not "explore our features." One specific action.

**2. Trust Transfer Problem**
Super-apps ask users to trust them with multiple financial products — checking, crypto, investing, insurance. Each new product added requires a new trust decision. Users who like the banking features may not trust the crypto features, and vice versa.

User language:
- "I use it for [feature A] but not [feature B]"
- "I trust it for my day-to-day banking but not for large crypto amounts"
- "The app feels like a bank for some things and a crypto exchange for others"

The lifecycle sequence should not try to cross-sell in activation phase. Activate the primary feature first. Cross-sell at Day 30+.

**3. Comparison Inertia**
Super-app users are often already using another super-app (Revolut, Cash App, PayPal). Switching cost is high — they need to update payment methods, direct deposits, saved recipients. The lifecycle sequence must address this switching barrier explicitly.

User language:
- "I already use Revolut for this"
- "Switching seems like too much work"
- "I'd need to update everything if I switched"
- "I use multiple apps because no single one does everything well"

Day 7 and Day 14 messages should address the switching cost directly with specific "here's what it takes to switch" guidance.

### Touchpoint Strategy (primary goal: first-deposit)

| Day | Email | Push | In-App |
|-----|-------|------|--------|
| 0 | Welcome + "One thing to do today: [single primary feature]" — ignore all other features | "One step to start: [primary action]." | "[Primary feature] → [button]" |
| 1 | "Here's why [single feature] is what makes [Company] different from [named competitor]" | "[Company] does this. [Competitor] doesn't." | "Try [feature] → [button]" |
| 3 | Address the most likely hesitation for the primary feature (product-specific) | "Most users [do X] on day 3. Ready?" | "[Feature]: still waiting for you" |
| 7 | Social proof for the primary feature. Specific numbers. | "[N] users used [feature] this week. Average result: $[X]." | "Join them → [button]" |
| 14 | Re-engage with a different angle on the same primary feature, or introduce ONE secondary feature | "You're missing [secondary feature]. Here's what it is." | "Explore [secondary feature] → [button]" |
| 30 | Graduated: multi-feature summary. Not activated: "You signed up. What stopped you? [specific friction options]" | "Quick question: what stopped you from [action]?" | "Tell us → [button]" |

### Voice Notes

**Super-app voice should match the product's primary positioning.** If the product leads with crypto (Bybit MyBank), use professional-to-crypto-native voice. If it leads with mainstream banking (Revolut), use casual-to-professional voice.

**Key rule:** Never use a super-app sequence to sell multiple features simultaneously. Pick one. Activate one. Add more later.

---

## Universal Copy Rules (All Product Types)

These rules apply to every message in every framework:

1. **Subject lines**: Never use a question as a subject line if the answer is obvious ("Ready to start earning?"). Use a statement that creates tension or reveals value ("You're losing [X] every month you don't deposit.").

2. **CTA buttons**: One per email. The button text should describe the action, not the result. "Make your first deposit" not "Start earning today." (The result is implied by the action.)

3. **Personalization tokens**: Use `[Company Name]`, `[Product Name]`, `[User First Name]`, `[Balance]`, `[Days Since Signup]`, `[Activation Status]` wherever available. Personalized messages outperform generic by 2-3x for activation.

4. **Push notification length**: Title under 50 chars. Body under 50 chars. Total under 100. Shorter is better. The notification should be completeable in 2 seconds of reading.

5. **In-app messages**: Headline under 40 chars. Body under 60 chars. One button. Appear on login if user hasn't completed the activation goal for that day's trigger.

6. **Proof by specificity**: "Thousands of users" is weak. "12,847 users made their first deposit last week" is strong. If you don't have the real number, use a realistic placeholder like "[X] users" with a note to replace with live data.

7. **Never use countdown pressure unless it's real**: "Offer expires in 24 hours" only works if it's true. Fake urgency trains users to ignore it.
