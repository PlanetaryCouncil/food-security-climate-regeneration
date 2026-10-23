"""The UK Strategic Food Reserve: cost model, version 2.

Illustrative only. Nutrient values are rounded typical composition figures
(UK McCance & Widdowson / USDA FoodData order of magnitude); prices are
rounded 2025-26 wholesale ASSUMPTIONS, not quotes; storage, rotation and
operations costs are assumptions. See research/notes/16, 17, 20 and 21.

Changes from version 1 (after adversarial review round 1, notes/20):
- every line is costed bottom-up; operations are itemised, not a residual;
- the basket is "mill-feasible": wheat is capped below demonstrated UK milling;
- rotation follows each item's shelf life instead of a flat 25% a year;
- seed loses its premium every year (it must be turned annually);
- nitrogen is held as protected urea and UAN (not ammonium nitrate), on a
  nutrient basis;
- new lines: 10 weeks of soya meal, a high-protein milling-wheat tranche, a
  no-cook tranche for vulnerable people, itemised premix/formula/amino acids;
- sensitivity cases and a break-even table with an "aversion fraction".

Run:  python3 research/model/reserve_basket.py
"""

POP = 69.5e6
FINANCE = 0.04              # cost of holding stock value, per year
MILL_WHEAT_T_YR = 4.8e6     # UK Flour Millers: wheat milled in 2025 (usage, not capacity)
EXTRACTION = 0.78           # flour out / wheat in (3.8 / 4.9)

# item: g/person/day, kcal/100g, protein g/100g, fat g/100g,
#       calcium mg/100g (as stored), calcium if fortified on milling,
#       price GBP/t, shelf life yrs (good storage), storage GBP/t/yr,
#       share of value lost when rotated out, rotation outlet
BASKET = {
    "Wheat, food grade (milled and fortified on release)":
        (180, 340, 12.0, 2.0, 20, 140, 210, 6.0, 15, 0.05, "millers / feed"),
    "Oats (stabilised)":
        (30, 375, 11.0, 8.0, 50, 50, 200, 1.5, 15, 0.05, "oat millers / feed"),
    "Rice (white, milled)":
        (130, 360, 7.0, 1.0, 10, 10, 500, 5.0, 20, 0.05, "importers' normal trade"),
    "Pulses (peas, beans, lentils)":
        (90, 340, 24.0, 2.0, 90, 90, 350, 3.0, 20, 0.05, "canners / feed"),
    "Rapeseed oil (sealed tanks, nitrogen blanket)":
        (55, 900, 0.0, 100.0, 0, 0, 1000, 1.5, 25, 0.05, "food industry / biodiesel"),
    "Sugar":
        (25, 400, 0.0, 0.0, 0, 0, 500, 5.0, 15, 0.05, "food industry"),
    "Skimmed milk powder":
        (25, 360, 36.0, 1.0, 1250, 1250, 2500, 2.5, 60, 0.05, "food industry / schools / calf feed"),
    "Canned mackerel or herring":
        (25, 230, 20.0, 15.0, 250, 250, 5000, 4.0, 80, 0.05, "public catering / food banks"),
}
# vitamin C 40 mg + vitamin D 10 ug tablets, per person-day (wholesale)
TABLETS_GBP_PER_PERSON_DAY = 0.01
NEEDS = {"kcal_planning": 2250, "kcal_defra": 2119, "protein_g": 46, "calcium_mg": 700}


def daily_totals(fortified=True):
    t = dict(g=0.0, kcal=0.0, protein_g=0.0, fat_g=0.0, calcium_mg=0.0, gbp=0.0)
    for g, kcal, p, f, ca, ca_fort, price, *_ in BASKET.values():
        t["g"] += g
        t["kcal"] += g * kcal / 100
        t["protein_g"] += g * p / 100
        t["fat_g"] += g * f / 100
        t["calcium_mg"] += g * (ca_fort if fortified else ca) / 100
        t["gbp"] += g / 1e6 * price
    t["gbp"] += TABLETS_GBP_PER_PERSON_DAY
    return t


def carry(tonnes, price, store, rotation, loss, finance=FINANCE,
          store_mult=1.0, loss_mult=1.0, price_mult=1.0):
    """Annual carrying cost: storage + financing + value lost when rotating."""
    v = tonnes * price * price_mult
    return tonnes * store * store_mult + v * finance + v * rotation * loss * loss_mult


def basket_line(days, items=None, people=POP, **s):
    tonnes = value = annual = 0.0
    for name, (g, *_rest) in BASKET.items():
        if items and name not in items:
            continue
        _, _, _, _, _, _, price, life, store, loss, _ = BASKET[name]
        t = g / 1e6 * people * days
        tonnes += t
        value += t * price * s.get("price_mult", 1.0)
        annual += carry(t, price, store, min(1.0, 1 / life), loss, **s)
    return tonnes, value, annual


