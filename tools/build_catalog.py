#!/usr/bin/env python3
"""Build matim's catalog from the live skills-il org.

Emits catalog/_index.md (category router) plus one shard per category.
Descriptions are copied whole and never truncated -- the "Do NOT use for ..."
clause they end with is the highest-value content in the index.

Stdlib only, by design: step 1 ships no dependencies.

  python3 tools/build_catalog.py            # build
  python3 tools/build_catalog.py --verify   # build, then check every row resolves
  python3 tools/build_catalog.py --refresh  # ignore the cache and refetch
"""
import argparse, json, os, re, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

ORG = "skills-il"
API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache")
OUT = os.path.join(ROOT, "catalog")
HE_TERMS = os.path.join(ROOT, "tools", "hebrew_terms.tsv")
UA = {"User-Agent": "matim-catalog-builder", "Accept": "application/vnd.github+json"}

# Repos in the org that hold no skills (CLI, MCP servers, bundles, CI).
NOT_SKILL_REPOS = {"skills-il-cli", "release-workflow", ".github", "mcps",
                   "bundles", "shufersal-mcp", "rami-levy-mcp", "design-systems"}

# Ordering for _index.md: audience-1 categories first. See plans/00.
CATEGORY_ORDER = ["tax-and-finance", "government-services", "legal-tech", "accounting",
                  "health-services", "education", "travel", "food-and-dining",
                  "localization", "communication", "marketing-growth",
                  "security-compliance", "developer-tools", "courses"]

NET = re.compile(r"\b(requests\.|urllib|httpx|aiohttp|http\.client|socket\.|fetch\()", re.I)


def get(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA["User-Agent"]} if raw else UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def cached(key, fn):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, key)
    if os.path.exists(path) and not ARGS.refresh:
        return json.load(open(path, encoding="utf-8"))
    val = fn()
    json.dump(val, open(path, "w", encoding="utf-8"))
    return val


def discover():
    """-> {repo: {branch, skills: [{slug, path, py: [...]}]}}"""
    repos = json.loads(cached("org.json", lambda: get(f"{API}/orgs/{ORG}/repos?per_page=100")))
    out = {}
    for r in repos:
        name = r["name"]
        if name in NOT_SKILL_REPOS:
            continue
        tree = json.loads(cached(f"tree-{name}.json",
                                 lambda n=name, b=r["default_branch"]:
                                 get(f"{API}/repos/{ORG}/{n}/git/trees/{b}?recursive=1")))
        if tree.get("truncated"):
            print(f"  !! {name}: tree truncated, rows will be incomplete", file=sys.stderr)
        blobs = [e["path"] for e in tree.get("tree", []) if e["type"] == "blob"]
        skills = []
        for p in blobs:
            if p.endswith("SKILL.md"):
                d = p[: -len("SKILL.md")]
                skills.append({"slug": d.rstrip("/").split("/")[-1], "path": p,
                               "py": [b for b in blobs if b.startswith(d) and b.endswith(".py")]})
        if skills:
            out[name] = {"branch": r["default_branch"], "skills": sorted(skills, key=lambda s: s["slug"])}
    return out


def parse_frontmatter(body):
    if not body.startswith("---"):
        return {}
    end = body.find("\n---", 3)
    if end < 0:
        return {}
    fm, cur = {}, None
    for line in body[3:end].split("\n"):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            cur = m.group(1)
            fm[cur] = m.group(2).strip().strip('"').strip("'")
        elif line.strip().startswith("-") and cur:
            fm[cur] = (fm.get(cur, "") + " " + line.strip().lstrip("- ")).strip()
    return fm


def classify(py_sources):
    """Sc = compute-bearing (portable). Si = does I/O (needs the network)."""
    if not py_sources:
        return "-"
    return "Si" if any(NET.search(s) for s in py_sources) else "Sc"


