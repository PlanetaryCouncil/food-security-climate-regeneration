"""The UK Strategic Food Reserve: cost model, version 3.1 (hybrid, human food first).

Illustrative carrying-cost model with explicit allowances. It is NOT a
procurement estimate: prices, fees and allowances are assumptions, not quotes.
See research/notes/20 (round 1) and 24 (round 2) for what changed and why.

Design after review round 2:
- Tier 1, PUBLIC CRISIS TRANCHE (owned and paid by the state, from taxation):
  what markets will not hold and week one needs - no-cook food, infant formula,
  micronutrient tablets, flour premix, sacks, bottled water, plus operations
  (agency, local plans, priority fuel/AdBlue/backup power, last mile).
- Tier 2, COMPULSORY COMMERCIAL STOCKS (Swiss / Singapore model): importers,
  millers, merchants and compounders must hold stock ADDITIONAL to their normal
  working stock. It rotates through their own trade, stays off the public
  balance sheet, and its cost is passed through food prices. Each line is
  sized against UK annual use so rotation stays a small share of the market.

Version 3.1 (author decision, note 25): human food first and food for EVERYONE.
Food-grade wheat raised to 4 Mt (bread for the whole population), a universal
3-day no-cook grain ration (crispbread / biscuits / oatcakes made from reserve
grain) for all 69.5 m, and a smaller specialist top-up for people who cannot
use standard rations. Grain is first in the priority schedule.

Run:  python3 research/model/reserve_basket.py
"""

POP = 69.5e6
FINANCE = 0.04              # cost of holding stock value, per year
MILL_WHEAT_T_YR = 4.8e6     # UK Flour Millers: wheat milled in 2025 (usage, not capacity)
EXTRACTION = 0.85           # emergency flour (1942 "National Loaf" was 85%); bran to feed
HANDLING = 18               # GBP per rotated tonne: handling in/out + local haulage (Camgrain
                            # publishes GBP 9.90/t handling, haulage extra)


def annuity(rate, years=25):
    return rate / (1 - (1 + rate) ** -years)


# ---------------------------------------------------------------------------
# Tier 2: compulsory commercial stocks
# name: (stock t, UK annual use t [for the market check], price GBP/t,
#        rotation share per yr, value lost per rotated tonne, storage GBP/t/yr)
# UK annual use figures are rounded orders of magnitude; see note 24.
# ---------------------------------------------------------------------------
COMMERCIAL = {
    "Food-grade milling wheat (4 Mt; half in new stores)":
        (4.0e6, 4.8e6, 210, 0.20, 0.03, 18),
    "High-protein wheat for the grist (~90 days of the imported share)":
        (0.35e6, 1.3e6, 260, 0.25, 0.02, 18),
    "Rice, ~4 months of UK use":
        (0.22e6, 0.67e6, 500, 0.25, 0.03, 20),
    "Vegetable oil, ~4 months of rapeseed-oil use":
        (0.135e6, 0.41e6, 1000, 0.50, 0.03, 25),
    "Sugar, ~2 months of UK use":
        (0.33e6, 2.0e6, 500, 0.25, 0.02, 15),
    "Pulses (UK-grown, food grade)":
        (0.30e6, 0.68e6, 350, 0.33, 0.05, 20),
    "Oats (stabilised)":
        (0.10e6, 0.50e6, 260, 0.67, 0.05, 15),
    "Skimmed milk powder":
        (0.05e6, 0.25e6, 2500, 0.40, 0.05, 60),
    "Canned fish (mackerel/herring/sardine)":
        (0.04e6, 0.15e6, 5000, 0.25, 0.05, 80),
    "Soya meal, 10 weeks of imports":
        (2.39e6 * 10 / 52, 2.39e6, 450, 3.0, 0.01, 12),
    "Cereal seed, winter 0.2 Mt + spring 0.1 Mt (segregated)":
        (0.30e6, 0.60e6, 300, 1.0, 100 / 300, 15),     # premium lost each year
    "Protected urea, extra pre-season merchant stock (92 kt N)":
        (0.20e6, 0.38e6, 380, 1.0, 0.03, 20),
    "UAN-28, heated/recirculated tanks (70 kt N)":
        (0.25e6, 0.56e6, 300, 1.0, 0.03, 12),
}
NEW_STORE_T = 2.0e6          # half the wheat needs new capacity
NEW_STORE_CAPEX = 350        # GBP/t of capacity (reviewers: GBP 200 too low; 300-600 range)


