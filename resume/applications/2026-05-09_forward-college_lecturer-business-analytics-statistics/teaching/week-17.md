# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 17: Optimisation Models
**Format:** 90-minute lab seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Formulate a simple linear programming (LP) problem from a business description: decision variables, objective function, and constraints
- Solve an LP model in Excel using Solver and interpret the output: optimal solution, shadow prices, and sensitivity report
- Identify when an LP model's feasibility assumption breaks — and what happens to the optimal solution when a constraint is violated
- Distinguish between binding and non-binding constraints and explain the business meaning of each

These map to ST2187 syllabus topic 14 (optimisation) and to the Block 4 arc: having modelled what happened (Weeks 16) and what might happen (Week 18), students here model what *should* happen given constraints.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 13 — read the following sections only:
- §13-2 Introduction to optimisation — decision variables, objective function, constraints (pp. 601–602)
- §13-3 A two-variable product mix model — formulation and graphical solution (pp. 602–615)
- §13-4 Sensitivity analysis — Solver's sensitivity report and shadow prices (pp. 615–626)
- §13-5 Properties of linear models — linearity assumption and binding constraints (pp. 626–629)

Students who completed the DecisionTools Suite setup in the course introduction should confirm that Excel Solver is enabled: Data tab → Solver. If it's not there, go to File → Options → Add-ins → Excel Add-ins → Solver Add-in.

