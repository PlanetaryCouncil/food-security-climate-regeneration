# Research notes: UK food security, climate and regeneration

Research base for a ~14-page briefing (one page per chapter): **Can Britain Feed Itself? Store and grow.** Date: 23 October 2026.

**Labels:** **[P]** primary source · **[S]** secondary · **[E]** our own calculation or model · **[I]** interpretation or position · **[?]** not yet verified.
**Final figures:** where a note and the briefing differ, the briefing (`draft/briefing_full_context.md`) is the final version.

---

## The briefing, chapter by chapter (and which notes feed each page)

| # | Chapter | Notes |
|---|---|---|
| 1A | **What we get: the value of safety and stability** (benefits first) | 27 |
| 1 | **Can Britain feed itself?** Resilient on paper, fragile in practice | 01, 09 |
| 2 | **Nature's gift:** world-class yields per hectare, land-poor per person, soils that can recover | 17 |
| 3 | **Climate is changing the odds:** compound extremes, Europe failing together, new pests | 07 |
| 4 | **Hidden dependencies:** nitrogen, phosphorus, potash, diesel, AdBlue, CO₂, cyber, cold chain | 01, 03, 06 |
| 5 | **Protein, livestock and the sea:** soya, feed to food, fewer and better animals, fish | 02, 09, 15 |
| 6 | **Geopolitics and prices:** Hormuz, Black Sea, export bans, stabilising neighbours | 05, 18, 20 |
| 7 | **Food and stability:** "nine meals", unrest evidence, fairness, local plans | 10, 11 |
| 8 | **How other countries prepare:** Finland, Switzerland, Norway, Sweden, Germany, Japan | 13, 14 |
| 9 | **Pillar 1, STORE: the UK Strategic Food Reserve,** about £10 per person per year; human food first, food for everyone | 16, 19, 22 |
| 10 | **Pillar 2, GROW: domestic resilience:** soil, water, seed, fertiliser, protein, regenerative farming | 24, 03, 15, 17 |
| 11 | **Running it:** a lean (~65), open, automated agency; port hubs, district stores, local points | 23 |
| 12 | **Work, prestige and a food-producing nation:** jobs across both pillars, AI and work, the 16 benefits of regenerative farming, a food surplus | 04, 18, 21, 25 |
| 13 | **A new economy of food:** one carbon price, full-cost accounting, the four nations | 08, 12, 18, 21 |
| 14 | **The plan:** both pillars, the contingency ladder (rationing, livestock, nitrogen), governance | 15, 19 |
| – | **Related concept (not costed): Homes, Land and Livelihoods:** garden villages, new towns, shared land and land work | 26 |

## All notes

| # | Note |
|---|---|
| 01 | Stocks, days of cover and single points of failure |
| 02 | Fisheries and aquaculture |
| 03 | Phosphorus, potash and inputs beyond nitrogen |
| 04 | Meaningful work in nature and technological unemployment |
| 05 | Geopolitics, prices, social unrest and cultural change |
| 06 | Food tech, energy and a power-cut stress test |
| 07 | Climate, pests and correlated failure |
| 08 | Devolved policy, support schemes and tax |
| 09 | Diet shift, feed–food mass balance and waste (cereal model) |
| 10 | Household equity and local response |
| 11 | Food as the foundation of social stability |
| 12 | Carbon credits, nature markets and a new economy of food |
| 13 | How other countries store food: reserves, plans and costs |
| 14 | Who has food reserves, why "six months", and is it enough? |
| 15 | From feed to food, and a full system restructure |
| 16 | Storing a complete diet, not just grain |
| 17 | Nature's gift: how the UK stacks up as a place to grow food |
| 18 | The big picture: carbon markets, geopolitics, culture, regenerative farming and AI |
| 19 | The contingency ladder: rationing, the livestock destocking order, safe nitrogen |
| 20 | Stabilising the region: trade and mutual support, earning without gouging |
| 21 | Our position: one carbon price, work in nature after AI, the consciousness shift |
| 22 | Human food first, food for everyone, and the jobs |
| 23 | Running it: a lean, open, automated agency and a decentralised network |
| 24 | Domestic resilience: soil, water, seed and fertiliser |
| 25 | Work, prestige and a food-producing nation (with the 16-benefits infographic) |
| 26 | Homes, Land and Livelihoods: garden villages, new towns and land work (related concept) |
| 27 | The value of safety and stability (benefits and break-even thresholds) |

