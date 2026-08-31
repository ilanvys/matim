<div dir="rtl">

# matim · מתאים

**מוצא את המיומנות הישראלית שמתאימה לשאלה שלך, משתמש בה פעם אחת, ושוכח אותה.**

</div>

> Finds the Israeli skill that fits your question, uses it once, and forgets it.

You ask an ordinary question in Hebrew — about מס הכנסה, פנסיה, ביטוח לאומי, a form, an
invoice. `matim` works out that a specialist skill exists for exactly that, pulls it into the
conversation for this one answer, and lets it go when the conversation ends.

You never say the word "skill". You never browse a catalog. You install nothing a second time.

**Status: step 1 is live.** [The skill bundle](https://github.com/ilanvys/matim/releases/latest/download/matim.zip)
is released, `matim-mcp` is deployed, and [ilanvys.github.io/matim](https://ilanvys.github.io/matim/)
carries the install instructions. Step 2 — the task-local runtime for Claude Code — is next.

---

## The gap

[skills-il](https://agentskills.co.il/he) is a public, MIT-licensed catalog of 209 skills
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

## What's actually in the catalog

Measured 2026-08-31 by [`tools/build_catalog.py`](tools/build_catalog.py) against the live org:
**209 skills across 14 categories.** Every one has consistent frontmatter, and every raw URL
resolves.

### How much of it can a browser chat actually use?

The catalog ships Python alongside its instructions, and browser chat can't run Python. But
"can't execute" and "can't answer" are different problems, so each skill is classified by what
its scripts actually do:

| Flag | What the scripts do | Count | What we do instead | Works in browser chat? |
|---|---|---|---|---|
| `Sc` | pure computation | **119** (57%) | port the logic and compute the answer | ✅ equivalent to running it |
| `-` | no scripts at all | **66** (32%) | follow the instructions | ✅ nothing to run |
| `Si` | plain unauthenticated GET | **13** (6%) | read the request contract, make the real call | ⚠️ depends on fetch rules |
| `Sx` | needs credentials, or writes | **11** (5%) | honest handoff — answer as far as we can, then point to the real thing | ❌ genuinely out of reach |

**89% of the catalog — 185 of 209 — is reachable without any network call beyond fetching the
skill itself.** That is the number that makes a browser-only version worth building.

<details>
<summary><strong>The 13 <code>Si</code> skills</strong> — need a live call to answer fully</summary>

`boi-economic-data` · `hebrew-survey-builder` · `israel-gov-api` ·
`israeli-accessibility-compliance` · `israeli-election-data` · `israeli-personal-assistant` ·
`israeli-public-transit` · `israeli-shelter-guide` · `israeli-statistics` ·
`pelecard-payment-gateway`\* · `shabbat-aware-scheduler` · `shekel-currency-converter` ·
`tranzila-payment-gateway`\*

\* the payment gateways almost certainly need credentials in real use — the classifier only sees
what's in the first three scripts. See the caveat below.
</details>

<details>
<summary><strong>The 11 <code>Sx</code> skills</strong> — out of reach in a browser, by design</summary>

`cloudinary-assets` · `green-invoice` · `hebrew-chatbot-builder` · `israeli-drug-database` ·
`israeli-heritage-explorer` · `israeli-property-appraisal` · `israeli-sms-gateway` ·
`israeli-tech-interview-prep` · `israeli-whatsapp-business` · `jfrog-devops` ·
`tase-stock-analysis`

These send messages, upload files, or authenticate against a paid account. They are what a
local runtime is *for*; a browser tab should not be doing them.
</details>

### Who the catalog is for

Grouping the 14 categories by who asks the question:

| | Categories | Skills |
|---|---|---|
| **Everyday life** | tax-and-finance (40), government-services (30), legal-tech (19), accounting (14), health-services (11), education (6), travel (4), food-and-dining (3) | **127** (61%) |
| **Professional / technical** | developer-tools (30), marketing-growth (13), localization (12), communication (11), security-compliance (10), courses (6) | **82** (39%) |

**But that table undercounts the first row, and the reason matters.** The categories describe a
skill's technical domain, not its audience. Sorted by who actually asks:

- `israeli-shelter-guide` and `pikud-haoref-safety-protocols` sit in **security-compliance**
- `israeli-apartment-hunting` and `israeli-wedding-planner` sit in **localization**
- `israeli-cv-builder`, `israeli-job-market`, `israeli-telecom-comparator` sit in **communication**
- `israeli-pension-decoded`, `miluim-rights-and-money`, `making-aliyah-first-90-days` sit in **courses**

Every one of those is an ordinary-life question filed under an engineering label. Which is a
finding about the *routing problem*, not a complaint about the catalog: the person asking where
their nearest bomb shelter is will never think "security compliance", and neither would a router
matching on category names alone.

### Two things the flags do not tell you

**The flag describes the scripts, not the skill's data needs.** A skill marked `-` has no
fetching problem — but if its instructions embed 2026 tax brackets, it still has a *staleness*
problem. Nothing here measures that.

**The classifier is a regex over at most three scripts per skill.** A script reaching the
network through a helper import gets misfiled. Treat the split as a good estimate that needs a
manual pass, not a fact — it decides whether an answer is computed or retrieved.

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
