"""Build the print PDFs from markdown in print/:
  briefing.md  -> pdf/can-britain-feed-itself.pdf (22 pages, references at the foot of each page)
  one-pager.md -> pdf/uk-food-reserve-at-a-glance.pdf (one page, then all sources and working)
  regen-business-case.md -> pdf/regenerative-farming-business-case.pdf (same format)

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
CSS = (PRINT / "style.css").read_text()
DOCS = [
    ("briefing.md", "can-britain-feed-itself.pdf", "Can Britain Feed Itself? Store and grow", ""),
    ("one-pager.md", "uk-food-reserve-at-a-glance.pdf", "Strategic Food Reserve and Food Independence",
     '@page { @bottom-left { content: "Strategic Food Reserve and Food Independence · Planetary Council · planetarycouncil@protonmail.com"; } }'
     '@page :first { @bottom-left { content: "Planetary Council · planetarycouncil@protonmail.com · sources and working from page 2"; } }'),
    ("regen-business-case.md", "regenerative-farming-business-case.pdf", "Farming That Rebuilds Soil: The Business Case",
     '@page { @bottom-left { content: "Farming That Rebuilds Soil · Planetary Council · planetarycouncil@protonmail.com"; } }'
     '@page :first { @bottom-left { content: "Planetary Council · planetarycouncil@protonmail.com · sources and working from page 2"; } }'),
]

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
    for src, out, title, extra_css in DOCS:
        pdf = OUT / out
        body = md_to_html(preprocess((PRINT / src).read_text()))
        html = PRINT / src.replace(".md", ".html")
        html.write_text(PAGE.format(title=title, css=CSS + extra_css, body=body))
        over = render(html, pdf)
        for page, px, t in over:
            print(f"OVERFLOW page {page} ({t}): {px}px")
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        n = [l for l in info.splitlines() if l.startswith("Pages:")][0].split()[-1]
        print(f"{pdf.relative_to(ROOT)}: {n} pages, {pdf.stat().st_size/1e6:.1f} MB")


if __name__ == "__main__":
    main()