Models: `research/model/reserve_basket.py` (cost of both pillars, sensitivity, priority schedule, break-even, jobs) and `research/model/cereal_balance.py` (month-by-month grain stocks). Run with `python3`.

## Key findings

1. **Resilient on paper, fragile in practice.** Farms produce ~101% of energy need (a 31 kcal per person margin) but rest on imported nitrogen, soya, phosphate and stable weather. There is **no public food reserve**. (01, 09)
2. **About one month of wheat** at the pre-harvest low (1.514 Mt, ~39 days of all wheat use), privately owned and not earmarked. (01)
3. **2026: the UK, France and Germany lost harvests together.** Trade insurance fails when the neighbours claim too. (07)
4. **Two chokepoints in one year**, Hormuz and the Black Sea; in 2022, export bans covered ~17% of traded calories. (05, 18)
5. **The risk is affordability:** food inflation 1.3% (Sep 2026), yet 12.2% of households are food-insecure. (05, 10)
6. **Several comparable countries hold reserves; the UK holds none.** (13, 14)
7. **Pillar 1, STORE: the UK Strategic Food Reserve, ~£10.33 per person per year.**
   - Human food first and food for everyone: bread from 4 Mt of food-grade wheat, a 3-day no-cook ration and tablets for all, plus specialist food.
   - Seed, safe nitrogen, soya meal and imported staples.
   - Paid as a public crisis tranche (~£5, taxes) plus compulsory commercial stocks (~£5, prices).

   (16, 19, 22)
8. **Pillar 2, GROW: domestic resilience, ~£4.46 per person per year of new money**, plus ~£70 per person of existing farm support aimed at resilience.
   - soil monitoring and soil health;
   - reservoirs and soil-moisture sensing;
   - seed security;
   - nutrient recycling;
   - home-grown protein;
   - regenerative bridging.

   (24)
9. **A lean (~65), open, automated agency** with a decentralised network near ports and people; open by default because a programme this size cannot be secret. (23)
10. **A contingency ladder** above both pillars: fair rationing, a livestock destocking order, safe nitrogen. (19)
11. **Per hectare, Britain is world-class; per person, it is land-poor.** Soils can recover. (17)
12. **One carbon price, no free allowances, no subsidies for emitting.** (12, 18, 21)
13. **Work and a food-producing nation:** up to ~3,600 gross jobs across both pillars (a work-in-nature pilot would be separate and separately funded); farming as a prestigious career; grow a surplus of what Britain grows best, which works as a reserve only for crops already in surplus and with an export-licence trigger. (25)
14. **The benefit first:** the plan insures a £162bn-a-year (value added) food sector and 4.1 m jobs for under 0.5% of that value; it pays for itself if it avoids a 1%-of-GDP shock once in ~40 years, or lifts wellbeing by an unmeasurably small amount. (27)
15. **Related concept:** Homes, Land and Livelihoods, clustered community-owned settlements with shared land, piloted on 2–3 sites first. Not part of the costed plan. (26)

## Open items

1. Re-open load-bearing primary sources before print (NAO report, AHDB workbook, Swiss and Swedish figures, FAOSTAT).
2. Quotes for storage, stores, fuel contracts, reservoirs and the last mile.
3. A dietitian-designed ration with variants.
4. ONS classification and subsidy-control treatment of compulsory stocks.
5. Flour-mill surge capacity; UK seed-multiplication capacity; bulk-grain ports and flood exposure.
6. Defra's reply to the FOI request (due ~18 Nov 2026).
7. ONS view on compulsory stocks; firms' financing terms; a feed-grade grain plan separate from the 4 Mt bread floor.
8. Water companies' emergency capacity for the whole population.