def commercial(finance=FINANCE, store_mult=1.0, loss_mult=1.0, price_mult=1.0, wheat_mt=4.0):
    rows = []
    for name, (t, use, price, rot, loss, store) in COMMERCIAL.items():
        if name.startswith("Food-grade milling wheat"):
            t = wheat_mt * 1e6
        v = t * price * price_mult
        rotated = t * rot
        a = (t * store * store_mult + v * finance + rotated * price * price_mult * loss * loss_mult
             + rotated * HANDLING * store_mult)
        if name.startswith("Food-grade milling wheat"):
            a += NEW_STORE_T * (wheat_mt / 4.0) * NEW_STORE_CAPEX * annuity(finance) * store_mult
        rows.append((name, t, v, a, rotated / use))
    return rows


# ---------------------------------------------------------------------------
# Tier 1: public crisis tranche (stock lines) and operations
# ---------------------------------------------------------------------------
def public(finance=FINANCE, store_mult=1.0, loss_mult=1.0, price_mult=1.0, nocook_gbp_day=6.0):
    rows = []

    def line(name, value, life, loss, storage_cost):
        v = value * price_mult
        a = v * finance + v * min(1.0, 1 / life) * loss * loss_mult + storage_cost * store_mult
        rows.append((name, v, a))

    # universal: 3 days of no-cook grain ration for EVERYONE (~500 g/day crispbread,
    # biscuits, oatcakes, ~2,000 kcal), rotated into schools, forces, food banks and
    # WFP-style high-energy-biscuit aid
    uni_t = POP * 3 * 0.5 / 1000
    line("No-cook grain ration for EVERYONE: 3 days (crispbread/biscuits/oatcakes from reserve grain)",
         uni_t * 2000, 2.0, 0.15, uni_t * 40)
    nc_days = 5e6 * 7
    line("Specialist no-cook top-up: 7 days for 5 m who cannot use standard rations",
         nc_days * nocook_gbp_day, 2.5, 0.25, nc_days / 1000 * 40)
    line("Infant formula ~7 kt standard powder (manufacturer-held) + ready-to-feed",
         7000 * 12000, 1.5, 0.05, 2.5e6)
    line("Specialised infant formula and medical foods (allowance)", 30e6, 1.5, 0.10, 1.0e6)
    line("Tablets: vitamins A, C, D + zinc, 90 days for everyone", POP * 90 * 0.015, 2.0, 0.30, 1.0e6)
    line("Flour premix incl. folic acid, potassium iodate, feed amino acids, dried yeast",
         24e6, 2.0, 0.10, 0.7e6)
    line("Flour sacks, oil bottles, labels, pallets (one-off stock, rotated into mills)",
         50e6, 3.0, 0.05, 1.0e6)
    line("Bottled water: 90 m litres (10 m people x 3 days x 3 L)", 90e6 * 0.20, 2.0, 0.30,
         90e3 * 30)
    ops = {"agency, audit, intake and mycotoxin testing": 45,
           "local food plans in all four nations, exercises": 46,
           "priority fuel, AdBlue and backup power on a published priority list": 100,
           "last mile: registers, delivery contracts, water bowsers": 45,
           "security, insurance, fumigation": 15}
    for k, m in ops.items():
        rows.append(("Operations: " + k, 0.0, m * 1e6 * store_mult))
    return rows, ops


def totals(**kw):
    nocook = kw.pop("nocook_gbp_day", 6.0)
    wheat = kw.pop("wheat_mt", 4.0)
    c = commercial(wheat_mt=wheat, **kw)
    p, _ = public(nocook_gbp_day=nocook, **kw)
    return sum(r[3] for r in c), sum(r[2] for r in p), sum(r[2] for r in c), sum(r[1] for r in p)


