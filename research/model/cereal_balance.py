"""First-cut monthly UK cereal balance under import-stop scenarios.

Illustrative only. Every input is a rounded assumption listed in BASE and
documented in research/notes/09-diet-shift-mass-balance.md. The model tracks one
pooled stock of wheat, barley and oats (Mt), starting 1 July (pre-harvest low).
It answers one question: under a given shock, in which month does the pooled
cereal stock run out, and how much feed must be cut to keep food milling whole?
It does not model protein, fats, micronutrients, quality, milling capacity or
regional logistics. It pools grades: a tonne of feed barley here is not a tonne
of bread wheat, so it cannot show that the same stock both feeds people and
avoids a livestock cull. Lost co-products (distillers' grains, CO2) are not
subtracted when industrial use is cut. Onset is always 1 July (the seasonal low); other onset
months are not modelled. Negative stock means unmet demand, not stored grain.
Imports are calibrated (an imposed closure, not a measured balance) and the
pool includes imported maize.

Run:  python3 research/model/cereal_balance.py
"""

MONTHS = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
          "Jan", "Feb", "Mar", "Apr", "May", "Jun"]

BASE = {
    "opening_stock": 3.006,  # Mt at 1 Jul 2026: wheat 1.514 + barley 1.337 + oats 0.155 (AHDB, Sep 2026)
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
        extra_reserve=0.0, floor=0.0):
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
            log.append((f"Y{y+1}-{m}", stock))      # full precision; round only for display
    # floor: working stock in mills, merchants and transit that cannot be drawn
    first = next(((i + 1, t) for i, (t, s) in enumerate(log) if s < floor), None)
    low = min(s for _, s in log)
    label = f"{first[1]} (month {first[0]})" if first else "never"
    return {"scenario": name, "first_month_empty": label,
            "lowest_stock_Mt": low, "log": log}


def feed_needed_to_survive(years, harvest_factors, other_hi_factor, extra=0.0, floor=0.0):
    """Largest feed factor (0-1) that keeps the stock >= floor over the horizon.
    Returns None if even zero feed breaches the floor (infeasible case)."""
    def ok(f):
        r = run("probe", years, harvest_factors, other_hi_factor=other_hi_factor,
                feed_factor=f, extra_reserve=extra, floor=floor)
        return r["lowest_stock_Mt"] >= floor
    if not ok(0.0):
        return None
    if ok(1.0):
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(30):
        mid = (lo + hi) / 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


