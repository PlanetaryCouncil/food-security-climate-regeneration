# 14 · Who has food reserves, why "six months", and is it enough?

Tags: `research:international-comparison`, `research:supply-chain-reserves`, `research:scale-up-emergency`
Follows note 13. Status: 22 Oct 2026, web search + model (`research/model/cereal_balance.py`, `reserve_table()`). Labels: [P] primary, [S] secondary, [E] my estimate or model, [?] unresolved.

---

## 1. Can we actually know which countries have food reserves?

**Only partly.** There is no global register of national food reserves.
- **FAO/World Bank/WFP (2025)**, *Strengthening Strategic Grain Reserves*: only **about 30 countries** have *actively used* public stocks for food security, mostly developing grain importers (plus exporters India, Pakistan and Zambia) [P].
- **WTO**: developing countries notify "public stockholding for food security" spending (Agreement on Agriculture, Annex 2 para 3, Table DS:1). India is the prominent notifier. This covers *subsidy accounting*, not stock size, and rich countries' compulsory private stocks (Switzerland) are not reported this way [S].
- **AMIS/USDA** publish *total* ending stocks by country (public plus private), not strategic reserves. China alone holds ~44% of world wheat stocks by USDA-based estimates [S].
- **Secrecy is deliberate.** China (reserve size), Singapore (state stockpile size and location) and Sweden (site locations) keep details classified, because a known reserve is a target, and a known *shortfall* invites panic or speculation [S].

**What we can say with confidence (sources in notes 13 and 14):**

| Type | Countries (examples) |
|---|---|
| Public / state-owned grain reserve | Finland, Norway, Sweden (2026), Germany, Japan (rice), China, India, Indonesia (rice ~5.2–5.4 Mt, 2026), Egypt, Saudi Arabia, South Korea [? size], Ethiopia (since 1982) |
| Compulsory private stocks | Switzerland, Singapore (rice importers), Israel (state-paid suppliers) |
| Regional reserves | ASEAN+3 Emergency Rice Reserve; ECOWAS regional reserve [? not re-verified] |
| **No public or compulsory reserve** | **United Kingdom**; also the US (beyond small humanitarian stocks), Canada, Australia, Ireland and the Netherlands rely on markets [? not individually verified this session] |

## 2. Why "six months"? There is no magic number

The figures cluster at **3–4 months** (FAO/World Bank rule of thumb, Switzerland, Norway, Israel) and **6–9 months** (Finland, Egypt after harvest). The logic behind them:

1. **Time to organise an alternative.** FAO's classic guidance sizes a reserve to give "adequate lead time for government to … assess the size of the shortfall and initiate measures": find new suppliers, finance imports, reroute ships. That takes **weeks to a few months**, which is where the **3–4 month** benchmark comes from (plus a *cash* reserve for imports) [P FAO; S encyclopedia summary of the FAO/World Bank figure].
2. **Distance to the next harvest.** One growing season, from spring sowing to harvest, is **~5–6 months** in northern Europe. A reserve that bridges six months lets a country plant and harvest its way out of a shock that starts in winter [E].
3. **History and geography.**
   - **Finland**: in 1917–18, with grain self-sufficiency at ~60%, Russian imports stopped and there was no reserve to fall back on. Both world wars brought embargo-driven hunger. The security-of-supply system grew out of that. The legal minimum is **6 months**; it was raised to **~9 months** in 2022–23, and a 2025 attempt to cut back to 6 months to save ~€20m (~£17m) became a political row [P NESA; S].
   - **Switzerland** stored for 6 months, cut to 4 months in 2003 (and lowered its planning ration from 3,300 to 2,300 kcal/day). It then consulted in 2023 on **12 months at a reduced ration**: cereals +50%, oils +25%, feed stocks *down*. Outcome not confirmed [?] [S].
4. **Cost and spoilage.** Grain keeps 4–10 years with good storage (Norway requires ≤4-year-old grain; Germany rotates at ~10 years). The carrying cost rises in proportion to size, while the benefit falls once alternatives can be organised. **Six months is a political compromise between insurance value and holding cost**, not a scientific optimum [E].

## 3. Is six months enough to take emergency action?

*(Read here as "enough time to put emergency measures in place". If you meant medical treatment, tell me.)*

### What can be done, and how fast (UK) [E]

| Time after shock | Emergency measures available | Needs |
|---|---|---|
| Days 1–14 | Release stocks; ration fairly; stop grain-to-ethanol and distilling; ban grain exports; prioritise fuel for food logistics; household guidance | Legal powers (Defra lacks a "power to direct", note 10) |
| Weeks 2–12 | Divert feed grain to milling; cut pig and poultry numbers (they run short of *soya* anyway); find alternative import routes and suppliers; waste reduction | Milling capacity (~5–5.5 Mt/yr wheat today) |
| 3–6 months | Spring sowing (Mar–Apr) of cereals, potatoes and pulses on temporary grass and extra land; WWII-style tillage drive | Seed, nitrogen, diesel, labour, machinery |
| 6–13 months | First harvest from the expanded area (Aug–Sep) | Weather |
| 1–3 years | Pulses replace soya; new storage; on-farm water | Investment |

