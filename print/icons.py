"""Line icons for the print edition (24x24 grid, drawn by hand).

Used in print/briefing.md as :i-name: and replaced by inline SVG at build time,
so they take the card's text colour.
"""

ICONS = {
    "wheat": '<path d="M12 22V8"/><path d="M12 8c-2-1-3-3-3-5 2 1 3 3 3 5z"/><path d="M12 8c2-1 3-3 3-5-2 1-3 3-3 5z"/>'
             '<path d="M12 13c-2.5-.5-4-2.5-4-4.5 2.5.5 4 2.5 4 4.5z"/><path d="M12 13c2.5-.5 4-2.5 4-4.5-2.5.5-4 2.5-4 4.5z"/>'
             '<path d="M12 18c-2.5-.5-4-2.5-4-4.5 2.5.5 4 2.5 4 4.5z"/><path d="M12 18c2.5-.5 4-2.5 4-4.5-2.5.5-4 2.5-4 4.5z"/>',
    "silo": '<path d="M5 21V9a4 4 0 0 1 8 0v12"/><path d="M5 12h8M5 16h8"/><path d="M13 21v-8h6v8"/><path d="M3 21h18"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "ship": '<path d="M3 15h18l-2.5 5h-13z"/><path d="M6 15v-4h4v4M10 15V9h4v6M14 15v-4h4v4"/><path d="M2 22c2 0 2-1 4-1s2 1 4 1 2-1 4-1 2 1 4 1 2-1 4-1"/>',
    "people": '<circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M2.5 20a5.5 5.5 0 0 1 11 0"/><path d="M14 20a4 4 0 0 1 7.5-2"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    "pound": '<circle cx="12" cy="12" r="9"/><path d="M14.5 8.5A2.5 2.5 0 0 0 10 10v6M8 13h5M8 16h7"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9s1-6.5 3.5-9z"/>',
    "thermo": '<path d="M10 14V5a2 2 0 0 1 4 0v9a4 4 0 1 1-4 0z"/><path d="M12 9v7"/><path d="M17 6h3M17 9h2M17 12h3"/>',
    "sprout": '<path d="M12 21v-9"/><path d="M12 12c0-4-3-6-7-6 0 4 3 6 7 6z"/><path d="M12 14c0-3.5 2.5-5.5 6.5-5.5 0 3.5-2.5 5.5-6.5 5.5z"/><path d="M6 21h12"/>',
    "house": '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
    "sheep": '<path d="M6 11a3 3 0 0 1 3-3 3 3 0 0 1 5 0 3 3 0 0 1 3 4 3 3 0 0 1-2 5H8a3 3 0 0 1-2-6z"/><path d="M9 17v3M14 17v3"/><circle cx="19.5" cy="10" r="1.8"/>',
    "scale": '<path d="M12 4v16M7 20h10M4 7h16"/><path d="M6 7 3 13a3 3 0 0 0 6 0z"/><path d="m18 7-3 6a3 3 0 0 0 6 0z"/>',
    "chart": '<path d="M4 20V4"/><path d="M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
    "alert": '<path d="M12 4 2.5 20h19z"/><path d="M12 10v4.5"/><circle cx="12" cy="17.3" r=".6" fill="currentColor"/>',
    "factory": '<path d="M3 21V11l5 3V11l5 3V7h3l1-4h2l1 4v14z"/><path d="M3 21h18"/><path d="M7 18h2M12 18h2"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "fish": '<path d="M3 12c3-4 8-5 12-3l4-3v12l-4-3c-4 2-9 1-12-3z"/><circle cx="7.5" cy="11.5" r=".8" fill="currentColor"/>',
    "seed": '<path d="M12 3c4 3 6 7 6 11a6 6 0 0 1-12 0c0-4 2-8 6-11z"/><path d="M12 7v13"/>',
    "ladder": '<path d="M7 3v18M17 3v18"/><path d="M7 7h10M7 11h10M7 15h10M7 19h10"/>',
    "law": '<path d="M5 21h14M7 18h10"/><path d="M6 9h12M12 5l7 4H5z"/><path d="M8 9v9M12 9v9M16 9v9"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "tractor": '<circle cx="7" cy="16" r="4"/><circle cx="18" cy="17.5" r="2.5"/><path d="M11 16h4.5M5 12V7h6l2 5h6v3"/><path d="M8 7V4"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "box": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/>',
    "heart": '<path d="M12 20s-8-4.5-8-10.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 8 2.5C20 15.5 12 20 12 20z"/>',
}


def svg(name, cls="ico"):
    body = ICONS[name]
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')
