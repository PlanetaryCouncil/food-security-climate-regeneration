"""Rotating national food reserve: a nutritionally complete storable ration.

Illustrative only. Nutrient values are rounded typical composition figures
(UK McCance & Widdowson / USDA FoodData order of magnitude); prices are
rounded 2025-26 wholesale assumptions; storage and rotation costs are
assumptions. See research/notes/16-storable-full-diet-reserve.md.

Run:  python3 research/model/reserve_basket.py
"""

POP = 69.5e6

# item: grams/person/day, kcal/100g, protein g/100g, fat g/100g,
#       calcium mg/100g, B12 ug/100g, price GBP/t, shelf life (years, good storage),
#       storage GBP/t/yr, rotation outlet
BASKET = {
    "Wheat (milled to fortified flour on release)": (350, 340, 12.0, 2.0, 140, 0.0, 200, "5-10 (grain)", 15, "millers / feed"),
    "Oats":                         (60, 375, 11.0, 8.0, 50, 0.0, 200, "1-2 (stabilised)", 15, "oat millers / feed"),
    "Rice (white)":                 (50, 360, 7.0, 1.0, 10, 0.0, 500, "5+", 20, "retail / feed"),
    "Pulses (peas, beans, lentils)": (80, 340, 24.0, 2.0, 90, 0.0, 350, "2-4 (hard-to-cook after)", 20, "canners / feed"),
    "Rapeseed oil":                 (35, 900, 0.0, 100.0, 0, 0.0, 1000, "1-2 (sealed, cool, N2)", 25, "food industry / biodiesel"),
    "Sugar":                        (25, 400, 0.0, 0.0, 0, 0.0, 500, "indefinite if dry", 15, "food industry"),
    "Skimmed milk powder":          (30, 360, 36.0, 1.0, 1250, 4.0, 2500, "2-3", 60, "food industry / schools / calf feed"),
    "Canned oily fish (mackerel, sardine)": (30, 200, 22.0, 12.0, 300, 9.0, 5000, "3-5", 80, "public catering / food banks"),
}

# micronutrient tablets: vitamin C 40 mg, vitamin D 10 ug, plus iodised salt
SUPPLEMENTS_GBP_PER_PERSON_DAY = 0.01

NEEDS = {"kcal": 2250, "protein_g": 46, "calcium_mg": 700, "b12_ug": 1.5}


def daily_totals():
    t = {"g": 0, "kcal": 0, "protein_g": 0, "fat_g": 0, "calcium_mg": 0, "b12_ug": 0, "gbp": 0}
    for g, kcal, p, f, ca, b12, price, *_ in BASKET.values():
        t["g"] += g
        t["kcal"] += g * kcal / 100
        t["protein_g"] += g * p / 100
        t["fat_g"] += g * f / 100
        t["calcium_mg"] += g * ca / 100
        t["b12_ug"] += g * b12 / 100
        t["gbp"] += g / 1e6 * price
    t["gbp"] += SUPPLEMENTS_GBP_PER_PERSON_DAY
    return t


def reserve_costs(days, share_of_population=1.0, finance=0.04, rotation_discount=0.05):
    people = POP * share_of_population
    tonnes = value = storage = rot = 0.0
    for g, *_, price, _life, store, _out in BASKET.values():
        t = g / 1e6 * people * days
        tonnes += t
        value += t * price
        storage += t * store
    # assume ~1/4 of stock rotates each year, sold at a 5% discount
    rot = value * 0.25 * rotation_discount
    supp = SUPPLEMENTS_GBP_PER_PERSON_DAY * people * days
    value += supp
    annual = storage + value * finance + rot
    return tonnes, value, annual


if __name__ == "__main__":
    d = daily_totals()
    print("Daily ration per person:")
    print(f"  weight {d['g']:.0f} g dry | {d['kcal']:.0f} kcal | protein {d['protein_g']:.0f} g |"
          f" fat {d['fat_g']:.0f} g ({d['fat_g']*9/d['kcal']:.0%} of energy) |"
          f" calcium {d['calcium_mg']:.0f} mg | B12 {d['b12_ug']:.1f} ug | cost £{d['gbp']:.2f}")
    print("  vs needs:", NEEDS, "+ vitamin C and D from tablets, iodine from iodised salt\n")
    print("| Reserve | Tonnes (Mt) | Stock value (£bn) | Annual carrying cost (£m) | £/person/yr |")
    print("|---|---|---|---|---|")
    for label, days, share in [
        ("Full ration, whole population, 30 days", 30, 1.0),
        ("Full ration, whole population, 90 days", 90, 1.0),
        ("Full ration, whole population, 6 months", 182, 1.0),
        ("Full ration, whole population, 12 months", 365, 1.0),
    ]:
        t, v, a = reserve_costs(days, share)
        print(f"| {label} | {t/1e6:.1f} | {v/1e9:.2f} | {a/1e6:.0f} | {a/POP:.2f} |")