SCENARIOS = [
    ("A. Normal trade, normal harvests", dict(imports_on=True, exports_on=True)),
    ("B. Imports and exports stop 1 Jul, no change in use", dict()),
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
        print(f"| {name} | {r['first_month_empty']} | {r['lowest_stock_Mt']:.2f} |")
    print()
    print("Max feed level (share of today's 13.4 Mt) that keeps cereals positive for 24 months,"
          " with other H&I cut 75%:")
    for label, hf, extra in [("normal harvests", (1.0, 1.0), 0.0),
                             ("two -15% harvests", (0.85, 0.85), 0.0),
                             ("two -15% harvests + 1.5 Mt reserve", (0.85, 0.85), 1.5),
                             ("2nd harvest -35% (N cut)", (1.0, 0.65), 0.0)]:
        f = feed_needed_to_survive(2, hf, 0.25, extra)
        print(f"- {label}: " + ("infeasible even with zero feed" if f is None else f"feed at {f:.0%} of today"))
    june_low_days = BASE["opening_stock"] * 1e6 * KCAL_PER_T / NEED_KCAL_DAY
    print(f"\nPooled 1 July stock = {june_low_days:.0f} days of total population energy need")


def reserve_needed(harvest_factors, feed_factor, other_hi_factor=0.25, years=2, floor=0.0):
    """Smallest extra reserve (Mt, added 1 Jul) that keeps the pooled stock >= floor.
    The upper bound is checked to bracket a solution; it doubles up to 200 Mt."""
    def ok(x):
        r = run("probe", years, harvest_factors, other_hi_factor=other_hi_factor,
                feed_factor=feed_factor, extra_reserve=x)
        return r["lowest_stock_Mt"] >= floor
    if ok(0.0):
        return 0.0
    lo, hi = 0.0, 30.0
    while not ok(hi):
        if hi >= 200:
            raise ValueError("no reserve up to 200 Mt meets the floor")
        lo, hi = hi, min(hi * 2, 200.0)
    for _ in range(40):
        mid = (lo + hi) / 2
        r = run("probe", years, harvest_factors, other_hi_factor=other_hi_factor,
                feed_factor=feed_factor, extra_reserve=mid)
        if r["lowest_stock_Mt"] >= floor:
            hi = mid
        else:
            lo = mid
    return hi


def reserve_table():
    days_per_mt = 1e6 * KCAL_PER_T / NEED_KCAL_DAY
    cases = [
        ("Normal harvests, feed kept at 100%", (1.0, 1.0), 1.0),
        ("Two -15% harvests, feed kept at 100%", (0.85, 0.85), 1.0),
        ("Two -15% harvests, feed cut to 80%", (0.85, 0.85), 0.8),
        ("2nd harvest -35% (N cut), feed 100%", (1.0, 0.65), 1.0),
        ("2nd harvest -35% (N cut), feed 80%", (1.0, 0.65), 0.8),
        ("Two -30% harvests (N and weather), feed 80%", (0.7, 0.7), 0.8),
        ("Two -30% harvests, feed cut to 50%", (0.7, 0.7), 0.5),
    ]
    print("\n| Case (imports stop 1 Jul; ethanol/distilling cut 75%; no exports) |"
          " Extra reserve needed (Mt) | ≈ days of national energy |")
    print("|---|---|---|")
    for label, hf, ff in cases:
        mt = reserve_needed(hf, ff)
        mt = 0.0 if mt < 0.05 else mt
        print(f"| {label} | {mt:.1f} | {mt * days_per_mt:.0f} |")


if __name__ == "__main__":
    reserve_table()


def robust_table(years=3, floor=1.0):
    """36 months, a 1.0 Mt working-stock floor, and the minimum stock reported."""
    print(f"\n{years*12}-month runs, imports stopped 1 Jul, ethanol/distilling cut 75%, exports stopped, "
          f"working-stock floor {floor} Mt")
    print("| Case | Feed level | Lowest stock (Mt) | First month below floor | Extra reserve needed (Mt) |"
          " Lowest stock with 4 Mt extra | First month below floor with 4 Mt |")
    print("|---|---|---|---|---|---|---|")
    cases = [("Normal harvests", (1.0,) * years, 1.0),
             ("Normal harvests", (1.0,) * years, 0.9),
             ("Two -15% harvests, then normal", (0.85, 0.85) + (1.0,) * (years - 2), 0.8),
             ("Two -15% harvests, then normal", (0.85, 0.85) + (1.0,) * (years - 2), 0.7),
             ("2nd harvest -35% (nitrogen), then normal", (1.0, 0.65) + (1.0,) * (years - 2), 0.8),
             ("Three -15% harvests", (0.85,) * years, 0.7),
             # persistent-shock stress test (round-3 review): no recovery in year 3
             ("Three -30% harvests (persistent)", (0.7,) * years, 0.8),
             ("Three -30% harvests (persistent)", (0.7,) * years, 0.5)]
    for label, hf, ff in cases:
        r = run(label, years, hf, other_hi_factor=0.25, feed_factor=ff, floor=floor)
        need = reserve_needed(hf, ff, years=years, floor=floor)
        need_s = "0.0" if need == 0 else ("<0.1" if need < 0.05 else f"{need:.1f}")
        r4 = run(label, years, hf, other_hi_factor=0.25, feed_factor=ff, extra_reserve=4.0, floor=floor)
        print(f"| {label} | {ff:.0%} | {r['lowest_stock_Mt']:.2f} | {r['first_month_empty']} | {need_s} |"
              f" {r4['lowest_stock_Mt']:.2f} | {r4['first_month_empty']} |")


if __name__ == "__main__":
    robust_table()
