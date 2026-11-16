# meta

speaker:        claire gouze
title:          context engineering for analytics agents that actually work

# notes

* we went from service to product (human-serve, to self-serve, agentic-serve)
* data teams are becoming product teams - controlling all aspects of the agents
* open questions:
    * what do i do with 5,000 vibe-coded dashboards
    i still can't understand the root cuase of this
    how do i improve my agents?
* agents are not taking our jobs, but they're taking our feedback loops away, because they become the main interface for our users

a good angentic-serve product:

for the businesss:
* reliable
* fast (speed)
* tranasparent
* actionable

for the data team:
* observable
* cost
* security (impersonation, agents)

the layer:
* context
* prompts
* evals (do this in a determinsitic way - comparing the accuracy vs costs, and looking into the errors)
* taste (teaching an agent how your best analyst investigates a problem)
* models
* harness (context window management, tools integration, memory, user rules)
* UI

there are many optiosn for context candidates,
but there is only one option for what is a good context

prompting:
1. context priority (semantics, docs, databases)
2. domains 
3. the analysis process in rules
3. and clarify user intent first


structuring an analysis:
1. frame the question
2. check data freshness
3. break into a metric tree
4. compare to a baseline (is it accurate)
5. lead with the biggest driver

which model do you use? jev/claude? impact on the cost and the speed

one experience, ui last, but most imporantly, explainable.
a lot of teams are building in-house (deel, adyen, etc.)
