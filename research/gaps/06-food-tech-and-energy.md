# 06 · Food tech, energy and a power-cut stress test

Tags: `research:food-tech-energy`, `research:horticulture`
Gaps addressed: "Food-tech / alternative proteins" (energy intensity, scale-up, whether it *relocates* the soya and nitrogen problem) and "Energy system integration" (no single energy–food stress test).
Status: web-search research, 22 Oct 2026. Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

## 1. Headline finding

**Food tech mostly moves the dependency; it rarely removes it.** Precision fermentation swaps land and soya for electricity, sugar and *ammonia*, so it re-enters the nitrogen fracture. Vertical farms swap sunlight for grid power, and UK operators have gone bust on energy costs. The technologies that genuinely *reduce* dependency are the boring ones: gene editing for disease resistance (less pesticide, fewer lost harvests), waste heat for glasshouses, and backup power for the cold chain. **The single most important energy fact is that food is now an electricity system**: over half of UK food is chilled or frozen, payments and ordering are digital, and grain needs drying. A long power cut breaks food faster than a bad harvest does.

## 2. Precision fermentation and alternative proteins

| Item | Evidence | Source |
|---|---|---|
| Carbon footprint | Fermentation-derived whey protein (β-lactoglobulin): **5.5–17.6 t CO₂e per t protein**, the same order as extracted dairy protein; driven by sugar feedstock and electricity | [S] 2026 preprint review (not peer-reviewed) |
| Trade-off | Uses 50–85% less land than whey or soy isolates, but has *higher* GHG and water use on a fossil grid; 6–9 kg CO₂e/kg with renewable power | [P] T. reesei LCA dataset |
| Electricity | ~13–17 kWh per kg protein (Perfect Day LCA; Solar Foods via Monbiot); excludes ammonia energy | [S] |
| Scale-up | Price parity needs titres ≥50 g/L and 100,000 L fermenters | [S] 2026 review |
| Market signal | UK plant-based *meat* volume −9.4% in 2025; Tesco dropped its 300% target (see note 05) | [P] GFI Europe |

**Scale arithmetic [E]:**
- UK population protein need ≈ 69.5 m × 46.3 g × 365 ≈ **1.17 Mt protein/yr**.
- Imported feed soya (2.3 Mt meal at ~46% protein) carries ≈ **1.06 Mt protein**, about 90% of the population's protein *need*. That is consistent with the dossier's "≈ ¾ of what we eat", since consumption exceeds need.
- Replacing that soya protein with fermentation at ~15 kWh/kg needs **~16 TWh/yr of electricity**, roughly **5–6% of UK electricity demand**, *plus* the sugar feedstock (land) and the nitrogen source (ammonia).
- Supplying 10% of human protein the same way needs ~1.8 TWh/yr.

**Read:** precision fermentation is a credible *niche* (whey, egg proteins, fats, infant-formula components) and a possible use for surplus renewable power. It is not a sovereignty fix: the nitrogen still comes from Haber–Bosch, and the sugar still comes from fields. Gemini's "precision-fermentation patriotism" phase is not supported.

## 3. Vertical farming

| Item | Evidence |
|---|---|
| Jones Food Company (Ocado ~70%) | The UK's largest vertical farm operator entered **administration in April 2025**; 61 jobs lost; never profitable; ~£22m owed [S] |
| Infarm | Collapsed on energy costs and capital intensity; assets sold to a new entity for ~€40m [S] |
| Others | Vertical Futures (administration, >£10m losses in 2024), GrowUp Farms (pre-pack rescue), Upward Farms and Agricool [S] |

**Read:** vertical farms grow leafy greens and herbs, crops with almost no calories, using electric light. They are not a staple-security technology. Gemini's claim that they act as "grid stabilisers" is theoretical; no UK operator survived long enough to show it.

## 4. Glasshouses and waste heat (the useful middle)
- Tomato self-sufficiency is 17% and fresh fruit 14% (dossier). Glass needs affordable winter heat.
- UK projects: Humber Tech Park (N. Lincs) plans a **27,000 m² tomato glasshouse on data-centre waste heat** (~£3.5m/yr sales) [S, status ?]. Low Carbon Farming plans **41 glasshouse sites on waste heat** from wastewater and recycling sites [S, paywalled].
- Netherlands: Aalsmeer growers are switching from gas to data-centre heat networks [S].
- **Read:** the UK's data-centre build-out (AI) creates a large low-grade heat stream. Pairing new data centres with glasshouses is a concrete win across AI, energy and food, and fits the project's AI theme. Planning policy could *require* heat-use plans for large data centres.