def package(finance=FINANCE, store_mult=1.0, loss_mult=1.0, price_mult=1.0,
            grain_mt=3.0):
    """Bottom-up Strategic Food Reserve package. Returns rows of
    (code, label, tonnes, stock value GBP, annual cost GBP)."""
    s = dict(finance=finance, store_mult=store_mult, loss_mult=loss_mult,
             price_mult=price_mult)
    rows = []

    t, v, a = basket_line(90, **s)
    tab = TABLETS_GBP_PER_PERSON_DAY * POP * 90 * price_mult
    a += tab * (finance + 0.5 * 0.10 * loss_mult)       # tablets: 2-yr life, 10% loss
    rows.append(("A", "90-day survival ration for everyone (mill-feasible basket + vitamin tablets)",
                 t, v + tab, a))

    # imported or import-dependent items only; pulses are UK-grown (field beans, peas)
    ext = ("Rice (white, milled)", "Rapeseed oil (sealed tanks, nitrogen blanket)")
    t, v, a = basket_line(92, items=ext, **s)
    rows.append(("B", "Rice and oil extended to 6 months (import-dependent items)", t, v, a))

    # C1 cereal seed: half a season, turned every year, premium (300 vs 200) lost on turn
    seed_t = 0.3e6
    a = seed_t * (15 * store_mult + 300 * price_mult * finance + 100 * price_mult * loss_mult)
    rows.append(("C1", "Cereal seed, ~half a season (0.3 Mt), turned yearly", seed_t,
                 seed_t * 300 * price_mult, a))

    # C2 nitrogen ~350 kt N (about a third of a season) as protected urea + UAN, no ammonium nitrate
    urea_t, uan_t = 0.5e6, 0.4e6          # 46% N and ~30% N -> 230 + 120 kt N
    a = carry(urea_t, 380, 20, 1.0, 0.03, **s) + carry(uan_t, 300, 10, 1.0, 0.03, **s)
    rows.append(("C2", "Nitrogen ~350 kt N (~1/3 season) as protected urea + UAN, rotated through merchants",
                 urea_t + uan_t, (urea_t * 380 + uan_t * 300) * price_mult, a))

    # P protein feed: 10 weeks of imported soya meal, compulsory stock at importers/compounders
    soya_t = 2.39e6 * 10 / 52
    a = carry(soya_t, 450, 12, 3.0, 0.01, **s)
    rows.append(("P", "Protein feed: 10 weeks of soya meal (compulsory stock, Swiss model)",
                 soya_t, soya_t * 450 * price_mult, a))

    # Q high-protein milling wheat so UK feed-type wheat can still make bread
    q_t = 0.15e6
    a = carry(q_t, 260, 15, 0.25, 0.05, **s)
    rows.append(("Q", "High-protein milling wheat tranche (gluten for the loaf)", q_t,
                 q_t * 260 * price_mult, a))

    # R no-cook tranche: 7 days of ready-to-eat food for 10 m vulnerable people
    r_days = 10e6 * 7
    r_t = r_days * 1.0 / 1000           # ~1 kg per person-day
    r_v = r_days * 2.50 * price_mult
    a = r_t * 40 * store_mult + r_v * finance + r_v * 0.4 * 0.20 * loss_mult
    rows.append(("R", "No-cook tranche: 7 days ready-to-eat for 10 m vulnerable people",
                 r_t, r_v, a))

    # D small critical items: stock value (GBP m), shelf life (yrs)
    small = {"infant formula and medical foods (manufacturer-held)": (60, 1.5),
             "flour premix (Ca, Fe, niacin, thiamin, folic acid) + potassium iodate": (8, 3.0),
             "feed amino acids (methionine, lysine, threonine)": (10, 2.0),
             "dried yeast and food-grade CO2 alternatives": (6, 2.0)}
    d_v = sum(v for v, _ in small.values()) * 1e6 * price_mult
    d_a = sum(v * 1e6 * price_mult * (finance + min(1, 1 / life) * 0.10 * loss_mult + 0.03 * store_mult)
              for v, life in small.values())
    rows.append(("D", "Small critical items: formula, premix, iodine, amino acids, yeast (allowances)",
                 None, d_v, d_a))

    # E food-grade grain stock in new stores (capex GBP 200/t, 25-yr annuity at 4%)
    e_t = grain_mt * 1e6
    annuity = 200 * 0.06401
    a = carry(e_t, 210, 15, 0.2, 0.05, **s) + e_t * annuity * store_mult
    rows.append(("E", f"Food-grade grain, {grain_mt:.1f} Mt, in new stores (human / feed / aid; human first)",
                 e_t, e_t * 210 * price_mult, a))

    # F operations, itemised (GBP m/yr); assumptions, not quotes
    ops = {"reserve agency (~400 staff, audit, testing, IT)": 40,
           "local food plans in ~45 resilience bodies, four nations": 36,
           "priority fuel and backup power at mills, dryers, cold stores, depots": 40,
           "offline / degraded-mode operations and national exercises": 10,
           "insurance, security, fumigation, extra testing": 15,
           "last-mile delivery and drinking-water contracts": 15}
    f_a = sum(ops.values()) * 1e6 * store_mult
    rows.append(("F", "Operations (itemised: agency, local plans, fuel/power, exercises, security, last mile)",
                 None, 0.0, f_a))
    return rows, ops, small


