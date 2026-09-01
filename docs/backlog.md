# Backlog

Things found while shipping step 1 that are real but were not worth stopping for.
Ordered by how much they cost if left alone.

## 1. Disclosure does not fire on a connector-only install  — FIXED 2026-09-01

**What happens:** the model loads a skill through `get_skill` and applies it without telling
the user which skill it used. Design rule 3 allows silence when *nothing* loads; it does not
allow a silent load.

**Why:** the disclosure rule lives in two places, and on claude.ai with only the connector
installed, neither reaches the model reliably.

| Channel | Carries disclosure? | Reaches the model? |
|---|---|---|
| `get_skill` tool description | no | **always** — tool schemas are in every request |
| MCP `serverInfo.instructions` | yes | client-dependent; claude.ai may not surface it |
| `SKILL.md` §4 | yes | only if the skill bundle is installed |

The provenance block that *does* arrive with every result is explicitly marked "not orders,
don't print them" (§3), so it cannot carry the requirement either.

**Fix:** move one sentence of the disclosure rule into the `get_skill` tool description in
`app/api/mcp/route.ts` — the only channel guaranteed to be in context. Keep the fuller rule in
`SKILL.md` for installs that have it. Do not rely on `instructions` for anything load-bearing.

**Shipped.** Observed live with *both* pieces installed: the model followed §3's ladder exactly
(so `SKILL.md` was loaded and §4 *was* in context) and still disclosed nothing. So the fix is not
only about connector-only installs — a rule the model has read is not a rule it applies. The
attribution duty now rides in the one channel it cannot skim past: the tool result itself,
written as an instruction rather than as the `source:`/`license:` metadata it had been treating
as plumbing. `SKILL.md` §4 additionally now credits matim alongside skills-il. Covered by S15.

## 2. Nothing tells the model to fetch a script for an `Sc` skill  — FIXED 2026-09-01

`Sc` is 119 of 209 skills — 57%, the largest group. `SKILL.md`'s flag table says to "port the
script's logic to compute the real answer", but the model cannot port logic from a file it
never read, and no tool description tells it to fetch one. `get_skill`'s description names
`references/` and says when to fetch them; it is silent on `scripts/`.

So the largest flag class silently degrades to "follow the prose instructions" — which is
rung-2 behaviour with a working connector, the exact failure mode the ladder was written to
prevent.

**Fix:** name `scripts/` in the `get_skill` description with its own trigger condition, the way
`references/` already has one.

**Shipped.** The trigger is now "when a step asks you to compute or check a threshold and the
skill ships a `scripts/` file for it" — with the reason attached, that the script is where the
current rule lives. Still unmeasured against a model: C01 and C03 in `cases.tsv` are the test.

## 3. Catalog rows whose description is `>-`

`israeli-urban-renewal-owner-guide` and `israeli-wills-inheritance` (at least) have `>-` as
their description — a leaked YAML block-scalar indicator from upstream frontmatter.

Routing ranks on `Use when …` / `Do NOT use for …` text. A row with no description is
effectively unroutable: it can never win a match, so those skills are invisible to matim even
though they are in the catalog and `get_skill` resolves them fine.

**Fix:** have `tools/build_catalog.py` detect a description that is only a YAML indicator and
either fall back to the first line of the skill body or fail loudly. Failing loudly is better —
a silent unroutable row is the same class of bug as the `__fixtures/` leak.

## 4. Unverified claims on the landing page

`docs/index.html` states three things nobody has checked:

- the claude.ai skill-upload path (`Settings → Capabilities → Skills → Upload skill`) — wording
  written from memory, and it is the first step a non-technical visitor takes
- that connectors and skill uploads need a paid plan — probably true, not stated on the page
- the Cowork tab's two steps — `plans/02` names the connector without naming the screens

## 5. Repo map is one row

`README.md`'s repo map lists only `docs/design.md`. It should carry `SKILL.md`, `catalog/`,
`tools/`, `tests/` and `docs/index.html` — the map is how a first-time reader finds the thing
they came for.

