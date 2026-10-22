# 09 · Diet shift, feed–food mass balance and waste

Tags: `research:calories-protein`, `research:diets-livestock-externalities`, `research:scale-up-emergency`
Gap addressed: "Diet-shift mass balance and waste": no briefing runs a monthly feed/food/waste balance, and "less but better meat" stays qualitative. This note adds a **first-cut monthly cereal model** (`research/model/cereal_balance.py`) and pulls together the dossier's Part 3 arithmetic.
Status: 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate or model, [?] unresolved.

---

## 1. Headline finding

**Grain is not the binding constraint in an import shock; protein feed, fats and next year's fertiliser are.** In the model, if imports stop on 1 July, the UK's own cereals cover food milling *and* today's full livestock feed for two years, **provided bioethanol and distilling grain use is cut and exports stop**. Without that policy response, cereal stocks run out within 12 months. Two poor harvests in a row (−15% each) need feed cut by about a fifth; a ~30-day reserve (1.5 Mt) reduces that cut. The problem is that pigs and poultry cannot run on grain alone: they need the ~2.3–2.5 Mt of imported soya meal. So the *monogastric herd contracts because of protein, not energy*. That is the "less meat" mechanism, and it would happen whether or not policy chooses it.

## 2. Model: monthly pooled cereal stock (wheat + barley + oats) [E]

Assumptions (rounded, editable in the script): opening stock at 1 July **2.95 Mt** (AHDB wheat 1.514 + barley ~1.3 + oats ~0.15); harvest **19.5 Mt** (2025), arriving Aug 60% / Sep 40%; food milling 6.0 Mt/yr; other human and industrial uses (malting, distilling, bioethanol, starch) 3.2 Mt/yr; feed 13.4 Mt/yr; seed 0.6 Mt/yr; exports 1.0 Mt/yr; imports 4.5 Mt/yr including maize (calibrated so the baseline roughly closes).

| Scenario | First month stock < 0 | Lowest stock (Mt) |
|---|---|---|
| A. Normal trade, normal harvests | never | 1.16 |
| B. Imports stop 1 Jul, no policy response | **Y1-Jun** (month 12) | −4.45 |
| C. Imports stop; bioethanol/distilling cut 75%; feed −20% | never | 1.49 |
| D. As C, two poor harvests (−15% each) | Y2-Jul (month 25) | −0.14 |
| E. As D, plus 1.5 Mt (~30-day) reserve | never | 1.36 |
| F. Imports stop; 2nd harvest −35% (nitrogen cut); feed −20% | **Y2-Jun** (month 24) | −1.12 |

