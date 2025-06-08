# Presidential Primary Simulator – User Stories

## Core Features (MVP)

### Candidate Modeling
- As a campaign analyst, I want to define candidates with names, factions, and support levels, so that I can simulate how different ideologies perform in various districts.

### District-Level Simulation
- As a strategist, I want to assign support percentages to candidates in each congressional district, so that I can calculate delegate allocation based on vote share and viability thresholds.

- As a reader-facing storyteller, I want to simulate delegate allocation using DNC rules (15% threshold, proportional distribution), so that the race feels realistic and grounded.

### Delegate Math
- As a campaign manager, I want to aggregate district-level delegate allocations per candidate, so that I can track the running total across the campaign.

---

## Functional Expansions (Tier 2)

### Momentum and Narrative Shifts
- As a simulation user, I want to simulate events (e.g., debate win, scandal), so that candidate support can shift dynamically over time.

- As a strategist, I want to simulate regional strengths and weaknesses, so that candidates can win even if they lose the national vote.

### Statewide Delegate Allocation
- As a DNC modeler, I want to simulate statewide delegate allocation (at-large and PLEO), so that I can more accurately model how full states contribute to totals.

### Polling and Momentum Modeling
- As a strategist, I want to track polling data at the state or district level, so that I can identify where candidates are gaining or losing support over time.

- As a simulation engine, I want events (debates, ads, scandals) to modify polling values in specific areas or voter blocs, so that momentum feels responsive.

- As a realism modeler, I want a portion of voters to be undecided or swingable, so that campaign efforts can meaningfully change outcomes.

---

## Storytelling & Immersion Features (Tier 3)

### Campaign Finance
- As a campaign strategist, I want each candidate to have a fundraising total and weekly income, so that I can simulate resource constraints and advantages.

- As a campaign manager, I want to allocate funds per state or district (e.g., ads, field offices, organizing), so that spending affects polling or turnout.

- As a simulation user, I want debate wins or endorsements and leads in polls to increase donations, so that events influence both support and capacity.

- As a game planner, I want over-spending to reduce a candidate’s future viability or invite media scrutiny, so that I must make trade-offs.

### In-World Artifacts
- As a content creator, I want to export simulated outcomes as campaign memos or media briefings, so that I can publish in-world materials without spoiling the plot.

### Timeline Modeling
- As a writer, I want to simulate week-by-week changes in support and polling, so that I can narratively map how Caldwell rises without early wins.

### Re-Runs and Alternate Scenarios
- As a worldbuilder, I want to simulate multiple alternate scenarios (e.g., what if Monroe had won Michigan?), so that I can explore what makes Caldwell’s win unique.

### Polling vs. Reality (Optional)
- As a narrative writer, I want polls to be slightly inaccurate or overfit to recent events, so that candidates can underperform or overperform expectations.

---

## Prioritization Summary

| Tier     | Goal                                           | Key Stories                                            |
|----------|------------------------------------------------|--------------------------------------------------------|
| MVP      | Simulate delegate allocation at CD level       | Candidate setup, CD modeling, delegate math           |
| Tier 2   | Add realism, momentum, and statewide logic     | Events, demographics, statewide delegates, polling    |
| Tier 3   | Build immersive world and reader engagement    | Campaign finance, narrative outputs, alternate paths  |