## 6. No CI

Nothing runs on push. The two checks that would have caught real bugs already:

- catalog ↔ manifest drift in both directions (a catalog row with no manifest entry is the
  unsafe direction — it offers a skill `get_skill` cannot resolve)
- the bundle in `dist/` matching the committed tree, so a release can never ship content that
  is not in its own tag

Both are a few lines each and both correspond to mistakes that actually happened.

## 7. The manifest refresh is documented but not scheduled

`matim-mcp`'s README says a daily redeploy is the refresh, and `lib/upstream.ts`
says the manifest refreshes on deploy (daily). Nothing schedules it. A rebuild
happens only on push, so the manifest drifts from the live org at whatever rate
skills-il changes, silently and with no failure to notice.

Both repos are in sync today — 209/209, no unsafe drift — which is exactly when
this is cheapest to fix and easiest to forget.

**Fix:** a Vercel Cron, or a scheduled GitHub Action hitting a Vercel Deploy
Hook. Either is a few lines. The build already fails loudly on a short manifest
(`MIN_REPOS`, `MIN_SKILLS`), so a scheduled rebuild that goes wrong shows up as
a failed deploy rather than a quietly truncated catalog.

Whichever runs it, the same job should re-check catalog ↔ manifest drift in both
directions (§6), since a refresh is exactly when the unsafe direction appears.

## 8. Hebrew tool results were being truncated at ~32%  — FIXED 2026-09-01

**What happened:** a Hebrew `SKILL_HE.md` came back cut a third of the way through, with four of
its nine steps missing, and nothing in the reply said so. The model answered anyway, from the
breadcrumbs the surviving text left behind plus its own training data. The answer was largely
correct, which is the dangerous part: nothing distinguishes it from the same pipeline producing
a confident wrong answer on a skill whose truncated half held a corrected figure.

**Why:** the client meters a tool result in JSON-escaped characters. Every Hebrew letter widens
to a six-character `\uXXXX` escape, so `israeli-pension-advisor/SKILL_HE.md` — 27,314 characters,
comfortably inside the reported "50,000 character limit" — escapes to 120,378 and is cut.
Hebrew pays a ~4.4x inflation that ASCII does not, so **a Hebrew-first router hits this first and
hardest**, and the smaller Hebrew file broke while the larger English one did not. English is not
safe either: the same skill's English `SKILL.md` escapes to 35,158, within 5% of the cliff.

The exact metering rule is not documented and is not simply "50,000": the observed cut had
delivered 36,815 escaped characters. That is the only measured survival, so the budget is set
below it rather than to the reported number.

**Fix (shipped):** `lib/upstream.ts` measures the ASCII-safe escaped length itself — deliberately
not `JSON.stringify().length`, which V8 leaves un-escaped and which would report a Hebrew file as
its own character count and never split anything — and slices files at markdown headings into
numbered parts, each budgeted at 30,000. `get_skill` takes a `part` argument; a non-final part
says so and names the next one; `SKILL.md` §4 gained "a part is not the file". Covered by
S13, S14, S16.

**Still open:** the budget is derived from a single observation. If parts get split more finely
than necessary, 36,815 is the ceiling to tune against — do not raise it without a new measurement.

## 9. Hebrew queries missed the tool search entirely  — FIXED 2026-09-01

Clients that defer MCP tools behind a keyword search index the tool titles and descriptions.
Every one of ours was written in English, so on the live trace `{"query": "פנסיה עזיבת עבודה"}`
returned **"No matching tools found."** and the tools were only reached on a second, English
attempt. On a Hebrew-first product the *first hop* failed in Hebrew.

**Fix (shipped):** all three tool titles and descriptions now carry Hebrew domain vocabulary
alongside the English. Unverified against the live index — worth re-running the Hebrew query on
claude.ai after deploy, since this is the one fix in this batch that `smoke.py` cannot check.
