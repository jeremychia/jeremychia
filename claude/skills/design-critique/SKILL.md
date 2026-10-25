---
name: design-critique
description: Give structured design feedback on a page or design, covering usability, visual hierarchy, consistency and default design tells. Use when asked to critique, review or give feedback on a UI, layout or design. For accessibility conformance use a11y-audit.
allowed-tools: Read Grep Bash
argument-hint: <path-to-html | url> [--focus usability|hierarchy|consistency]
---

# Design critique

`$ARGUMENTS` is a local HTML file or URL. `--focus` limits the critique to one lens. Otherwise cover all three. Report only. Never edit files unless asked afterwards.

Name a location, the user's experience and a change for every point. Leave out taste-only remarks.

## Step 1 — Set the brief

State in two lines before judging anything:
- Who the page is for and what they came to do. Name each audience or mode.
- The one thing the page must get right.

Judge against that brief.

## Step 2 — Load the page

- Read local files in full, with linked CSS. Read the template strings inside scripts.
- Fetch URLs with `curl -sL`. Never use WebFetch, which summarises.
- Say that you reviewed source, not pixels. Mark anything that depends on rendering as an inference.
- Prefer a render at desktop, 375px and 320px wide when a browser tool is available. Screenshots catch what source cannot: wrapped rows, clipped pills, controls on top of each other, text that renders at full size when it should be hidden. Read each screenshot before you judge.
- Read the data behind the page, not only the markup. Open the JSON or the build script and look at 20 real values: names, addresses, timestamps, links and image URLs. Most "design" problems on data-driven pages are data problems shown raw.
- Find out whether the HTML is generated (a `*_template.*` file, `__PLACEHOLDER__` tokens, a scheduled workflow that commits it). Findings go against the output, but any later edit belongs in the template.

## Step 3 — Apply three lenses

**Usability**
- Check that a first-time user can tell what to do on the first screen.
- Count the clicks and scroll before the user reaches the payload.
- Flag controls that look like something they are not: boxes that look like checkboxes, clickable things that look static.
- Check for feedback after each action, a next step, and a way to keep the result (copy, save, print).
- Check empty, loading, error and small-data states. Each should say what to do.
- Check mobile: floating elements that collide or cover content, tap target size, horizontal scroll.
- Check copy is in the user's voice, in active voice, with one name per action.
- Check each label against what it does. "See all 12 posts on Facebook" linked to one arbitrary post. Follow every link and button to its real target, and say what it does in the label ("View the most-liked post on Facebook").
- Check raw database or geocoder strings are not the user-facing name. ALL CAPS addresses with the postcode and a repeated road ("80 CIRCUIT ROAD CIRCUIT ROAD MARKET … SINGAPORE 370080") hide the part people recognise behind a one-line ellipsis. Clean at display time, let names wrap to two lines, and keep the raw value for ids, search and external forms.
- Check scraped or relative timestamps ("4d", "1w"). They freeze at scrape time and make old posts look current. Show an absolute date or nothing.
- Check every image source. Signed CDN URLs (Facebook, Instagram) expire and return 403. If the repo holds local copies, prefer them, and give every image an `onerror` that tries the other source before hiding. Count how many images load in a browser.
- Check derived numbers say how they were derived: "estimated from 66 comments", not "based on 66 reviews", when a keyword model produced it.
- Check controls that do nothing in the current state. Sort pills that "Near me" overrides should be disabled, with a title saying why.
- Check every failure path: data fails to load, geolocation denied, no results. Each needs a message in the page (not `alert()`) and no endless "Loading…". Block the request in a browser to test.
- Check third-party defaults. Leaflet paints popup links in its own blue, puts zoom buttons top-right where a phone popup's close button sits, and gives popups a fixed width. Look for these in a 320px render.
- Check tap targets at 32px or more for pills, filter chips, text links and ⓘ buttons. Raise them after the type-size pass, and re-check that rows still fit.

**Hierarchy**
- Run the squint test. Name the first, second and third thing seen. Compare them with the brief.
- Check there is one primary action per view.
- Check size, weight and colour encode importance. Flag many equal cards, one accent colour doing five jobs, and body text so small it reads as caption.
- Check dividers, borders, labels and eyebrow text carry information.
- Keep lines under about 80 characters. Break long passages with a lead-in.
- Check content order follows what the user needs, not what the author finds interesting.

**Consistency**
- List colours, spacing, radii and type sizes outside the token set.
- Check the same component looks and behaves the same everywhere.
- Check one dash style, one capitalisation style, one icon style.
- Check interaction patterns match across modes and sections.
- Compare claims with behaviour. Flag copy that says numbers are computed when they are hardcoded.

## Step 3b — Check for default design tells

Run on every critique, whatever the focus. Count each tell with grep, then report the counts. Never flag a tell the brief asks for. Treat a tell as a finding only when it is a default, not a choice made for this subject.