def totals(rows):
    t = sum(r[2] or 0 for r in rows)
    v = sum(r[3] for r in rows)
    a = sum(r[4] for r in rows)
    return t, v, a


def print_package():
    rows, ops, small = package()
    print("| Line | Component | Stock (Mt) | Stock value (£bn) | Annual cost (£m) | £/person/yr |")
    print("|---|---|---|---|---|---|")
    for code, label, t, v, a in rows:
        ts = f"{t/1e6:.2f}" if t else "-"
        print(f"| {code} | {label} | {ts} | {v/1e9:.2f} | {a/1e6:.0f} | {a/POP:.2f} |")
    t, v, a = totals(rows)
    print(f"| | **Total** | **{t/1e6:.1f}** | **{v/1e9:.2f}** | **{a/1e6:.0f}** | **{a/POP:.2f}** |")
    print("\nOperations itemised (£m/yr):", ops)
    print("Small critical items, stock value (£m):", {k: v for k, (v, _) in small.items()})
    capex = 3.0e6 * 200
    print(f"\nOne-off: new grain stores £{capex/1e9:.2f}bn (£{capex/POP:.0f}/person, inside the annual cost "
          f"as an annuity); stock bought once £{v/1e9:.2f}bn (£{v/POP:.0f}/person, an asset, cash spent up front).")


def sensitivity():
    cases = [
        ("Low: gilt-guaranteed finance 3.5%, storage -10%", dict(finance=0.035, store_mult=0.9)),
        ("Central", dict()),
        ("Prices +30%", dict(price_mult=1.3)),
        ("Stress: finance 6%, storage +50%, rotation losses x2", dict(finance=0.06, store_mult=1.5, loss_mult=2.0)),
        ("Severe stress: as above + prices +30%",
         dict(finance=0.06, store_mult=1.5, loss_mult=2.0, price_mult=1.3)),
        ("Central with 5 Mt grain instead of 3", dict(grain_mt=5.0)),
    ]
    print("\n| Case | Annual (£m) | £/person/yr |")
    print("|---|---|---|")
    for label, kw in cases:
        _, _, a = totals(package(**kw)[0])
        print(f"| {label} | {a/1e6:.0f} | {a/POP:.2f} |")


def checks():
    d, du = daily_totals(True), daily_totals(False)
    print("\nDaily survival ration per person:")
    print(f"  {d['g']:.0f} g of listed commodities | {d['kcal']:.0f} kcal | protein {d['protein_g']:.0f} g |"
          f" fat {d['fat_g']:.0f} g ({d['fat_g']*9/d['kcal']:.0%} of energy) | £{d['gbp']:.2f}/day wholesale")
    print(f"  calcium {d['calcium_mg']:.0f} mg if flour is fortified, {du['calcium_mg']:.0f} mg if not (RNI 700)")
    wheat_g = BASKET["Wheat, food grade (milled and fortified on release)"][0]
    ceiling = MILL_WHEAT_T_YR / 365 / POP * 1e6
    print(f"\nMilling check: ration wheat {wheat_g} g/day = {wheat_g*POP/1e6:,.0f} t/day; demonstrated mill use "
          f"{MILL_WHEAT_T_YR/365:,.0f} t/day = {ceiling:.0f} g/person/day -> {wheat_g/ceiling:.0%} of demonstrated use")
    for mt in (3.0, 5.0):
        print(f"  {mt:.0f} Mt grain = {mt*1e6/(MILL_WHEAT_T_YR/365):.0f} days of mill intake, or "
              f"{mt*1e6*3.3e6/(POP*2250):.0f} days of national calories (raw grain, not edible as is)")
    print(f"  Daily movement of the whole ration: {d['g']*POP/1e6:,.0f} t/day = "
          f"{d['g']*POP/1e6/25:,.0f} lorry-loads of 25 t")


def break_even():
    _, _, a = totals(package()[0])
    gdp = 2.9e12
    print("\nBreak-even: how often must a shock occur for the reserve to pay for itself?")
    print("| Shock size | Share of loss the reserve prevents | Break-even: once every … years |")
    print("|---|---|---|")
    for size in (0.01, 0.02):
        for frac in (1.0, 0.5, 0.25, 0.10):
            years = size * gdp * frac / a
            print(f"| {size:.0%} of GDP | {frac:.0%} | {years:.0f} |")


if __name__ == "__main__":
    print_package()
    sensitivity()
    checks()
    break_even()
