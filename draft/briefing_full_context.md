# Can Britain Feed Itself? Full-context briefing draft for fact-checking

**Version:** draft-3 (23 October 2026)
**Project:** UK food security, climate, resilience and regeneration; a ~12-page public briefing (one page per chapter) for MPs, officials and the public.
**Repository:** `planetarycouncil/food-security-climate-regeneration`, branch `claude/focused-mendel-5qswh8`, folders `research/notes/` (19 research notes) and `research/model/` (two Python models).

---

## 0. Instructions for the reviewing AI (please read first)

You are reviewing a draft policy briefing about UK food security. The authors have a clear agenda (section 1). Your job is **not** to change the agenda. It is to make sure every factual claim used to support it is **correct, current and properly sourced**, so the briefing survives hostile scrutiny.

For each numbered claim in each chapter:
1. Give a verdict: **CORRECT / WRONG / OUTDATED / UNVERIFIABLE / MISLEADING IN CONTEXT**.
2. If not correct, give the corrected value, year and geography, plus a **primary source URL** (government statistics, peer-reviewed papers, official agencies preferred).
3. Flag where a stronger or more recent source exists.
4. For estimates labelled **[E]**, check the arithmetic and say whether the assumptions are reasonable.
5. Separately, list any **important counter-evidence** the authors should know about, even if it weakens the argument.

**Labels used:** **[P]** primary source (seen only via search extracts; originals not opened) · **[S]** secondary (press, trade body, NGO) · **[E]** the authors' own estimate or model · **[?]** not yet verified.
**Today's date in the document's world:** 22 October 2026. Prefer 2025–2026 data. UK = United Kingdom unless England, GB or a devolved nation is stated. Note whether figures are by value or volume.

Each chapter has **Included claims** (intended for the page) and **Proactive criticism and context** (caveats, counterpoints and cut claims, kept so you have the full picture).

**Resilience through transparency.** We welcome critical thinking and adversarial scenarios. Proactive criticism is part of the design: please attack the weakest assumptions, propose worst cases we have missed, and tell us where a hostile reader would push.

---

## 1. The agenda (what this briefing argues)

1. **Britain is resilient on paper, fragile in practice.** It grows enough calories in a normal year but depends on imported gas-based fertiliser, imported soya for animal feed, a just-in-time supply chain, and weather that is getting more volatile. It holds **no public food reserve**.
2. **Nature gave Britain world-class farmland per hectare but little land per person.** That makes *what we grow and who eats it* the key choice. Soils can recover.
3. **Food is the foundation of social stability and a tool of geopolitics.** Price shocks and unfairness, not empty fields, break public trust. Countries that hold reserves get through crises better and act as reliable partners.
4. **The central proposal: the Natural Insurance (not National Insurance), £10 per person per year.** A rotating, multi-purpose reserve of grain, protein, oils, vitamins, seed and fertiliser. Grain serves as a human backup, a livestock-feed buffer, or overseas stabilisation aid. Old stock is rotated into school meals, hospitals, food banks, millers and animal feed, so there is **no waste and minimal downside**. It costs about 1% of the defence budget.
6. **Resilience through transparency.** We publish our own critique and welcome adversarial review; every claim carries its source and confidence label.
5. **A full system change built around it:** grow more food for people and less animal feed; fewer, better animals; close nutrient loops; price pollution honestly and give the money back; pay for real carbon removal; and create meaningful, AI-enabled work in nature.

---

## 2. The Natural Insurance (not National Insurance): £10 per person per year, in one table

[E] Model: `research/model/reserve_basket.py`, function `ten_pound_package()`. UK population 69.5 m. Assumptions: wholesale prices (wheat and oats £200/t, rice £500, pulses £350, rapeseed oil £1,000, sugar £500, skimmed milk powder £2,500, canned fish £5,000, nitrogen fertiliser product £350, seed £300); storage £15–80/t/yr by item; financing 4%; ~¼ of stock rotated per year at a 5% discount; new grain stores £200/t of capacity, amortised over 25 years at 4%.

| Component | Stock | Stock value (one-off, recovered on rotation) | Annual cost | £/person/yr |
|---|---|---|---|---|
| A. 90-day complete ration for everyone (grain, oats, rice, pulses, oil, sugar, milk powder, canned fish, vitamins) | 4.1 Mt | £2.61bn | £225m | £3.24 |
| B. Oils, rice and pulses topped up to 6 months | 1.1 Mt | £0.56bn | £52m | £0.74 |
| C. Seed grain (0.3 Mt) + nitrogen fertiliser (~⅓ of a season, ~1 Mt product) | 1.3 Mt | £0.44bn | £48m | £0.68 |
| D. Vitamins, fortificants, infant formula (allowance) | – | £0.06bn | £21m | £0.30 |
| E. **Multi-purpose grain** (human backup / feed buffer / overseas aid), incl. new stores | 5.0 Mt | £1.00bn | £192m | £2.76 |
| F. Operations: reserve agency, audit, local food plans, exercises, backup power at key distribution and cold-store sites | – | – | £158m | £2.28 |
| **Total** | **~11.5 Mt** | **~£4.7bn** | **~£695m** | **£10.00** |

What the multi-purpose grain alone (5 Mt) equals [E]: ~10 months of UK food-grain use, **or** ~106 days of total national calories, **or** ~4.5 months of UK livestock cereal feed, **or** about 6× the 787,000 t ASEAN+3 regional emergency rice reserve.

Scale checks [E]: £695m a year ≈ 0.02% of GDP (~£2.9trn); ≈ 14% of UK agricultural support (£4.87bn, 2025); ≈ the Swiss whole-system stockpile cost scaled to the UK (~CHF 14 per person per year, 2019, including fuel and medicines).

---

## Chapter 1 · Can Britain feed itself?

**Headline:** Resilient on paper, fragile in practice.

**Narrative:** Britain produces about 60% of the food it eats by value, and on paper its farms produce enough calories and twice the protein people need. That paper picture hides three fractures. The protein depends on imported soya fed to animals. Yields depend on imported gas-based nitrogen. The whole system runs on just-in-time logistics with no public reserve. Self-sufficiency, food security and resilience are different questions, and this briefing is about resilience.

**Included claims**
1. All-food production-to-supply ratio **60%** (2025, provisional, by farmgate value); 65% in 2024; 62% in 2023. Source: Defra, *Agriculture in the UK 2025*, ch.14: https://www.gov.uk/government/statistics/agriculture-in-the-united-kingdom-2025/chapter-14-the-food-chain [P]
2. Indigenous-type food (foods that can be grown in the UK) **72%** (2025). Same source [P]
3. The all-food ratio peaked near **78% in 1984** (above 80% in the mid-1980s by some series). Defra long-run series [P/?]
4. By volume, 2025: milk **105%**, lamb **103%**, oats **109%**, barley **107%**, eggs 88%, beef 84%, wheat **83%**, poultry 80%, potatoes 71%, pig meat 67%, sugar 61%, fresh veg **56%**, oilseed rape 49%, tomatoes 17%, fresh fruit **14%**. Defra AUK 2025 ch.14 [P]
5. Farm output ≈ **101%** of population energy need and ≈ **190–195%** of protein need (2025), before waste; "statistics in development". Defra, *Nutritional supply of agriculture in the UK 2025* (15 Oct 2026): https://www.gov.uk/government/statistics/nutritional-supply-of-agriculture-in-the-uk-2025/nutritional-supply-of-agriculture-in-the-uk-2025 [P]
6. That release states availability would fall if imported livestock feed stopped. Same source [P]
7. Imported soya meal (~2.3–2.5 Mt) carries **~1.1 Mt of protein**, roughly the whole population's protein requirement (~1.17 Mt/yr at ~46 g/person/day). LSE/AIC import data; authors' arithmetic [E]
8. Livestock use about **85%** of farmland (grazing plus feed crops) and supply about **32%** of calories. National Food Strategy (2021) [S]
9. Utilised agricultural area **16.8 Mha (69% of UK land)**; croppable 6.1 Mha. Defra land use June 2025: https://www.gov.uk/government/statistics/agriculture-in-the-united-kingdom-2025/chapter-2-structure-of-industry [P]
10. UK cereal harvest 2025: **19.5 Mt**. Defra/AHDB: https://www.gov.uk/government/statistics/agriculture-in-the-united-kingdom-2025/chapter-7-crops [P]
11. 2026 key-crop harvest forecast **18.5 Mt, a record low**; four of the five worst harvests on record fall in 2020–2026. ECIU via FarmingUK (Aug 2026) [S]
12. Defra: the UK has **"no national food stockpiles or plans to create these"** (written answer, 31 Mar 2026). https://questions-statements.parliament.uk/written-questions/detail/2026-03-20/HL15829/ [P]
13. Agriculture employs **446,200** people (1.3% of UK jobs); 40% of English farm holders are over 65, 5% under 35. Defra Farming Evidence Pack, Sep 2026 [P]
14. Food inflation peaked at **19.2%** (March 2023). Defra AUK 2025 [P]
15. Total income from farming **£8.4bn** (2025); total support £4.87bn. Defra AUK 2025 ch.10 [P]

**Proactive criticism and context**
- The 60% ratio is by *value* and includes exported production; the UK-origin share of consumption is 58% (a separate denominator). Do not convert either into a calorie share [P, Defra].
- Defra's nutrient-supply statistic subtracts feed crops but assumes no waste and minimal processing; protein figures differ inside the release itself (193%, 194%, 195%) [P].
- FAO food balance sheets put UK *supply* at ~3,435 kcal and 110 g protein per person per day (2023), about 60% above physiological need, because supply includes waste and overconsumption [S, dossier].
- Excluded: Gemini's import-dependence shares (40% domestic N, 25% domestic feed, 30% domestic agrochemicals) have no traceable source.

---

## Chapter 2 · Nature's gift

**Headline:** World-class farmland per hectare, land-poor per person, with soils that can recover.

