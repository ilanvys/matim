<div dir="rtl">

# matim · מתאים

**מוצא את המיומנות הישראלית שמתאימה לשאלה שלך, משתמש בה פעם אחת, ושוכח אותה.**

</div>

> Finds the Israeli skill that fits your question, uses it once, and forgets it.

You ask an ordinary question in Hebrew — about מס הכנסה, פנסיה, ביטוח לאומי, a form, an
invoice. `matim` works out that a specialist skill exists for exactly that, pulls it into the
conversation for this one answer, and lets it go when the conversation ends.

You never say the word "skill". You never browse a catalog. You install nothing a second time.

**Status: 🚧 planning + step 1 in progress. Nothing to install yet.**

---

## The gap

[skills-il](https://agentskills.co.il/he) is a public, MIT-licensed catalog of ~217 skills
written for Israeli specifics — tax rules, government APIs, Hebrew formats, local law. It is
genuinely good, and it already holds the answers to questions people ask LLMs every day.

But reaching it today means: *know the skill exists → find it on the site → install it → then
ask.* That works for developers. For everyone else, step one is impossible — you can't go
looking for a thing you don't know is there.

So the Israeli specifics stay in the catalog, and the confidently generic answer is what people
actually get.

`matim` closes that gap from the other direction: **ask → the skill shows up.**

## Two audiences, one artifact

| | Someone asking about their pension | Someone using Claude Code |
|---|---|---|
| Where | claude.ai / ChatGPT, in the browser | agentic terminal |
| Gets | the skill's instructions loaded into the chat, and a better answer | the skill materialized in a real task-local runtime |
| Knows what a "skill" is | no — and never needs to | yes |
| Ships in | step 1 | step 2 |

The first column is why this is worth building. The second is why it's buildable first.

## Design rules

1. **Zero infrastructure in step 1.** A released file, not a service. No server, no API key, no hosting bill.
2. **Read-only toward skills-il.** Never fork, vendor, or mirror skill content — fetch it live. Only the *index* is built ahead of time.
3. **Silence is the default.** A question that doesn't need a skill gets a normal answer, with no announcement that a search happened.
4. **Honest about "temporary".** In web chat nothing is installed, so nothing needs uninstalling. No theatrical cleanup step.
5. **Never emit a value as retrieved that wasn't retrieved.** Computing from logic is fine. Computing from imagination never is.

## Repo map

| Path | What |
|---|---|
| [`docs/design.md`](docs/design.md) | how it works — the mechanism, the three execution routes, and the two ways it fails |

## Relationship to skills-il

**`matim` is a client for [skills-il](https://agentskills.co.il/he), not a competitor to it.**

skills-il is the catalog — the source of truth, and the place skills are authored and reviewed.
This project only resolves and loads them, and sends attention and usage toward the catalog.
Skill content is fetched live from the public repos and never mirrored here.

Not affiliated with, endorsed by, or operated by skills-il or YooTech.

## License

MIT — see [LICENSE](LICENSE). Same license as the catalog it reads.
