# How `matim` works

No server. No embedding model. No index to maintain on your machine. The entire system is
**one catalog file and a decision procedure**, and most of the reason that's enough is an
observation about where the intelligence already lives.

---

## The claim

Israel's local specifics — tax rules, government API contracts, ID checksums, ביטוח לאומי
entitlements, Hebrew document formats — are already written down. [skills-il](https://agentskills.co.il/he)
holds ~217 skills encoding exactly that, publicly, MIT, reviewed.

The answers exist. They don't reach the people asking the questions.

They don't reach them because the path runs *know the skill exists → find it → install it →
then ask*, and that path has a precondition nobody can satisfy: **you cannot go looking for a
thing you don't know is there.** Someone asking about their pension doesn't know what a skill
is, doesn't know a catalog exists, and will never type its name. So they get the confident,
generic, subtly-wrong answer instead — while the correct one sits in a public repository.

`matim` runs the path backwards. **Ask → the skill shows up.**

## Browsing was never going to work

217 is a specific number: past what anyone browses, and far past what anyone installs. Even
the users who *do* know the catalog exists reach a handful of skills — the ones they already
knew to look for. Discovery-by-browsing rewards the people who least need help.

And it fails completely for everyone else, for the structural reason above. A better search
box doesn't fix that. Nothing the catalog does to itself fixes that, because the problem isn't
inside the catalog.

## The load-bearing observation

Here's the part that makes this a text file instead of a service:

> **The host model already does the expensive work, for free.**

Intent understanding, Hebrew comprehension, disambiguation, ranking a question against a list
of candidates — that's the hard machinery a discovery service would exist to provide, and it's
already running in the conversation, at no cost, before this project contributes anything.

So `matim` contributes only the three things the model genuinely lacks:

1. **A good index** — 217 rows it can scan in one read, carrying Hebrew trigger terms, because
   the user asks in Hebrew and the skills are documented in English. That bridge is the product.
2. **A fetch address** — where the real instructions live, fetched live so they're never stale.
3. **A decision procedure that knows when to stay quiet.**

A semantic-search runtime with a local binary and a vector index would do the same job worse,
because it would be re-implementing, offline and approximately, the comprehension the model is
already doing exactly.

## The mechanism

```
user asks something, in Hebrew or English
        ↓
 gap check ──── no ──→ answer normally. say nothing about skills. ← the common case
        ↓ yes
 read the catalog · rank · pick 0–2 candidates
        ↓ nothing good ──→ answer normally. still say nothing.
        ↓
 fetch the real SKILL.md, live, from the public repo
        ↓
 one line of disclosure — which skill, and that it's for this conversation only
        ↓
 apply it to THIS task
        ↓
 conversation ends → context gone → nothing was ever installed
```

Nothing is registered, so nothing needs uninstalling. That's not a limitation being spun —
it's why the temporary claim is true rather than a cleanup step performed for show.

## The sandbox is not the wall it looks like

Browser chat can't run the catalog's Python. That sounds fatal for any skill whose value is in
its code. It mostly isn't, because "can't execute" and "can't answer" are different problems:

| | For | The limit it gets around |
|---|---|---|
| **Port** | checksums, date conversion, VAT, deterministic local rules | *No Python* — reimplement the source for this input. The source is the spec, so the port is faithful. Equivalent to running it. |
| **Live fetch** | public government datasets | *No network in the sandbox* — the model's own fetch tool **is** the network layer. Read the script for its request contract, then make the real call. |
| **Handoff** | auth, writes, anything touching your machine | Genuinely out of reach. Answer as far as the instructions support, in Hebrew, uncertainty stated, plus where to verify. |

The bet is that the first two cover most of the catalog, because most Israeli-specific value is
either a deterministic local rule or a public dataset — and neither one needs your machine.

## The two ways this fails

Not "it can't find the skill." Retrieval is the easy part. The real failure modes:

**Over-triggering.** A system that answers every question with *"let me load a skill for
that!"* is theater, and it's worse than not existing. Silence is the default: a skill loads
only when the task is genuinely Israel-specific, a catalog entry matches the actual task rather
than sharing a keyword, and the skill would change the output instead of decorating it. A
search that finds nothing is never announced.

**Fabrication.** Reading a script tells you its endpoint, its parameters, and its response
schema. It tells you nothing about the values that endpoint would return — and knowing the
schema is exactly what would make an invented answer look credible. So the guard sits on
output, not on fetching:

> **Never emit a value as retrieved that was not retrieved.**
> Computing from logic: fine. Computing from imagination: never.

For questions about someone's pension or tax liability, that rule is the whole product.

## Trust is one decision, made once

Because there's exactly one catalog: one GitHub org, one owner, MIT, a documented review
process, every file publicly fetchable and traceable to a real URL.

So the trust question collapses to *do I trust skills-il?* — answered once, by you, at install
time. No cross-registry provenance, no reputation scoring, no revocation infrastructure.
Everything downstream of that single answer is plumbing, which is the reason a system like this
can be a file instead of a company.

Skill content is fetched live and never mirrored here. The catalog stays the source of truth.

## What's still unsettled

Written down, unanswered, and each one can still move the design:

- Whether browser chat can fetch raw file content mid-conversation. The "load the real
  instructions" step depends on it; there's a designed fallback that degrades to discovery if not.
- How someone non-technical gets this without uploading a file. That's the distribution
  question, and it gates the audience this is actually for.
- Whether the catalog runs deep in the consumer domains — pension, tax, זכויות — or leans
  engineering. Cheap to measure, and it decides who ships first.