```bash
grep -c -E 'text-transform: *uppercase' FILE
grep -o '→' FILE | wc -l
grep -o ' · ' FILE | wc -l
grep -o -E 'border-radius: *[0-9.]+(px|rem)' FILE | sort | uniq -c | sort -rn
grep -o -E 'box-shadow:[^;}]*' FILE | sort | uniq -c | sort -rn
grep -c gradient FILE
grep -o -E 'font-family: *[^;]*' FILE | sort | uniq -c | sort -rn
grep -c -E '#(0b0b0b|111|111111)\b' FILE
grep -n -E '<h1[^>]*>.*<(em|strong|span)' FILE
grep -c -E '@keyframes|animation:|:hover[^}]*transform' FILE
grep -c 'prefers-reduced-motion' FILE
```

Flag each of these:
- **Card kit.** Content split into identical rounded cards, one radius on everything, the same soft grey shadow under each, gradient washes as decoration. Count distinct radii. Many radii with no hierarchy is as bad as one radius everywhere.
- **Template chrome.** A tracked ALL-CAPS eyebrow above headings, especially one that repeats the heading. Meta strings joined with middle dots. Labels built as `WORD — fragment`. A monospace face for small data labels. `→` appended to link or button text. Tinted near-black standing in for black.
- **Palette defaults.** A warm cream background with a high-contrast serif and a terracotta accent. Near-black with one acid-green or vermilion accent. A newspaper layout with hairline rules and zero radius.
- **One accent, many jobs.** Check that one colour does not mark links, eyebrows, stats, bars, active states and chart categories at once.
- **Headline tells.** One word or phrase in a headline set in italic, bold or another colour.
- **Hero.** Check the hero opens with the most characteristic thing in the subject's world. Flag a big number, small label and gradient accent used by default.
- **Type.** Flag a system font stack used without a decision, an ad-hoc size scale, and body lines over 80 characters.
- **Numbered markers** on content that is not a sequence.
- **Motion.** Flag fade-and-slide entrances on every section and hover transitions on every card. Welcome motion that answers an action. Flag a missing `prefers-reduced-motion` rule.
- **Restraint.** Name the one memorable element. If there is none, say so. List what to cut: decoration that serves no part of the brief.

Report counts in one line, such as `tells: 10 uppercase labels, 9 arrows, 22 middle dots, 12 radii, 1 shared shadow`.

## Step 4 — Report

Open with a verdict of two or three sentences against the brief. Then:

1. **What works.** Two to four specific things to keep.
2. **Findings**, grouped by lens, with default design tells as a fourth group:

```
[High|Med|Low] <short title> — <file:line or selector>
  Observed: what is on the page
  Impact: what the user experiences
  Change: the specific fix
```

   High blocks the main task or damages trust. Med slows or confuses. Low is polish.
3. **Suggested order.** At most five steps, cheapest and highest impact first.
4. **Not assessed.** Anything that needs a real render, real users or analytics.

Merge findings that share a root cause. Never pad with generic advice. Send contrast, keyboard and screen-reader issues to a11y-audit instead of repeating them.

Close with one line offering to implement the top findings, or to run a11y-audit on the same file.

## Step 5 — If asked to implement the findings

Work in the order suggested, one change per commit, and verify each in a browser before the next.

- Edit the template and source, then mirror into the generated output (see Step 2). Check `git status` and `git log -3` before each batch, because a daily build can overwrite local edits.
- Do mechanical sweeps with a script, then look at screenshots. A "raise every font under 12px" sweep changed 47 declarations at once and wrapped three rows.
- Consolidate by aliasing before deleting. Two oranges plus a star and a hover red became two real colours by setting the star to the primary and the hover red to the button colour. Folding an always-on theme class into `:root` removed a whole dead token set. Compare computed values before and after to prove nothing shifted.
- Consolidate radii to a small scale (4 / 8 / 12 / pill) with one regex, then check a screenshot of each surface (list, popup, modal).
- Drop decorative glyphs (a "→" on a button). Keep "↗" on links that open a new tab, because it tells the user they are leaving.
- Remove dead code by reference scan: take every class and function name the markup and scripts use, then delete CSS and functions nothing references. Run the browser checks again.
- Verify the data layer the UI depends on: link permalinks match `/groups/ID/posts/ID`, local image files exist, names stay distinct after cleaning (count duplicates before and after).
- Test with Playwright, then stop the dev server you started. Leave pushing to the user. Offer it, and confirm the branch is not behind.

## Pitfalls log (from the Hokkien Mee Map pass)

- A stray `</style>` in `map.css` made the browser drop `.sr-only`, so hidden headings showed at full size. Always confirm hidden text is hidden.
- The page tried expired Facebook CDN URLs first and all list thumbnails were blank. Nobody noticed because the card layout still looked tidy.
- "See all N posts" linked to the first scraped post. For 67 of 108 multi-post stalls it was not even the quoted post. Five stored links had their post id stripped and opened Facebook's home page.
- A failed `data.json` fetch would have made the popup refresh itself forever.
- The popup was 320px wide on a 320px phone, with the zoom buttons covering its close button.
- Bigger pill padding pushed the ⓘ button to a new row. Shrink horizontal padding before accepting a wrap.
- An edit made only to the generated `docs/index.html` vanished when the daily build ran. Edit the template.
