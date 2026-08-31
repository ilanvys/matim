# Backlog

Things found while shipping step 1 that are real but were not worth stopping for.
Ordered by how much they cost if left alone.

## 1. Disclosure does not fire on a connector-only install

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

## 2. Nothing tells the model to fetch a script for an `Sc` skill

`Sc` is 119 of 209 skills — 57%, the largest group. `SKILL.md`'s flag table says to "port the
script's logic to compute the real answer", but the model cannot port logic from a file it
never read, and no tool description tells it to fetch one. `get_skill`'s description names
`references/` and says when to fetch them; it is silent on `scripts/`.

So the largest flag class silently degrades to "follow the prose instructions" — which is
rung-2 behaviour with a working connector, the exact failure mode the ladder was written to
prevent.

**Fix:** name `scripts/` in the `get_skill` description with its own trigger condition, the way
`references/` already has one.

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
