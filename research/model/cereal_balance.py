"""First-cut monthly UK cereal balance under import-stop scenarios.

Illustrative only. Every input is a rounded assumption listed in BASE and
documented in research/gaps/09-diet-shift-mass-balance.md. The model tracks one
pooled stock of wheat, barley and oats (Mt), starting 1 July (pre-harvest low).
It answers one question: under a given shock, in which month does the pooled
cereal stock run out, and how much feed must be cut to keep food milling whole?
It does not model protein, fats, micronutrients, quality or regional logistics.

Run:  python3 research/model/cereal_balance.py
"""

MONTHS = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
          "Jan", "Feb", "Mar", "Apr", "May", "Jun"]

BASE = {
    "opening_stock": 2.95,   # Mt at 1 Jul: wheat 1.514 + barley ~1.3 + oats ~0.15 (AHDB 2025/26)
    "harvest": 19.5,         # Mt wheat+barley+oats, 2025 (Defra/AHDB, rounded)
    "harvest_split": {"Aug": 0.6, "Sep": 0.4},
    "food_milling": 6.0,     # Mt/yr flour milling, oat milling, food barley (assumption)
    "other_hi": 3.2,         # Mt/yr malting, distilling, bioethanol, starch (AHDB H&I ~9.2 total)
    "feed": 13.4,            # Mt/yr cereals fed to livestock (AHDB 2025/26)
    "seed": 0.6,             # Mt/yr, drawn Sep-Oct (winter) and Mar (spring)
    "seed_split": {"Sep": 0.35, "Oct": 0.35, "Mar": 0.30},
    "exports": 1.0,          # Mt/yr
    "imports": 4.5,          # Mt/yr, incl. maize; calibrated so scenario A roughly closes
}

KCAL_PER_T = 3.3e6           # kcal per tonne of whole cereal grain (rounded)
NEED_KCAL_DAY = 69.5e6 * 2250  # population energy need, kcal/day


def run(name, years=2, harvest_factors=(1.0, 1.0), imports_on=False,
        exports_on=False, other_hi_factor=1.0, feed_factor=1.0,
        extra_reserve=0.0, start=None):
    p = dict(BASE)
    stock = p["opening_stock"] + extra_reserve
    log = []
    for y in range(years):
        for m in MONTHS:
            stock += p["harvest"] * harvest_factors[y] * p["harvest_split"].get(m, 0)
            if imports_on:
                stock += p["imports"] / 12
            out = (p["food_milling"] + p["other_hi"] * other_hi_factor
                   + p["feed"] * feed_factor) / 12
            out += p["seed"] * p["seed_split"].get(m, 0)
            if exports_on:
                out += p["exports"] / 12
            stock -= out
            log.append((f"Y{y+1}-{m}", round(stock, 2)))
    first_empty = next((t for t, s in log if s < 0), None)
    low = min(s for _, s in log)
    return {"scenario": name, "first_month_empty": first_empty or "never",
            "lowest_stock_Mt": low, "log": log}


def feed_needed_to_survive(years, harvest_factors, other_hi_factor, extra=0.0):
    """Largest feed factor (0-1) that keeps the stock >= 0 over the horizon."""
    lo, hi = 0.0, 1.0
    for _ in range(30):
        mid = (lo + hi) / 2
        r = run("probe", years, harvest_factors, other_hi_factor=other_hi_factor,
                feed_factor=mid, extra_reserve=extra)
        if r["lowest_stock_Mt"] >= 0:
            lo = mid
        else:
            hi = mid
    return lo


SCENARIOS = [
    ("A. Normal trade, normal harvests", dict(imports_on=True, exports_on=True)),
    ("B. Imports stop 1 Jul, no policy response", dict()),
    ("C. Imports stop, bioethanol/distilling cut 75%, feed -20%",
     dict(other_hi_factor=0.25, feed_factor=0.8)),
    ("D. As C, two poor harvests (-15% each)",
     dict(other_hi_factor=0.25, feed_factor=0.8, harvest_factors=(0.85, 0.85))),
    ("E. As D, plus 1.5 Mt (~30-day) reserve",
     dict(other_hi_factor=0.25, feed_factor=0.8, harvest_factors=(0.85, 0.85),
          extra_reserve=1.5)),
    ("F. Imports stop, 2nd harvest -35% (nitrogen cut), feed -20%",
     dict(other_hi_factor=0.25, feed_factor=0.8, harvest_factors=(1.0, 0.65))),
]


if __name__ == "__main__":
    print("| Scenario | First month stock < 0 | Lowest stock (Mt) |")
    print("|---|---|---|")
    for name, kw in SCENARIOS:
        r = run(name, **kw)
        print(f"| {name} | {r['first_month_empty']} | {r['lowest_stock_Mt']} |")
    print()
    print("Max feed level (share of today's 13.4 Mt) that keeps cereals positive for 24 months,"
          " with other H&I cut 75%:")
    for label, hf, extra in [("normal harvests", (1.0, 1.0), 0.0),
                             ("two -15% harvests", (0.85, 0.85), 0.0),
                             ("two -15% harvests + 1.5 Mt reserve", (0.85, 0.85), 1.5),
                             ("2nd harvest -35% (N cut)", (1.0, 0.65), 0.0)]:
        f = feed_needed_to_survive(2, hf, 0.25, extra)
        print(f"- {label}: feed at {f:.0%} of today")
    june_low_days = BASE["opening_stock"] * 1e6 * KCAL_PER_T / NEED_KCAL_DAY
    print(f"\nPooled 1 July stock = {june_low_days:.0f} days of total population energy need")
