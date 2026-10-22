# Gap research: index and synthesis

Project: UK food security, climate, resilience, work and regeneration. Research phase for a ~12-page PDF (one page per topic).
Date: 22 October 2026. Inputs: four AI briefings (Claude, GPT, Gemini, Grok), the Claude research dossier, the GPT evidence notes and the cross-briefing gap analysis. This folder fills the gaps that analysis named, plus the new themes (AI and work, wellbeing, geopolitics, unrest, culture).

**Method and limits.** Web search only. Direct page fetches (gov.uk, nao.org.uk, ons.gov.uk and others) were blocked by the session's network policy, so figures come from search-result extracts of primary and secondary sources. Each figure is labelled: **[P]** primary source via extract, **[S]** secondary, **[E]** my own calculation or model, **[?]** unresolved. Check every [P] against the original page before final publication.

## Notes in this folder

| # | Note | Research tags | Gap it closes |
|---|---|---|---|
| 01 | Stocks, days of cover and single points of failure | supply-chain-reserves | Days of cover; CO₂, cyber, cold chain, Short Straits |
| 02 | Fisheries and aquaculture | fisheries-aquaculture | Seafood ratios, salmon, UK–EU deal, fuel |
| 03 | Phosphorus, potash and other inputs | inputs | P and K risk and recovery |
| 04 | Nature work and technological unemployment | labour-jobs, agroecology-biology | Tests the core thesis |
| 05 | Geopolitics, unrest and culture | international-comparison, diets-livestock-externalities | Hormuz, Black Sea, prices, unrest, diet trends |
| 06 | Food tech and energy | food-tech-energy, horticulture | Fermentation, vertical farms, gene editing, power-cut stress test |
| 07 | Climate, pests and correlated failure | climate | Compound extremes, European correlation, pests |
| 08 | Devolved policy and incentives | subsidies-tax-incentives, governance-policy | Four nations' schemes, Roadmap 2050, IHT |
| 09 | Diet shift and mass balance (+ model) | calories-protein, scale-up-emergency | Monthly cereal balance; protein; waste |
| 10 | Household equity and local response | supply-chain-reserves, governance-policy | LRFs, food insecurity, three-layer design |
| 11 | Food as the foundation of social stability | governance-policy, supply-chain-reserves | "Nine meals", unrest evidence, Egypt / Sri Lanka / Japan / WWII, reserves abroad, ports and strikes, the Defra FOI |
| 12 | Carbon credits, nature markets and a new economy | subsidies-tax-incentives, forestry | WCC / Peatland / BNG prices, CBAM on fertiliser, Denmark livestock tax, soil-credit integrity, food as foundational infrastructure |
| 13 | How other countries store food: reserves, plans, costs | international-comparison, supply-chain-reserves | Finland, Switzerland, Norway, Sweden, Germany, Japan, Singapore, Israel, Egypt, India, China, Gulf vs UK; UK cost scaling |
| 14 | Who has reserves, why six months, is it enough? | international-comparison, scale-up-emergency | Data limits; sizing logic; UK reserve-vs-feed trade-off (model) |
| 15 | Feed to food and full system restructure | calories-protein, diets-livestock-externalities, agroecology-biology | Can people eat feed grain; rotating reserve; fewer animals; swill; full-cost; carbon-negative options; blueprint |
| 16 | Storable full-diet reserve and rotation | supply-chain-reserves, calories-protein | Complete storable ration, costs (£1–13/person/yr), rotation outlets, honest downsides |
| 17 | The €2 insurance framing | supply-chain-reserves | What €2/person/yr buys, ROI break-even odds, economies of scale, slogans |

Models: `research/model/cereal_balance.py` and `research/model/reserve_basket.py` (run with `python3`).

Tags the dossier already covers well and this folder leaves alone: `baseline-self-sufficiency`, `soils-land`, `water`, `forestry`. `international-comparison` (reserves abroad) is in dossier Part 8.

## Ten findings that change or sharpen the story

