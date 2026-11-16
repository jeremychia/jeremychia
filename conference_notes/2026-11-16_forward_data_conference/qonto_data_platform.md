# meta

organisation:       qonta
title:              How a Small Data Platform Team Serves 2,000 People — with Self-Service and AI

# notes

self-service

* job orchestator (how do people know their jobs without knowing airflow)
* the schedule.yaml (this is quite similar to what we have - the abstraction) / dockerfile is in the team's code
* isolated by design (one pod per task)

* every source was a config PR
* data contract - what is the level of abstraction

* so they have decided to interact with it through the UI

* they also defined based on KPIs, the P1 dashboards, and if it is late 
* 3.2 merged PRs, same team size - all repos are AI-ready: AGENTS.md
* AI increases porductivity, but humans are the bottleneck on support

80% by next year, for resolving issues.

--

this is quite similar to what vinted is doing
direction - empowerment, letting people do more things, but removing the knowledge of how the actual things actually work
initially it was streamlit, but now it's react.js