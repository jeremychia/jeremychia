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