Highest feed level (as a share of today's 13.4 Mt) that keeps cereals positive for 24 months, with other industrial use cut 75%:
- normal harvests: **100%**
- two −15% harvests: **79%**
- two −15% harvests + 1.5 Mt reserve: **85%**
- second harvest −35% (nitrogen shortage): **76%**

Pooled 1 July stock ≈ **62 days** of total population energy need (energy only; consistent with note 01).

**What the model shows:**
1. **Policy response matters more than the reserve in year 1.** Stopping grain-to-ethanol, distilling and exports is worth several Mt; a 30-day reserve is 1.5 Mt.
2. **The reserve earns its keep in multi-year shocks** (scenarios D and E) and at the *seasonal low* before the first harvest (July–August). That is the window where a shock hits hardest.
3. **A nitrogen shock is worse than a weather shock** (F vs D), because it compounds: imported N fails exactly when imported food fails.

**What it does not show:** protein, fats, micronutrients, grain quality (feed wheat vs milling wheat), milling capacity (~5–5.5 Mt/yr of wheat milled today), regional logistics, or household access. It is a pooled tonnage model and should be read as a *bounding* exercise.

## 3. The protein and nutrient side (from dossier Part 3, not yet re-verified)

| Item | Figure | Status |
|---|---|---|
| Population protein need | ~1.17–1.2 Mt/yr (46 g/person/day) | [E] |
| Imported soya meal | 2.3 Mt (2020, feed) / 2.51 Mt (2022, all uses) ≈ **1.1 Mt protein**, about the population's whole protein need | [S] LSE/AIC; dossier |
| Feed cereals if eaten directly | ~38 trillion kcal gross, ~1,500 kcal/person/day; ~1.3 Mt crude protein; lysine is limiting | [E] dossier |
| Lost if pigs, poultry and eggs went | ~6 trillion kcal and ~0.45–0.5 Mt protein | [E] dossier |
| Net energy gain from diverting feed | ~25–30 trillion kcal/yr | [E] dossier |
| Milk | ~0.54 Mt protein/yr; milk and upland suckler beef are the only livestock systems that return more human-edible protein than they eat (Wilkinson 2011) | [P/E] |
| Fats | UK farming meets ~53% of current fat supply | [S] SFT |
| WWII benchmark | 1944 household intake ~2,390–2,400 kcal and 73–74 g protein | [S] |

**Nutrients that get harder in a lower-meat crisis diet:** vitamin B12 (animal foods or fortification only), calcium (dairy, fortified flour), iodine (milk is the main UK source), vitamin D, and bioavailable iron and zinc. Keeping **dairy** and **flour fortification** running (note 01: the calcium carbonate supply) is the cheapest nutrient insurance. Infant formula and medical diets need their own named stock.

## 4. Waste: the fastest lever

| Item | Figure | Source |
|---|---|---|
| Total UK food waste | 10.7 Mt (2021; total including households, hospitality, retail and manufacture), carrying ~18 MtCO₂e | [P] UKFSR via Grok briefing |
| Households | 6.4 Mt (2021) total; **4.4–4.5 Mt edible** (WRAP; ~£14bn/yr) | [P] WRAP |
| Trend | Food waste per person −7% over three years (WRAP C2025 milestone, 2018 data) | [P] |

[E] At 1,000–1,500 kcal/kg, 4.4 Mt of edible household waste ≈ **28–42 days of national energy need per year**. Halving it ≈ 2–3 weeks a year, without new land, fertiliser or ships. In a crisis, waste falls naturally (higher prices, rationing): WWII households wasted little. This is "the reserve already in our bins".

## 5. "Less but better" made concrete

A quantitative version of the briefings' qualitative position:
1. **Monogastrics (pigs, poultry, eggs)** are sized by the *domestic protein supply*: home-grown beans, peas, rapeseed meal and distillers' grains. Model this as a pulse-area target: replacing 1.1 Mt of soya protein needs ~4 Mt of field beans at ~27% protein, roughly 1 Mha at ~4 t/ha [E]. That is about **6× today's pulse area (0.68 Mt production)** and bumps into the one-in-five-to-six-year rotation limit (GPT notes). A realistic target is perhaps a third of soya replaced within a decade.
2. **Ruminants on grass** stay; their constraint is methane and land-sparing for trees on grade 4–5 land, not food security.
3. **Diets already moving:** meat −17% per person 2008–2019, driven by smaller portions (note 05). A crisis plan works *with* that trend.

## 6. Still missing (next modelling steps)
- Add a protein ledger (soya, rapeseed meal, beans, peas) and herd response to the model.
- Add milling and dehulling capacity as a monthly ceiling.
- Use AHDB's grade split (milling vs feed wheat) and the barley and oat closing stocks from the September 2026 final balance.
- Add oils (rapeseed 49% self-sufficiency) and a micronutrient check.

## Sources
- Model: `research/model/cereal_balance.py` (this repo)
- AHDB end-of-season balance, Sep 2026: https://ahdb.org.uk/end-of-season-uk-cereal-supply-and-demand-september-2026
- WRAP household waste: https://wrap.ngo/resources/report/courtauld-2025-baseline-and-restated-household-food-waste-figures ; https://www.circularonline.co.uk/news/food-waste-falls-by-7-per-person-in-three-years/
- Dossier Part 3 (calories, protein and feed) and its cited sources: Defra UKFSR 2024; FAO food balance sheets; SFT; Wilkinson 2011
