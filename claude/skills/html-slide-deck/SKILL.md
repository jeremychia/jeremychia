---
name: html-slide-deck
description: Build or change a single-file HTML slide deck with a 16:9 stage, a house palette, inline SVG diagrams and step-through animations driven by the arrow keys. Use when asked to make a deck, add or reorder a slide, draw a diagram as a slide, or animate a slide (step through cases, modes or a timeline).
allowed-tools: Read Edit Write Bash
argument-hint: <path-to-deck.html | topic> [slide number]
---

# HTML slide deck

Build the deck as one HTML file: inline CSS, inline JS, Google Fonts only. Keep the source in a private repo when the content is internal, and commit each change on its own.

## Step 1 — Lay out the stage

- Wrap every slide in `<section class="slide">` inside one `.stage`. Show one at a time with `.slide.on`.
- Size the slide as a 16:9 box: `width:min(100%, calc((100vh - 84px) * 16 / 9)); aspect-ratio:16/9; container-type:size`.
- Size everything inside in container units (`cqw`, `cqh`), so text and diagrams scale with the slide. Use `px` only inside SVG, where the `viewBox` scales it.
- Put content in `.pad{position:absolute;inset:6cqh 3.6cqw 7cqh 3.6cqw}`.
- Add a fixed bottom `nav` with ← prev, a `n / total` counter and next →. Bind →, Space and PageDown to next, and ← and PageUp to prev.
- Write the slide number to the hash with `history.replaceState`, and open the slide in `location.hash` on load, so a link can point at one slide.
- Under 700px wide, drop the fixed canvas: static stage, `aspect-ratio:auto`, one-column grids, `px` font sizes, and tables in an `overflow-x:auto` wrapper.
- Add a print stylesheet: every slide on its own page, no nav.
- Mark each slide with a comment, `<!-- 12 · dbt-core -->`, so a slide can be found by number and topic.

## Step 2 — Apply the design

- Define colours as tokens on `:root`, and use only the tokens. Take them from the house template when one exists. The default set: `--teal:#004654` (ink on accents, links, selected), `--mint:#edffe9` (selected fill, text on dark), `--lilac:#ceceff` (highlight slides, active row), `--violet:#9999ff` (tests, secondary marks), `--peach:#ffa580` (major events), `--grey:#f7f7f7` (panels), `--line:#e3e3e3`, `--ink:#111`, `--muted:#5a6465`, `--ok:#0b7a52`, `--bad:#c2410c`, `--merged:#8250df`.
- Colour a pull request's status by state: purple `.merged` for merged, green `.ok` for approved, `--bad` for in review or blocked. Recheck each state on the day the slide's "status on" date says.
- Pair two typefaces: Inter Tight 600 for covers, dividers and big numbers, and Inter 400–700 for everything else. Never ship the system default.
- Keep one type scale: `h2` 2.5cqw, body 1.6cqw, small 1.4cqw, tables 1.32cqw, captions in teal.
- Use four slide kinds: cover, `.dark` divider (teal ground, mint text) to open each section, `.highlight` (lilac) for the one sentence the audience must keep, and plain white content slides.
- Write each `h2` as a sentence that states the slide's claim, in lowercase. "the fix depends on what the test reads", never "fixes".
- Group content in `.cols.c2` or `.c3` grids and grey `.panel` boxes. Put one numbers table on a slide, not two.
- Link every claim, quote, pull request and doc where it appears. Repeat the link on each slide that cites it.
- Close with a sources slide.

## Step 3 — Draw diagrams in SVG

- Copy the visual language of the template's own diagrams before inventing one. Use rounded boxes, thin edges and short labels.
- Share one set of classes across slides: `.box` (white node), `.sel` (mint fill, teal stroke: the node in focus), `.test` (violet dashed: a check or reader), `.edge` (teal: depends on), `.tedge` (violet dashed: reads), `.lbl` (muted note).
- Encode state in colour, with a ✓ or ✗ in the label: green stroke and ✓ for runs or passes, `--bad` dashed stroke and ✗ for skipped or broken, grey fill for never runs.
- Keep labels to two or three words. Move the explanation into the caption under the panel.
- Show a before and an after side by side when the slide explains a fix.
- Give every SVG a `role="img"` and an `aria-label` that says what it shows.

## Step 4 — Animate by steps

- Animate only to walk through cases, modes or events in order. Never animate for decoration.
- Mark the slide `data-steps="N"`. Step 0 is the overview, with a caption that says "use → to step through …".
- Write one `setX(k)` per animated slide. It sets `data-k` on the section and swaps the caption text. Key all visual changes off `[data-k="…"]` in CSS.
- Register each slide in one map, `const STEPPERS=new Map([[elem,k=>setX(k)], …])`. `next()` advances the step until the last one, then moves to the next slide. `prev()` steps back, and arriving from the next slide lands on the last step.
- Add clickable pills, one per step, that jump to that step and stay in sync with the arrow keys.
- When the slide has a table, highlight the active row (lilac) and dim the others to `.28` in step with the diagram.
- Use four motions, each once per step: fade the rest to `.12`–`.28`, pulse the node that changed once, march the dashes on a live edge, and draw a new edge with `stroke-dashoffset`. Restart a one-shot animation with `el.style.animation='none'; void el.getBBox(); el.style.animation=''`.
- For a timeline, reveal events up to the next major one per step, pulse that major's dot, and caption it with its date and what it changed. Reveal everything on the last step.
- Switch every motion off under `prefers-reduced-motion:reduce`.

## Step 5 — Check every slide you touched

- Render each changed slide headlessly at 1185×720: `chrome-headless-shell --headless --hide-scrollbars --window-size=1185,720 --virtual-time-budget=3000 --screenshot=out.png "file://…/index.html#N"`.
- Render each step of an animated slide. Force a step by injecting `<script>step=k;setX(k);</script>` into a copy, with transitions disabled.
- Read every screenshot. Look for labels clipped at a panel edge, text running out of its box, labels on top of edges, and headings wrapping onto a third line. Fix by shortening the label first, then by widening the box.
- Check one slide at 400px wide.

## Step 6 — Publish

- Publish to the same artifact URL each time, from a copy of the source with everything before `<title>`, and the `</head><body>` and `</body></html>` lines, removed.
- Commit the source change with a Conventional Commits subject, then republish.

## Worked case

Asked for a slide on a check that reads two unrelated tables:

1. Place it right after the slide that lists the fixes. The problem comes before the mechanism, and the example after the concept.
2. Title it with the claim: "when no model is built from both, make one model build from the other".
3. Draw two panels. Before: two `.box` nodes, "no link", a dashed `.test` node, and both edges labelled "✗ skipped". After: one node turned `.sel` with a "depends on" edge, the test in green, and "✓ model_a is built", "✓ model_b is upstream".
4. Put the one-line fix under the after panel, in `code`.
5. Render it. "✗ model_b isn't upstream" was clipped at the panel edge, so the label became "✗ skipped" and the reason moved into the caption.
