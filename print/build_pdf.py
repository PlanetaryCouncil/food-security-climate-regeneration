"""Build the print PDFs.

1. pdf/can-britain-feed-itself-briefing.pdf  (short edition, from print/briefing.md)
2. pdf/can-britain-feed-itself-evidence.pdf  (full evidence edition, from draft/briefing_full_context.md)

Needs pandoc and Playwright's Chromium.
Run:  python3 print/build_pdf.py
"""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRINT = ROOT / "print"
OUT = ROOT / "pdf"
CSS = (PRINT / "style.css").read_text()

PAGE = """<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>{title}</title>
<style>{css}</style></head>
<body class="{body_class}">
{body}
</body></html>
"""


def md_to_html(md_path, fmt="markdown+fenced_divs+pipe_tables+bracketed_spans"):
    return subprocess.run(
        ["pandoc", "-f", fmt, "-t", "html5",
         "--wrap=none", str(md_path)],
        check=True, capture_output=True, text=True).stdout


def write_html(name, title, body, body_class=""):
    path = PRINT / name
    path.write_text(PAGE.format(title=title, css=CSS, body=body, body_class=body_class))
    return path


def render(html_path, pdf_path):
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{html_path}', {{ waitUntil: 'networkidle' }});
  await p.pdf({{ path: '{pdf_path}', preferCSSPageSize: true, printBackground: true }});
  await b.close();
}})();
"""
    subprocess.run(["node", "-e", js], check=True)


def main():
    OUT.mkdir(exist_ok=True)
    short = write_html("briefing.html", "Can Britain Feed Itself? Store and grow",
                       md_to_html(PRINT / "briefing.md"))
    render(short, OUT / "can-britain-feed-itself-briefing.pdf")

    full_md = (ROOT / "draft" / "briefing_full_context.md").read_text()
    tmp = PRINT / "_evidence.md"
    tmp.write_text(full_md)
    evidence = write_html("evidence.html", "Can Britain Feed Itself? Evidence edition",
                          md_to_html(tmp, fmt="gfm"), body_class="evidence")
    tmp.unlink()
    render(evidence, OUT / "can-britain-feed-itself-evidence.pdf")
    for f in sorted(OUT.glob("*.pdf")):
        pages = subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout
        n = [l for l in pages.splitlines() if l.startswith("Pages:")][0].split()[-1]
        print(f"{f.relative_to(ROOT)}: {n} pages, {f.stat().st_size/1e6:.1f} MB")


if __name__ == "__main__":
    main()