# ---------------------------------------------------------------------------
# £10 multi-purpose package (see research/notes/20-ten-pound-multipurpose-reserve.md)
# ---------------------------------------------------------------------------

def per_tonne_carry(price, store, finance=0.04, rotation_share=0.25, discount=0.05):
    """Annual carrying cost per tonne: storage + financing + rotation discount."""
    return store + price * finance + price * rotation_share * discount


def ten_pound_package(budget_per_person=10.0):
    budget = budget_per_person * POP
    rows = []
    # A. 90-day complete ration for everyone
    tA, vA, aA = reserve_costs(90)
    rows.append(("A. 90-day complete ration (whole population)", tA, vA, aA))
    # B. extra 92 days of the import-dependent items (oil, rice, pulses) -> 6 months total
    extra_days = 92
    tB = vB = aB = 0.0
    for key in ("Rapeseed oil", "Rice (white)", "Pulses (peas, beans, lentils)"):
        g, _, _, _, _, _, price, _, store, _ = BASKET[key]
        t = g / 1e6 * POP * extra_days
        tB += t; vB += t * price; aB += t * per_tonne_carry(price, store)
    rows.append(("B. Oils, rice and pulses topped up to 6 months", tB, vB, aB))
    # C. farm inputs: seed grain 0.3 Mt; nitrogen fertiliser ~1/3 of a season (~1 Mt product)
    tC_seed, tC_n = 0.3e6, 1.0e6
    vC = tC_seed * 300 + tC_n * 350
    aC = tC_seed * per_tonne_carry(300, 15) + tC_n * per_tonne_carry(350, 20)
    rows.append(("C. Seed (0.3 Mt) + nitrogen fertiliser (~1/3 season, ~1 Mt product)", tC_seed + tC_n, vC, aC))
    # D. micronutrients, infant formula, fortificants (allowance)
    aD = 0.30 * POP
    rows.append(("D. Vitamins, fortificants, infant formula (allowance)", None, aD * 3, aD))
    # E. multi-purpose grain: capped at a realistic size (~a quarter of one harvest),
    #    needing new storage (capex ~£200/t capacity, 25-year annuity at 4%)
    tE = 5.0e6
    capex_annuity = 200 * 0.064
    carry_grain = per_tonne_carry(200, 15) + capex_annuity
    rows.append(("E. Multi-purpose grain, 5 Mt (human backup / feed buffer / overseas aid), incl. new stores",
                 tE, tE * 200, tE * carry_grain))
    # F. the rest of the budget runs the system: agency, audit, LRF food plans, exercises,
    #    backup power at key distribution/cold-store nodes, regional hubs
    used = sum(r[3] for r in rows)
    rows.append(("F. Operations: agency, audit, local food plans, exercises, backup power at key nodes",
                 None, 0.0, max(0.0, budget - used)))
    return rows, budget


def print_ten_pound_package():
    rows, budget = ten_pound_package()
    print("\n| Component | Tonnes (Mt) | Stock value (£bn) | Annual cost (£m) | £/person/yr |")
    print("|---|---|---|---|---|")
    tot_v = tot_a = 0.0
    for label, t, v, a in rows:
        tot_v += v; tot_a += a
        ts = f"{t/1e6:.1f}" if t else "-"
        print(f"| {label} | {ts} | {v/1e9:.2f} | {a/1e6:.0f} | {a/POP:.2f} |")
    print(f"| **Total** | | **{tot_v/1e9:.2f}** | **{tot_a/1e6:.0f}** | **{tot_a/POP:.2f}** |")
    tE = rows[-2][1]
    food_grain_months = tE / 6.0e6 * 12
    days_energy = tE * KCAL_ENERGY_PER_T / (POP * 2250)
    print(f"\nMulti-purpose grain {tE/1e6:.1f} Mt = ~{food_grain_months:.0f} months of UK food-grain use,"
          f" or ~{days_energy:.0f} days of total national calories, or ~{tE/13.4e6*12:.1f} months of UK livestock cereal feed.")


KCAL_ENERGY_PER_T = 3.3e6

if __name__ == "__main__":
    print_ten_pound_package()
