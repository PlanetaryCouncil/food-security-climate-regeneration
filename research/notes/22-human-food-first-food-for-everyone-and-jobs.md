# 22 · Human food first, food for everyone, and the jobs


Date: 23 October 2026. Status: author decision, implemented in `reserve_basket.py` and the briefing (chapter 9).

## 1. The decisions

1. **Human food first.** Grain is stored to food specification and reserved for people. Only stock above a protected floor rotates into animal feed or export.
2. **Food for everyone, not only "the vulnerable".** The core covers all 69.5 million people:
   - **bread** from 4 Mt of food-grade wheat (up from 3 Mt);
   - a **3-day no-cook grain ration** for every person;
   - **vitamin tablets** for everyone for 90 days.
3. **Specialist needs are an addition, not the core.** Some people need *different* food, not more food: infants (formula), people on medical diets, care-home residents and people who cannot chew or cook (soft and ready meals). They get a 7-day top-up (~5 m people).
4. **Continuous rotation, inspection and monitoring.** About a fifth of the wheat rotates every year:
   - into flour mills (~17% of their intake);
   - into animal feed (a ~13 Mt market);
   - abroad as export or aid, to help stabilise other regions (note 20).

## 2. Checking the premises

**"You could survive on just bread."** True for weeks, and with tablets for months. Fortified UK flour already adds calcium, iron, thiamin, niacin and, from 13 December 2026, folic acid.

What bread alone lacks over months is vitamin C (scurvy appears after roughly 1–3 months), vitamin A, vitamin D, B12 and enough calcium and zinc for some groups. A tablet of vitamins A, C and D plus zinc for everyone costs about £0.27 per person per year to hold. So **bread + tablets is a genuine survival backbone**. Adding pulses, milk powder and fish turns it into a diet.

The limit is **milling**, not grain. At today's throughput the mills can supply ~160 g of flour per person per day (~550 kcal), about a quarter of energy needs. So bread is the backbone, not the whole diet. In a long crisis the rest comes from:
- domestic potatoes and oats;
- **whole-grain wheat** cooked as porridge, bulgur or flatbreads, including diverted feed wheat, which needs no roller mill.

**"Grain never goes out of date."** Nearly true with good practice. Wheat keeps 5–10 years if dry (below ~14.5% moisture), cool, aerated and protected from insects and rodents, and it is tested on intake and before release. Bad storage can ruin it in one season, which is why inspection and monitoring are part of the design, not an extra.

**Why a no-cook ration for everyone, not 7 days of ready meals for everyone?** Cost:
- 7 days of ready meals for all 69.5 m at £6 a day would be ~£2.9bn of stock and ~£400m a year to carry.
- Three days of grain-based crispbread, biscuits and oatcakes (~500 g, ~2,000 kcal a day) is ~104,000 t, ~£208m of stock and ~£28m a year.

It uses the reserve's own grain. It is a familiar humanitarian product (WFP-style high-energy biscuits), so rotated stock has an aid outlet as well as schools, the forces and food banks. It must be **pre-positioned locally** (schools, councils, depots), because moving 104,000 t in a crisis would take ~4,200 lorry loads.

## 3. What it costs now

`reserve_basket.py`: **~£718m a year ≈ £10.33 per person** (public £4.93 via taxes; compulsory stocks £5.40 via prices). Range £9.40–16.56; £18.34 under severe stress.

**Priority schedule, human food first:**

| Up to (per person) | Buys |
|---|---|
| £2.71 | Bread for everyone: 4 Mt food-grade wheat, high-protein wheat, premix, sacks |
| £3.48 | + no-cook for everyone: 3-day grain ration, tablets, bottled water |
| £6.92 | + operations: lean agency, local plans, priority fuel/power, last mile, security |
| £7.55 | + infants and special needs |
| £9.19 | + next season: seed, urea, UAN, soya meal |
| £10.33 | + imported staples and variety |

**Grain and livestock:** 4 Mt covers all three hard cases in the 36-month cereal model with a 1.0 Mt working floor:
- full feed with normal harvests (2.3 Mt needed);
- 80% feed through two −15% harvests (2.5 Mt);
- 80% feed through a nitrogen-shock harvest (3.5 Mt).

So it buys the choice **not** to order a livestock cull, while still being food for people first.

## 4. The employment aspect [E]

Planning assumptions, not a labour-market study (`jobs()` in the model).

| Work | Jobs (approx.) |
|---|---|
| Lean agency incl. innovation and domestic-resilience monitoring (note 23) | ~65 |
| Grain and food stores: intake, drying, aeration, maintenance (automated, ~1 per 20 kt) | ~280 |
| Confirmatory labs: mycotoxin and contaminant certificates on release | ~40 |
| Haulage of rotated stock (~3.4 Mt a year) | ~300 |
| Crispbread, biscuit and canning production for rotation | ~150 |
| Local food-plan officers (~45 resilience bodies) | ~135 |
| Exercises, training, delivery registers | ~100 |
| **Total permanent** | **~1,070** |
| Construction while ~£0.7bn of new stores are built over ~5 years | ~1,400 a year |

**Food Reserve Volunteers (optional):** a paid, trained civil reserve, like the Army Reserve but for food. For example, 10,000 people on a ~£1,000 yearly retainer (~£10m a year), trained in store work, distribution and community kitchens, and mustered for releases and exercises. This is part-time, practical, local work that links to the AI-transition argument (note 21) without overclaiming it.

**Where the jobs are:** mostly rural and port areas, near the stores, dryers and mills. That is useful for regions that lose office work to automation, but the numbers are modest. This is meaningful work, not a mass employment programme.

## 5. Open questions

- Can crispbread and biscuit makers produce and rotate ~52,000 t a year of no-cook ration (UK capacity and market for that format)?
- Where are local stores (schools, councils, depots) for pre-positioning, and who guards them?
- Jobs-per-tonne benchmarks from UK grain stores (Camgrain, Frontier, Openfield) to replace our assumption.
- A dietitian-checked "bread + tablets" survival specification, with variants.
