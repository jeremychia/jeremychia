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
- [Linear Programming — Khan Academy](https://www.youtube.com/watch?v=Bzzqx1F23a8) (12 min) — graphical method
- [Excel Solver Tutorial](https://www.youtube.com/watch?v=dRm5MEoA3OI) (8 min) — Solver setup and sensitivity report

**Worked example (attempt T1 first, then read this):**

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