def hebrew_terms():
    if not os.path.exists(HE_TERMS):
        return {}
    out = {}
    for line in open(HE_TERMS, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#") or "\t" not in line:
            continue
        slug, terms = line.split("\t", 1)
        out[slug.strip()] = terms.strip()
    return out


def build():
    repos = discover()
    jobs = [(r, d["branch"], s) for r, d in repos.items() for s in d["skills"]]
    print(f"{len(repos)} repos, {len(jobs)} skills")

    def fetch(job):
        repo, branch, s = job
        url = f"{RAW}/{ORG}/{repo}/{branch}/{s['path']}"
        body = json.loads(cached(f"skill-{repo}-{s['slug']}.json", lambda: json.dumps(get(url, raw=True))))
        py = [json.loads(cached(f"py-{repo}-{os.path.basename(p)}.json",
                                lambda p=p: json.dumps(get(f"{RAW}/{ORG}/{repo}/{branch}/{p}", raw=True))))
              for p in s["py"][:3]]
        return {"repo": repo, "slug": s["slug"], "url": url, "fm": parse_frontmatter(body),
                "flag": classify(py), "n_py": len(s["py"])}

    with ThreadPoolExecutor(max_workers=12) as ex:
        rows = list(ex.map(fetch, jobs))

    he = hebrew_terms()
    missing_he = [r["slug"] for r in rows if r["slug"] not in he]
    os.makedirs(OUT, exist_ok=True)

    by_repo = {}
    for r in rows:
        by_repo.setdefault(r["repo"], []).append(r)
    order = [c for c in CATEGORY_ORDER if c in by_repo] + sorted(set(by_repo) - set(CATEGORY_ORDER))

    # shards
    for repo in order:
        rs = sorted(by_repo[repo], key=lambda r: r["slug"])
        L = [f"# {repo}", "",
             f"{len(rs)} skills. Fetch a skill's real instructions from its URL before applying it.",
             "Descriptions are the authors' own, unedited -- including the \"Do NOT use for\" clauses,",
             "which are load-bearing: they are how you tell near-misses apart.", ""]
        for r in rs:
            L.append(f"## {r['slug']}  `{r['flag']}`")
            if r["slug"] in he:
                L.append(f"**he:** {he[r['slug']]}")
            L.append(f"{r['fm'].get('description','(no description)')}")
            L.append(f"`{r['url']}`")
            L.append("")
        open(os.path.join(OUT, f"{repo}.md"), "w", encoding="utf-8").write("\n".join(L))

    # router
    L = ["# Category index", "",
         "Pick 1-2 categories, then read only those files. Never read them all.", ""]
    for repo in order:
        rs = by_repo[repo]
        slugs = ", ".join(sorted(r["slug"] for r in rs)[:6])
        L.append(f"- **{repo}** ({len(rs)}) — e.g. {slugs}…")
    L += ["", f"Flags: `Sc` port the logic and compute · `Si` extract the request contract · `-` instructions only.",
          f"Generated from github.com/{ORG} — {len(rows)} skills."]
    open(os.path.join(OUT, "_index.md"), "w", encoding="utf-8").write("\n".join(L))

    return rows, missing_he


def verify(rows):
    bad = []
    dupes = {}
    for r in rows:
        dupes.setdefault(r["slug"], []).append(r["repo"])
    for slug, repos in dupes.items():
        if len(repos) > 1:
            bad.append(f"duplicate slug {slug!r} in {repos}")
    for r in rows:
        if not r["fm"].get("description"):
            bad.append(f"{r['repo']}/{r['slug']}: no description")

    def head(r):
        try:
            req = urllib.request.Request(r["url"], method="HEAD", headers={"User-Agent": UA["User-Agent"]})
            urllib.request.urlopen(req, timeout=20)
            return None
        except Exception as e:
            return f"{r['repo']}/{r['slug']}: URL failed ({e})"

    with ThreadPoolExecutor(max_workers=12) as ex:
        bad += [b for b in ex.map(head, rows) if b]
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    ARGS = ap.parse_args()

    rows, missing_he = build()
    sizes = {f: os.path.getsize(os.path.join(OUT, f)) for f in sorted(os.listdir(OUT))}
    print(f"\nwrote {len(sizes)} files to catalog/")
    for f, n in sorted(sizes.items(), key=lambda kv: -kv[1])[:6]:
        print(f"  {f:<28} {n:>7,} chars  ~{n//4:>5,} tok")
    print(f"  router (_index.md)         ~{sizes['_index.md']//4:,} tok")
    print(f"\nHebrew terms: {len(rows)-len(missing_he)}/{len(rows)} rows "
          f"({len(missing_he)} missing -> tools/hebrew_terms.tsv)")

    if ARGS.verify:
        print("\nverifying...")
        bad = verify(rows)
        print("  OK" if not bad else "\n".join("  FAIL " + b for b in bad))
        sys.exit(1 if bad else 0)
