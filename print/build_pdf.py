"""Build the print PDF: pdf/can-britain-feed-itself.pdf (one file, from print/briefing.md).

Each page is a two-column grid of cards with numbered references at its foot.
In briefing.md, ^1^ or ^1,2^ marks a reference to item 1 (and 2) of that page's
::: {.refs} list, and :i-name: inserts an icon from print/icons.py.

Needs pandoc and Playwright's Chromium.
Run:  python3 print/build_pdf.py
"""
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from icons import svg  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRINT = ROOT / "print"
OUT = ROOT / "pdf"
PDF = OUT / "can-britain-feed-itself.pdf"
CSS = (PRINT / "style.css").read_text()

PAGE = """<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>{title}</title>
<style>{css}</style></head>
<body>
{body}
</body></html>
"""


def link_page(md, k):
    """Turn ^n^ markers and the numbered refs list of page k into anchors."""
    def sup(m):
        nums = m.group(1).split(",")
        links = ",".join(f'<a href="#p{k}r{n}">{n}</a>' for n in nums)
        return f'<sup class="fn">{links}</sup>'
    md = re.sub(r"\^(\d+(?:,\d+)*)\^", sup, md)
    head, sep, refs = md.partition("::: {.refs}")
    if sep:
        refs = re.sub(r"^(\d+)\. ", lambda m: f"{m.group(1)}. []{{#p{k}r{m.group(1)}}}",
                      refs, flags=re.M)
    return head + sep + refs


def preprocess(md):
    md = re.sub(r":i-([a-z]+):", lambda m: svg(m.group(1)), md)
    pages = re.split(r"(?m)^(?=::: \{\.page)", md)
    return "".join(link_page(p, k) for k, p in enumerate(pages))


def md_to_html(md):
    return subprocess.run(
        ["pandoc", "-f", "markdown+fenced_divs+pipe_tables+bracketed_spans+superscript",
         "-t", "html5", "--wrap=none"],
        input=md, check=True, capture_output=True, text=True).stdout


def render(html_path, pdf_path):
    """Print to PDF and report any page whose content overflows its A4 box."""
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{html_path}', {{ waitUntil: 'networkidle' }});
  await p.emulateMedia({{ media: 'print' }});
  await p.addStyleTag({{ content: 'body {{ width: 180mm; }}' }});
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')]
    .map((el, i) => [i + 1, Math.max(el.scrollHeight - el.clientHeight, ...[...el.querySelectorAll('.grid')].map(g => g.scrollWidth - g.clientWidth)), (el.querySelector('h2,h1')||{{}}).textContent])
    .filter(x => x[1] > 1));
  console.log(JSON.stringify(over));
  await p.addStyleTag({{ content: 'body {{ width: auto; }}' }});
  await p.pdf({{ path: '{pdf_path}', preferCSSPageSize: true, printBackground: true }});
  await b.close();
}})();
"""
    out = subprocess.run(["node", "-e", js], check=True, capture_output=True, text=True).stdout
    return json.loads(out.strip().splitlines()[-1])


def main():
    OUT.mkdir(exist_ok=True)
    body = md_to_html(preprocess((PRINT / "briefing.md").read_text()))
    html = PRINT / "briefing.html"
    html.write_text(PAGE.format(title="Can Britain Feed Itself? Store and grow", css=CSS, body=body))
    over = render(html, PDF)
    for page, px, title in over:
        print(f"OVERFLOW page {page} ({title}): {px}px")
    info = subprocess.run(["pdfinfo", str(PDF)], capture_output=True, text=True).stdout
    n = [l for l in info.splitlines() if l.startswith("Pages:")][0].split()[-1]
    print(f"{PDF.relative_to(ROOT)}: {n} pages, {PDF.stat().st_size/1e6:.1f} MB")


if __name__ == "__main__":
    main()