**Narrative:** Few places grow cereals and grass as well as Britain: mild, wet, rarely frozen, rain-fed. The world wheat-yield record was set in Lincolnshire. But Britain has a third of France's arable land per person, and its best land sits in the drying east and on shrinking Fen peat. The lesson is not "grow more of everything". It is to use the gift wisely: food for people on the best land, grass and trees on the rest, and soils rebuilt, as Britain's own century-old experiments show is possible.

**Included claims**
1. Most of the UK is **Köppen Cfb** (temperate oceanic, no dry season). Met Office: https://weather.metoffice.gov.uk/climate/climate-explained/climate-zones [P]
2. Growing season (days >5 °C): ~250–290 in lowland England, 330+ on Atlantic coasts; 2016–2025 had less than half the icing days of 1961–90. Met Office / State of the UK Climate 2025 [P/S]
3. Rainfall ranges from ~550–650 mm in the east (Cambridge ~560 mm) to over 3,000 mm at Seathwaite. Met Office station averages 1991–2020 [P]
4. UK wheat averages ~**7.8 t/ha** (five-year average implied by 2026's 6.9 t/ha being 11% below it). AHDB: https://ahdb.org.uk/news/final-harvest-report-confirms-cereal-yields-are-below-historic-averages-across-the-uk [E]
5. Scotland's 10-year average wheat yield **8.6 t/ha**; 9.2 t/ha in 2023. https://gov.scot/publications/cereal-and-oilseed-rape-harvest-2023-final-estimates/pages/wheat-yield-and-production-remain-high-despite-small-decreases [P]
6. World average wheat yield ~**3.5–3.7 t/ha**; UK yields are about double. FAOSTAT [?]
7. **World record wheat yield 17.95 t/ha**, Tim Lamyman, Louth, Lincolnshire, 10 Aug 2022. https://guinnessworldrecords.com/world-records/highest-wheat-yield [P]
8. Arable land ≈ **0.09 ha per person** in the UK vs ≈ **0.27–0.29 ha** in France. FAO arable totals ÷ population [E/?]
9. Population density ~**285/km²** (UK) vs ~**120/km²** (metropolitan France) [E]
10. About **71%** of UK farmland is grass (9.5 Mha permanent, 1.3 Mha temporary, 1.2 Mha rough grazing). Defra June 2025 [P]
11. England's "best and most versatile" land (ALC grades 1–3a) is about **42%** of agricultural land. Natural England survey data [S]
12. **59.2%** of Grade 1 land lies in river or sea flood-risk areas; ~1.12 Mha (13%) of English farmland is in mapped flood zones. Environment Agency, Oct 2026 [P/?]
13. Fen peat loses **1–2+ cm a year**; ~25–50 years left under arable. Wildlife Trusts / Farmers Weekly [S]
14. Soil degradation costs **~£1.2bn/yr** (range £0.9–1.4bn) in England and Wales: organic matter loss 47%, compaction 39%, erosion 12%; 80% of the cost is off-farm. Graves et al. 2015, *Ecological Economics* 119:399–413: https://ideas.repec.org/a/eee/ecolec/v119y2015icp399-413.html [P]
15. A 3-year grass-clover ley in a 5-year rotation raised topsoil organic carbon from **0.98% to 1.23% in 28 years**, then plateaued (~1.3%); continuous arable declined. Johnston et al. 2017: https://repository.rothamsted.ac.uk/item/8v42x/changes-in-soil-organic-matter-over-70-years-in-continuous-arable-and-ley-arable-rotations-on-a-sandy-loam-soil-in-england [P]
16. Rothamsted Broadbalk (since 1843): unfertilised plots ~**1.6 t/ha**, manured or fertilised plots ~7–8 t/ha. Rothamsted guide [P]
17. Without action, England faces a **~5 bn L/day** public water shortfall by 2055 (EA scenario); in the East, spray irrigation is 51% of non-public-supply demand. EA National Framework 2025: https://www.gov.uk/government/publications/national-framework-for-water-resources-2025-water-for-growth-nature-and-a-resilient-future/3-how-much-additional-water-we-need-national-framework-for-water-resources-2025 [P]
18. Woodland **3.29 Mha (~14%)** of UK land vs an EU average of roughly 38–40%. Forest Research, Forestry Statistics 2025 [P/?]

**Proactive criticism and context**
- The ALC grades (1–5, with 3a/3b) apply to England and Wales; Scotland uses a different system.
- Excluded as unsupported: Gemini's claim that the UK "ranks alongside Ukraine's chernozem" and is "capable of total autonomy".
- The Slater et al. projection that mean yields may hold up to 2080 does not mean the *bad years* are covered (chapter 3).
- Country-by-country FAOSTAT yields (France, Germany, Ukraine, Russia, US) need pulling directly.

---

## Chapter 3 · Climate is changing the odds

**Headline:** One bad week doesn't hurt British wheat. Bad weather stacked across a season does, and that is now the pattern.

**Narrative:** British farming handles a single wet spell or heatwave. What breaks it is extremes stacked across one season, and these are becoming more common: wet autumns that stop sowing, dry springs, wet harvests. In 2026 drought hit Britain, France and Germany together, so the neighbours we rely on failed at the same time. New pests and livestock diseases are arriving with warmer winters. A reserve is the hedge against correlated failure that trade cannot provide.

**Included claims**
1. UK wheat yields since 1990 show "substantial resilience" to single extremes; significant losses come from **combinations of extremes within a season** (e.g. 2020: wet autumn, dry spring, August downpours). Slater et al. 2022, *Earth System Dynamics* 13:1377: https://esd.copernicus.org/articles/13/1377/2022/ [P]
2. Wheat yield volatility has increased significantly, driven by compound extremes across growth stages. NERC/NORA paper: https://nora.nerc.ac.uk/id/eprint/533430/1/N533430JA.pdf [P]
3. 2026 winter wheat **6.9 t/ha (−11% vs 5-yr average)**; spring barley −17%; earliest harvest on record. AHDB (2026) [P]
4. 2026 abstraction restrictions: **1,412** by 27 Aug; mandatory 50% cuts on 288 spray-irrigation licences in East Anglia; about half the potato crop is irrigated. EA via trade press [S]
5. **France: cereal output ~−8 Mt** in 2026 vs 2025; grain maize ~−35%. European Commission via Carbon Brief: https://carbonbrief.org/how-this-summers-heat-and-drought-impacted-crops-in-europe-in-six-charts [S]
6. **Germany:** grain shortfall up to ~3 Mt (~€600m / ~£520m) in 2026. DBV/Raiffeisen [S]
7. EU soft-wheat yields −7% vs 2025 (JRC MARS); Hungary's worst drought since 1991. https://ukragroconsult.com/en/news/mars-lowers-harvest-forecasts-for-all-crops-in-the-eu-for-2026/ [S]
8. **2025 was the UK's warmest year on record** (series from 1884). Met Office, Feb 2026: https://www.metoffice.gov.uk/about-us/news-and-media/media-centre/weather-and-climate-news/2026/met-office-science-helps-protect-uk-plants-from-rising-pest-risks [P]
9. Met Office/Defra Climate-Pest Risk tool covers nine insect pests (e.g. Colorado potato beetle); targeted Colorado beetle eradication in Kent, 2025. Same source [P]
10. **Wheat stem rust is re-emerging** in the UK and Ireland. EPPO-hosted study: https://pra.eppo.int/pra/c1804e50-2029-488f-b92f-d38429142e81 [S]
11. **Bluetongue BTV-3**: 160 cases in England (Aug 2024–May 2025); new vector season from 11 Jul 2025, with cases through winter 2025/26. GOV.UK: https://gov.uk/bluetongue [P]
12. Four of the five worst UK harvests on record: **2020, 2024, 2025, 2026**. ECIU [S]
13. Wheat volume self-sufficiency fell from 96% (2023) to 79% (2024, wet autumn) and recovered to 83% (2025). Defra [P]

**Proactive criticism and context**
- Slater et al. also project that warmer winters and drier June–July *could benefit* average yields to 2080; the risk is the tail, not the mean.
- The 2026 European losses were partly due to farmers planting less because of input costs (Hormuz), not only weather (USDA FAS).
- Not yet modelled: correlation coefficients between UK, French and German yield anomalies (a doable FAOSTAT/Eurostat exercise).

---

## Chapter 4 · Hidden dependencies

**Headline:** A loaf of bread runs on gas, diesel, ships and software.

**Narrative:** Britain's farms turn imported energy into food. The country no longer makes its own ammonia. All its phosphate is imported, and much of it ends up in sewage. Food-grade CO₂, needed to stun animals and pack meat, comes from a handful of gas-dependent plants. Half of what we eat is chilled or frozen, and a ransomware attack on one distributor can stop orders to every major supermarket. A week-long power cut would break the food system faster than any harvest failure.

**Included claims**
1. CF Fertilisers closed the **Billingham ammonia plant in 2023** (Ince closed 2022); the UK no longer synthesises ammonia; ammonium nitrate is made from imported ammonia. CF/industry press [S]
2. Defra's UK Food Security Report 2024 records the end of domestic primary ammonia production and reliance on imports. https://www.gov.uk/government/statistics/united-kingdom-food-security-report-2024/united-kingdom-food-security-report-2024-theme-3-food-supply-chain-resilience [P]
3. Manufactured nitrogen use fell **43%** (1990–2025); phosphate **−71%**. Defra Farming Evidence Pack 2026 [P]
4. UK imports **~174 kt of phosphorus a year**; **less than half** is used productively; phosphate fertiliser prices quadrupled mid-2020 to mid-2022. UK Phosphorus Transformation Strategy (Lancaster, Dec 2022): https://www.lancaster.ac.uk/news/scientists-release-uk-roadmap-for-managing-key-ingredient-behind-all-the-food-we-eat [P]
5. ~**55 kt P/yr** reaches wastewater works; ~22.5 kt is recycled to land in sludge (2009 data). Birmingham substance-flow analysis: https://research.birmingham.ac.uk/en/publications/a-substance-flow-analysis-of-phosphorus-in-the-uk-food-production [P]
6. Potash: Boulby (ICL) produces **polyhalite (~1.0 Mt, FY2023)**; Anglo American's Woodsmith polyhalite project has 2026 capex cut to zero, with an investment decision from 2028. Mining Weekly: https://www.miningweekly.com/article/woodsmith-polyhalite-project-uk-update-2026-08-07 [S]
7. CF Billingham historically supplied ~**60%** of UK food-grade CO₂ [S, 2021–23 reporting]
8. Government backed a **£100m three-month restart** of the Ensus bioethanol/CO₂ plant (Teesside) after it stopped in autumn 2025; CO₂ supply-resilience call for evidence closed 20 Aug 2026. https://www.gasworld.com/story/uk-government-launches-call-for-evidence-on-co2-supply-resilience/2256311.article/ [S]
9. Vivergo (Hull), the largest single UK wheat buyer (>1 Mt/yr), closed in 2025 after the UK–US deal removed the 19% US ethanol tariff. ABF/press [S]
10. **Over 50%** of food consumed in the UK is chilled or frozen; ~450 temperature-controlled warehouses and ~100,000 refrigerated vehicles. Cold Chain Federation: https://www.coldchainfederation.org.uk/policy-strategy-2026/ [S]
11. May 2025: ransomware at **Peter Green Chilled** (supplier to Tesco, Sainsbury's, M&S, Waitrose, Aldi, Co-op and others) halted order processing; M&S and Co-op were hit in the same wave. https://www.foodingredientsfirst.com/news/ransomware-uk-supermarket-supplier-food-security.html [S]
12. The Short Straits (Dover/Folkestone) carry ~18% of food, feed and drink imports but ~**42% of dairy and eggs**, 39% of meat and 29% of fruit and veg. Defra UKFSR 2024 [P/?]
13. About ten supermarkets handle ~95% of shop-bought food. Dossier / NPC *Just in Case* (2025) [S]
14. 98% of English farms use red diesel (2023/24); implied UK farm volume ~**0.9 bn litres/yr** (£384m rebate ÷ 42.8p/L duty gap). Defra energy-use survey; authors' arithmetic [P/E]
15. Farm red diesel **123.7p/L in April 2026, +79%** on the 2025 average; ECIU estimates **£337m** extra farm fuel cost in 2026. Early Day Motion: https://edm.parliament.uk/early-day-motion/65676 [S]
16. **Iberian blackout** (28 Apr 2025): ~50–60 m people, ~10+ hours; payments, warehouse systems and refrigeration failed; ~$1.8bn cost to Spain. https://www.slimstock.com/blog/the-iberian-blackout-and-its-consequences-on-the-supply-chain/ [S]
17. Calcium carbonate for flour fortification has depended on deliveries from a **single French quarry**. Grok briefing citing UKFSR [?]
18. NAO (Sep 2026): **no food supply-chain assets are in the government's critical national infrastructure database**. NAO: https://www.nao.org.uk/reports/resilience-of-the-food-supply-chain-to-disruptions/ [P]

**Proactive criticism and context**
- Phosphorus is a *slow* risk: UK arable soils hold legacy P, so a 1–3 year disruption is far less damaging than a nitrogen cut.
- Manure recycles nutrients already in the system; it is not new P or K.
- Pesticide active ingredients are believed to be mostly made abroad; no quantified inventory found [?].
- Food tech (chapter 12 context): precision fermentation needs ~13–17 kWh per kg of protein *plus* sugar and ammonia; replacing feed-soya protein this way would take ~16 TWh/yr (~5–6% of UK electricity) [E]. UK vertical farms (Jones Food Company, Apr 2025; Infarm) went into administration [S].

---

## Chapter 5 · Protein, livestock and the sea

**Headline:** Grain isn't the weak point. Imported protein is. And our "animal" grain is our biggest hidden reserve.

**Narrative:** About half of Britain's wheat, barley and oats is fed to animals, far more than the global third. Most of it could feed people if needed: the dividing line between "feed" and "food" wheat is a quality grade, not a different crop. If imports stopped, Britain's grain could keep both people and animals going if industrial uses and exports stopped; the real gap is imported soya, which pig and poultry farming stands on. The answer: grow more protein at home, keep grass-fed cattle and sheep on land nothing else can use, size pig and poultry numbers to home-grown protein, and eat the fish our own seas provide.

**Included claims**
1. **~52%** of UK wheat, barley and oats goes to animal feed (2023). Defra [P]
2. **13.45 Mt** of cereals fed to livestock (2025/26). AHDB [P]
3. Globally, **~⅓** of cereals go to feed; **86%** of livestock feed (dry matter, ~6 bn t/yr) is not human-edible; grains are 13% of feed. Mottet et al. 2017, *Global Food Security* 14:1–8: https://research.wur.nl/en/publications/livestock-on-our-plates-or-eating-at-our-table-a-new-analysis-of- [P]
4. One kg of boneless meat needs on average **2.8 kg** (ruminants) or **3.2 kg** (pigs and poultry) of human-edible feed. Same source [P]
5. 3 kg of grain ≈ 9,900 kcal vs ~1,500–2,500 kcal in 1 kg of meat: **4–6× fewer calories out than in** [E]
6. "Feed wheat" is mostly the same species (softer, lower-protein varieties); usable for biscuits, flatbreads, porridge and wholegrain. The feed–milling price gap was ~£14/t in Nov 2025 (feed £166/t, milling £180/t). Farmers Weekly [S]
7. EU food limit for the mould toxin DON in unprocessed cereals was **cut from 1,250 to 1,000 µg/kg** (Reg. 2024/1022, from 1 Jul 2024); feed guidance values are much higher. https://www.nfuonline.com/news/eu-changes-to-maximum-limits-for-mycotoxins/ [P]
8. UK flour millers process **~5–5.5 Mt** of wheat a year. UK Flour Millers / AHDB [S]
9. Model: with imports stopped on 1 July, bioethanol and distilling grain use cut 75% and exports stopped, **UK cereals cover food and today's full livestock feed for two years with normal harvests**; two −15% harvests require feed cut to ~79% of today. `research/model/cereal_balance.py` [E]
10. Halving pigs and poultry and diverting ~6 Mt of feed grain to people: **net ≈ +17 trillion kcal/yr ≈ 29% of annual national energy need** [E]
11. Replacing imported soya protein fully with UK field beans would need ~**4 Mt of beans (~1 Mha)**, ~6× today's pulse output (0.68 Mt) [E]
12. Only milk and upland suckler beef return more human-edible protein than they consume (UK data). Wilkinson 2011, *Animal* [P]
13. UK field beans are already exported to Egypt for ful medames. Trade press [S]
14. Domestic landings plus aquaculture fell from **89% (1975) to 40% (2019)** of UK seafood consumed. Harrison et al. 2023, *Rev Fish Biol Fisheries*: https://repository.essex.ac.uk/36032/1/s11160-023-09776-5.pdf [P]
15. The UK eats **31% less** seafood than recommended; even with local species, domestic production would be 73% short of guidance levels. Same source [P]
16. UK-vessel landings **~745 kt (£1.16bn)** in 2024; imports 633 kt (£3.5bn); exports 380 kt (£2.0bn). MMO: https://assets.publishing.service.gov.uk/media/692db8a7345e31ab14ecf833/2025_12_02_-_UK_Sea_Fisheries_Statistics_2024_report_-_.pdf [P]
17. Scottish farmed Atlantic salmon **197,836 t** (2025); salmon is the UK's largest food export by value (~£828m, ~111 kt). https://www.gov.scot/news/scottish-fish-farm-production-survey-2025 ; Salmon Scotland/HMRC [P/S]
18. UK–EU fisheries access extended to **30 June 2038** (May 2025 deal). https://oceans-and-fisheries.ec.europa.eu/news/eu-and-uk-formalise-agreement-full-reciprocal-access-waters-until-2038-2025-06-20_en [P]
19. Climate Change Committee, Seventh Carbon Budget (Feb 2025): **cattle and sheep −27% by 2040**, meat consumption −25%, dairy −20% by 2040; the government says this is not policy. https://www.farminguk.com/news/uk-livestock-numbers-must-fall-climate-change-committee-says_66183.html [S]
20. Average UK meat intake fell from **103.7 g to 86.3 g/day** (2008–2019, −17%), mainly smaller portions. Oxford, *Lancet Planetary Health*: https://www.oxfordmartin.ox.ac.uk/news/reduction-in-uk-red-and-processed-meat-intake-but-more-needed-to-meet-our-climate-targets [P]

**Proactive criticism and context**
- The global "86% inedible" figure is driven by grazing systems; UK pigs and poultry eat mostly human-edible grain and soya, so UK feed–food competition is *higher* than the global average.
- Mottet et al. themselves say the ~3 kg figure is lower than older estimates and needs confirmation.
- Pulse rotations are limited by soil-borne disease: field beans only once every ~5–6 years (AHDB).
- Cutting UK livestock while importing meat would move emissions abroad ("leakage").
- Salmon depends on imported feed and has high mortality (2.85% in Sep 2025), so its crisis value is limited [S].
- UK plant-based *meat* sales fell 9.4% by volume in 2025 (GFI Europe); diet change is happening through smaller portions and whole foods, not processed substitutes.

---

## Chapter 6 · Geopolitics and prices

**Headline:** Two chokepoints in one year. Britain buys from neither directly, and pays for both.

**Narrative:** In 2026 the Strait of Hormuz closed and Black Sea grain shipping came under attack. Fertiliser prices doubled within weeks. World food prices hit their highest level since 2022. In every big crisis, exporting countries ban exports and the supply that remains flows to whoever holds stock. Britain has felt little so far, because the shock arrives with a lag through next year's fertiliser and harvest. A reserve is foreign policy: it stops Britain panic-buying, lets it keep exports open and help partners, and makes it a reliable ally rather than a competitor for scarce supplies.

**Included claims**
1. Strait of Hormuz disrupted from late **Feb 2026** (Iran war); tanker traffic fell >90% within days. FAO: https://www.fao.org/newsroom/detail/fao-chief-economist-warns-of-severe-global-food-security-risks-from-disruption-to-strait-of-hormuz-trade-corridor/en [P]
2. Hormuz carries ~20% of world LNG and **up to 30% of internationally traded fertilisers**. Same source [P]
3. Urea rose from **~$400/t to >$850/t (Apr 2026)**, then $453/t in June. WTO data blog, Jul 2026: https://www.wto.org/english/blogs_e/data_blog_e/blog_dta_10jul26_451_e.htm [P]
4. Input costs rose while crop prices did not, so farmers face an "affordability crisis" with lower fertiliser use and yields likely. IFPRI: https://www.ifpri.org/blog/iran-war-from-fertilizer-to-food-crisis/ [P]
5. Russian strikes removed ~⅓ of Ukraine's grain export capacity; **Ukraine 2026/27 wheat exports forecast 8.3 Mt (−53%)**; Novorossiysk terminals suspended. S&P Global: https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/082026-factbox-black-sea-grain-trade-strained-by-escalating-russia-ukraine-conflict [S]
6. Russia and Ukraine supply ~**30%** of world wheat exports. Same source [S]
7. **FAO Food Price Index 136.0 (Sep 2026)**, highest since Nov 2022; cereals +17% and vegetable oils +18% year on year. https://fastmarkets.com/insights/fao-food-price-index-rises-in-september-on-higher-cereal-vegoil-prices-and-benchmark-at-highest-since-november-2022 [P]
8. In 2022, **32 countries imposed 77 food export restrictions**; at the late-May peak ~**17% of traded food and feed calories** were restricted; only 19% of measures were notified to the WTO. IFPRI tracker: https://www.ifpri.org/blog/food-export-restrictions-have-eased-russia-ukraine-war-continues-concerns-remain-key/ [P]
9. Indonesia's palm-oil export curbs accounted for about a third of restricted calories in 2022. Same source [P]
10. UK food inflation **1.3% (Aug 2026)**; headline CPI 3.1%; Bank of England expects food inflation ~3.5% by Dec 2026. ONS via Trading Economics: https://tradingeconomics.com/united-kingdom/inflation-cpi/news/584098 [S]
11. Spring 2026 warnings of food inflation of "at least 9%" (FDF) and >8% (IGD worst case) **have not materialised** so far. https://www.retailgazette.co.uk/blog/2026/03/middle-east-conflict-risks-pushing-uk-food-inflation-above-8-warns-igd/ [S]
12. UK CBAM (carbon border tax) on imported fertiliser starts **1 Jan 2027**; NFU and others want a delay because of Hormuz. https://www.nfuonline.com/news/nfu-calls-for-delay-to-cbam/ [S]
13. China holds ~**44%** of world wheat ending stocks (2025/26). USDA WASDE via secondary source [S/E]
14. Indonesia's government rice reserve reached a record **~5.2–5.4 Mt** in 2026. Antara: https://en.antaranews.com/news/419164/indonesias-rice-stock-hits-historic-high-of-53-mln-tons-minister [S]
15. ASEAN+3 Emergency Rice Reserve: **787,000 t** earmarked (agreement 2011, in force 2012); used after Typhoon Haiyan (2013). ASEAN: https://www.asean.org/wp-content/uploads/images/2015/October/outreach-document/Edited%20APTERR-2.pdf [P]
16. Phosphate rock comes mainly from Morocco, China and Russia. Lancaster (2022) [P]

**Proactive criticism and context**
- The UK imports little Black Sea grain directly; its exposure is through world prices, feed and fertiliser.
- Excluded: the "unified global carbon market by 2030" (Gemini): not on any negotiating table.
- Whether Hormuz is open as of late October 2026 is unconfirmed.
- UK aid fell to 0.43% of GNI (2025), heading to 0.3% by 2027; humanitarian bilateral aid fell 11% to £1.29bn (Bond): https://www.bond.org.uk/press-releases/2026/04/uk-aid-spend-falls-by-over-1-billion-as-over-18-of-uk-aid-budget-diverted-towards-asylum-support-costs-in-2025/ [S]. This is context for the "overseas stabilisation" use of the multi-purpose grain.

---

## Chapter 7 · Food and stability

**Headline:** It is rising prices, not empty fields, that break the peace. And people forgive scarcity sooner than unfairness.

**Narrative:** "Mankind is nine meals from anarchy" is an old line, and the modern evidence is more precise. Rising food prices, not price swings, are followed by unrest. In rich countries, logistics fail first: in the 2000 fuel blockade, supermarkets warned they would run out within days. What turns shortage into disorder is unfairness: governments that cut bread subsidies overnight, ministers who "never buy rice", stockpiling by those who can afford it. Britain already has one household in eight food-insecure, most local resilience forums have no food plan, and the state lacks the power to direct food businesses in a crisis. Fair, visible preparation is the stability policy.

**Included claims**
1. "There are only nine meals between mankind and anarchy": **Alfred Henry Lewis**, 1896 (New York Journal) and *Cosmopolitan*, March 1906. Quote Investigator: https://quoteinvestigator.com/2022/05/02/nine-meals/ [P]
2. Rising food price **levels** are followed by more social unrest (1990–2011, monthly international data); **volatility is not**. Bellemare 2015, *American Journal of Agricultural Economics* 97(1):1–21: https://ideas.repec.org/a/oup/ajagec/v97y2015i1p1-21..html [P]
3. 2008 and 2011 food riots clustered around global food price peaks. Lagi, Bertrand & Bar-Yam 2011: https://arxiv.org/pdf/1108.2455 [P]
4. **Sep 2000 UK fuel protests:** ~3,000 daily fuel deliveries virtually stopped; ~90% of filling stations dry; Sainsbury's warned it would run out of food "within days"; Safeway rationed bread and milk. Press and Journal; CNN: https://www.cnn.com/TRANSCRIPTS/0009/13/ee.10.html [S]
5. **Egypt, Jan 1977:** cutting the bread subsidy triggered riots in nearly every major city; reversed within two days. NPR: https://www.npr.org/sections/money/2011/02/01/133403007/protests-and-the-price-of-bread [S]
6. **Japan 2025:** rice nearly doubled (¥2,023 → ¥3,688 per 5 kg); only ~10% of released reserve rice reached shops at first; the farm minister resigned after saying he "never had to buy rice". AP via Food Manufacturing: https://www.foodmanufacturing.com/supply-chain/news/22941833/japans-rice-crisis-prices-soar-supplies-dwindle-and-minister-resigns [S]
7. **Sri Lanka 2021:** an overnight ban on synthetic fertiliser cut rice output ~20% in six months, led to ~$450m of rice imports, and was reversed in Dec 2021. Reuters timeline via press [S]
8. **UK WWII rationing:** infant mortality fell from 58 to 45 per 1,000 (1937–1944); nutrition gaps between classes narrowed. Working paper citing Ministry of Health 1946: https://arxiv.org/pdf/2301.09982 [S]
9. Household food insecurity **12.2%** (Jul 2026): 6.5 m adults and 2.2 m children; 16.7% of households with children; **35.9% of Universal Credit households**; 27.1% of single parents. Food Foundation: https://foodfoundation.org.uk/news/food-prices-tracker-july-2026 [P]
10. 60% of people "highly concerned" about food prices (Feb 2026), the highest since tracking began. Food Foundation: https://foodfoundation.org.uk/news/food-prices-tracker-february-2026 [P]
11. Trussell: **2.6 m emergency food parcels in 2025**; 2.9 m in Apr 2024–Mar 2025 (+51% on five years earlier). https://www.trussell.org.uk/news-and-research/news/food-banks-provide-over-2.6-million-food-parcels [P]
12. NAO (4 Sep 2026): local resilience forum capability for food disruption is **"insufficient"**; **most LRFs do not plan specifically for food disruption**; the last national food-disruption exercise was in **2023**; Defra lacks a **power to direct** businesses in a catastrophe. https://www.nao.org.uk/wp-content/uploads/2026/09/Resilience-of-the-food-supply-chain-to-disruptions-summary.pdf [P]
13. UK household survey 2026 (n = 10,791): **60%** have three days of no-cook food (down from 66%); **4%** have three days of bottled water; **13%** feel well prepared. https://www.gov.uk/government/statistics/uk-public-survey-of-risk-perception-resilience-and-preparedness-2026/uk-public-survey-of-risk-perception-resilience-and-preparedness-2026-headline-findings-html [P]
14. Open letter to PM Andy Burnham (5 Oct 2026), 150–180+ experts: the UK has no central food reserve (the post-war stockpile ended in the 1990s); calls for a National Council of Food Security, Defence and Resilience and storage at national, regional, local and community level. https://www.globalgovernmentforum.com/create-department-for-food-security-to-address-uk-government-complacency-on-impending-shocks-say-experts/ [S]
15. Lords debate on food security (15 Oct 2026): a peer said there are "virtually no strategic food reserves". https://hansard.parliament.uk/Lords/2026-10-15/debates/1A83180F-4DDD-4033-B32A-CD71EFEB8FEA/FoodSecurity [P/?]
16. FOI request "Strategic food reserves and compound risk" sent to Defra on 21 Oct 2026; reply due ~18 Nov 2026. https://www.whatdotheyknow.com/request/strategic_food_reserves_and_comp [S]
17. UK–Mediterranean context: dockworker unions at ~40 European and Mediterranean ports called a day of action against war on **30 Oct 2026**; no UK dock strike found for autumn 2026. https://inthesetimes.com/article/dockworkers-six-countries-announce-port-strikes-october-30 [S]

**Proactive criticism and context**
- The Lagi "210" riot threshold used the pre-2020 FAO index base; today's index (2014–16 = 100) is not comparable. Do not use "210".
- The "three meals" variant has no clear source; the attribution to Lord Cameron of Dillington is unverified.
- The Sri Lanka collapse also had debt, tourism and currency causes; the fertiliser ban was a trigger, not the sole cause.
- An aggregator's claim that "80% of experts expect food violence within 50 years" is excluded as poorly sourced.
- Felixstowe dock strikes (Aug–Sep 2022) caused no food shortages, because fresh food mostly arrives by roll-on/roll-off ferry via Dover.

---

## Chapter 8 · How other countries prepare

**Headline:** Finland, Switzerland, Norway, Sweden, Germany and Japan keep food in reserve. Britain keeps none.

**Narrative:** Countries similar to Britain treat food as critical infrastructure. Finland is legally required to hold at least six months of grain, and holds about nine. Switzerland makes importers hold three to four months of wheat, sugar, rice, oils, feed and fertiliser, and drew on its feed reserve this summer when drought stalled river transport. Norway is rebuilding three months of bread grain; Sweden passed a stockpile law in 2026; Germany is adding ready-to-eat meals for power cuts. Japan shows what goes wrong when a reserve is run down and refilled too late. Britain is alone among its peers in having no public or compulsory food stock.

**Included claims**
1. Only about **30 countries** actively use public food stocks for food security (mostly developing grain importers). World Bank/FAO/WFP 2025: https://documents1.worldbank.org/curated/en/099042625211562573/pdf/P504545-488431b2-0565-40f9-852c-e8db32d22559.pdf [P]
2. FAO/World Bank rule of thumb: a grain reserve covering **3–4 months** of consumption plus a cash reserve for imports. FAO: https://www.fao.org/4/w4979e/w4979e0a.htm ; secondary summary [S]
3. **Finland:** legal minimum **6 months** of normal human grain consumption (Government Decision 568/2024); raised to ~**8.5–9 months** in 2022–23 (top-up 64% oats, 36% wheat). NESA: https://huoltovarmuuskeskus.fi/en/a/procurement-of-additional-grain-for-emergency-stockpiles-completed [P]
4. Finland's National Emergency Supply Fund ~**€2bn (~£1.7bn)**; strategic stockpile fee on electricity ~€66m (~£57m) in 2026, ~€92m (~£79m) in 2027; ~€25m/yr admin from the budget; ~**€16 (~£14) per person per year** for all security of supply. https://www.huoltovarmuuskeskus.fi/en/organisation/funding [P]
5. Finland released up to **15,000 t of spring seed** from reserves after the poor 2021 harvest; rebuilding takes 1–3 years. NESA [P]
6. A 2025 plan to cut Finland's reserve from 9 to 6 months to save ~€20m (~£17m) caused a political row. MTV Uutiset, 6 Feb 2025 [S]
7. **Switzerland:** compulsory private stocks covering **3–4 months** overall; 2019 targets: wheat 4 months (195,000 t), sugar 3 (59,000 t), rice 4 (16,400 t); protein feed 93,000 t (2 months); edible oils 35,000 t (4 months, in tanks); N fertiliser ~⅓ of a season. FONES: https://www.bwl.admin.ch/en/range-of-compulsory-stocks ; SRF 2019 [P/S]
8. Swiss stocks cost about **CHF 14 per person per year** (whole system, incl. fuel and medicines). SRF, 2019: https://www.srf.ch/news/schweiz/schweizer-vorratskammer-kein-kaffee-im-krisenfall [S]
9. **31 Aug 2026:** Switzerland released up to **20% (~16,000 t) of protein-feed stocks** (Sep 2026–Feb 2027) because drought and low Rhine/Danube water stalled imports; only the second such release. https://www.cash.ch/news/notreserven-fur-protein-tierfutter-werden-freigegeben-964808 [S]
10. Switzerland consulted (2023) on moving from 4 to **12 months** at reduced rations (cereals +50%, oils +25%, feed down); outcome unconfirmed. https://swissinfo.ch/eng/politics/swiss-government-proposes-expanding-national-food-stockpiles/48446798 [S/?]
11. **Norway:** rebuilding **82,500 t of bread grain ≈ 3 months** by 2029; the state owns the grain, millers store it on 25-year contracts; ~NOK 300m to buy. Norwegian government: https://www.regjeringen.no/no/aktuelt/staten-ber-om-tilbod-pa-beredskaplagring-av-korn/id3028355/ [P]
12. **Sweden:** law on state-owned food-chain stockpiles (grain, seed, fertiliser, feed, spare parts) in force **1 Jul 2026**; **SEK 575m** in the 2026 budget; site locations secret. Riksdag MJU25: https://data.riksdagen.se/dokument/HD01MJU25.html [P]
13. **Germany:** federal grain reserve **705,000 t** (end-2021; ~1 month of bread) plus ~126,000 t of rice and pulses and 5,000 t of condensed milk; ~150 private storage sites; ~10-year rotation; planned **€80–90m (~£70–78m)** ready-to-eat reserve. top agrar: https://www.topagrar.com/panorama/news/das-ist-uber-deutschlands-getreidevorrate-bekannt-20020375.html [S]
14. **Japan:** rice reserve target **1 Mt**; released 590,000 t in 2025; **320,000 t in Sep 2026**; 210,000 t buyback announced 1 Sep 2026, criticised as "too late". Adnkronos/Jiji: https://english.adnkronos.com/2026/09/01/japan-govt-to-buy-back-210000-tons-of-rice-after-stockpile-release/ [S]
15. Japan's system: buys ~200,000 t a year, holds each lot ~5 years, then sells unused rice as **animal feed**. Asia News Network: https://asianews.network/japanese-government-criticised-for-slow-response-to-soaring-rice-prices/ [S]
16. **Singapore:** rice importers must hold **2× average monthly imports** as a licence condition (since 1968); the state stockpile is secret. MTI: https://www.mti.gov.sg/newsroom/written-reply-to-pq-on-stockpiling-of-key-food-items [P]
17. **Israel:** state-paid private stocks of staples estimated at ~**3 months** (INSS, Dec 2023). https://www.inss.org.il/publication/food-supply-chains/ [S]
18. **India:** central pool **92.6 Mt** of wheat and rice (1 Jul 2026) vs a buffer norm of 41.1 Mt; food subsidy budget ₹2.35 lakh crore (2026–27) for 813.5 m beneficiaries. Business Today; PRS: https://prsindia.org/budgets/parliament/demand-for-grants-2026-27-analysis-food-and-public-distribution [S/P]
19. **Egypt:** officially 4 months (Feb 2026) to ~9 months (Jun 2026) of wheat reserves. Ahram Online [S]
20. EU Preparedness Union Strategy (Mar 2025): households should be able to manage **72 hours**. Press coverage [S]

**Proactive criticism and context**
- Most data on national reserves is incomplete or secret (China, Singapore, Sweden); there is no global register.
- China's reserve is often claimed at ~700 Mt (one year); unverified, and ~650 Mt is *storage capacity*.
- India illustrates mismanagement risk: CAG found 4.72 lakh t of wheat (₹700 crore) deteriorated in Punjab, 2011–16 [S].
- Japan's 2025 release worked poorly: slow distribution and a run-down reserve.
- Finland's levy covers all security of supply (energy, medicines, food), not only food.

---

## Chapter 9 · The Natural Insurance (not National Insurance): £10 per person per year

> **The Natural Insurance** *(not National Insurance)*. Insurance for the nation's food, backed by nature's own harvest: everyone pays in a little each year, and when the shock comes, the shelves stay full.

**Headline:** £10 per person per year, under 3p a day, buys Britain a complete, rotating food backup: three months of a full diet for everyone, plus a multi-purpose grain reserve. Nothing is wasted. An army defends the border; this defends the dinner table.

**Narrative:** Britain can store a complete diet, not just grain: wheat, oats, rice, pulses, oil, sugar, milk powder, canned fish and vitamins. On top sits a **multi-purpose grain reserve**: in normal years it buffers animal feed and supports allies in crisis; in a national emergency it feeds people. Stock is rotated before it ages, into school meals, hospitals, food banks, millers and animal feed, so nothing goes to waste.

The reserve is a **stabilising force**, held in readiness the way a nation holds an army. You hope never to use it. If supply chains break (a war at sea, a cyber attack, a failed harvest across Europe, a week without power), it kicks in, keeps shelves stocked and prices calm, and buys the weeks the country needs to adapt. No government wants its citizens going hungry, queuing outside empty shops, or watching anger turn into looting.

Measured the way it is paid, per person, the cost is modest. Running it costs **£10 per person per year**. Building the new stores is a one-off **~£14 per person**, already spread inside the £10. The food itself, about **£68 per person**, is not spent: it is held, rotated and sold back. Dry stores need **no refrigeration**, only a little ventilation. At under 3p a day it costs about **1% of what Britain spends on defence**.

**Resilience through transparency.** We publish the downsides ourselves (costs, warehouses, mismanagement, political raiding, sabotage) and how each is handled. Proactive criticism is part of the design, not a footnote.

**Included claims**
1. The **£10 package** totals ~**£695m a year**: 90-day complete ration (£3.24/person); oils, rice and pulses to 6 months (£0.74); seed and ~⅓ season of nitrogen (£0.68); vitamins, fortificants and infant formula (£0.30); 5 Mt multi-purpose grain incl. new stores (£2.76); operations, audit, local plans and backup power (£2.28). `reserve_basket.py` [E]
2. Per person: **£10 a year** running; **~£14 once** for new stores (≈ £0.92 a year over 25 years, inside the £10); **~£68 of food held** (≈ £4.7bn, ~11.5 Mt), recovered as stock is rotated and sold [E]
3. Complete storable daily ration: 660 g dry → **~2,450 kcal, ~89 g protein, ~1,060 mg calcium, ~3.9 µg B12**; ~£0.42/day at wholesale; vitamin C and D from tablets, iodine from iodised salt [E]
4. Typical good-storage life: wheat grain 5–10 years; rice 5+; pulses 2–4 (then hard-to-cook); milk powder 2–3; canned fish 3–5; oils several years in sealed tanks; sugar indefinite if dry [S/E]
5. The 5 Mt multi-purpose grain ≈ **10 months** of UK food-grain use, **or ~106 days** of total national calories, **or ~4.5 months** of livestock cereal feed, **or** ~6× the 787,000 t ASEAN+3 emergency rice reserve [E]
6. Today: commercial wheat stocks at the pre-harvest low (30 Jun 2026) were **1.514 Mt**, the lowest since 2020/21, ≈ **1 month** of national calories, privately owned and not earmarked. AHDB: https://ahdb.org.uk/end-of-season-uk-cereal-supply-and-demand-september-2026 ; authors' arithmetic [P/E]
7. Retailers hold "in the region of **10 days**" of stock. Full Fact: https://fullfact.org/economy/uks-food-supply-hanging-balance/ [S]
8. **No refrigeration, little electricity:** grain cooling by aeration uses roughly **0.3 kWh per tonne over six months** in trials. https://doaj.org/article/2bfcbd50940640bf804c8ee2f94c2a61 [P]. At ~1 kWh/t/yr the whole reserve would use ~11.5 GWh (~£3m) a year; well-dried grain keeps for weeks without fans in a power cut [E]
9. **Rotation into feed:** Japan sells 5-year-old reserve rice as animal feed. https://asianews.network/japanese-government-criticised-for-slow-response-to-soaring-rice-prices/ [S]
10. **Rotation through trade:** Swiss compulsory stocks are rotated through companies' normal sales; Finland's are contracted to "keep circulating through normal business". https://huoltovarmuuskeskus.fi/en/security-of-supply/methods-and-tools [P]
11. **Overseas stabilisation:** the ASEAN+3 reserve (787,000 t) supplied disaster relief after Typhoon Haiyan (2013). https://www.asean.org/wp-content/uploads/images/2015/October/outreach-document/Edited%20APTERR-2.pdf [P]
12. **It works in practice:** Switzerland released up to 16,000 t of protein feed from its reserve in Sept 2026 when drought stalled river imports, with no consumer price impact expected. https://www.cash.ch/news/notreserven-fur-protein-tierfutter-werden-freigegeben-964808 [S]
13. **Calm instead of panic:** in the 2000 fuel blockade, Sainsbury's warned it would run out of food "within days" and Safeway rationed bread and milk. https://www.pressandjournal.co.uk/fp/past-times/4057166/fuel-price-rises/ [S]
14. **Rising food prices are followed by unrest** across countries (1990–2011). Bellemare 2015, *AJAE*: https://ideas.repec.org/a/oup/ajagec/v97y2015i1p1-21..html [P]
15. **Fairness:** 12.2% of households are food-insecure (35.9% of Universal Credit households) and cannot stockpile; a national reserve covers them. https://foodfoundation.org.uk/news/food-prices-tracker-july-2026 [P]
16. **Economies of scale:** households asked to keep 3 days of food spend roughly **£15–20 per person** at retail; the state can hold 30 days of complete food per person for ~£12.50 of stock and ~£1 a year [E]
17. **Defence comparison:** UK defence spending is ~2.36% of GDP (NATO definition, 2025–26), ≈ **£68bn a year**; the Natural Insurance (~£0.7bn) ≈ **1%** of it. https://www.instituteforgovernment.org.uk/explainer/uk-defence-spending [P/E]
18. **NATO resilience:** allies committed to 3.5% of GDP on core defence **plus up to 1.5% on defence-related resilience** (civil preparedness, critical infrastructure) by 2035; 1.5% of UK GDP ≈ £43bn, of which the reserve would be ~1.6%. https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/chart-of-the-week-defence-spending [S/E; eligibility to be checked]
19. **Peer precedents:** Sweden funds its food stockpiles from its total-defence budget (SEK 575m in 2026). https://data.riksdagen.se/dokument/HD01MJU25.html [P]. Finland funds all security-of-supply stocks with a levy at ~€16 (~£14) per person per year. https://www.huoltovarmuuskeskus.fi/en/organisation/funding [P]. Switzerland's whole system costs ~CHF 14 (~£12) per person per year (2019, incl. fuel and medicines) [S]
20. £695m a year ≈ **0.02% of GDP** and ≈ 14% of current UK farm support (£4.87bn) [E]
21. **Break-even:** if a severe national food disruption costs 1–2% of GDP (~£420–830 per person), the Natural Insurance pays for itself if such an event happens about **once every 40–85 years** [E]
22. Recent record of shocks: COVID (2020), CO₂ crisis (2021), energy and fertiliser shock (2022), salad rationing (2023), retail cyber attacks (2025), Hormuz and Black Sea disruption (2026) [S]
23. **Jobs (a bonus, not the reason):** the operations budget (~£158m/yr) could fund roughly **2,000 direct jobs** in stock management, inspection, logistics and local food planning, plus a ~£1bn construction programme for new stores [E]
24. The UK has **no** such reserve and **"no current plans"** (Defra, Mar 2026). https://questions-statements.parliament.uk/written-questions/detail/2026-03-20/HL15829/ [P]

**Per person, at a glance [E]**

| | Per person |
|---|---|
| Running the Natural Insurance (food, inputs, stores, people, plans) | **£10 a year** (under 3p a day) |
| Building the new stores (one-off, already inside the £10) | ~£14 once (≈ £0.92 a year over 25 years) |
| Food held in store (not spent; sold back on rotation) | ~£68 held |
| A severe national disruption, if it happens | ~£420–830 lost, each time |
| Today's advice: 3 days of food bought at retail | ~£15–20 for 3 days of cover |
| What each person gets | 3 months of complete food + a share of 5 Mt multi-purpose grain + next season's seed and fertiliser |

**Proactive criticism: resilience through transparency (adversarial review welcome)**

| Criticism | Evidence | How it is handled |
|---|---|---|
| It costs money | £10 per person per year (~£695m) [E] | Small per person; stock value recovered on rotation; candidate for NATO-counted resilience spending |
| It needs new warehouses and materials | ~£14 per person once (~£1bn) for ~5 Mt of new storage at an assumed £200/t; silos, tanks, pallets, packaging [E] | Spread over 25 years inside the £10; contract existing merchant and farm stores first |
| Rotation loses value | Older stock sold at a modelled 5% discount on ~¼ of stock a year [E] | Rotate into public catering and feed at known prices |
| Building it can push up prices | Japan's 2026 rice buyback was criticised as "too late"; big purchases in tight markets raise prices. https://english.adnkronos.com/2026/09/01/japan-govt-to-buy-back-210000-tons-of-rice-after-stockpile-release/ [S] | Buy gradually over 3–5 years, at harvest and in surplus years, as Finland did in 2022–23 [P] |
| It can be mismanaged | India's auditor found 4.72 lakh t of wheat (₹700 crore) deteriorated in Punjab, 2011–16. https://www.tribuneindia.com/news/punjab/wheat-worth-rs-600-cr-allowed-to-rot-cag-48189 [S] | Covered storage, first-in-first-out, temperature probes, independent audit, published stock reports |
| It can be raided by politicians | Finland tried in 2025 to cut 9 → 6 months to save ~€20m (~£17m); Japan's reserve fell to 320,000 t against a 1 Mt target [S] | Statutory minimum; release and refill rules in law (Japan must buy back within a year) |
| It can be a sabotage or theft target | Sweden keeps its new grain-store locations secret. https://www.thelocal.se/20251014/sweden-to-establish-emergency-grain-stocks-in-north [S] | Many dispersed contracted sites (Germany: ~150 sites of 2,000–8,000 t, inspected every 4–6 weeks); security vetting |
| Grain stores have physical hazards | Dust explosions and self-heating fires. https://www.fireengineering.com/firefighting/an-overview-grain-dust-explosions/ [S] | Housekeeping, bearing monitoring, drying standards, fire codes |
| Stored fertiliser is dangerous | Ammonium nitrate explosion risk (Beirut, 2020) [S] | Hold as supply contracts or safer products, at regulated sites |
| Quality loss | Insects, moulds, mycotoxins; pulses harden after 2–4 years; oils oxidise [S/E] | Specification at intake, testing, rotation before end of life |
| Firms may hold less of their own stock | Crowding out [E] | Contract firms to hold *extra* on top of working stock (Finland, Norway, Switzerland) |
| "No electricity" is overstated | Stores need aeration fans and handling kit [E] | Accurate claim: **no refrigeration; very low, interruptible power use** |

**Knowing what to expect: rare, extreme events**

The Natural Insurance is sized for the **common** shock (weeks to months). History also shows rare events hitting **many countries over several years**. They are not a reason to be discouraged; they are the reason to prepare in layers.

| Event | What happened | Lesson |
|---|---|---|
| 1783–84, Laki eruption (Iceland) | Volcanic haze over Europe, severe winter, crop losses [?] | One eruption can hit a continent's harvest |
| 1816, "the year without a summer" (Tambora, 1815) | Harvests failed across Europe; bread prices soared; crowds looted shops and grain stores in Germany and France. https://www.dhm.de/journal/en/post/the-year-without-a-summer-how-europe-descended-into-climate-chaos [S] | Multi-country failure → hunger → disorder within one season |
| 1845–52, Irish famine | Potato blight over several years; ~1 m deaths, ~1 m emigrants [S] | Single-crop dependency plus policy failure turns disease into catastrophe |
| 1972–74, world food crisis | Soviet harvest failure and large grain purchases drove world grain prices sharply up [?] | One big buyer can empty world markets |
| 2007–08, 2010–11 | Food price spikes; riots in dozens of countries; then the Arab Spring (Lagi et al. 2011) [P] | Price levels trigger unrest |
| 2022, Ukraine war | 32 countries imposed 77 export restrictions; ~17% of traded calories restricted at the peak (IFPRI) [P] | Exporters close the door in a crisis |
| 2026 | Hormuz, Black Sea, and drought across the UK, France and Germany at once (chapters 3, 6) | Shocks now arrive together |

- The annual probability that all major **wheat** breadbaskets are hit together rose from **0.3% (1967–90) to 1.2% (1991–2012)**; maize 0.8% → 1.1%; soy 1.7% → 2.0%. Gaupp et al. 2020, *Nature Climate Change* 10:54–57: https://previous.iiasa.ac.at/web/home/about/news/191209-Global-breadbaskets-failure.html [P]
- For maize, multiple-breadbasket failure risk rises from 6% to **40% at 1.5 °C** and 54% at 2 °C (Gaupp et al., follow-up) [P/S]
- Lloyd's 2015 "Food System Shock" scenario: staple prices **quadruple**. https://assets.lloyds.com/media/39690c48-2a31-474b-8ff0-9d27f8d02c7c/pdf-food-system-shock-exec-summary-june-2015.pdf [P, scenario]

**Layers [E]:** (1) weeks to months: the Natural Insurance keeps shelves and prices steady; (2) up to two years: Britain's own harvest refills grain every August, and feed grain can be diverted to people (two −15% harvests are manageable with feed cut ~⅕, chapter 5); (3) multi-year: the 5 Mt multi-purpose grain, stored seed and fertiliser, and a planned switch of grassland to crops (1939–44: cultivated land 12m → 18m acres); (4) throughout: a published plan and fair rationing rules prevent panic.

**Context for the reviewer**
- The capex (£200/t of new storage) and storage fee (£15/t/yr for grain) are assumptions; UK quotes should be gathered.
- Job numbers are rough; the policy is not justified by jobs.
- The break-even depends on an illustrative disruption cost (1–2% of GDP).
- Whether NATO's 1.5% resilience category can include food stockpiles needs checking against the 2025 Hague Summit text.
- In the UK, the realistic failure mode is panic buying, empty shelves and loss of trust, not mass riots. Present unrest as a risk the reserve reduces, not a prediction.
- The Laki and 1972–74 rows and the Gaupp follow-up figures need primary sources.
- An earlier draft used £2 per person (≈ 8 weeks of complete food); the £10 Natural Insurance buys the complete programme.
- With domestic production continuing, the reserve's main value is **time and choice** (sowing, rerouting imports, managing livestock reductions), not calories alone.

**Lines for the page**
- "The Natural Insurance (not National Insurance). £10 a year, and the shelves stay full."
- "An army defends the border. A food reserve defends the dinner table."
- "Under 3p a day. About 1% of the defence budget."
- "The rare catastrophe isn't a reason to despair. It's the reason to prepare."
- "No fridges, no waste, no panic."

---

## Chapter 10 · Work, wellbeing and the AI economy

**Headline:** Meaningful work in nature for tens of thousands, with AI as the tool, not the threat.

**Narrative:** AI and automation are hollowing out entry-level office work. Meanwhile Britain needs skilled people to rebuild soils, hedges, woodland and peat, run glasshouses and manage a national food reserve. Structured work outdoors measurably improves mental health, and America's 1930s conservation corps improved participants' health and earnings for decades. Farm work today is badly designed: seasonal, isolated and stressful. So the jobs must be rebuilt, not just offered. A **regenerative transition corps** could employ tens of thousands, with AI handling drudgery and precision, and people doing the judgement work. It is not a mass answer to AI job losses; it is meaningful work that also buys national resilience.

**Included claims**
1. Graduate job adverts **8,383 in Jul 2026, −45.6% y/y**, lowest since 2016. Adzuna via press: https://e.vnexpress.net/news/news/education/uk-graduate-jobs-plunge-to-record-low-as-ai-reshapes-entry-level-employment-market-5127639.html [S]
2. Youth (16–24) unemployment **16.2%** (three months to Mar 2026); ~981,000 young people not in education, employment or training (NEET) (Apr–Jun 2026). ONS via press [S]
3. Over a third of UK employers cut entry-level roles in the past year, partly due to AI. Reuters-reported survey [S]
4. Up to **8 million** UK jobs at risk in a worst-case second wave of generative AI; 11% of tasks exposed now, up to 59% later. IPPR, Mar 2024: https://www.ippr.org/media-office/up-to-8-million-uk-jobs-at-risk-from-ai-unless-government-acts-finds-ippr [P]
5. Structured nature-based outdoor activity: standardised mean difference **−0.64 (depression), −0.94 (anxiety)**, +0.95 positive affect; best at 8–12 weeks, 20–90 min sessions. Coventry et al. 2021, *SSM Population Health* 16:100934: https://eprints.whiterose.ac.uk/id/eprint/178622 [P]
6. Green social prescribing pilots (England, 2021–23): >8,500 referred; **85% uptake**; wellbeing improved; horticulture and care farming beat sport. NIHR ARC Yorkshire & Humber: https://arc-yh.nihr.ac.uk/new-findings-green-social-prescribing-for-adults-with-mental-health-problems [P]
7. **US Civilian Conservation Corps** (1933–42, ~3 m enrolees): no short-run job gains, but longer enrolment raised height, health, longevity and lifetime earnings. Aizer, Eli, Lee & Lleras-Muney, NBER w27103: https://www.nber.org/papers/w27103 [P]
8. Organic arable farms usually use **more labour per hectare** than conventional ones (European review); organic farms employ ~32% more per farm (Soil Association/Essex, 2006). https://orgprints.org/10178 [P/S]
9. Meeting tree-planting targets needs a **~70% larger** forestry workforce. Groundwork: https://www.groundwork.org.uk/environmental-employer-resource-hub/ [S]
10. Seasonal worker visas: **41,000** horticulture + 1,900 poultry (2026 and 2027). Home Office [P]
11. **Pick for Britain (2020):** UK workers filled ~**5–11%** of 70,000 picking roles; first-time UK workers stayed 9.5 weeks vs 14. NFU survey: https://www.farminguk.com/news/uk-residents-made-up-just-11-of-harvest-2020-workforce_56861.html [S]
12. **91%** of 750 young farmers call poor mental health the industry's "biggest hidden problem" (2025). Farm Safety Foundation: https://www.farmersguardian.com/news/4409724/mental-health-steadily-decreasing-farmers [S]
13. Strawberry-picking robots: ~50 units in commercial use in 2026, 4,000 targeted by 2029 (Dogtooth). https://www.futurefarming.com/crop-solutions/strawberry-picking-robot-dogtooth-ready-for-practical-use/ [S]
14. Robotic spot-spraying cut herbicide **35% at 97% efficacy** (peer-reviewed, sugarcane, Australia, 2025). https://researchonline.jcu.edu.au/89739 [P]
15. Data-centre waste heat for glasshouses: Humber Tech Park plans a **27,000 m² tomato glasshouse**; Dutch growers are switching to data-centre heat networks. https://datacenterdynamics.com/en/news/humber-tech-park-lincolnshire-uk-district-heating [S]
16. Gemini's "+300% farm labour" would mean ~1.34 m extra workers ≈ **£33bn/yr** at £25k, ~4× total income from farming [E]
17. Realistic scale: **tens of thousands, up to low hundreds of thousands** of paid land-based jobs over a decade [E]

**Proactive criticism and context**
- The share of entry-level decline caused by AI is contested: the Institute of Student Employers saw only an 8% dip in graduate hiring, and employers also cite higher national insurance and minimum-wage costs.
- The wellbeing evidence applies to *structured, social, part-time* activity, not 50-hour piece-rate picking.
- The CCC's long-run benefits may come partly from nutrition and structure rather than the work itself.
- Recommend pairing the corps with income policy for an AI economy.

---

## Chapter 11 · A new economy of food

**Headline:** Price what harms, pay for what protects, and give the money back.

**Narrative:** Cheap food has hidden costs: emissions, polluted rivers, degraded soils and diet-related disease. Carbon pricing is reaching farming anyway, starting with a border tax on imported fertiliser in January 2027. Carbon money is shifting towards durable removal (trees, peat, biochar) while soil-carbon offsets remain unreliable. Denmark shows a workable model: tax livestock emissions, deduct most of it, and recycle the revenue into farming and land conversion. The lesson from Europe's 2024 farmer protests is that change imposed on farmers fails, and change that pays them works.

**Included claims**
1. Agriculture emits **47 MtCO₂e (12% of UK GHG, 2024)**: 49% of methane, 59% of N₂O, 89% of ammonia. Defra Farming Evidence Pack 2026 [P]
2. FAO: global agrifood **hidden costs ≥ $10 trillion a year**, ~70% from unhealthy diets (SOFA 2023) [P]
3. UK **CBAM** covers imported fertiliser from **1 Jan 2027**; manufacturers say +£50/t or more on-farm in some cases; AIC worst case £152.5m/yr. Farmers Weekly: https://www.fwi.co.uk/business/how-the-carbon-tax-on-fertiliser-will-impact-farm-businesses [S]
4. UK ETS will integrate engineered greenhouse gas removals by **end-2029** (legislation by 2028), with a 200-year storage minimum; woodland removals undecided. https://sustainabilitymag.com/news/how-the-uk-gov-is-aiming-to-integrate-carbon-removal-by-2029 [S]
5. UK–EU ETS linking negotiations open; UK allowances ~£58/t (Nov 2025), analysts expect >£60 average in 2026. S&P Global; Carbon Pulse [S/?]
6. EU carbon-farming certification methodologies (CRCF, Reg. 2024/3012) adopted **Jul 2026**: mineral soils and agroforestry, peatland rewetting, afforestation; ≥10% uncertainty deduction. LexisNexis: https://www.lexisnexis.co.uk/legal/news/commission-adopts-delegated-regulation-establishing-crcf-carbon-farming-certification-methodologies [S]
7. Woodland Carbon Code units averaged **£28.32 (2025)**; Peatland Code **£39.57**. https://www.woodlandcarboncode.org.uk/news-events/uk-woodland-and-peatland-carbon-prices-continue-increase-2025 [P]
8. UK carbon credits contributed ~**£1.2bn** to the economy in 2025 (City of London Corp / UK Carbon Markets Forum) [S]
9. Biodiversity Net Gain statutory credits **£42,000** per unit (most habitats), £125,000 (ponds); market units ~£20k–140k. gov.uk (mirror); Savills [P/S]
10. Soil carbon credits: in Australia, most credited gains were explained by **unusually high rainfall**, not management. Mitchell et al. 2024, *Carbon Management*: https://doaj.org/article/caea2b9f2e8b4afa9934d7b36cbe5a7e [P]
11. >90% of Verra rainforest credits analysed were judged likely "phantom" (Guardian / Die Zeit / SourceMaterial, Jan 2023; disputed by Verra). https://www.carbonbrief.org/daily-brief/revealed-more-than-90-of-rainforest-carbon-offsets-by-biggest-provider-are-worthless-analysis-shows [S]
12. **Denmark:** livestock emissions tax from **2030**; 300 DKK/t CO₂e rising to 750 DKK (2035) with a 60% deduction (effective 120 → 300 DKK, ~£14 → ~£35); revenue funds converting ~10% of farmland to nature. https://www.thelocal.dk/20241118/denmark-confirms-plan-for-world-first-livestock-co2-tax-by-2030 [P/S]
13. Danish-style rates applied to UK agriculture: ~**£0.65bn/yr (2030) rising to ~£1.6bn/yr (2035)**, comparable to today's £1.8bn agri-environment budget [E]
14. UK agricultural support **£4.87bn (2025)**: agri-environment £1.85bn (+65%), area payments £1.05bn (−34%), red-diesel rebate ~£384m. Defra AUK 2025 ch.10 [P]
15. **Farming Roadmap 2050** (24 Jun 2026): food production is the "primary purpose" of farming; agri-environment (ELM) spending rises from £1.8bn (2025/26) to >£2bn by 2028/29. https://www.foodmanufacture.co.uk/Article/2026/07/03/farming-roadmap-2050-defra-unveils-plans-to-boost-english-farming/ [S]
16. SFI26: £100k cap per business; 102 → 71 actions; £240m for new agreements; Window 2 closed within hours (22 Sep 2026); herbal-ley payment cut from £382 to £224/ha. Andersons; FWI: https://www.fwi.co.uk/business/payments-schemes/analysis-what-sfi26-means-for-farm-businesses [S]
17. Inheritance tax: 100% agricultural and business property relief (APR/BPR) on the first **£2.5m** per person from 6 Apr 2026, 50% above (effective 20%); estates affected in 2026/27 halve from 375 to 185. https://www.saffery.com/insights/news/planned-cap-on-apr-and-bpr-inheritance-tax-reliefs-raised-to-2-5m/ [P/S]
18. Farmers protested with tractors in Westminster (Nov 2024, Feb 2025); the EU **withdrew its pesticide-halving regulation** (Feb 2024) after farmer protests; the Nature Restoration Law passed weakened. Euronews: https://www.euronews.com/my-europe/2024/02/06/von-der-leyen-announces-withdrawal-of-contentious-pesticide-law-the-first-defeat-of-the-gr [S]
19. **56%** of Barclays' farm customers report adopting some regenerative practices (24% planning to). https://farming.co.uk/news/barclays-more-than-half-of-uk-farmers-report-adopting-regenerative-practices-as-climate-volatility-and-cost-pressures-intensify [S]
20. Regenerative practices are modelled as **profitable after 3–5 years** across Europe, but with €2,000–5,000/ha (~£1,700–4,300/ha) upfront costs. Deloitte/WBCSD: https://www.wbcsd.org/resources/closing-the-gap-an-analysis-of-the-costs-and-incentives-for-regenerative-agriculture-in-europe/ [S]
21. "Foundational economy": Greater Manchester's "Everyday Economy" treats food production and distribution as essential infrastructure. GMCA: https://www.greatermanchester-ca.gov.uk/what-we-do/economy/the-everyday-economy/ [P]

**Proactive criticism and context**
- Excluded: Gemini's "unified global carbon market with zero carve-outs by 2030" (not achievable; it also ignores that methane is short-lived).
- The methane metric matters: GWP100 vs GWP* changes how ruminants look.
- Pricing UK livestock without a border adjustment on *food* imports exports the emissions.
- Applying a full UK ETS price (~£60/t) to all 47 Mt ≈ £2.8bn/yr ≈ a third of farm income: politically impossible without recycling [E].
- Wales (Sustainable Farming Scheme from 2026; 10% tree rule dropped; £107/ha social value payment), Northern Ireland (Farm Sustainability Payment, capped above £60k) and Scotland (four-tier framework, details not found) all differ; none pays for food *resilience* (storage, protein crops, backup power).

---

## Chapter 12 · The plan

**Headline:** Store. Grow for people. Fewer, better animals. Close the loops. Price the truth. Draw down carbon. Bring people with us.

**Narrative:** A secure Britain starts with the £10 insurance policy and builds outwards. Grow less animal feed and more food for people: pulses instead of imported soya, vegetables and fruit in glasshouses warmed by data centres. Keep cattle and sheep on grass; size pig and poultry numbers to home-grown protein. Recover phosphorus from sewage and, under strict licence, feed treated food waste to pigs as Japan and Korea do. Put an honest price on pollution, give the revenue back to farmers and households, and pay for carbon that is genuinely locked away in hedges, trees, peat and rock dust. Above all, do it with farmers and communities, not to them.

**Included claims**
1. 0–12 months: legislate the reserve, a statutory minimum and a **power to direct**; begin buying grain at harvest; local food plans in every LRF; public-catering rotation contracts [E, proposal]
2. 1–3 years: 90-day complete ration built; pulse expansion; phosphorus-recovery mandate; transition corps pilots [E]
3. 3–10 years: protein shift cuts soya imports by ~a third; glasshouses on waste heat; livestock levy phased in with revenue recycled [E]
4. 10–30 years: soils rebuilt (+25% soil carbon is achievable within a generation); woodland and hedges on poor land; carbon removal at scale if verified [E, citing Johnston et al. 2017]
5. Japan and South Korea recycle **~36% and ~43%** of food waste as heat-treated pig feed (≥70 °C for 30 min or 80 °C for 3 min), with no swill-linked outbreaks reported. Feedipedia: https://www.feedipedia.org/node/21259 [S]
6. Legalising treated swill in the EU would save **~1.8 Mha** of land (incl. >0.25 Mha of Brazilian forest and savannah), cut pork's land use 21.5% and roughly halve feed costs. zu Ermgassen et al. 2016, *Food Policy* (model): https://www.cambridgenetwork.co.uk/news/feeding-food-waste-pigs-could-save-vast-swathes-threatened-forest-and-savannah [P]
7. The UK banned swill in 2001 after the foot-and-mouth outbreak (~£8bn cost); the EU followed in 2002. Same source [S]
8. Germany requires phosphorus recovery from sewage sludge from 2029 (large plants) [?]
9. Enhanced rock weathering: modelled UK arable potential **6–30 MtCO₂/yr by 2050**; a first-year UK trial found **crop yields +15%** (+20.5% under direct drilling) and soil pH +0.2–0.29. https://goldschmidtabstracts.info/2025/32039.pdf ; https://www.agriland.co.uk/?p=381736 [S]
10. Precision Breeding Regulations (England, plants) in force **13 Nov 2025**; pipeline includes blight-resistant potatoes and disease-resistant beet. https://www.mofo.com/resources/insights/251125-uk-finalizes-precision-breeding-rules [S]
11. Household food waste **4.4–4.5 Mt edible a year (~£14bn)**: ≈ 28–42 days of national energy need [P/E]
12. Food as critical national infrastructure: the NAO found **no food assets** in the CNI database; the Cold Chain Federation is lobbying for CNI status [P/S]
13. The plan aligns with official advice on livestock (CCC −27% cattle and sheep by 2040) but leads with resilience: **pigs and poultry on imported soya first** [E]
14. A food reserve is one of the few policies farmers, environmentalists and security hawks can all support [E, judgement]

**Proactive criticism and context**
- **Sri Lanka:** sudden input bans destroy food and trust, so phase everything.
- **Leakage:** cutting UK livestock while importing meat exports emissions; pair with diet change and border measures.
- **Rural livelihoods:** upland grazing farms get ~42% of income from support payments.
- **Disease:** swill feeding needs licensed central treatment (African swine fever is now in Europe).
- **ERW** is still at the field-trial stage; per-hectare UK removal rates are not yet published.
- **Excluded:** precision fermentation and vertical farming as staple-security solutions (energy-intensive; UK firms failed); a 300% farm-labour expansion; "total autonomy" claims.

---

## Appendix A · Model assumptions (for checking the [E] claims)

**`research/model/cereal_balance.py`**: monthly pooled stock of wheat, barley and oats. Opening stock at 1 Jul: 2.95 Mt (AHDB wheat 1.514 + barley ~1.3 + oats ~0.15). Harvest 19.5 Mt (Aug 60% / Sep 40%). Food milling 6.0 Mt/yr; other industrial uses 3.2 Mt/yr; feed 13.4 Mt/yr; seed 0.6 Mt/yr; exports 1.0 Mt/yr; imports 4.5 Mt/yr (incl. maize; calibrated so the baseline roughly closes). 3.3 m kcal/t grain; need 69.5 m × 2,250 kcal/day.

**`research/model/reserve_basket.py`**: ration per person per day: wheat 350 g, oats 60, rice 50, pulses 80, rapeseed oil 35, sugar 25, skimmed milk powder 30, canned oily fish 30, + vitamin C 40 mg and D 10 µg tablets. Prices: wheat and oats £200/t, rice £500, pulses £350, oil £1,000, sugar £500, milk powder £2,500, canned fish £5,000, N fertiliser product £350, seed £300. Storage £15–80/t/yr; finance 4%; ¼ of stock rotated a year at a 5% discount; new grain stores £200/t capacity amortised over 25 years at 4%. The £10 package is in `ten_pound_package()`.

Other estimates: break-even uses a severe disruption costing 1–2% of GDP (illustrative); GDP ~£2.9trn; £1 ≈ €1.16.

## Appendix B · Verification status
- Source of all [P] items: search extracts. Originals for gov.uk, nao.org.uk, ons.gov.uk and parliament.uk could not be opened in the drafting session.
- Highest-priority checks: FAOSTAT yields and land per person (ch.2); the NAO report (ch.4, 7); AHDB 2025/26 closing stocks (ch.9); Swiss stock tonnages and cost (ch.8); UK CBAM scope (ch.6, 11); UK ETS removals and EU CRCF dates (ch.11); every [E] in chapter 9.
