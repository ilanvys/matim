#!/usr/bin/env python3
"""Server-level smoke tests for matim-mcp.

This checks what the *service* does, not what a model chooses to do with it.
Routing, ranking and disclosure are model behaviour and cannot be tested from
here -- those are cases.tsv, run by hand on each surface. See tests/README.md.

    python3 tests/smoke.py                 # all checks
    python3 tests/smoke.py S05 S07 S08     # only these
    MATIM_MCP_URL=... python3 tests/smoke.py
"""
import json, os, sys, urllib.request, urllib.error

URL = os.environ.get("MATIM_MCP_URL", "https://matim-mcp.vercel.app/api/mcp")
TIMEOUT = 30
# A skill that has both a references/ file and a scripts/ file, so the two
# lazily-loaded classes are covered by a real fetch rather than a listing.
SLUG, REF, SCRIPT = ("israeli-urban-renewal-owner-guide",
                     "references/tracks-and-majorities.md",
                     "scripts/majority_threshold.py")

_id = [0]


def rpc(method, params=None):
    _id[0] += 1
    body = json.dumps({"jsonrpc": "2.0", "id": _id[0],
                       "method": method, "params": params or {}}).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        raw = r.read().decode()
    # Streamable HTTP answers as SSE; the JSON sits on the data: line.
    for line in raw.splitlines():
        if line.startswith("data: "):
            return json.loads(line[6:])
    return json.loads(raw)


def call(tool, args):
    """A tool result is text. Failures arrive as ordinary text from a call that
    succeeded, so callers must inspect the string -- not just the absence of an error."""
    d = rpc("tools/call", {"name": tool, "arguments": args})
    if "error" in d:
        return "<<JSONRPC ERROR>> " + json.dumps(d["error"])
    return d["result"]["content"][0]["text"]


CHECKS = []


def check(fn):
    CHECKS.append(fn)
    return fn


@check
def S01_initialize():
    """initialize reports serverInfo.name = matim-mcp"""
    d = rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                           "clientInfo": {"name": "smoke", "version": "0"}})
    n = d["result"]["serverInfo"]["name"]
    assert n == "matim-mcp", f"serverInfo.name = {n!r}"


@check
def S02_tools_listed():
    """all three tools are advertised"""
    names = {t["name"] for t in rpc("tools/list")["result"]["tools"]}
    assert names == {"get_catalog", "list_skill_files", "get_skill"}, names


@check
def S03_catalog_index():
    """get_catalog with no argument returns the category index"""
    t = call("get_catalog", {})
    assert "tax-and-finance" in t and "government-services" in t, t[:200]


@check
def S04_catalog_bad_category():
    """an unknown category is answered with the list of real ones, not a stack trace"""
    t = call("get_catalog", {"category": "not-a-category"})
    assert "not-a-category" in t and "tax-and-finance" in t, t[:200]


@check
def S05_skill_default():
    """get_skill defaults to SKILL.md and carries provenance"""
    t = call("get_skill", {"slug": SLUG})
    assert t.startswith("source:"), t[:120]
    assert "license: MIT (skills-il)" in t, "license line missing"
    assert "catalog: https://agentskills.co.il" in t, "catalog line missing"


@check
def S06_skill_hebrew():
    """SKILL_HE.md resolves and is actually Hebrew"""
    t = call("get_skill", {"slug": SLUG, "file": "SKILL_HE.md"})
    assert t.startswith("source:"), t[:120]
    body = t.split("\n\n", 1)[1]
    assert any("֐" <= c <= "ת" for c in body[:2000]), "no Hebrew in SKILL_HE.md"


@check
def S07_reference_file():
    """a references/ file is fetchable by path"""
    t = call("get_skill", {"slug": SLUG, "file": REF})
    assert t.startswith("source:"), t[:200]
    assert REF in t.splitlines()[0], "source line does not name the reference"
    assert len(t) > 400, f"reference suspiciously short ({len(t)} chars)"


@check
def S08_script_file():
    """a scripts/ file is fetchable, and comes back as real source"""
    t = call("get_skill", {"slug": SLUG, "file": SCRIPT})
    assert t.startswith("source:"), t[:200]
    body = t.split("\n\n", 1)[1]
    assert "def " in body or "import " in body, "does not look like Python source"


@check
def S09_unknown_slug():
    """an unknown slug is refused by name, and does not 500"""
    t = call("get_skill", {"slug": "no-such-skill-at-all"})
    assert t.startswith("Unknown skill"), t[:200]


@check
def S10_unknown_file():
    """a wrong path lists what does exist, so the caller can recover"""
    t = call("get_skill", {"slug": SLUG, "file": "references/nope.md"})
    assert "does not exist for" in t, t[:200]
    assert "SKILL.md" in t, "the recovery list is missing"


@check
def S11_list_files():
    """list_skill_files exposes both lazily-loaded classes"""
    t = call("list_skill_files", {"slug": SLUG})
    assert "references/" in t and "scripts/" in t, t[:300]


@check
def S12_no_folder_fetch():
    """a folder is not a file -- it must be refused, not silently concatenated"""
    t = call("get_skill", {"slug": SLUG, "file": "references/"})
    assert "does not exist for" in t, t[:200]


def main():
    only = {a.upper() for a in sys.argv[1:]}
    todo = [c for c in CHECKS if not only or c.__name__.split("_")[0] in only]
    if not todo:
        print("no checks matched", file=sys.stderr)
        return 2
    print(f"matim-mcp smoke  ->  {URL}\n")
    bad = 0
    for c in todo:
        cid = c.__name__.split("_")[0]
        try:
            c()
            print(f"  PASS  {cid}  {c.__doc__}")
        except AssertionError as e:
            bad += 1
            print(f"  FAIL  {cid}  {c.__doc__}\n          {e}")
        except Exception as e:
            bad += 1
            print(f"  ERROR {cid}  {c.__doc__}\n          {type(e).__name__}: {e}")
    print(f"\n{len(todo) - bad}/{len(todo)} passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
