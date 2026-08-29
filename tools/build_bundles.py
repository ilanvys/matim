#!/usr/bin/env python3
"""Package the uploadable skill bundles into dist/.

claude.ai expects a .zip whose root contains ONE folder, and that folder must
hold SKILL.md at its top level. Reference files sit alongside it.
"""
import os, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")


def build(name, files):
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, f"{name}.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in files:
            z.write(os.path.join(ROOT, src), f"{name}/{arc}")
    print(f"{out}  ({os.path.getsize(out):,} bytes, {len(files)} files)")


if __name__ == "__main__":
    build("q1b-probe", [("tests/q1b-probe/SKILL.md", "SKILL.md"),
                        ("tests/q1b-probe/urls.md", "urls.md")])
    build("matim", [("SKILL.md", "SKILL.md")] +
          [(f"catalog/{f}", f"catalog/{f}") for f in sorted(os.listdir(os.path.join(ROOT, "catalog")))])