## 5. Gene editing
- **The Genetic Technology (Precision Breeding) Regulations 2025 took effect on 13 Nov 2025** (England, plants only; animals deferred) [P via law-firm summaries].
- Pipeline: disease-resistant beet and potato (fewer fungicides), climate-resilient tomato, methane-reducing barley [S NIAB].
- [?] Whether any precision-bred variety is on the National List yet; one commentary says farmers cannot grow them until it is.
- **Read:** this is the most *resilience-relevant* biotech, because it cuts pesticide dependence (largely imported) and protects yields in wet years (blight). It does not fix nitrogen. Scotland and Wales have not adopted the regime: a devolution friction point (see note 08).

## 6. Energy dependencies in the food system

| Dependency | Figure | Source |
|---|---|---|
| Farm diesel | 98% of English farms use red diesel (2023/24). Implied UK farm volume ≈ **0.9 bn litres/yr** from the £384m rebate value at the 42.8p/L duty gap [E] | [P] Defra energy-use survey; [E] |
| Diesel price 2026 | 123.7p/L in April 2026, +79% on the 2025 average (69p); ECIU estimates **£337m extra** farm fuel cost this year | [S] EDM citing ECIU |
| Chilled and frozen share | >50% of UK food consumed | [S] Cold Chain Federation |
| CO₂ and nitrogen | Both tied to gas prices (note 01) | |

## 7. Stress test: a 7-day national power loss (structural reading, not a model)

Precedents: the **Iberian blackout of 28 April 2025** hit ~50–60 m people for 10–24 hours. Card payments failed, warehouse management systems stopped, refrigeration failed, and gas plants led the restoration [S]. The National Risk Register lists national power outage as a catastrophic-impact risk (dossier). The UK fuel protests of 2000 showed shelves emptying within days once deliveries stopped (note 05).

| Hours / days | What breaks first | Why |
|---|---|---|
| 0–6 h | Payments, ordering IT, store tills, traffic lights, fuel pumps | Everything electronic; few stores can trade for cash at scale |
| 6–24 h | Chilled retail stock, home fridges; milking parlours and dairy cooling (farms with generators continue) | No cooling; milk must be cooled or dumped |
| 1–3 days | Distribution centres on generator fuel only; water pumping and treatment pressure (water companies hold generators for key sites) | Generator autonomy unknown (data gap, note 01); diesel resupply needs working pumps |
| 3–7 days | Frozen stock at risk; poultry and pig units (ventilation, feed systems) at welfare crisis; bakeries and mills stop; dry goods and household cupboards become the food supply | The **household 72-hour kit** and dry stocks matter here |
| Recovery | Restart needs coordinated power, fuel and IT; spoiled chilled stock must be replaced through a supply chain that is itself restarting | |

**Implications:** (a) backup-power autonomy standards for food distribution and cold stores, plus a priority list for fuel; (b) cash and offline payment fallbacks; (c) household 72-hour guidance (the government's 2025 Resilience Action Plan and its preparedness website already push this); (d) dry staples (grain, pulses, oats) are the *power-independent* reserve. This strengthens the case for a grain and pulse reserve over a chilled or frozen one.

## 8. PDF lines
- "A fermenter needs sugar, power and ammonia. We import two of those."
- "Vertical farms grew lettuce and went bust. Data-centre heat can grow tomatoes."
- "Food is an electricity system now. Half of what we eat is chilled or frozen."

## Sources
- Fermentation LCA review (preprint, 2026): https://www.preprints.org/manuscript/202609.1464/v1
- Perfect Day LCA: https://perfectday.com/blog/life-cycle-assessment-of-perfect-day-protein
- Critique of manufactured-food energy: https://www.resilience.org/stories/2024-01-23/the-energetic-implausibility-of-manufactured-food-revisited/
- Jones Food Company administration: https://www.farminguk.com/news/uk-s-largest-vertical-farm-operator-enters-administration_66548.html ; https://www.just-food.com/news/vertical-farming-business-jones-food-placed-into-administration
- Infarm: https://igrownews.com/infarm-news-enters-administration-in-the-uk-netherlands
- Precision breeding regulations: https://www.mofo.com/resources/insights/251125-uk-finalizes-precision-breeding-rules
- Humber Tech Park greenhouse: https://datacenterdynamics.com/en/news/humber-tech-park-lincolnshire-uk-district-heating
- Low Carbon Farming 41 sites: https://www.hortweek.com/wastewater-heat-behind-plan-41-glasshouse-projects-multi-billion-plan-decarbonise-british-horticulture/fresh-produce/article/1680176
- Aalsmeer data-centre heat: https://www.hortidaily.com/article/9859964/data-centre-to-provide-heat-for-dozens-of-greenhouse-growers/
- Defra energy use on farms 2023/24: https://www.gov.uk/government/statistics/energy-use-on-farms-in-england/energy-use-on-farms-in-england-202324
- Red diesel EDM: https://edm.parliament.uk/early-day-motion/65676
- Iberian blackout analysis: https://www.slimstock.com/blog/the-iberian-blackout-and-its-consequences-on-the-supply-chain/ ; https://www.ees.tf.fau.de/files/2025/05/Blackout_ES_PT_FR_28_04_2025_en.pdf
