# SaaS Metrics Deep Dive

## Monthly Recurring Revenue (MRR)

**Definition:** The total predictable revenue a SaaS company expects to generate each month from active subscriptions.

**Calculation:**
- MRR = (Number of customers) × (Average monthly subscription price)
- Or: Sum of all active subscription values for the month

**Why it matters:**
- Directly indicates business health and burn rate sustainability
- Easier to track than ARR for month-to-month planning
- Used to calculate customer acquisition cost (CAC) payback period

**Key nuances:**
- Only includes recurring subscription revenue (excludes one-time fees, professional services)
- Should be "net" MRR (accounting for churn that same month)
- Different from bookings—MRR is what actually comes in; bookings may be annual contracts

**Example:** If you have 100 customers paying $50/month, MRR = $5,000

---

## Annual Recurring Revenue (ARR)

**Definition:** The total predictable revenue a SaaS company expects over a 12-month period.

**Calculation:**
- ARR = MRR × 12
- Or: (Annual subscription price) × (Number of annual subscribers)

**Why it matters:**
- Easier to compare against venture capital benchmarks
- More stable metric than monthly revenue (smooths out seasonality)
- Used by investors to assess company valuation and growth trajectory

**Key nuances:**
- Assumes no change in customer base (no churn, no new customers)—this is the "static" view
- Magic number: ARR growth rate > 3x/year is considered excellent for early-stage SaaS
- Should normalize expansion revenue (customers upgrading) separately from net new ARR

**Example:** Company with $5,000 MRR has $60,000 ARR

---

## Churn Rate

**Definition:** The percentage of customers who cancel or stop paying during a given period.

**Calculation:**
- Monthly churn rate = (Customers lost in month) / (Customers at start of month) × 100
- Annual churn rate ≈ (1 - Monthly churn)^12 (exponential decline)

**Why it matters:**
- Indicates product-market fit and customer satisfaction
- Most directly impacts unit economics and lifetime value
- Can signal whether growth is sustainable or just burning cash on poor retention

**Key nuances:**
- **Logo churn:** Percentage of customer accounts lost
- **Revenue churn:** Percentage of MRR lost (accounts for downgrades, not just cancellations)
- 5% monthly churn is considered acceptable for B2B SaaS; <3% is excellent
- More critical metric than acquisition at scale—much cheaper to retain than acquire

**Example:** Start month with 100 customers, 5 cancel → 5% monthly churn

---

## Lifetime Value (LTV)

**Definition:** The total profit a company expects to generate from a single customer over their entire relationship.

**Calculation:**
- Simple: LTV = (Average customer monthly revenue) / (Monthly churn rate)
- More detailed: LTV = ARPU × Gross Margin / Monthly Churn Rate
- Or: Sum of all future cash flows from a cohort, discounted by time

**Why it matters:**
- Determines how much you can spend to acquire a customer (CAC)
- LTV/CAC ratio shows profitability: 3:1 or higher is healthy
- Guides pricing strategy, feature prioritization, and market expansion

**Key nuances:**
- Higher LTV justifies higher CAC (you can afford to spend more on marketing)
- Should account for gross margin (SaaS gross margins are typically 70-80%)
- For low-churn products, LTV becomes massive—even small improvements in churn have outsized impact
- Payback period (CAC / monthly profit per customer) should be <12 months

**Example:** ARPU $100/month, 5% monthly churn, 80% gross margin → LTV ≈ $12,800

---

## Cohort Analysis

**Definition:** Segmenting customers into groups (cohorts) based on acquisition date or shared characteristics, then tracking their behavior over time.

**Why it matters:**
- Reveals whether product improvements actually improve retention
- Identifies which acquisition channels deliver better customers
- Detects seasonality or product quality changes over time
- Benchmarks "cohort X" against "cohort Y" to measure progress

**Key metrics tracked by cohort:**
- Retention rate by month (month 1, 2, 3... after acquisition)
- Churn per cohort
- Expansion revenue (upgrades/add-ons) by cohort
- LTV variation across cohorts

**How to read a cohort analysis:**
```
Cohort        M0    M1    M2    M3    M4    M5
Jan 2025     100%  92%   88%   85%   82%   80%
Feb 2025     100%  94%   91%   89%   87%    —
Mar 2025     100%  95%   93%    —     —     —
Apr 2025     100%  96%    —     —     —     —
```
(Each row shows retention; columns show months after signup)

**Interpretation:** Feb cohort has better retention curves than Jan—something improved.

**Types of cohorts:**
- **Temporal:** By signup date (month/quarter/year)
- **Behavioral:** By feature usage, plan tier, geography
- **Channel:** By acquisition source (organic, paid, partner)

**Example:** Lovable might cohort users by signup date to track whether retention improved after launching a key feature in their product.

---

## How These Metrics Connect

```
MRR/ARR
  ↓ (affected by)
Churn Rate ←→ LTV
  ↓ (enables)
CAC Budget
  ↑ (validates)
Cohort Analysis
```

**Real scenario:** 
- MRR growing but churn rising = unsustainable (need to fix retention before scaling)
- LTV/CAC ratio < 1 = losing money on each customer (broken unit economics)
- Best cohorts (low churn, high expansion) inform which segments to focus sales on

---

## Expected Challenges at Lovable

1. **Early-stage volatility:** With a small customer base, individual churn events dramatically move the percentage (e.g., 1 customer out of 20 = 5% monthly churn)

2. **Expansion vs. new:** Hard to separate organic MRR growth (expansion) from new customer growth (each tells different stories)

3. **Cohort sample sizes:** Recent cohorts won't have full retention curves yet—can't compare Jan 2025 cohort to Apr 2025 until Apr ends

4. **Definition ambiguity:** 
   - Is a trial user "churned" or never acquired?
   - Does pausing a subscription count as churn?
   - How to handle freemium → paid conversions in LTV?

5. **Channel attribution:** Especially for product-led growth (PLG), unclear which customer should be attributed to which cohort/channel

6. **Seasonality:** If Lovable has seasonal revenue patterns (e.g., more usage in certain quarters), annual metrics can obscure month-to-month drivers

7. **Low-churn products:** If churn is very low (<1-2%), LTV becomes so large it's almost meaningless as a decision driver—focus shifts to CAC payback period instead

---

## Questions to Ask at Lovable

- What's the current MRR/ARR and growth rate?
- What's the churn rate (and how is it defined)?
- How are they measuring expansion revenue vs. new customer revenue?
- Do they run cohort analyses? If so, what's the retention curve shape?
- What's the typical CAC payback period, and how does it vary by channel?
- Are they focusing on logo churn or revenue churn?
