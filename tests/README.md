# Tests

Two layers that fail independently, so they are tested separately.

| | `smoke.py` | `cases.tsv` |
|---|---|---|
| Tests | the service | the model's behaviour |
| Answers | can the file be fetched? | did it decide to fetch, and say so? |
| Runs | automatically, in seconds | by hand, one conversation per case |
| Fix belongs in | `matim-mcp` | `SKILL.md`, the catalog, `tools/` |

A green `smoke.py` says nothing about routing. `S08` and `S17` passing prove a
script *can* be fetched and run — case `C03` is what proves the model actually
fetches it.
That distinction is the whole reason both exist: every behaviour reported so
far has been a client-side gap sitting on top of a healthy server.

## smoke.py — the service

```bash
python3 tests/smoke.py                 # all 19
python3 tests/smoke.py S05 S07 S08     # a subset
MATIM_MCP_URL=http://localhost:3000/api/mcp python3 tests/smoke.py
```

Nineteen checks in four groups:

| | Asks |
|---|---|
| `S01`-`S04` | handshake, tool advertisement, the catalog index |
| `S05`-`S12` | the files: `SKILL.md`, `SKILL_HE.md`, a `references/`, a `scripts/`, and the four recovery paths (unknown category, unknown slug, unknown file, folder) |
| `S13`-`S16` | the splitter: a long Hebrew file stays under the measured cliff, rejoins losslessly, and every part carries the attribution duty |
| `S17`-`S19` | the ladder's preconditions — see below |

The recovery paths matter as much as the happy ones. **A failure arrives as
ordinary text from a call that succeeded**, so a check that only asserts "no
JSON-RPC error" would pass while the model receives `Could not reach the
source` and treats it as content.

### S17-S19 — what a server-level test *can* say about scripts and references

Whether the model **decides** to fetch a script or a cited reference is
behaviour, and is `cases.tsv` (`C01`-`C06`, `R01`-`R04`). It cannot be observed
from here. What can be observed is whether that decision could possibly
succeed, and each of these three preconditions fails silently:

- **`S17` — the script is actionable, not merely present.** `S08` asserts the
  reply "looks like Python", which a file cut in half also does. `S17`
  `compile()`s it and requires an entry point. A truncated script reads as
  source, gets ported by the model, and produces a number with no error
  anywhere.
- **`S18` — the skill names its own script and reference.** If the text never
  cites `scripts/majority_threshold.py`, nothing sends a model to it, and no
  tool description fixes that. The rung has to exist in the file being read.
- **`S19` — no citation dangles.** A cited path that is not in
  `list_skill_files` hands the model `"…" does not exist for …` mid-step. The
  likely recovery is to compute from memory, which is exactly the failure the
  script exists to prevent.

Together they say: *if* the model reaches for the script, it will get something
it can actually run. They say nothing about whether it reaches.

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