def print_package():
    c = commercial()
    p, ops = public()
    print("TIER 2: compulsory commercial stocks (off the public balance sheet; cost passed through prices)")
    print("| Line | Stock (kt) | Stock value (£m) | Annual cost (£m) | Rotation as % of UK use |")
    print("|---|---|---|---|---|")
    for name, t, v, a, share in c:
        print(f"| {name} | {t/1e3:,.0f} | {v/1e6:,.0f} | {a/1e6:.0f} | {share:.0%} |")
    ca = sum(r[3] for r in c); cv = sum(r[2] for r in c); ct = sum(r[1] for r in c)
    print("(Soya, seed and nitrogen rotate inside their normal flow, first-in-first-out: the % is the share of "
          "normal trade passing through the extra stock, not extra supply.)")
    print(f"| **Tier 2 total** | **{ct/1e6:.1f} Mt** | **{cv/1e6:,.0f}** | **{ca/1e6:.0f}** | |")
    print("\nTIER 1: public crisis tranche and operations (owned by the state; paid from taxation)")
    print("| Line | Stock value (£m) | Annual cost (£m) |")
    print("|---|---|---|")
    for name, v, a in p:
        print(f"| {name} | {v/1e6:,.0f} | {a/1e6:.0f} |")
    pa = sum(r[2] for r in p); pv = sum(r[1] for r in p)
    print(f"| **Tier 1 total** | **{pv/1e6:,.0f}** | **{pa/1e6:.0f}** |")
    print(f"\nTOTAL annual £{(ca+pa)/1e6:.0f}m = £{(ca+pa)/POP:.2f}/person/yr "
          f"(public £{pa/POP:.2f} via taxes; compulsory stocks £{ca/POP:.2f} via prices)")
    print(f"Public stock on the balance sheet: £{pv/1e9:.2f}bn (£{pv/POP:.0f}/person). "
          f"Commercial stock: £{cv/1e9:.2f}bn, held by firms. New wheat stores: "
          f"£{NEW_STORE_T*NEW_STORE_CAPEX/1e9:.2f}bn, financed by store operators.")


def sensitivity():
    cases = [
        ("Low: finance 3.5%, storage/ops -10%", dict(finance=0.035, store_mult=0.9)),
        ("Central", dict()),
        ("No-cook at £8/day instead of £6", dict(nocook_gbp_day=8.0)),
        ("Prices +30%", dict(price_mult=1.3)),
        ("Stress: finance 6%, storage/ops +50%, rotation losses x2",
         dict(finance=0.06, store_mult=1.5, loss_mult=2.0)),
        ("Severe stress: stress + prices +30%",
         dict(finance=0.06, store_mult=1.5, loss_mult=2.0, price_mult=1.3)),
    ]
    print("\n| Case | Public (£/person) | Compulsory stocks (£/person) | Total (£/person) |")
    print("|---|---|---|---|")
    for label, kw in cases:
        ca, pa, _, _ = totals(**kw)
        print(f"| {label} | {pa/POP:.2f} | {ca/POP:.2f} | {(ca+pa)/POP:.2f} |")


def priority_schedule():
    """What each funding level buys, in order of priority (round-2 request)."""
    c = {r[0]: r[3] for r in commercial()}
    p, _ = public()
    p = {r[0]: r[2] for r in p}
    order = [
        ("1. Bread for everyone: 4 Mt food-grade wheat, high-protein wheat, premix, sacks",
         [k for k in c if k.startswith(("Food-grade", "High-protein"))]
         + [k for k in p if k.startswith(("Flour premix", "Flour sacks"))]),
        ("2. No-cook for everyone: 3-day grain ration, tablets, bottled water",
         [k for k in p if k.startswith(("No-cook grain", "Tablets", "Bottled"))]),
        ("3. Operations: agency, local plans, priority fuel/power, last mile, security",
         [k for k in p if k.startswith("Operations")]),
        ("4. Infants and special needs: formula, medical foods, specialist top-up",
         [k for k in p if k.startswith(("Infant", "Specialised", "Specialist"))]),
        ("5. Next season: seed, protected urea, UAN, soya meal",
         [k for k in c if k.startswith(("Cereal seed", "Protected urea", "UAN", "Soya"))]),
        ("6. Imported staples and variety: rice, oil, sugar, pulses, oats, milk powder, fish",
         [k for k in c if k.startswith(("Rice", "Vegetable oil", "Sugar", "Pulses", "Oats", "Skimmed", "Canned"))]),
    ]
    print("\nPriority schedule: cumulative cost per person")
    print("| Tier | Adds (£/person) | Cumulative (£/person) |")
    print("|---|---|---|")
    cum = 0.0
    for label, keys in order:
        add = sum(p.get(k, 0) + c.get(k, 0) for k in keys) / POP
        cum += add
        print(f"| {label} | {add:.2f} | {cum:.2f} |")


