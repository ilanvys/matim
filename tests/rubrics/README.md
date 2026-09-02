# Rubrics

One file per case, keyed by `id` in `../cases.tsv`. A judge grading `H01` loads
`H01.md` and nothing else.

`cases.tsv` answers *did it route correctly*. A rubric answers *was the answer
any good* — and those fail independently. A case can pick the right skill, load
it, disclose it perfectly, and still hand back a paraphrase of pretraining.

## The three tiers

They are not five equal checks. Ranking them is the point.

| Tier | Graded by | Effect |
|---|---|---|
| **Gates** `G1 G2` | judge, binary | Any fail = the case fails. No score is reported. |
| **Transcript** `T1…` | grep over the transcript | Any fail = the case fails. |
| **Anchors** `A1…` | judge, binary, with the source file in context | Scored `k/n`. |

Report as `PASS 3/3`, `PASS 2/3`, or `FAIL G2` — never as a percentage. A
percentage is what lets a fabricated number score 80%.

**Why gates are not anchors.** `SKILL.md` §4: *"Never emit a value as retrieved
that was not retrieved … for money, rates, deadlines and entitlements this rule
is the product."* As one of five equal checks, a case that invents a תגמול
figure still scores 4/5. As a gate it scores nothing.

## The two gates, identical in every rubric

- **G1 — the right skill, or the right silence.** Matches the `expected` column.
  For `NONE` cases: nothing was loaded and no fruitless search was announced.
- **G2 — nothing stated as retrieved that no tool returned.** Every figure,
  deadline, form number and rate in the answer traces to a tool result in this
  transcript. Computing from stated logic is fine. A plausible number is not.

## Transcript checks are grep, not judgment

Deterministic, so do not spend a judge on them:

- `T1` a `get_skill` call for the expected slug appears, and its result came back
- `T2` when `needs` is `skill+script` or `skill+ref`, that file was fetched too
- `T3` the disclosure line is present, uses the correct one of the two forms in
  `SKILL.md` §4, and names an `agentskills.co.il` URL (never `raw.githubusercontent`)

Two nondeterministic systems are already stacked here — the model under test and
the judge. Every check moved into this tier is variance you stop paying for.

## Anchors

2–4 per case. Each names a **specific** fact from the actual file — a form
number, a coefficient, a threshold, a named section. Never "reflects the skill."

The judge MUST have the cited source file in context. Asked whether an answer
matches a skill it cannot see, a judge agrees.

**An anchor is not a quotation check.** Correct paraphrase passes. Verbatim
quoting is scored by `T1`, mechanically — a model can produce quote-shaped text
about Israeli pension rules from pretraining alone, so quotation on its own is
evidence of nothing.

### Anti-anchors

Each rubric lists claims whose *presence* fails the anchor tier outright. These
are the specific errors general knowledge makes here — a stale rate, a repealed
rule, a threshold that moved. They are what separates "loaded the skill" from
"answered from memory and happened to name the skill."

## Counts vary by class

`hit` and `nearmiss` get 2 gates + 3 transcript + 3 anchors. `compute` adds an
anchor for *ran the script* vs *computed from memory*. `crossrepo` adds *loaded
both, neither speculatively*. `negative` and `outofcatalog` are **G1 + G2 and
nothing else** — there is no source to anchor to, and padding them to five
invents checks. Let the class set the count.

## Sources

Anchors were written against the files as of **2026-09-02**. Israeli figures move
on 1 January and some tables reissue mid-year. Re-verify the cited lines before a
benchmark run, or a correct answer will fail against a stale rubric.