**Videos (~20 minutes total):**
- [Linear Programming — Khan Academy](https://www.youtube.com/watch?v=Bzzqx1F23a8) (12 min) — graphical method. *Active watching: when the video identifies the feasible region (the area that satisfies all constraints), pause and write: what are the two types of boundaries that define it — and what makes a constraint "binding" vs "non-binding" at the optimal corner? This distinction is what T3 and T4 test.*
- [Excel Solver Tutorial](https://www.youtube.com/watch?v=dRm5MEoA3OI) (8 min) — Solver setup and sensitivity report. *Active watching: when the video shows the Solver sensitivity report (shadow prices and allowable ranges), pause and write: what does a shadow price tell you in business terms? The shadow price interpretation in the worked example is what T5 tests.*

**Worked example (read this before attempting the tutorial problems):**

> **Problem:** A bakery can produce two products: croissants and muffins. Production data:
>
> | | Croissants | Muffins |
> |---|---|---|
> | Oven time (min/unit) | 3 | 5 |
> | Labour time (min/unit) | 2 | 1 |
> | Profit (€/unit) | 1.50 | 2.00 |
>
> **Constraints:** oven available 240 min/day; labour available 80 min/day. Minimum production: 10 of each.
>
> **Decision variables:** C = croissants produced, M = muffins produced.
>
> **LP formulation:**
> Maximise: 1.5C + 2.0M
> Subject to:
> - 3C + 5M ≤ 240 (oven)
> - 2C + 1M ≤ 80 (labour)
> - C ≥ 10
> - M ≥ 10
>
> **Solver solution:** C = 25, M = 33; Profit = 37.5 + 66.0 = **€103.50**
>
> **Shadow prices (sensitivity report):**
> - Oven constraint shadow price = €0.35/minute: each additional minute of oven time adds €0.35 to maximum profit
> - Labour constraint shadow price = €0.55/minute: each additional minute of labour adds €0.55 to maximum profit
>
> **Business implication:** labour is more valuable than oven time. If you can hire one more baker (adding 60 minutes/day), you could increase profit by 60 × 0.55 = **€33/day**. Is that worth the hiring cost?

*This worked example is marked optional for students who feel confident formulating an LP (decision variables, objective function, constraints) and interpreting the Solver output (optimal values and shadow prices). If you can write the LP for T1 without guidance, you don't need it. If shadow prices felt abstract from the reading, read the worked example's sensitivity report section carefully before T2.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

*The Khan Academy video's feasible region is the graphical version of the constraint inequalities in this worked example — each constraint is one boundary line. The shadow price you noted from the Solver tutorial maps directly onto the worked example's labour shadow price (€0.55/min). The tutorials extend this.*

**Tutorial:**

*T1 — Formulation:*
> A logistics company has two warehouse locations (A and B) and must supply three retail stores (1, 2, 3). Transportation costs per pallet (€):
>
> | From\To | Store 1 | Store 2 | Store 3 |
> |---|---|---|---|
> | Warehouse A | 4 | 8 | 6 |
> | Warehouse B | 3 | 7 | 5 |
>
> Warehouse A has 120 pallets; Warehouse B has 80 pallets. Store 1 needs 70, Store 2 needs 90, Store 3 needs 40.
>
> (a) Define decision variables.
> (b) Write the objective function (minimise cost).
> (c) Write the supply constraints (each warehouse sends at most what it has).
> (d) Write the demand constraints (each store receives exactly what it needs).
> (e) What type of LP is this? (Transportation problem)

*T2 — Solver setup:*
> Set up the bakery problem from the worked example in Excel and run Solver. Verify the solution. Then:
>
> (a) Increase the oven time available to 260 minutes. What is the new optimal profit?
> (b) What is the profit increase from 20 additional minutes of oven time? Does this match the shadow price?
> (c) At what point does the shadow price for oven time stop being valid? (Find the allowable increase in Solver's sensitivity report.)

*T3 — Build and break:*
> The bakery receives an order requiring them to produce at least 30 muffins per day (not 10).
>
> (a) Update the model and find the new optimal solution.
> (b) Has the original binding constraint changed?
> (c) Is the new constraint binding or non-binding at the optimum?

**Additional tutorial questions (attempt after T1–T3 above):**

*T4 — Boundary case: what if a constraint is violated or the problem is infeasible:*

> Return to the bakery problem from the worked example. The original model:
> Maximise: 1.5C + 2.0M
> Subject to: 3C + 5M ≤ 240 (oven); 2C + 1M ≤ 80 (labour); C ≥ 10; M ≥ 10
>
> (a) Add the constraint that the bakery has received a special order requiring at least 40 muffins per day (M ≥ 40). Find the new optimal solution using Solver. Has the objective value changed?
>
> *Solution (approximate):* The binding constraints shift. With M ≥ 40 binding: oven: 3C + 200 ≤ 240 → C ≤ 13.33; labour: 2C + 40 ≤ 80 → C ≤ 20. Labour is non-binding; oven binding gives C = 13 (rounded down for feasibility or accept 13.33). Profit ≈ 1.5 × 13.33 + 2.0 × 40 = 20 + 80 = **€100 per day** (vs €103.50 without the M ≥ 40 constraint). The special order costs the bakery approximately €3.50/day in lost flexibility.
>
> (b) Now add a second order: the bakery must produce at least 30 croissants (C ≥ 30) AND at least 40 muffins (M ≥ 40). Check whether this is feasible. Verify algebraically.
>
> *Solution:* Check oven constraint: 3(30) + 5(40) = 90 + 200 = 290 > 240. **Infeasible** — the minimum requirements exceed oven capacity.
>
> (c) What does infeasibility mean in the real-world business context? What options does the bakery have when Solver returns "No feasible solution"?
> (d) Suppose the bakery can rent additional oven time at €0.50 per minute. How many additional minutes of oven time must be rented to make the model in (b) feasible? What is the minimum cost of renting this capacity?
>
> *Solution:* Needs 290 − 240 = 50 additional minutes. Cost = 50 × €0.50 = **€25/day.** This should be compared against the profit from fulfilling both orders.
>
> (e) Explain why shadow prices from the original optimal solution cannot be used to calculate the cost of becoming feasible in this case. (Hint: the shadow price is valid only within the allowable range; the required oven increase exceeds the allowable range.)

*T5 — Interpretation: reading shadow prices and sensitivity ranges:*

> A printing company uses Solver to optimise its weekly production of two products: brochures and posters. The Solver sensitivity report shows:
>
> | Constraint | Shadow Price | Current RHS | Allowable Increase | Allowable Decrease |
> |---|---|---|---|---|
> | Machine hours | €18.50/hour | 120 hours | 40 hours | 30 hours |
> | Paper stock | €0/kg | 800 kg | 1E+30 (unlimited) | 200 kg |
> | Min brochures | −€4.20 | 50 | 20 | 50 |
>
> (a) The shadow price on machine hours is €18.50/hour. Interpret this in business terms.
> (b) The shadow price on paper stock is €0. What does this tell you about the paper stock constraint? Is the company using all its paper?
> (c) The shadow price on the minimum brochures constraint is −€4.20. Why is this negative? What does a negative shadow price on a minimum constraint mean?
> (d) If the company can rent 50 additional machine hours from a partner firm at €15/hour, is it worth doing? Show your calculation.
>
> *Solution:* The additional profit from 40 hours (allowable increase) = 40 × €18.50 = €740. Cost = 40 × €15 = €600. Net gain = **€140** — worth it. For the next 10 hours (hours 41–50, outside the allowable range), the shadow price may have changed; cannot assume €18.50 applies.
>
> (e) What happens to the shadow price on machine hours if the company adds a new product line that also uses machine hours? Does the shadow price increase, decrease, or could it go either way? What would you need to rerun to find out?

*T6 — Multi-step: transportation problem formulation and solving:*

> Complete the transportation problem from T1. Use Solver to find the optimal shipping plan for the logistics company.
>
> Recall: Warehouse A has 120 pallets, Warehouse B has 80 pallets. Store 1 needs 70, Store 2 needs 90, Store 3 needs 40. Transportation costs:
>
> | From\To | Store 1 | Store 2 | Store 3 |
> |---|---|---|---|
> | Warehouse A | €4 | €8 | €6 |
> | Warehouse B | €3 | €7 | €5 |
>
> (a) Set up the Solver model with 6 decision variables (A1, A2, A3, B1, B2, B3) and run it. What is the optimal total shipping cost?
>
> *Solution:* Set up: Minimise 4A1 + 8A2 + 6A3 + 3B1 + 7B2 + 5B3. Subject to: A1+A2+A3 ≤ 120; B1+B2+B3 ≤ 80; A1+B1 = 70; A2+B2 = 90; A3+B3 = 40; all variables ≥ 0. One typical optimal solution: A1 = 0, A2 = 90, A3 = 30, B1 = 70, B2 = 0, B3 = 10. Cost = 0 + 720 + 180 + 210 + 0 + 50 = **€1,160.**
>
> (b) Identify which warehouse constraint is binding and which is non-binding in the optimal solution. What does a non-binding supply constraint mean?
> (c) The shadow price for Store 2's demand constraint is €7 (the cost of supplying one additional pallet to Store 2). Store 2 requests an additional 10 pallets (demand increases to 100). What is the expected increase in total shipping cost?
>
> *Solution:* 10 × €7 = **€70** (valid if within the allowable range for this constraint).
>
> (d) Warehouse A faces a capacity reduction from 120 to 90 pallets due to a flood. Can the remaining supply (90 + 80 = 170 pallets) still meet total demand (70 + 90 + 40 = 200 pallets)? What does Solver return? What are the business options?
> (e) A new shipping route from Warehouse B to Store 2 becomes available at €6/unit (slightly cheaper than the current €7). Does Solver incorporate this automatically, or must the model be updated? After updating, does the optimal shipping plan change?

*T7 — Comparison: LP versus heuristic decision-making:*

> A hospital must assign nurses to three 8-hour shifts (morning, afternoon, night) for a week. Minimum nursing cover required per shift: morning 12 nurses, afternoon 10 nurses, night 8 nurses. Available nurses: 25 total. Each nurse works exactly 5 shifts per week. The hospital wants to minimise overtime (hours worked beyond 40 per week per nurse).
>
> The hospital has historically used a heuristic: the head nurse assigns nurses based on experience and requests. This takes about 2 hours per week of planning time and routinely results in 3–4 nurses working overtime.
>
> (a) Formulate this as a linear programming problem. What are the decision variables, the objective function, and the constraints?
> (b) If an LP solution finds a schedule with 1 nurse working overtime (instead of 3–4), is the LP solution definitely better? What does "better" mean here?
> (c) The LP model ignores nurse preferences (some nurses dislike night shifts), seniority rules (senior nurses have priority for preferred shifts), and the fact that two specific nurses refuse to work consecutive night shifts. How would you incorporate these factors, and what type of constraint do they require?
> (d) The head nurse says: "The LP doesn't understand the human side of scheduling." Is this a valid critique of the LP approach, or a misunderstanding of what LP is designed to do?
> (e) In what sense is the heuristic approach (head nurse's experience) also an "optimisation model"? What is its implicit objective function, and what are its constraints?

*T8 — Real-world translation: LP constraints in airport slot allocation (2025 context):*

> In 2025, the UK's Competition and Markets Authority (CMA) and the Civil Aviation Authority (CAA) were reviewing the rules governing takeoff and landing slot allocation at London Heathrow and Gatwick airports. Heathrow operates at or near its 480,000 annual flight slots limit — a binding regulatory capacity constraint. Airlines that hold slots (including BA/IAG, Lufthansa, United) assign very high values to them; slots at Heathrow have reportedly traded at over $50 million per pair in secondary markets.
>
> Suppose a simplified version of Heathrow's slot allocation problem for a single day (one terminal, 120 available slots for a 12-hour operating window):
>
> - Three airline categories: long-haul international (L), short-haul European (E), and domestic UK (D)
> - Minimum slot requirements (regulatory): L ≥ 20, E ≥ 15, D ≥ 10 (at least these numbers must be accommodated)
> - Maximum capacity: L + E + D ≤ 120
> - Revenue per slot to Heathrow (landing fees + associated income): L = €15,000, E = €8,000, D = €3,500
> - Environmental constraint (noise limits after 11pm): night slots for L capped at 8 per day (a constraint separate from the 120 total)
>
> (a) Define decision variables and write the LP formulation (objective function + all constraints).
>
> (b) Find the optimal number of each slot type by solving the LP. What is the maximum daily revenue, and which slot type does the optimum favour?
>
> *Indicative solution:* Without the night-slot constraint, the LP maximises revenue by maximising L (€15k/slot). Subject to L + E + D ≤ 120, L ≥ 20, E ≥ 15, D ≥ 10: set E = 15, D = 10, L = 95. Revenue = 95 × 15,000 + 15 × 8,000 + 10 × 3,500 = 1,425,000 + 120,000 + 35,000 = **€1,580,000.**
>
> (c) The minimum slot requirements (L ≥ 20, E ≥ 15, D ≥ 10) exist because of policy obligations — domestic connectivity and European competition rules — not revenue optimisation. Which constraints are binding and which are non-binding at the optimum? What does a non-binding minimum constraint mean in this context?
>
> (d) The shadow price on the total capacity constraint (L + E + D ≤ 120) is €15,000 — the value of one additional slot to Heathrow is equal to the revenue from one more long-haul flight. Why does the shadow price equal the long-haul revenue rate (not a weighted average)? What would have to be different for the shadow price to be lower?
>
> (e) A policy proposal suggests mandating that at least 25% of daily slots go to domestic flights (D ≥ 30). Reformulate the model with this constraint and re-solve. What is the cost of this policy to Heathrow's revenue? Express it as (i) a change in total daily revenue and (ii) a shadow price per additional domestic slot mandated.
>
> (f) Heathrow's actual slot allocation problem has thousands of variables (individual flight movements, terminal assignments, stand assignments, time-of-day variation, airline-specific constraints) and is a mixed-integer programme, not a simple LP. What limitation of the LP formulation above would become most problematic at the real-world scale — and what would an analyst need to add?

This question uses a verified 2025 policy context: the CMA and CAA review of Heathrow/Gatwick slot allocation is documented in their published market studies (cma.gov.uk, caa.co.uk). The secondary market price figures are from published aviation industry reports. The simplified LP is designed to make the constraint concepts concrete — binding vs non-binding, shadow prices, and policy cost trade-offs — in a context where real decisions with real values are being made.

---

## Answer Key

### T1 — LP formulation (transportation problem)

**(a)** Decision variables: Xᵢⱼ = number of pallets shipped from warehouse i to store j. Six variables: X_A1, X_A2, X_A3 (from Warehouse A), X_B1, X_B2, X_B3 (from Warehouse B).

**(b)** Objective (minimise cost): Minimise 4X_A1 + 8X_A2 + 6X_A3 + 3X_B1 + 7X_B2 + 5X_B3.

**(c)** Supply constraints: X_A1 + X_A2 + X_A3 ≤ 120 (Warehouse A capacity); X_B1 + X_B2 + X_B3 ≤ 80 (Warehouse B capacity).

**(d)** Demand constraints: X_A1 + X_B1 = 70 (Store 1 must receive exactly 70); X_A2 + X_B2 = 90 (Store 2 must receive exactly 90); X_A3 + X_B3 = 40 (Store 3 must receive exactly 40). Non-negativity: all Xᵢⱼ ≥ 0.

**(e)** This is a **transportation LP** — a special structure where each decision variable appears in exactly one supply constraint and one demand constraint. The total supply (200) equals total demand (200), making this a balanced transportation problem. It can be solved with the transportation simplex method or standard LP.

---

### T2 — Solver setup (bakery)

**(a)** After increasing oven time to 260 minutes: Solver adjusts the optimal mix. Using shadow price as a quick estimate: 20 extra minutes × €0.35/min = €7.00 more profit → predicted new profit ≈ €103.50 + €7.00 = **€110.50.** (Verify with Solver for exact answer, which should match if 260 is within the allowable range.)

**(b)** Profit increase = €110.50 − €103.50 = **€7.00 = 20 × €0.35** — yes, this matches the shadow price exactly (within the allowable range).

**(c)** The shadow price for oven time is valid only within the **allowable increase** shown in Solver's sensitivity report. If the allowable increase is, say, 30 minutes: the shadow price of €0.35/min applies for oven time up to 270 minutes. Beyond that, the optimal basis changes (a different constraint becomes binding or the current binding constraints shift) and the shadow price may change. To find a new profit estimate beyond the allowable range, Solver must be rerun with the new constraint value.

---

### T3 — Build and break (muffin constraint update)

**(a)** Adding M ≥ 30: Solver finds a new optimal. With the tighter muffin minimum, the feasible region shrinks. The new optimal will produce exactly 30 muffins (if the M ≥ 30 constraint is binding) or more (if it's not). From the original solution (M ≈ 33), M ≥ 30 is already satisfied — the constraint is **not binding** at the original optimum (the original solution produced 33 muffins, already above 30). The optimal solution and profit are **unchanged** by adding M ≥ 30 if the original optimum already has M > 30.

**(b)** The original binding constraints were the oven and/or labour constraints (at the optimal corner point). These remain unchanged since the M ≥ 30 constraint is non-binding.

**(c)** The new M ≥ 30 constraint is **non-binding** at the optimum — the optimal solution produces 33 muffins, which exceeds 30. A constraint is non-binding (slack) when the optimal solution satisfies it with room to spare: the constraint does not restrict the optimal solution.

---

### T4 — Boundary case: infeasibility

**(a)** With M ≥ 40 binding: oven constraint gives C ≤ (240 − 5×40)/3 = 40/3 ≈ 13.33; labour gives C ≤ (80 − 40)/2 = 20. Binding constraint is oven. Optimal: C ≈ 13.33, M = 40. Profit ≈ 1.5 × 13.33 + 2.0 × 40 = 20 + 80 = **€100/day.** The special order costs approximately €3.50/day in lost profit relative to the unconstrained optimum (€103.50).

**(b)** Feasibility check for C ≥ 30 AND M ≥ 40: oven check: 3(30) + 5(40) = 90 + 200 = 290 > 240. **Infeasible** — minimum requirements alone exceed oven capacity.

**(c)** Infeasibility means there is no production plan that satisfies all constraints simultaneously. In real business terms: the bakery cannot fulfil both special orders with its current oven capacity. Options: (i) negotiate to reduce one or both order minimums; (ii) rent additional oven time; (iii) prioritise one order over the other (decide which constraint to relax); (iv) invest in additional oven capacity. Solver returns "No feasible solution" — this is the correct answer and should be communicated to the client, not suppressed.

**(d)** Needs 290 − 240 = **50 additional oven minutes** to make the model feasible at the minimum requirements. Renting cost = 50 × €0.50 = **€25/day.** This is the cost of *becoming feasible* — the profit from fulfilling both orders must exceed €25/day for renting to be worthwhile.

**(e)** Shadow prices are valid only within the **allowable increase/decrease range** shown in the sensitivity report. The allowable increase for oven time in the original problem (let's say it was 20 minutes at a shadow price of €0.35/min) would give a cost estimate of 20 × €0.35 = €7. But making the infeasible model feasible requires 50 additional minutes — well outside any reasonable allowable range. At 50 minutes, the binding constraints have changed completely (the minimum M ≥ 40 and C ≥ 30 constraints are now active, not the oven constraint alone), so the shadow price from the original optimal basis is no longer applicable. The model must be rerun with the new capacity.

---

### T5 — Shadow prices and sensitivity ranges (printing company)

**(a)** Shadow price on machine hours = €18.50/hour: **for each additional machine hour available (within the allowable range of 40 hours), maximum weekly profit increases by €18.50.** This means machine hours are a binding constraint — the company is using all 120 available hours and is capacity-constrained. Each additional hour is worth €18.50 in extra contribution.

**(b)** Shadow price on paper stock = €0: paper stock is a **non-binding constraint** — the company is not using all 800 kg of available paper. The slack (unused paper) means the paper constraint does not restrict the optimal solution. Adding or removing paper (within the allowable decrease of 200 kg) would not change the optimal profit.

**(c)** The shadow price on the minimum brochures constraint (min 50) is **negative (−€4.20):** this means each additional unit of the minimum requirement *reduces* maximum profit by €4.20. A minimum constraint forces the model to produce something it would not otherwise produce at the optimum. The company would prefer to produce fewer than 50 brochures (brochures are less profitable than posters given machine hour limitations), but the minimum requirement forces some machine capacity toward brochures. Relaxing the minimum (reducing it) would increase profit; tightening it (increasing it) would decrease profit. Negative shadow prices on minimum (lower-bound) constraints are the norm — they reflect the opportunity cost of the forced production.

**(d)** Allowable increase is 40 hours. For 40 additional hours at €18.50: Profit increase = 40 × €18.50 = **€740.** Cost = 40 × €15 = **€600.** Net gain = **€140 — worth renting.** For hours 41–50 (beyond the allowable range), the shadow price may change; cannot assume €18.50. To evaluate the full 50 hours, rerun Solver with 170 machine hours.

**(e)** Adding a new product line that also uses machine hours could increase or decrease the shadow price — it depends on the new product's profit contribution per machine hour. If the new product has higher profit per machine hour than existing products, the opportunity cost of machine hours rises (shadow price increases). If lower, it competes for the binding resource less efficiently (shadow price stays the same or decreases). Crucially: you must **rerun Solver** with the new product included as a decision variable to find the new optimal and updated shadow prices. The existing sensitivity report is invalid as soon as the model structure changes.

---

### T6 — Transportation problem solution

**(a)** Optimal Solver solution (one optimal — multiple optima may exist for transportation problems): A1=0, A2=90, A3=30, B1=70, B2=0, B3=10. Total cost = 0×4 + 90×8 + 30×6 + 70×3 + 0×7 + 10×5 = 0 + 720 + 180 + 210 + 0 + 50 = **€1,160.**

**(b)** In the optimal solution: Warehouse A ships A2=90 + A3=30 = 120 pallets — all of its 120 pallets → **binding** (uses full capacity). Warehouse B ships B1=70 + B3=10 = 80 pallets — all of its 80 pallets → **binding** (uses full capacity). Both supply constraints are binding in this balanced problem (total supply = total demand = 200). A non-binding supply constraint would mean the warehouse ships fewer pallets than its capacity — it has slack capacity.

**(c)** Shadow price = €7/pallet for Store 2. Store 2 requests 10 more pallets: expected cost increase = 10 × €7 = **€70.** This is valid if 10 is within the allowable increase for Store 2's demand constraint.

**(d)** With Warehouse A reduced to 90: total supply = 90 + 80 = 170 pallets < total demand = 200 pallets. **Supply is insufficient** — the model is infeasible (cannot meet all demand). Solver returns "No feasible solution." Business options: (i) prioritise which stores receive partial shipment; (ii) source additional stock externally; (iii) renegotiate delivery commitments with one or more stores; (iv) switch to a partial-fulfilment model with backorders.

**(e)** Solver does not update automatically — the model must be **updated** manually (change the B-to-2 cost from €7 to €6 in the cost matrix). After updating and rerunning Solver: the cheaper route from B to Store 2 may become attractive. With B2 at €6 (now equal to A3's cost), the optimal plan may shift some Store 2 supply from Warehouse A to Warehouse B. The new optimal cost will be ≤ €1,160 (since a cheaper route is now available). Exact new allocation depends on the full LP solution — run Solver to confirm.

---

### T7 — LP vs heuristic (nurse scheduling)

**(a)** Decision variables: let M, A, N = number of nurses assigned to morning, afternoon, night shifts per day (simplified; a full model would have 7 × 3 = 21 variables for a week). Objective: minimise total overtime hours = Σ max(0, hours_worked_by_nurse − 40) per week. Constraints: M ≥ 12, A ≥ 10, N ≥ 8 (minimum cover); total nurse-shifts per week = 25 nurses × 5 shifts = 125 assignments; no nurse works more shifts than allowed. (Full formulation requires binary or integer variables for individual nurse-shift assignments.)

**(b)** Whether LP is "better" depends on the definition of better. **Fewer overtime hours** is one objective, but nursing scheduling also involves: nurse preferences (impacts retention), patient safety (experienced nurses on critical shifts), fairness (equitable distribution of undesirable shifts), regulatory compliance (minimum rest periods). If "better" means minimising overtime only, LP wins. If "better" means total cost including recruitment, retention, and care quality, LP needs to incorporate those objectives explicitly — or it may produce a technically optimal schedule that is operationally impractical.

**(c)** To incorporate nurse preferences: add preference scores as weighted objectives (multi-objective LP). Seniority rules: add priority constraints (e.g., senior nurse S1 must receive first choice of shifts before junior nurses). "Nurse A and B refuse consecutive night shifts": add binary constraints (if nurse A works night on Monday, they cannot work night on Tuesday). These require **integer or binary variables**, converting the LP to a Mixed Integer Program (MIP). MIP is significantly harder to solve than LP and requires specialised solvers (Excel Solver can handle small MIPs).

**(d)** The critique is partially valid but misses the point: the LP is designed to minimise overtime, not to optimise every human dimension of scheduling. The correct response to "the LP doesn't understand the human side" is: "You're right — so let's add those constraints to the model." The LP is a tool that optimises what you specify; the art is specifying the right constraints and objectives. Dismissing LP because it ignores preferences is not a valid critique of LP — it is a reminder to encode more of the problem structure into the model.

**(e)** The head nurse's heuristic is an implicit optimisation model: the objective function is something like "maximise nurse satisfaction and coverage quality, subject to meeting minimum staffing, seniority norms, and known preferences." The constraints are the head nurse's mental model of what is acceptable. The heuristic is faster (2 hours vs model setup time) and captures soft constraints implicitly — but it cannot guarantee optimality, scales poorly to larger hospitals, and its "objective function" may drift over time based on the head nurse's changing priorities. LP makes the objective explicit and finds the optimum systematically.

---

### T8 — Airport slot allocation LP (Heathrow 2025)

**(a)** Decision variables: L = number of long-haul slots; E = number of short-haul European slots; D = number of domestic slots.
Objective: Maximise 15,000L + 8,000E + 3,500D.
Constraints: L + E + D ≤ 120 (total capacity); L ≥ 20; E ≥ 15; D ≥ 10; L_night ≤ 8 (night long-haul cap — note this is a separate constraint on a subset of L, requiring an additional variable or approximation); all variables ≥ 0.

**(b)** Without the night constraint, the LP maximises revenue by maximising L (highest revenue per slot). Setting E = 15 (minimum), D = 10 (minimum): L = 120 − 15 − 10 = **95.** Revenue = 95 × €15,000 + 15 × €8,000 + 10 × €3,500 = €1,425,000 + €120,000 + €35,000 = **€1,580,000.** The optimum favours **long-haul slots** exclusively beyond the minimum requirements for E and D.

**(c)** At the optimum: L = 95 (constraint was L ≥ 20 — not binding, L is 95 >> 20); E = 15 (constraint E ≥ 15 — **binding**, E is at its minimum); D = 10 (constraint D ≥ 10 — **binding**, D is at its minimum). A non-binding minimum constraint means the LP's optimal solution naturally satisfies the minimum without being constrained by it — Heathrow would allocate at least that many long-haul slots anyway for revenue reasons. The binding minimum constraints on E and D mean these are the only European and domestic slots allocated — the LP would prefer fewer if regulations allowed.

**(d)** The shadow price on total capacity = €15,000/slot because at the optimum, the marginal slot is allocated to long-haul (the highest-revenue type). Adding one more slot to the 120-slot total frees space for one more long-haul flight, earning €15,000. The shadow price would be lower (a weighted average) only if the marginal slot could not all go to long-haul — for example, if a policy constraint required proportional allocation across all three types, or if the night-cap constraint were binding and prevented more long-haul flights.

**(e)** With D ≥ 30 added: D = 30, E = 15 (minimums bind), L = 120 − 30 − 15 = 75. Revenue = 75 × €15,000 + 15 × €8,000 + 30 × €3,500 = €1,125,000 + €120,000 + €105,000 = **€1,350,000.** (i) Change in daily revenue: €1,350,000 − €1,580,000 = **−€230,000/day.** (ii) Shadow price per additional domestic slot mandated: each domestic slot replaces one long-haul slot (revenue difference = €15,000 − €3,500 = **€11,500 lost per slot**). The shadow price on the D ≥ 30 constraint ≈ −€11,500 per additional domestic slot required.

**(f)** The most problematic limitation at real-world scale: the LP treats decision variables as **continuous** (fractional slots are allowed). At scale, slots are integer-valued (you cannot assign 0.3 of a flight) and must be assigned to specific time windows, terminals, and stands. The real problem is a Mixed Integer Programme (MIP) with discrete time slots, equipment compatibility constraints (not all aircraft fit all stands), airline-specific agreements, noise curfews at specific hours, sequencing constraints (arrival/departure separation minima), and safety regulations. An analyst would need to add binary/integer variables for individual slot assignments, time-indexed decision variables (one per slot per hour), and compatibility constraint sets for each aircraft type.

---

## In-Class Session (90 minutes)

### Part 1 — Opening Challenge (10 minutes)

The instructor projects a brief business description:

> "A consulting firm has 3 senior consultants and 5 junior consultants. Senior consultants earn €120/hour and bill clients at €200/hour; juniors earn €60/hour and bill at €120/hour. The firm has 40 billable hours available this week per consultant. A major client requires at least 30 hours of senior work and at least 50 hours of junior work. The firm wants to maximise net revenue (billing − salary costs)."

Students have 3 minutes to write: What are the decision variables? What is the objective function? What are the constraints?

After 3 minutes: volunteers share formulations. The class identifies which are complete, which are missing constraints, and which used the wrong objective function (billing revenue vs net revenue is a common error — students who write "maximise 200S + 120J" rather than "(200−120)S + (120−60)J" have missed the cost side).

This is a formulation exercise, not a solving exercise. The learning at this stage is in translating prose into algebra.

---

### Part 2 — Live Solver Demo (20 minutes + 10 minutes buffer)

Instructor sets up the bakery model in Excel live. Steps:
1. Set up a table: decision variables (cells for C and M), objective function cell, constraint cells
2. Open Solver: Data → Solver
3. Set objective (maximise profit cell), by changing variable cells (C and M)
4. Add constraints: each one individually
5. Run → OK → examine solution
6. Request sensitivity report: "Keep Solver Results" and check "Sensitivity"

**Teaching moments:**
- Solver requires a starting value in the variable cells — it is not symbolic, it is numerical. Start with 0 or 1, not blank.
- Integer constraints: LP allows fractional solutions (25.7 croissants). If units must be whole numbers, add integer constraint — but this makes the problem harder (Integer LP). For this course, allow continuous.
- Sensitivity report: shadow prices and allowable ranges. Shadow price applies only within the allowable range. Outside that range, the optimal basis changes and the shadow price is no longer valid.

Buffer: work through T2 (increasing oven time to 260 minutes) live. Verify that the profit increase matches 20 × shadow price. This is the most satisfying moment in LP for most students — seeing the mathematical prediction confirmed.

---

### Part 3 — Build-and-Break (25 minutes)

**Orientation (5 minutes before pairs start):** Linear programming is new for most students and has no analogue in descriptive statistics, inference, or regression. Before pairs begin, the instructor writes on the board:

> Every LP has exactly three things: **what you control** (decision variables), **what you want** (objective function), **what you can't change** (constraints). Formulation is naming all three. Solving is finding the values of the decision variables that optimise the objective without violating any constraint.

Ask the room: "In the bakery example — what are the three things?" Students name them from the worked example: C and M (control); profit (want); oven and labour limits (can't change). This confirms understanding before pairs attempt their own scenario. Students who can't name them correctly need the 5 minutes; students who can will still benefit from the discipline of stating it explicitly.

This orientation is not a repeat of the live demo — it is a formulation-first frame. The demo showed how to operate Solver; this confirms students can translate a business description into the three components before they have to do it themselves.

Each pair builds and breaks an LP model. "Break" means: find a change to the constraints or objective that makes the model infeasible, unbounded, or dramatically changes the optimal solution.

**Dataset:** each pair receives a different business scenario (pre-prepared cards or a shared document). Example scenarios:
- Staff scheduling: assign staff to shifts to meet demand while minimising cost
- Portfolio allocation: allocate €100,000 across 4 investments to maximise expected return subject to risk constraints
- Product mix: 5 products, 4 resources, maximise profit

Each pair must:
1. Formulate and solve their LP (15 minutes)
2. Find one constraint change that makes the problem infeasible (5 minutes)
3. Find one constraint change that makes the current binding constraint non-binding (5 minutes)

The infeasibility test: changing the minimum demand requirements or maximum resource constraints to values that can't simultaneously be satisfied. Infeasibility is not an error — it tells you the problem as specified cannot be solved. The real-world meaning: the plan is impossible. The fix is to relax a constraint or reduce the objective aspiration.

---

### Part 4 — Peer Presentation (20 minutes)

Two pairs present:
- Their business scenario
- Their formulation (objective, variables, constraints)
- Their optimal solution and what it means in business terms
- The constraint they broke — and what the infeasibility means for the business

The rest of the class asks: "Is there a constraint you missed?" This is the most common LP error: the modeller forgot a real-world constraint, and the optimal solution looks good mathematically but violates something obvious (e.g., the model says hire 2.7 staff members, or produce negative units of a product).

---

### Part 5 — Debrief (10 minutes)

**Close the loop:**

*"What is LP actually doing — and what are the three things it assumes?"*

1. The objective function is linear (constant returns — each unit of X contributes the same profit regardless of how many you produce)
2. The constraints are linear (resource consumption per unit is constant)
3. The solution can be fractional — or integer, if integer constraints are added

All three assumptions break in real business situations. The LP solution is a bound: the best you could possibly do if the world were this simple. Reality is more constrained.

**Bridge to Week 18:**

> *"LP finds the best outcome in a deterministic world. But next week: what if the inputs aren't fixed? The profit per unit might vary by ±20%. The resource capacities might fluctuate. What's the optimal decision if everything is probabilistic? That's Monte Carlo simulation."*

---

## After Class (Student Post-Work)

No LMS post. The LP model (Excel file with Solver setup and sensitivity report) is the lab output. Students who want to extend: reformulate their pair scenario with at least one integer constraint and compare the integer solution to the continuous relaxation. How different are they?

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Formulation challenge precedes solving | Lovett & Greenhouse (2000): the cognitive bottleneck in LP is not computation (Solver handles that) but formulation; the opening challenge puts formulation first, signalling its primacy |
| Build-and-break as core activity | Bjork (1994): studying failure cases (infeasibility) is more memorable than studying correct examples; finding the constraint that breaks the model reveals its assumptions more clearly than explaining them |
| Shadow price verified live against numerical test | Confirmation by example is more convincing than derivation for most business analytics students; seeing that 20 × 0.35 = €7 additional profit matches the Solver output is the "it works" moment |
| Five different business scenarios for pairs | Variability of practice (Bjork, 1994): different domains (scheduling, portfolio, product mix) deepen LP schema formation more than five versions of the same problem |
| No Mentimeter this week | Block 4 lab format: opening formulation challenge is more diagnostic than multiple-choice for this content |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Opening formulation challenge | 10 min | 3 min individual + class review of formulation errors |
| Live Solver demo | 20 min | Bakery model from scratch; sensitivity report |
| Buffer (explicit) | 10 min | T2 live verification; shadow price explanation |
| Build-and-break | 25 min | 15 min formulate and solve; 10 min break scenarios |
| Peer presentation | 20 min | Two pairs; "constraint you missed?" challenge |
| Debrief | 10 min | Three LP assumptions; bridge to Week 18 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Excel Solver setup is finicky and prone to common errors.

Students who set up constraints incorrectly (wrong inequality direction, missing constraints, wrong objective cell) will get wrong or infeasible results. Debugging Solver errors in a group setting is time-consuming.

**Resolution:** the live demo in Part 2 is the model to follow. Students who reproduce the demo setup before attempting their own scenario are less likely to make structural errors. The 10-minute buffer is partially reserved for Solver debugging.

---

### 2. Fractional solutions will seem absurd to students in some contexts.

If the model says produce 33.2 muffins or hire 2.7 people, students will ask "can we just round?" Rounding may violate constraints (rounding up could exceed resource limits; rounding down may miss demand requirements).

**Resolution:** acknowledge it directly: "In the continuous LP, fractional solutions are allowed. If you add integer constraints, Solver uses a different algorithm (branch and bound) and may take longer. For this course, accept continuous solutions and note that rounding introduces a small error." The professional answer is: for most business contexts, the continuous solution rounded to the nearest whole number is good enough; for contexts where fractions are genuinely impossible (staff scheduling), specify integer variables.

---

### 3. Shadow prices are only valid within the sensitivity range.

Students who compute "each additional minute of oven time adds €0.35, so 200 more minutes adds €70" are extrapolating beyond the allowable range. The shadow price changes when the basis changes.

**Resolution:** demonstrate live: add a large increase to oven time (say, 400 minutes) and observe that the shadow price in the new sensitivity report has changed. The allowable range from the first Solver run is the range within which the shadow price is constant — beyond that, recalculate.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Corrections + Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapters 13–14

Chapter 13 references are accurate (13-2 through 13-5, correct pages). But **three of the tutorials teach Chapter 14 content with only Chapter 13 assigned:**

- T1/T6 (transportation problem) = **§14-4a Transportation Models (p. 677)**
- T7 (nurse scheduling) = **§14-2 Employee Scheduling Models (p. 663)**
- T7(c)'s binary-constraints answer and T8(f)'s MIP discussion = **§14-7 Integer Optimization Models (p. 714)**

*Fix:* add §14-4a as required reading and cite 14-2/14-7 as "the textbook's fuller versions" in the relevant answer keys. Also: §13-6 (Infeasibility and Unboundedness, p. 629) is *exactly* the topic of T4 and Part 3's "break" task, and it's two pages — assign it. Finally, the pre-work's "DecisionTools Suite setup" is a mislabel: Solver is native Excel; DecisionTools is the Palisade add-in suite (PrecisionTree/@RISK, relevant Weeks 10/18). Correct the name so students don't hunt for the wrong installer.

## 2. Corrections to the Worked Example (must fix before use) + Extended Questions

**The worked example's printed solution is infeasible, and its business conclusion is backwards.**

- The claimed optimum C = 25, M = 33 violates the labour constraint: 2(25) + 33 = **83 > 80**.
- The true continuous optimum is at the oven∩labour intersection: 3C + 5M = 240 and 2C + M = 80 give **C ≈ 22.86, M ≈ 34.29, profit ≈ €102.86** (not €103.50).
- Solving the dual at that corner: **oven shadow price ≈ €0.357/min; labour shadow price ≈ €0.214/min** — not €0.35 and €0.55. So the punchline "labour is more valuable than oven time" is **reversed**: oven time is the scarcer resource. The hiring example becomes: one more baker (60 min) adds 60 × 0.214 ≈ **€12.86/day**, not €33 — and the sharper question is what the bakery would pay for more *oven* time.
- Cascades to fix: T2(a) new profit at 260 oven minutes = **€110.00** (102.86 + 20 × 0.357; Solver gives C = 20, M = 40 exactly); T2(c)'s allowable increase for the oven RHS runs to 330 minutes (where C hits its 10-unit floor); T4(a)'s "cost of the special order" = 102.86 − 100 = **€2.86/day**, not €3.50.

*Why this matters more than any other error in the 22 weeks:* every tutorial (T2, T3, T4) and the live demo rebuild this exact model, and students will watch Solver contradict the handout in the session's first ten minutes. Re-run once in Excel and reprint all dependent numbers.

**T9 — Unboundedness (completes the trio the objectives promise):**

> A junior analyst formulates the bakery model but forgets both capacity constraints, keeping only C ≥ 10, M ≥ 10.
>
> (a) What does Solver report, and what does it mean?
> (b) Infeasibility says "the plan is impossible." What does unboundedness say about the *model* (not the world)?
> (c) Give the one-line diagnostic habit for each of Solver's three outcomes (optimal / infeasible / unbounded).
>
> **Answers:** (a) "Objective Cell values do not converge" — profit can grow without limit because nothing restricts production. (b) Unboundedness is always a *modelling* error in business problems: the real world has capacity somewhere, so an unbounded LP means a real constraint was left out (infeasibility can be real; unboundedness never is). (c) Optimal → check the solution against common sense (fractional staff? negative production?); infeasible → ask which constraint to relax and at what price (T4(d)); unbounded → hunt for the missing constraint.

**T10 — Rounding trap (grounds Design Challenge 2 in a computation):**

> A continuous LP returns x₁ = 3.6, x₂ = 4.8 with constraint 5x₁ + 4x₂ ≤ 37.2 binding.
>
> (a) The analyst rounds to (4, 5). Feasible?
> (b) The analyst rounds down to (3, 4). Feasible but is it optimal among integer points?
> (c) What does this imply about "just round the LP answer"?
>
> **Answers:** (a) 5(4) + 4(5) = 40 > 37.2 — **infeasible**; rounding up broke the binding constraint. (b) Feasible (31 ≤ 37.2) but leaves slack 6.2 — likely dominated by, e.g., (3, 5): 35 ≤ 37.2, higher objective. (c) Rounding can break feasibility *or* discard profit; near-binding constraints make naive rounding unsafe, which is precisely why integer programming (branch and bound, §14-7) exists. For loose constraints, rounding is fine — the skill is knowing which regime you're in.

**T11 — Blending mini-problem (one more Ch14 structure, 10 minutes):**

> A feed producer blends two ingredients (A: €0.30/kg, 12% protein; B: €0.50/kg, 28% protein) into 1,000 kg of feed that must average ≥ 20% protein.
>
> (a) Formulate and solve by hand.
> (b) The shadow price on the protein constraint has what units, and what business decision does it price?
>
> **Answers:** (a) A + B = 1,000; 0.12A + 0.28B ≥ 200 → binding: 0.12A + 0.28(1000−A) ≥ 200 → 280 − 0.16A ≥ 200 → A ≤ 500. Cost-minimising: A = 500, B = 500, cost = 150 + 250 = **€400**. (b) €/percentage-point of required protein (per 1,000 kg): it prices the *specification itself* — exactly what a customer asks when negotiating quality standards ("what would you charge me for 21% instead of 20%?"). Blending (A&W §14-3) is the classic LP family the session otherwise skips.

## 3. Alternative In-Class Activities (additional options)

**A. Graphical solve on paper first (10 min, before the Solver demo).** Pairs shade the bakery's feasible region on printed axes and slide a ruler (the iso-profit line) until it leaves the region. The corner-point principle — the optimum is always at a vertex — is *seen* rather than asserted, and students immediately understand why Solver's answer lands where it does. (This is §13-3's graphical method, assigned in the reading but currently absent from class.)

**B. Oven-minute auction (15 min, the shadow-price activity).** Each team runs the corrected bakery model; the instructor auctions bundles of 10 extra oven minutes to the highest bidder over several rounds. Rational teams bid up to ~€3.57 per bundle-minute... and the market price converges on the shadow price — *before* anyone has named the concept. Then reveal the sensitivity report. Shadow prices as market prices for scarce capacity is the deepest idea in the week, and an auction teaches it in a way a report never will.

**C. Spot-the-missing-constraint gallery (10 min, Part 4 warm-up).** Three projected "optimal solutions" from deliberately under-constrained models: hire 2.7 nurses; produce −40 posters; run the machine 187 hours/week. Pairs name the missing constraint in each. Rehearses Part 4's standing question with guaranteed material, rather than hoping student models contain instructive gaps.

**D. Python mirror (optional handout).** The bakery model in `scipy.optimize.linprog` (or PuLP) is ~10 lines; shadow prices appear as the dual values (`result.ineqlin.marginals`). One handout keeps the Python thread alive through the Excel-native weeks and shows students the tool they'd actually use at scale.

**E. Constraint bingo during presentations (Part 4).** The audience holds cards listing constraint types (capacity, minimum-service, non-negativity, integrality, policy/regulatory, logical). As each pair presents, listeners mark which types appear — and which are *suspiciously absent*. Converts passive audience time into the "constraint you missed" hunt the plan wants.

## 4. Critique of the Lesson Plan

**What works (keep):** the formulation-first opening challenge with the net-vs-gross revenue trap; build-and-break as the core activity (infeasibility as information, not error); T5's negative-shadow-price question (most students never see one); T8's Heathrow LP (real values, real policy, and (e)'s "cost of policy" framing is exactly how LP earns its keep in public debate); the three-assumptions debrief.

**Problems, reasons, and fixes:**

1. **The worked example is infeasible and its conclusion reversed (see §2).** Highest-priority fix in the entire 22-week set: it anchors the demo, T2, T3, and T4, and Solver will publicly contradict it.
2. **T6(c) is ill-posed in a balanced transportation problem.** Total supply = total demand = 200, so increasing Store 2's demand by 10 makes the model **infeasible** — the allowable increase on that constraint is zero, and "10 × €7 = €70" extrapolates a shadow price across a range that doesn't exist. *Fix:* either give Warehouse A 130 pallets (slack of 10 makes the marginal-pallet question meaningful, shadow price = €8 via A) or keep the balance and make the question "what is the allowable increase, and why?" — where "zero" *is* the lesson, and a neat echo of T4(e).
3. **The timing table sums to 95 minutes** (10+20+10+25+20+10) — third occurrence of this arithmetic slip (Weeks 9, 16). *Fix here:* Part 4 to 15 minutes; with Activity E the audience stays engaged at the shorter length. Worth one template-level fix across all Block 4 files.
4. **Chapter 14 content taught without Chapter 14 reading (see §1).** Transportation, scheduling, and integer constraints all appear in tutorials; assign 14-4a and cite 14-2/14-7.
5. **Unboundedness is promised but never delivered.** Part 3 lists "infeasible, unbounded, or dramatically changes" as break targets, yet no example, tutorial, or answer key covers the unbounded case, and it *will* happen accidentally to at least one pair (delete a ≤ constraint and Solver's error message is cryptic). T9 closes this; without it, the instructor is improvising the explanation live.
6. **Part 3's scenario cards don't exist yet.** Staff scheduling / portfolio / product mix scenarios need actual numbers engineered so that (i) a feasible optimum exists, (ii) an achievable single change produces infeasibility, and (iii) another change flips a binding constraint — the same tested-dataset standard as Weeks 8/15/16. The portfolio scenario needs care: "risk constraints" in linear form (max % per asset) — anything variance-based is nonlinear and quietly breaks the "this is an LP" premise.
7. **T5(d)'s arithmetic quietly answers a different question.** The offer is 50 hours at €15; the key evaluates renting 40 (€740 gain vs €600 cost). Fine if partial rental is allowed — but then say so; if it's 50-or-nothing, the decision needs the re-run the key itself recommends. One clarifying sentence either way.