1. **Days of cover now has a number.** At the 1 July pre-harvest low, wheat in store ≈ **1 month** of national calories; wheat + barley + oats ≈ **2 months**. This is energy only, privately owned and not earmarked. (01)
2. **Grain isn't the binding constraint; protein feed and fertiliser are.** With bioethanol, distilling and exports stopped, UK cereals cover food *and* today's feed through an import stop with normal harvests. Two bad harvests need feed cut ~20%; a nitrogen shock is worse. Pigs and poultry shrink because the *soya* stops, not the grain. (09)
3. **2026's harvest failure was correlated across Europe.** France lost ~8 Mt of cereals and Germany up to ~3 Mt, alongside the UK. Trade insurance fails when the neighbours claim too. (07)
4. **Two chokepoints in one year:** Hormuz (LNG and up to 30% of traded fertiliser; urea more than doubled to >$850/t by April) and the Black Sea (Ukraine wheat exports forecast −53%). FAO index at its highest since Nov 2022. (05)
5. **Yet UK food inflation is only ~1.3% (Aug 2026)** while food insecurity *rises* to 12.2%. The shock is lagged and the risk is affordability. The Claude briefing's "9% warning" line is now out of date. (05)
6. **The weakest layer is local:** most LRFs have no food plan, there is no power to direct businesses, and the last national exercise was in 2023. (10)
7. **The AI-and-nature-work thesis holds at the scale of tens of thousands of jobs, not millions.** Structured nature activity has moderate to large mental-health effects (Coventry 2021); a conservation corps raised lifetime health and earnings (CCC). But Pick for Britain filled only 5–11% of roles, 91% of young farmers flag poor mental health, and picking robots are arriving. Gemini's "+300% farm labour" would cost ~£33bn/yr, about 4× farming income. (04)
8. **Food tech mostly relocates dependency.** Replacing feed-soya protein by fermentation needs ~16 TWh/yr (~5–6% of UK electricity) *plus* sugar and ammonia. UK vertical farms went bust. Data-centre heat for glasshouses is the practical AI–food crossover. (06)
9. **Seafood: we export what we catch and import what we eat.** Domestic share fell from 89% (1975) to 40% (2019). Mackerel and herring are the unused protein buffer, which makes this a culture question. (02)
10. **Phosphorus is the slow, permanent exposure:** ~174 kt P imported a year, under half used productively, ~32% equivalent flowing into sewage, and no national plan. Potash is the opposite: a world-class deposit (Woodsmith) on hold. (03)

## Corrections to the existing briefings
- **Claude PDF p.1:** "food industry warns [inflation] could reach 9% again this year" → overtaken; Aug 2026 food CPI 1.3%, Bank of England expects 3.5% by December.
- **All:** protein "194%" is not closed-loop. The imported soya alone carries roughly the population's whole protein need (09).
- **Gemini:** "+300% labour", "precision-fermentation patriotism", "vertical farms as grid stabilisers" and the "unified global carbon market by 2030" are unsupported (04, 06).
- **Gemini:** the UK "ranks alongside Ukraine's chernozem" is an assertion without a comparable soil or land dataset; drop or soften it.
- **Lagi "210" riot threshold:** don't apply it to today's FAO index (rebased in 2020), and it is not a UK model (05).
- **SFI26:** Window 2 is £180m base (+ rollover); the dossier's "~£253m" needs reconciling (08).

## Proposed 12-page structure (for when content is settled)
1. Can Britain feed itself? Headline numbers, three denominators
2. The natural endowment: climate, soils, water (existing)
3. Climate is changing the odds: compound extremes, correlated Europe, pests (07)
4. Inputs: nitrogen, phosphorus, potash, diesel, CO₂ (03, 01, 06)
5. Protein: soya, livestock, fish, "less but better" with numbers (09, 02)
6. Stocks and chokepoints: days of cover, single points of failure, the power-cut test (01, 06)
7. Geopolitics and prices: Hormuz, Black Sea, the lag (05)
8. People: food insecurity, fairness, unrest, local plans (10, 05)
9. Work: nature, wellbeing and the AI economy (04)
10. Culture: diets already changing, seafood, waste (05, 09, 02)
11. Money and policy: four nations, Roadmap 2050, tax, the missing resilience tier (08)
12. The plan: store, grow, rebalance, plant, with timelines and costs

## Top open items (next session)
1. Fetch the primary pages behind every [P] figure (NAO full report, AHDB Sep 2026 tables, ONS CPI Sep 2026, Food Foundation).
2. Extend the model with a protein ledger and a milling-capacity ceiling.
3. Scotland's 2026 tiered-support details and the NI per-hectare rate.
4. Salmon feed import share; mussel and oyster production.
5. UK household-preparedness survey data; a worked LRF food plan.
6. Cost a national dry-stock reserve properly: storage, rotation, finance.