# illustrative adult survival day released from the stocks, with domestic food continuing
# item: g/day, kcal/100g, protein/100g, calcium mg/100g (as eaten)
DAY = {
    "Flour, 85% extraction, fortified (from 180 g wheat)": (180 * EXTRACTION, 345, 12.0, 120),
    "Rice": (80, 360, 7.0, 10),
    "Pulses (part pre-cooked/canned)": (60, 340, 24.0, 90),
    "Oil": (50, 900, 0.0, 0),
    "Sugar": (25, 400, 0.0, 0),
    "Oats": (25, 375, 11.0, 50),
    "Skimmed milk powder": (20, 360, 36.0, 1250),
    "Canned fish (with bones)": (20, 230, 20.0, 250),
    "Potatoes (domestic, fresh)": (300, 77, 2.0, 5),
}


def checks():
    g = sum(v[0] for v in DAY.values())
    kcal = sum(v[0] * v[1] / 100 for v in DAY.values())
    prot = sum(v[0] * v[2] / 100 for v in DAY.values())
    ca = sum(v[0] * v[3] / 100 for v in DAY.values())
    print(f"\nIllustrative adult survival day (stocks + domestic potatoes): {g:.0f} g, {kcal:.0f} kcal, "
          f"{prot:.0f} g protein, calcium {ca:.0f} mg; + tablets (A, C, D, zinc). "
          "Not a dietitian-approved ration; variants needed.")
    flour_g = MILL_WHEAT_T_YR / 365 / POP * 1e6 * EXTRACTION
    print(f"Bread-first check: at today's mill throughput, flour per person = {flour_g:.0f} g/day "
          f"≈ {flour_g*3.45:.0f} kcal and {flour_g*0.12:.0f} g protein: about a quarter of energy needs. "
          "Bread is the backbone, not the whole diet; potatoes, oats, whole-grain wheat (porridge, "
          "bulgur, flatbreads from diverted feed wheat) and domestic food carry the rest.")
    wheat_t_day = 180 * POP / 1e6
    print(f"Milling: 180 g wheat/person/day = {wheat_t_day:,.0f} t/day vs demonstrated "
          f"{MILL_WHEAT_T_YR/365:,.0f} t/day ({wheat_t_day/(MILL_WHEAT_T_YR/365):.0%}); usage, not capacity.")
    print(f"4 Mt food-grade wheat = {4e6/(MILL_WHEAT_T_YR/365):.0f} days of mill intake: every UK flour mill "
          f"kept running for ~{4e6/MILL_WHEAT_T_YR*12:.0f} months with no imports and no harvest.")


def break_even():
    ca, pa, _, _ = totals()
    a = ca + pa
    print(f"\nBreak-even for £{a/1e6:.0f}m/yr (thresholds, not probabilities):")
    print("| Shock (share of GDP) | Share of loss prevented | Once every … years |")
    print("|---|---|---|")
    for size in (0.01, 0.02):
        for frac in (1.0, 0.25, 0.10):
            print(f"| {size:.0%} | {frac:.0%} | {size*2.9e12*frac/a:.0f} |")


def jobs():
    """Rough direct-employment estimate [E]; planning assumptions, not a labour-market study."""
    rows = [("Reserve agency: inspection, sampling, audit, stock ledger, IT", 400),
            ("Grain and food stores: intake, drying, aeration, monitoring (~1 FTE per 15 kt)",
             round((4.0e6 + 1.6e6) / 15e3)),
            ("Quality labs: moisture, insects, mycotoxin and nutrient testing", 120),
            ("Haulage of rotated stock (~3 Mt/yr, ~460 loads per driver-year)", round(3e6 / 25 / 460)),
            ("Crispbread/biscuit and canning production for rotation", 150),
            ("Local food-plan officers in ~45 resilience bodies (3 each)", 135),
            ("Exercises, training, delivery-register teams", 100)]
    total = sum(n for _, n in rows)
    print("\nDirect jobs (permanent, approximate)")
    for k, n in rows:
        print(f"- {k}: ~{n}")
    print(f"- Total permanent: ~{total:,}")
    build = NEW_STORE_T * NEW_STORE_CAPEX
    print(f"- Construction: £{build/1e9:.2f}bn of new stores over ~5 years ≈ ~{build/5/100e3:,.0f} "
          "construction jobs a year while building (at ~£100k of spend per job-year)")
    print("- Optional: a paid 'Food Reserve Volunteers' corps (e.g. 10,000 trained reservists on a "
          "~£1,000/yr retainer ≈ £10m/yr), mustered for releases and exercises")


if __name__ == "__main__":
    print_package()
    sensitivity()
    priority_schedule()
    checks()
    break_even()
    jobs()
