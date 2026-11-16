# meta

title:          how to build a context factory for analytics agents
organisations:  giorgias
speakers:       arthur edmond, jules guillot, emma wagner

# notes:

* gorgias - a company with context engineers

## context layer
* very specific company knowledge (e.g. "what is a billable ticket")
* "creates, structures, and serves the right context at the right moment, so every task is informed, never blind."

four building blocks:
1. knowledge (.md files - pages organised by hierachy, what is covered, what is not covered)
2. skills (also .md files - processes that teach the agent how to perform a specific task) - also the notion of scope (is it a personal skill or company skill)
3. tables (documented tables - with table descriptions and column descriptions, tag on whether to include in the context layer, and "when to use" (what kind of questions it can answer), "how to use" (grains, etc.))
4. metrics (semantic layer - and details differentiate what is fixed and what is optional)

knowledge graph is the context layer
840 catalog items, 600 skills, 3000 interactions per day 

## retrieval

techinques: keyword searches, RAG, LLM 
* pipe 1 - knowledge graph
* pipe 2: skills

progressive disclosures
* show a document's title and description only when it's doing the search (explore wide, open only a few)
* and using a decision model a an LLM - it chooses the next loop
* BM25 (derivation of elastic search)

## maintain

* conetxt decays over time
* and so, who owns the context layer evolution?
* business domain owners - how do they enforce it? how do we make it a frictionless as possible?
* there's a context manager, which sends a change request to ask people to review whether something is done or not

best feedback coverage, as early as possible
* humans: flag an issue
* agents, reactively - they will learn from completed runs
* agents, proactively, finding gaps before users do

how do you ensure that there is no duplication of skills?

## education

turning colleagues from consumers to informed contributors
there are lessons and context
for being context-literate: learning, hackathons, becoming an FDE


--

open thoughts:
1. is there an academic discipline for this? is it library and inforamtion science?
2. beyond the name and the hype, which are the group of people who think very long about this? taxonomist