**So six months is enough to reach the first emergency *spring* harvest only if the shock starts in autumn or winter.** A shock that starts in spring, after the sowing window, needs up to **~12 months** of bridging to the next harvest. That is why Finland went to nine and Switzerland is considering twelve.

### But the UK is different from Finland or Switzerland: it grows most of its own grain

The model (imports stop 1 July; ethanol and distilling cut 75%; no exports) asks how big a reserve is needed to avoid running out over two years:

| Case | Extra reserve needed | ≈ days of national energy |
|---|---|---|
| Normal harvests, feed kept at 100% | 0 Mt | 0 |
| Two −15% harvests, **feed kept at 100%** | **5.5 Mt** | ~116 (≈4 months) |
| Two −15% harvests, feed cut to 80% | 0.1 Mt | ~3 |
| 2nd harvest −35% (nitrogen cut), **feed 100%** | **6.5 Mt** | ~137 (≈4.5 months) |
| 2nd harvest −35% (nitrogen cut), feed 80% | 1.1 Mt | ~23 |
| Two −30% harvests (nitrogen + weather), feed 80% | 6.0 Mt | ~126 |
| Two −30% harvests, feed cut to 50% | 0 Mt | 0 |

**Key insight [E]:** for the UK, **reserve size is a trade-off with how much livestock feed you are willing to cut.**
- About 1 month of reserve (~1–1.5 Mt) covers bad-but-plausible shocks *if* feed is trimmed 20%.
- About **4–5 months (~5.5–6.5 Mt)** lets the country ride out a nitrogen or two-harvest shock **without forcing a cull**, but the herd still shrinks, because imported *soya* is gone (note 09).
- A **6-month** grain reserve for the UK (~3 Mt of *food* grain, note 13) is therefore generous for *calories*. Its real value is **time and choice**: time to sow, to re-route imports, and to manage livestock reductions without panic.

What six months of *grain* does **not** cover:
- **Protein and fats:** oils, pulses and feed protein need their own stocks (Switzerland stores protein feed for 2 months and oils for 3–4).
- **Nutrients:** B12, calcium, iodine, infant formula and medical diets (note 09).
- **Next season's inputs:** **nitrogen fertiliser and seed** (Switzerland stores N for a third of a season; Finland stores seed). Without them, the *second* harvest fails, and that is what turns a 6-month problem into a multi-year one.
- **Power and processing:** grain needs mills and bakeries running. That is why Germany is adding ready-to-eat meals.

## 4. Bottom line for the PDF
- "About 30 countries actively use public food reserves. The UK is not one of them."
- "Six months is a rule of thumb: the time it takes to find new suppliers, or to sow and harvest a spring crop. It is a compromise between insurance and cost, not a scientific number."
- "Because Britain grows most of its own grain, a reserve's job is to buy *time and choice*: a month covers the calories if we cut animal feed by a fifth; four to five months avoids forcing that choice in a nitrogen or double-harvest shock. But grain alone isn't enough. Store seed, nitrogen, oils and protein too."

## Sources
- FAO/World Bank/WFP 2025, Strengthening Strategic Grain Reserves: https://documents1.worldbank.org/curated/en/099042625211562573/pdf/P504545-488431b2-0565-40f9-852c-e8db32d22559.pdf ; blog: https://blogs.worldbank.org/en/agfood/leveraging-strategic-grain-reserves-to-enhance-food-security
- FAO on reserve sizing and lead time: https://www.fao.org/4/w4979e/w4979e0a.htm
- 3–4 month benchmark (secondary): https://www.encyclopedia.com/food/encyclopedias-almanacs-transcripts-and-maps/grain-reserves
- FAO SOCO 2026, public stockholding: https://openknowledge.fao.org/server/api/core/bitstreams/60c5116a-7dee-46fd-aa20-d2ce2446ae7e/content/state-of-agricultural-commodity-markets/2026/public-stockholding-buffer-emergency.html
- WTO public stockholding: https://www.southcentre.int/wp-content/uploads/2015/12/AN_MC10_3_Public-stockholding.pdf ; https://www.cuts-geneva.org/wp-content/uploads/2023/09/BP-EACGF16-Public_Food_Stockholding.pdf
- IFPRI on African reserves: https://www.ifpri.org/blog/strategic-grain-reserves-africa/
- Finland history: https://huoltovarmuuskeskus.fi/en/organisation/historic-view/1910s ; https://www.huoltovarmuuskeskus.fi/en/a/national-emergency-supply-agency-boosting-finlands-emergency-grain-stockpiles
- Switzerland 6 → 4 → 12 months: https://www.swissinfo.ch/eng/swiss-take-wider-view-of-food-supply/2180580 ; https://swissinfo.ch/eng/politics/swiss-government-proposes-expanding-national-food-stockpiles/48446798 ; https://www.swissinfo.ch/eng/business/mandatory-reserves_why-switzerland-stockpiles-for-possible-emergencies/44917424
- Indonesia rice reserve 2026: https://en.antaranews.com/news/419164/indonesias-rice-stock-hits-historic-high-of-53-mln-tons-minister
- Model: `research/model/cereal_balance.py`
