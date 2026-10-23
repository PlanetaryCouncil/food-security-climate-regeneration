"""Combine research/notes/README.md and every numbered note into one page.

Run:  python3 research/build_all_notes.py
Output: research/all-research-notes.md
"""

from pathlib import Path

NOTES = Path(__file__).parent / "notes"
OUT = Path(__file__).parent / "all-research-notes.md"


def title_of(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def main():
    notes = sorted(p for p in NOTES.glob("[0-9][0-9]-*.md"))
    parts = [
        "# All research notes: UK food security, climate and regeneration\n",
        "One page with the index and all research notes, generated from `research/notes/` "
        "by `research/build_all_notes.py`. Edit the individual notes, then re-run the script.\n",
        "## Contents\n",
        "- [Index and key findings](#index-and-key-findings)",
    ]
    for p in notes:
        anchor = f"note-{p.stem[:2]}"
        parts.append(f"- [{title_of(p)}](#{anchor})")
    parts.append("\n---\n")
    parts.append('<a id="index-and-key-findings"></a>\n')
    parts.append("## Index and key findings\n")
    readme = (NOTES / "README.md").read_text(encoding="utf-8")
    # demote headings by one level so the combined page has a single H1
    parts.append("\n".join(("#" + l) if l.startswith("#") else l for l in readme.splitlines()))
    for p in notes:
        parts.append("\n\n---\n")
        parts.append(f'<a id="note-{p.stem[:2]}"></a>\n')
        text = p.read_text(encoding="utf-8")
        parts.append("\n".join(("#" + l) if l.startswith("#") else l for l in text.splitlines()))
    OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB, {len(notes)} notes)")


if __name__ == "__main__":
    main()
