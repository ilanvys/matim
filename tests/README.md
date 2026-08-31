# Tests

Two layers that fail independently, so they are tested separately.

| | `smoke.py` | `cases.tsv` |
|---|---|---|
| Tests | the service | the model's behaviour |
| Answers | can the file be fetched? | did it decide to fetch, and say so? |
| Runs | automatically, in seconds | by hand, one conversation per case |
| Fix belongs in | `matim-mcp` | `SKILL.md`, the catalog, `tools/` |

A green `smoke.py` says nothing about routing. `S08` passing proves a script
*can* be fetched — case `C03` is what proves the model actually fetches it.
That distinction is the whole reason both exist: every behaviour reported so
far has been a client-side gap sitting on top of a healthy server.

## smoke.py — the service

```bash
python3 tests/smoke.py                 # all 12
python3 tests/smoke.py S05 S07 S08     # a subset
MATIM_MCP_URL=http://localhost:3000/api/mcp python3 tests/smoke.py
```

Twelve checks: protocol handshake, tool advertisement, catalog index, the
provenance block, `SKILL_HE.md`, a `references/` file, a `scripts/` file, and
the four recovery paths (unknown category, unknown slug, unknown file, folder).

The recovery paths matter as much as the happy ones. **A failure arrives as
ordinary text from a call that succeeded**, so a check that only asserts "no
JSON-RPC error" would pass while the model receives `Could not reach the
source` and treats it as content.

## cases.tsv — the model

54 cases. The plan's 50 (`plans/02-phase-1.md` §7) plus 4 `reference` cases,
because the plan covers scripts through the `compute` class but never checks
that a `references/` file gets fetched when the step being followed cites it.

| Class | n | Asks |
|---|---|---|
| `hit` | 20 | does the obvious skill get found at all |
| `negative` | 10 | does it stay silent when it should |
| `nearmiss` | 8 | ranking, not recall — four pairs that share vocabulary |
| `compute` | 6 | does it fetch the script and compute, or describe and guess |
| `reference` | 4 | does it fetch the cited `references/` file |
| `crossrepo` | 3 | more than one skill, without loading both speculatively |
| `outofcatalog` | 3 | does it decline instead of forcing a match |

46 of 54 are consumer phrasing. The plan requires at least half: an 80% top-1
that is 95% dev and 60% consumer is a failing result reported as a passing one.

**Columns.** `id query expected class audience needs` are fixed. Fill
`actual disclosed result failure_point notes` during validation.

`needs` says what must be *fetched*, not merely picked: `skill`,
`skill+script`, `skill+ref`, or `none`.

### Running one case

One clean conversation per case — a previously loaded skill contaminates the
next result. Paste the query verbatim, including the typos; they are there on
purpose. Record what happened, not what nearly happened.

### Scoring

Record which of the four independent failure points broke, because each has a
different home:

| # | Broke | Fix in |
|---|---|---|
| 1 | never triggered | `SKILL.md` frontmatter `description` |
| 2 | wrong category | `tools/category_intents.tsv` |
| 3 | wrong skill among near-misses | catalog descriptions, `Do NOT use for` lines |
| 4 | loaded but disclosed badly | `SKILL.md` §4, or the tool descriptions in the service |

**Automatic fail regardless of a correct pick:** any value stated as retrieved
that did not come back from a tool call. For money, rates, deadlines and
entitlements that rule *is* the product.

### The disclosure check — every triggering case

`disclosed` is scored on all four points. A load with no disclosure is a
**fail on point 4**, not a pass with a note:

- **D1 — names the skill.** The slug, e.g. `israeli-pension-advisor`.
- **D2 — credits skills-il and links a real source.** The `source:` URL from
  `get_skill`, or the catalog row's URL. The attribution is not decoration:
  routing attention back to the catalog is what makes matim a client rather
  than a fork.
- **D3 — scopes it.** For this conversation only. Nothing was installed.
- **D4 — matches what actually happened.** This is the one that bites. A
  `Could not reach the source` reply is a **non-load**; disclosing it as
  "טוען מיומנות" is the same category of error as inventing a number, and
  fails the case even if the eventual answer is correct.

Score `D1-4` when all four hold, `D2 D4` for a partial, `none` for silence.
For a plainly non-technical user the same four can be said in plain Hebrew
without the mechanism — judge the content, not the format.

**Known gap before you start:** on a connector-only install, disclosure has no
reliable channel to reach the model at all — see `docs/backlog.md` §1. Expect
`none` across the board there, and record it rather than working around it. It
is a finding about where the rule lives, not about any individual case.
