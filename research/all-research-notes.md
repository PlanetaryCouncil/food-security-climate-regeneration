# All research notes: UK food security, climate and regeneration

One page with the index and all research notes, generated from `research/notes/` by `research/build_all_notes.py`. Edit the individual notes, then re-run the script.

## Contents

- [Index and key findings](#index-and-key-findings)
- [01 · Stocks, days of cover and single points of failure](#note-01)
- [02 · Fisheries and aquaculture](#note-02)
- [03 · Phosphorus, potash and inputs beyond nitrogen](#note-03)
- [04 · Meaningful work in nature as an answer to technological unemployment](#note-04)
- [05 · Geopolitics, prices, social unrest and cultural change](#note-05)
- [06 · Food tech, energy and a power-cut stress test](#note-06)
- [07 · Climate, pests and correlated failure](#note-07)
- [08 · Devolved policy, support schemes and tax](#note-08)
- [09 · Diet shift, feed–food mass balance and waste](#note-09)
- [10 · Household equity and local response](#note-10)
- [11 · Food as the foundation of social stability](#note-11)
- [12 · Carbon credits, nature markets and a new economy of food](#note-12)
- [13 · How other countries store food: reserves, contingency plans and costs](#note-13)
- [14 · Who has food reserves, why "six months", and is it enough?](#note-14)
- [15 · From feed to food: can people eat "animal" grain, and what would a full system restructure look like?](#note-15)
- [16 · Can we store a complete diet, not just grain? And is a rotating reserve really "no downside"?](#note-16)
- [17 · Insurance framing: from the £2 entry tier to the £10 Natural Insurance](#note-17)
- [18 · Nature's gift: how the UK really stacks up as a place to grow food](#note-18)
- [19 · The big picture: carbon markets, geopolitics, culture, and regenerative farming in an AI economy](#note-19)

---

<a id="index-and-key-findings"></a>

## Index and key findings

## Research notes: UK food security, climate and regeneration

Research phase for a ~12-page PDF (one page per chapter). Date: 22 October 2026.
Built on: four AI briefings (Claude, GPT, Gemini, Grok), the Claude research dossier, the GPT evidence notes and the cross-briefing gap analysis.

**How to read the labels:** **[P]** primary source · **[S]** secondary · **[E]** our own calculation or model · **[?]** not yet verified.
**Limit:** this session could search the web but not open gov.uk, nao.org.uk and similar pages directly. Check [P] figures against the originals before publication.

---

### The PDF, chapter by chapter (and which notes feed each page)

| # | Chapter | Notes |
|---|---|---|
| 1 | **Can Britain feed itself?** Resilient on paper, fragile in practice | 09, dossier Part 1 |
| 2 | **Nature's gift:** world-class yields per hectare, land-poor per person, soils that can recover | **18**, dossier Parts 4–6 |
| 3 | **Climate is changing the odds:** compound extremes, Europe failing together, new pests | 07 |
| 4 | **Hidden dependencies:** nitrogen, phosphorus, potash, diesel, CO₂, cyber, cold chain | 01, 03, 06 |
| 5 | **Protein, livestock and the sea:** soya, feed-to-food, fewer and better animals, fish | 02, 09, 15 |
| 6 | **Geopolitics and prices:** Hormuz, Black Sea, export bans, food as foreign policy | 05, 19 |
| 7 | **Food and stability:** "nine meals", unrest evidence, fairness, local plans | 10, 11 |
| 8 | **How other countries prepare:** Finland, Switzerland, Norway, Japan… and the UK's empty shelf | 13, 14 |
| 9 | **The Natural Insurance (not National Insurance), £10 per person per year:** a storable full diet + multi-purpose grain, rotation, no waste, ROI | 16, 17 |
| 10 | **Work, wellbeing and the AI economy:** a regenerative transition corps | 04, 19 |
| 11 | **A new economy of food:** carbon markets, full-cost accounting, culture, the four nations | 08, 12, 19 |
| 12 | **The plan:** store, grow for people, rebalance, close loops, draw down carbon | 15, 17, 19 |

### All notes

| # | Note |
|---|---|
| 01 | Stocks, days of cover and single points of failure |
| 02 | Fisheries and aquaculture |
| 03 | Phosphorus, potash and other inputs |
| 04 | Nature work and technological unemployment |
| 05 | Geopolitics, prices, unrest and cultural change |
| 06 | Food tech, energy and a power-cut stress test |
| 07 | Climate, pests and correlated failure |
| 08 | Policy in the four nations, support schemes and tax |
| 09 | Diet shift and the cereal balance (model) |
| 10 | Households and local response |
| 11 | Food as the foundation of social stability |
| 12 | Carbon credits, nature markets and a new economy |
| 13 | How other countries store food: reserves, plans, costs |
| 14 | Who has reserves, why six months, is it enough? |
| 15 | Feed to food and full system restructure |
| 16 | Storable full-diet reserve and rotation |
| 17 | Insurance framing: from the £2 entry tier to the £10 Natural Insurance |
| 18 | Nature's gift: how the UK really stacks up |
| 19 | The big picture: carbon markets, geopolitics, culture, regenerative farming and AI |

Draft briefing for fact-checking: `draft/briefing_full_context.md` (the Natural Insurance, £10 per person per year; downsides integrated as proactive criticism).

Models: `research/model/cereal_balance.py` (month-by-month grain stocks) and `research/model/reserve_basket.py` (cost of a complete storable diet). Run with `python3`.

### Key findings

1. **About one month of wheat at the pre-harvest low**, privately owned and not earmarked. Wheat, barley and oats together ≈ 2 months of calories. (01)
2. **Grain isn't the binding constraint; protein feed and fertiliser are.** Pigs and poultry shrink when soya stops. (09)
3. **2026: the UK, France and Germany lost harvests together.** Trade insurance fails when the neighbours claim too. (07)
4. **Two chokepoints in one year**, Hormuz and the Black Sea; in 2022, export bans covered 17% of traded calories. (05, 19)
5. **The risk is affordability:** food inflation ~1.3% (Aug 2026), yet 12.2% of households are food-insecure. (05, 10)
6. **The UK is an outlier:** no public or compulsory food reserve; Finland holds 6–9 months, Switzerland 3–4. (13, 14)
7. **A complete diet can be stored and rotated with near-zero waste.** The headline policy is **the Natural Insurance (not National Insurance): £10 per person per year** (~£695m): a 90-day complete ration for everyone, 6 months of oils/rice/pulses, seed and nitrogen, 5 Mt of multi-purpose grain (human backup / feed buffer / overseas aid) and the operations to run it. (£2 buys ~8 weeks of complete food.) (16, 17; `ten_pound_package()`)
8. **Per hectare, Britain is world-class** (wheat-yield world record, Lincolnshire); **per person, it is land-poor** (~⅓ of France's arable per head). Soils can recover: +25% soil carbon in 28 years with clover leys. (18)
9. **Carbon money is shifting to durable removals** (UK ETS from 2029, EU carbon-farming rules from 2026); soil-carbon offsets remain low-trust. (12, 19)
10. **Nature work helps people and resilience at the scale of tens of thousands of jobs, not millions.** AI is the enabler (precision spraying, robots, data-centre heat), not the enemy. (04, 19)

### Corrections to the earlier briefings
- Claude PDF: "food inflation could reach 9% this year" has been overtaken (1.3% in Aug 2026).
- All: protein "194%" is not closed-loop; imported soya carries about the population's whole protein need.
- Gemini: "+300% farm labour", "precision-fermentation patriotism", "vertical farms as grid stabilisers", "global carbon market by 2030" and "UK ranks with Ukraine's chernozem" are unsupported.
- The Lagi "210" riot threshold doesn't apply to today's rebased FAO index.
- SFI26 Window 2: £180m base (+ rollover) vs the dossier's "~£253m"; reconcile.

### Open items
1. Verify the key [P] figures against originals (NAO report, AHDB Sep 2026 tables, ONS CPI, Food Foundation, Swiss stock figures, FAOSTAT yields and land per person).
2. Add a protein ledger and milling-capacity limit to the cereal model.
3. Scotland's 2026 support tiers; NI per-hectare rate.
4. Salmon feed import share; mussel and oyster production.
5. A worked local resilience forum (LRF) food plan example.
6. Defra's reply to the FOI request (due ~18 Nov 2026).


---

<a id="note-01"></a>

## 01 · Stocks, days of cover and single points of failure

Tag: `research:supply-chain-reserves`
Gaps addressed: "no audited days-of-cover figure" and "processing, packaging, fortification and retail concentration".
Status: researched 22 Oct 2026 by web search only. The session's network blocked direct fetches of gov.uk, nao.org.uk and others, so every figure below comes from search-result extracts. **Check against the primary page before final publication.**

Evidence labels used in all gap notes:
- **[P]** figure attributed to a primary source (official statistics, the organisation's own release); seen via search extract
- **[S]** secondary report (trade press, news, NGO)
- **[E]** my own calculation; method shown
- **[?]** unresolved or conflicting

---

### 1. Headline finding

**Nobody publishes a whole-population days-of-cover figure, but grain gives a usable floor.** At the annual low point (end of June 2026, before harvest) UK wheat stocks held about one month of the whole population's calories, and wheat plus barley about two months. That covers energy only, not diet. After harvest the figure is many times higher. So the risk is seasonal: the system is thinnest in early summer.

### 2. What is known

| Item | Figure | Source |
|---|---|---|
| Official position | "No national food stockpiles and no current plans to create them" (Commons written answer, Apr 2026) | [P] Hansard via search |
| Retail stock | "Something in the region of 10 days" across grocery retailers; excludes fresh/chilled lines that skip warehouse storage | [S] Full Fact (date of article unconfirmed) |
| Wheat closing stocks, end of 2025/26 season (30 Jun 2026) | **1.514 Mt**, lowest since 2020/21; 466 kt below 2024/25 | [P] AHDB end-of-season balance, 22 Sep 2026 |
| Wheat human & industrial use 2025/26 | 6.564 Mt, down 8% (mainly bioethanol, after Vivergo closed) | [P] AHDB, Sep 2026 |
| Wheat stocks, end June 2025 | On-farm (England & Wales) 651 kt, −44% y/y; merchants/ports/co-ops 494 kt home-grown + a **record 303 kt imported** | [P] Defra/AHDB |
| Barley closing stocks 2025/26 | ~1.31 Mt (March 2026 forecast; September final not seen) | [P] AHDB [?] |
| NAO, 4 Sep 2026 | Defra has not done enough to engage households, communities and industry; may lack powers (e.g. to direct) in a catastrophic event; catastrophic-scenario exercises largely excluded food businesses; **no food supply chain assets in the government's CNI asset database** | [P] NAO press release, via search and the existing dossier |
| Open letter to PM Andy Burnham, 5 Oct 2026 | 150–180+ experts: no central food reserve (the post-WWII stockpile was ended in the 1990s); calls for a National Council of Food Security, Defence and Resilience under the Cabinet Office; storage at national, regional, local and community level; rename Defra the "Department for Environment and Food Security" | [S] Global Government Forum, FPC FreshTalk |

Context: Andy Burnham became Prime Minister on 20 July 2026 after Keir Starmer resigned. He has said the cost of living is an immediate priority [S].

### 3. Days-of-cover calculation [E]

Method: tonnes × energy density ÷ population daily need.
- Wheat: 1.514 Mt × 3.27 m kcal/t = 4.95 trillion kcal.
- Need: 69.5 m × 2,250 kcal = 156 bn kcal/day. On the GPT scenario of 70 m × 2,400 kcal it is 168 bn kcal/day.
- **Wheat at its annual low ≈ 29–32 days of total population energy.**
- Barley at ~1.31 Mt ≈ another 26–28 days, but most of it is feed or malting grade and much less usable as human food.
- Against current human and industrial wheat demand (6.56 Mt/yr), the same stock is ≈ **84 days**.

Caveats: the stock is mixed in grade, partly feed wheat and partly imported. It is privately owned and already committed to buyers, held at farms and ports, and needs milling, power and transport before it becomes food. This is the *upper bound* of what grain alone could do at the worst time of year. It is not a ration plan. The GPT briefing's 30-day / 1.48 Mt reserve scenario lines up almost exactly with this, so a "30-day reserve" largely duplicates existing June stocks in tonnage. What it would add is ownership, grade, location and release rights.

**What to say in the PDF:** "At its lowest point each year, Britain's wheat in store equals about a month of the nation's calories. It belongs to private firms, much of it is feed grade, and none of it is earmarked for an emergency."

### 4. Single points of failure

| Node | Evidence | Risk reading |
|---|---|---|
| **Food-grade CO₂** | By-product of ammonia and bioethanol. CF Billingham historically supplied ~60% of UK food-grade CO₂ [S, 2021–23]. Ensus (Teesside bioethanol) stopped in autumn 2025; the government backed a **£100m three-month restart** and the plant was kept on standby. Government call for evidence on CO₂ supply resilience closed 20 Aug 2026. Supply tightens each summer when plants do maintenance; ammonia becomes uneconomic above ~€60/MWh TTF gas [S]. | HIGH. CO₂ is used to stun pigs and poultry, in modified-atmosphere packaging and in drinks. It is a gas-price-linked chokepoint with no strategic stock. Status after the restart window: **[?]** |
| **Cyber / IT** | May 2025: ransomware at Peter Green Chilled (supplies Tesco, Sainsbury's, M&S, Waitrose, Aldi, Co-op and others) halted order processing; M&S and Co-op were hit in the same wave [S]. The NAO names cyber as a rising risk. | HIGH-frequency, short duration. Attacks stop the *order* systems while the lorries still run. |
| **Cold chain** | ~450 temperature-controlled warehouses and ~100,000 refrigerated vehicles; **over 50% of food consumed in the UK is chilled or frozen** (Cold Chain Federation letter, older) [S]. The CCF's 2026 strategy asks for critical national infrastructure (CNI) status and energy resilience. No public figure exists for backup-generator autonomy (hours of run time). | HIGH under a long power cut. This is a data gap. |
| **Short Straits (Dover/Folkestone)** | ~18% of food, feed and drink imports, but ~42% of dairy & eggs, 39% of meat and 29% of fruit & veg (UKFSR, early 2020s) [P via Grok briefing] | MED–HIGH for perishables |
| **Fortificants** | Calcium carbonate for flour fortification has relied on tanker deliveries from a single French quarry [Grok briefing, not re-verified] [?] | Low cost to fix: store 90 days |
| **Retail concentration** | ~10 retailers handle ~95% of shop-bought food (dossier) | The concentration is also a strength: few actors to coordinate in a crisis |

### 5. What is still missing (honest gaps)
- Barley, oats, oilseed and pulse closing stocks from the September 2026 final balance. The AHDB tables need downloading.
- Stocks held by manufacturers, cold stores and wholesalers, by category. The NAO says these exist; no public number was found.
- Backup-power autonomy for distribution centres and cold stores.
- CO₂ supply after the Ensus standby period ends.

### Sources
- AHDB, End of season UK cereal supply and demand, Sep 2026: https://ahdb.org.uk/end-of-season-uk-cereal-supply-and-demand-september-2026
- AHDB, Record-high imported and low home-grown wheat stocks: https://ahdb.org.uk/news/record-high-imported-and-low-home-grown-wheat-stocks-grain-market-daily
- AHDB, UK H&I demand 20-year low: https://ahdb.org.uk/news/analyst-insight-uk-human-and-industrial-demand-to-hit-20-year-low
- NAO report page: https://www.nao.org.uk/reports/resilience-of-the-food-supply-chain-to-disruptions/
- Full Fact: https://fullfact.org/economy/uks-food-supply-hanging-balance/
- Written answer on stockpiles (via Westminster Brief): https://westminsterbrief.co.uk/archive/pq/124514
- Global Government Forum on the expert letter: https://www.globalgovernmentforum.com/create-department-for-food-security-to-address-uk-government-complacency-on-impending-shocks-say-experts/
- FPC FreshTalk: https://www.fpcfreshtalkdaily.co.uk/post/experts-urge-burnham-to-put-food-security-at-heart-of-national-resilience
- Burnham becomes PM (NPR/OPB): https://www.opb.org/article/2026/07/20/andy-burnham-succeeds-keir-starmer-as-the-u-k-s-7th-prime-minister-in-10-years/
- Gasworld, CO₂ resilience call for evidence: https://www.gasworld.com/story/uk-government-launches-call-for-evidence-on-co2-supply-resilience/2256311.article/
- Farmers Weekly, Ensus: https://fwi.co.uk/business/markets-and-trends/urgent-call-for-new-co2-deal-to-ensure-food-and-drink-supply
- Food Ingredients First, Peter Green Chilled ransomware: https://www.foodingredientsfirst.com/news/ransomware-uk-supermarket-supplier-food-security.html
- Cold Chain Federation 2026 strategy: https://www.coldchainfederation.org.uk/policy-strategy-2026/


---

<a id="note-02"></a>

## 02 · Fisheries and aquaculture

Tag: `research:fisheries-aquaculture`
Gap addressed: "Fisheries & aquaculture almost absent" (no ratios, fuel or cold-chain dependency, quota limits or resilience role).
Status: web-search research, 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**Seafood is the UK's clearest example of trade mismatch, not of scarcity.** The UK catches and farms species it mostly exports (mackerel, herring, scallops, langoustine, salmon) and imports species it mostly eats (cod, haddock, tuna, warm-water prawns). By volume the UK's own landings plus aquaculture were **89% of seafood consumed in 1975 and 40% in 2019** [P, Harrison et al. 2023]. Exeter's press release puts imports at about **80% of demand** [S]. In a crisis, domestic supply could cover much more of the gap *if* people ate mackerel and herring and *if* fuel, processing and cold chain kept running. But production would still fall short of healthy-eating guidance, so fish is a supplement, not a staple fix.

### 2. Key numbers

| Item | Figure | Source |
|---|---|---|
| UK-vessel landings 2024 | ~**745 kt**, £1.16bn; +4% volume | [P] MMO UK Sea Fisheries Statistics 2024 (Dec 2025) |
| Seafood imports 2024 | 633 kt fish & preparations, £3.5bn | [P] MMO |
| Seafood exports 2024 | 380 kt, £2.0bn | [P] MMO |
| Trade 2025 | Total £6.09bn; record imports £4.1bn; cod prices up ~30% and haddock ~50% after quota cuts | [S] Seafish via trade press |
| Fleet | 5,232 vessels; 79% are under 10 m but land only 4% of the catch | [P] MMO |
| Scottish farmed Atlantic salmon 2025 | **197,836 t** (+3%); survival to harvest 68.8% (2023 year class) | [P] Scottish Fish Farm Production Survey 2025 |
| Salmon exports 2025 | ~111 kt, ~£828m: the **UK's largest food export by value**; France, US and China take ~89% | [S] Salmon Scotland/HMRC |
| UK share of global consumption | ~25% of Atlantic cod, ~50% of haddock | [S] Norwegian Seafood Council analyst |
| Consumption vs guidance | UK eats 31% less seafood than recommended; even with local species, domestic production would be 73% short of the guidance level | [P] Harrison et al. 2023 |

[?] Long-run series disagree on scope. Harrison et al. give landings of 869 kt (1975) falling to 349 kt (2020); the MMO gives 745 kt for 2024. The MMO total counts landings by UK vessels abroad and pelagic catches. Don't compare the two directly.

[E] Crude apparent supply in 2024 = 745 + 633 − 380 ≈ 1,000 kt. This mixes live weight with product weight, so it is only an order of magnitude.

### 3. Policy and access
- **UK–EU deal (May 2025):** reciprocal access extended to **30 June 2038**. Quota shares stay at 2025 levels unless both sides agree; annual quota talks with the EU and Norway continue. A £360m fishing and coastal growth fund was announced alongside. The industry called it a "sell-out" and a "horror show" [P/S].
- Cod and haddock quotas are falling, and global cod supply is forecast to drop another ~7% from 2025 [S]. The UK's main species are a *global* price risk.

### 4. Resilience reading

| Factor | Assessment |
|---|---|
| Fuel | Fishing is among the most diesel-intensive ways to make protein. Cornish producers say red diesel above £1/L threatens the fleet [S]. In a fuel shock the fleet competes with farms and food lorries. |
| Processing and cold chain | Whitefish processing (Grimsby, Peterhead) runs on *imported* frozen cod and haddock, mainly from Norway, Iceland and Russia-origin supply chains. In a severe shock, processors have the wrong raw material. [?] Needs a figure. |
| Salmon | Big protein output, but feed is largely imported (marine oils and meal, soya concentrate); mortality runs high (2.85% in a single month, Sep 2025); and the product is export-oriented. Its value in a crisis depends on feed imports, the same fracture as pigs and poultry. [?] Feed origin share not found. |
| Pelagic (mackerel, herring) | The UK's most abundant protein from the sea, nearly all exported. This is the biggest *unused* domestic buffer: a cultural question (taste, recipes), not a biological one. |
| Shellfish (mussels, oysters) | Filter feeders need no feed; mussels have very low inputs. Scale is limited by water quality, classification, sewage pollution and norovirus. Low-cost resilience with co-benefits for water quality. [?] Production tonnage not yet pulled. |

### 5. What this adds to the PDF
- One line for the protein page: "We export the fish we catch and import the fish we eat. In a crisis, mackerel is the protein we already have."
- It links to culture: the Essex study's recommendation, "fall out of love with flaky white fish", is a diet-change lever with no land cost.
- It links to jobs and coastal communities: coastal towns are among the most deprived places in the UK, so fisheries carry social weight beyond calories.

### 6. Still missing
- Salmon feed composition and import share.
- Mussel and oyster production and growth potential.
- Fuel use per tonne by fleet segment (Seafish has a fuel-consumption method paper).
- Processing capacity by species and location.

### Sources
- MMO, UK Sea Fisheries Statistics 2024: https://assets.publishing.service.gov.uk/media/692db8a7345e31ab14ecf833/2025_12_02_-_UK_Sea_Fisheries_Statistics_2024_report_-_.pdf
- Harrison, Engelhard, Thurstan & Sturrock (2023), Rev Fish Biol Fisheries: https://repository.essex.ac.uk/36032/1/s11160-023-09776-5.pdf
- Heard, Roberts & Thurstan (2025), Rev Fish Biol Fisheries 35:943–961; Exeter press release: https://news.exeter.ac.uk/research/study-tracks-uks-journey-from-seafood-self-sufficiency-to-dependence-on-imports/
- Scottish Fish Farm Production Survey 2025: https://www.gov.scot/news/scottish-fish-farm-production-survey-2025
- Salmon exports 2025: https://www.salmonbusiness.com/salmon-defies-global-headwinds-to-keep-top-spot/?amp=1
- Seafish 2025 trade: https://seafish-newsroom.prgloo.com/news/uks-seafood-trade-tops-gbp-6-billion-as-domestic-and-global-demand-strengthens
- EU–UK access to 2038: https://oceans-and-fisheries.ec.europa.eu/news/eu-and-uk-formalise-agreement-full-reciprocal-access-waters-until-2038-2025-06-20_en
- Full Fact on the fishing deal: https://fullfact.org/politics/whats-been-agreed-between-the-uk-and-the-eu-on-fishing/
- Fuel and fleet: https://www.bairdmaritime.com/fishing/high-diesel-costs-threaten-uk-fishing-fleet-viability-group-warns
- Pelagic/whitefish outlook: https://fishfocus.co.uk/whitefish-at-a-crossroads-2/


---

<a id="note-03"></a>

## 03 · Phosphorus, potash and inputs beyond nitrogen

Tag: `research:inputs`
Gap addressed: "Phosphorus, potash and other inputs beyond nitrogen" (no risk quantification or recovery pathways).
Status: web-search research, 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**Phosphorus is a slow-burn dependency; nitrogen is a fast one.** Losing nitrogen cuts yields in the *same* season. Losing phosphorus bites over *years*, because UK arable soils hold large legacy reserves built up by decades of over-application. That makes phosphorus the less urgent input in a crisis, but a permanent strategic exposure: the UK has no phosphate rock and imports from a market dominated by Morocco, China and Russia. Potash is the reverse: the UK has a world-scale domestic resource in North Yorkshire, but it is being developed slowly and mostly as polyhalite, a lower-grade multi-nutrient product.

### 2. Phosphorus

| Item | Figure | Source |
|---|---|---|
| Imports | ~**174 kt P/yr** in fertiliser, feed and food; rock originates mainly in Russia, Morocco and China | [P] UK Phosphorus Transformation Strategy (RePhoKUs, Lancaster, Dec 2022) |
| Efficiency | **Less than half** of imported P is used productively to grow food | [P] same |
| Price shock | Phosphate fertiliser price **quadrupled** mid-2020 to mid-2022 | [P] same |
| Use trend | Phosphate fertiliser use down 71% since 1990 | [P] Defra Farming Evidence Pack 2026 (dossier) |
| Sewage | ~**55 kt P/yr** reached wastewater works (2009); 57% captured in sludge; ~22.5 kt P recycled to land in sludge | [P] Birmingham substance-flow analysis (2009 data) |
| Recovery tech | Thames Water's Slough struvite reactor (designed for ~150 t/yr product) **has since closed**, and the technology was not rolled out elsewhere | [S] Utility Week |
| Governance | "The UK does not have a coherent plan for managing phosphorus" (Prof. Paul Withers) | [P] |

[E] Wastewater P is about **32%** of imports; sludge already returns about **13%** to land. Manure P is larger but *internal*: it recycles P that arrived in imported feed, so cutting livestock cuts manure P too.

**Resilience reading:**
- Short shock (1–3 years): low risk on most arable soils with P index 2 or above, which can run down legacy P. Higher risk for low-index soils, potatoes and veg, and new leys.
- Long shock: real. Biological substitution is impossible. Phosphorus cannot be fixed from the air the way nitrogen can.
- Main lever: **mandated P recovery at large wastewater works**. The EU is moving this way; Germany requires P recovery from sewage sludge from 2029 [?, verify]. The UK has no equivalent. Co-benefit: less river pollution (algal blooms, e.g. the Wye).
- Risk to manage: sludge spread to land carries PFAS ("forever chemicals"), microplastics and heavy metals. Recovery processes like struvite and ash-based recovery give cleaner products than raw sludge.

### 3. Potash and polyhalite

| Item | Figure | Source |
|---|---|---|
| Boulby (ICL, Cleveland Potash) | Moved from potash (muriate of potash, MOP) to **polyhalite**, a mineral containing potassium, sulphur, magnesium and calcium. Polyhalite output ~**1.0 Mt in FY2023**. Remaining potash is mined at reduced rates until exhausted; the end date is unconfirmed. | [S] Wikipedia/ICL [?] |
| Woodsmith (Anglo American) | The world's largest polyhalite deposit, near Whitby. **Capex cut to zero in 2026**; Fluor running feasibility studies; final investment decision **from 2028**; design capacity ~13 Mt/yr; ~$9bn spent or estimated | [S] Mining Weekly, Aug 2026 |

**Resilience reading:** The UK is *not* structurally short of potassium. Polyhalite carries only ~14% K₂O, against ~60% in MOP, so more tonnage must be spread for the same potassium, which costs more diesel and haulage. Woodsmith is a strategic asset that the market has paused. Asking whether the state should treat it as critical-minerals or food-security infrastructure is a legitimate PDF point.

### 4. Other inputs flagged but not yet quantified
- **Pesticide active ingredients:** overwhelmingly made abroad; no inventory found [?].
- **Seed:** the UK breeding base is strong, but vegetable seed is largely imported [?].
- **Spare parts and machinery:** no data found. A real gap: modern tractors depend on imported electronics and software.
- **Veterinary medicines and vaccines:** not covered by any briefing.

### 5. PDF line
"We can grow nitrogen with clover. We cannot grow phosphorus. A third of what we import already flows down our drains."

### Sources
- Lancaster/RePhoKUs, UK Phosphorus Transformation Strategy (Dec 2022): https://www.lancaster.ac.uk/news/scientists-release-uk-roadmap-for-managing-key-ingredient-behind-all-the-food-we-eat
- Birmingham, UK phosphorus substance flow analysis: https://research.birmingham.ac.uk/en/publications/a-substance-flow-analysis-of-phosphorus-in-the-uk-food-production
- Utility Week, Slough reactor closure: https://staging4.utilityweek.co.uk/is-the-uk-ready-to-close-the-loop-on-phosphorus
- ICL polyhalite transition: https://www.icl-uk.uk/cleveland-potash-announces-polyhalite-transition-timescale
- Boulby Mine overview: https://en.wikipedia.org/wiki/Boulby_Mine
- Woodsmith update, Aug 2026: https://www.miningweekly.com/article/woodsmith-polyhalite-project-uk-update-2026-08-07
- Fluor feasibility, May 2026: https://www.miningweekly.com/article/fluor-tasked-for-feasibility-study-work-on-worlds-largest-polyphalite-deposit-2026-05-08


---

<a id="note-04"></a>

## 04 · Meaningful work in nature as an answer to technological unemployment

Tags: `research:labour-jobs`, `research:agroecology-biology` and the new theme "work, wellbeing and AI".
Gap addressed: the project's thesis that land work can absorb people displaced by automation and is good for wellbeing. None of the four briefings tested this.
Status: web-search research, 22 Oct 2026. Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Verdict on the thesis

**Partly supported, but not as a mass-employment answer.** The evidence supports three narrower claims:
1. Structured time in nature improves mental health, by roughly a moderate effect size.
2. A conservation-corps model can improve participants' health and lifetime earnings decades later.
3. A lower-input, more resilient food and land system does need more skilled people per hectare.

The evidence does *not* support the idea that land work can absorb AI-scale job losses. The numbers are an order of magnitude apart; the jobs are rural while displaced workers are mostly urban; British workers have repeatedly not taken seasonal farm work; and farming itself is automating. Farm work as it is today is also bad for many farmers' mental health.

A defensible version of the thesis: **"A national programme of paid, trained, partly part-time work on land, food and nature can give tens of thousands of people meaningful work, give many more people regular contact with nature, and buy resilience at the same time. It complements income policy for an AI economy; it does not replace it."**

### 2. The technological unemployment side

| Item | Figure | Source |
|---|---|---|
| Youth (16–24) unemployment | **16.2%**, three months to March 2026 | [S] citing ONS |
| NEETs | ~**981,000** aged 16–24, Apr–Jun 2026 | [S] citing ONS |
| Graduate vacancies | 8,383 advertised in July 2026, **−45.6% y/y**, lowest since tracking began in 2016 | [S] Adzuna |
| Employers | Over a third of British employers cut entry-level roles in the past year, partly due to AI and automation | [S] Reuters-reported survey |
| Worst-case exposure | Up to **8 million** UK jobs at risk in a "second wave" of generative AI; 11% of tasks exposed now, up to 59% later; best case, no job losses and +13% GDP | [P] IPPR, Mar 2024 |
| Counter-evidence | ISE saw only an 8% dip in graduate hiring; HESA finds 7% of graduates unemployed at 15 months; employers also blame higher NICs and minimum wage | [S] |

**Read:** the entry-level squeeze is real; how much of it AI causes is still contested. The thesis should say "automation *and* a weak labour market", not claim AI alone.

### 3. The nature-and-wellbeing side

| Evidence | Finding | Strength |
|---|---|---|
| Coventry et al. 2021, *SSM Population Health* 16:100934. Systematic review and meta-analysis, 50 studies | Structured outdoor activity in green or blue space (gardening, green exercise, nature-based therapy): standardised mean difference **−0.64 depressive mood, −0.94 anxiety, +0.95 positive affect**. Best results from **8–12 week** programmes, **20–90 min** sessions | [P] Good. Some CI formatting in the abstract looks garbled; check the paper. |
| Giammanco et al. 2026, with Coventry | People with psychiatric disorders: pooled effect **0.71** on clinical symptoms versus controls | [S] new; verify |
| Natural England NECR204 (Bragg & Atkins, 2016) | Care farming, therapeutic horticulture and conservation volunteering reduce depression, anxiety and stress, and build social inclusion and belonging. Potentially cost-effective. | [P] narrative review |
| Natural England NECR228 | Efficacy strong, but referrals small; the bottleneck is delivery, not demand | [P] |
| Green social prescribing "test and learn" (7 sites, 2021–23; >£5.5m) | >8,500 referred; **85% uptake** when offered; wellbeing improved; 9–12 week activities beat 1–4 week ones; horticulture and care farming gave gains beyond sport | [P] York/NIHR evaluation |

**Read:** "nature is good for the vibes" is scientifically defensible when the activity is *structured, social, a few hours a week, and lasts at least 8 weeks*. That describes volunteering, training or part-time work. It does not describe 50-hour piece-rate picking weeks.

### 4. The reality of land work today

| Item | Figure | Source |
|---|---|---|
| Farm workforce | 446,200 (1.3% of UK jobs); 40% of English holders over 65, 5% under 35 | [P] Defra 2026 (dossier) |
| Seasonal visas | 41,000 horticulture + 1,900 poultry for 2026 and 2027, about 9% of the farm workforce | [P] Home Office (dossier) |
| Pick for Britain (2020) | British workers filled ~**5–11%** of 70,000 picking/packing roles; first-time UK workers stayed **9.5 weeks** against 14 for non-UK workers; scheme dropped | [S] NFU survey of 244 growers; Defra claimed ~⅓ |
| Farmer mental health | **91%** of 750 respondents call poor mental health the industry's "biggest hidden problem" (2025); wellbeing falling year on year, linked to longer hours | [S] Farm Safety Foundation |
| Farm suicides | 36 deaths in farming and agriculture in 2021 | [S] ONS via press |
| Automation in farming | Dogtooth strawberry robots: ~50 units in commercial use in 2026, targets of 200 (2027) to 4,000 (2029); Fieldwork Robotics fleets from 2027; second-generation picker ~£20k | [S] company targets |

**Read:** farming is short of people *and* bad at keeping them. What fails is the job design (pay, seasonality, housing, isolation, risk), not nature itself. Robotics is also coming for the very tasks that are hardest to fill.

### 5. Labour intensity of a lower-input system

| Evidence | Finding |
|---|---|
| European literature review | Organic *arable* farms usually use **more labour per hectare** than conventional; organic livestock farms use similar or less; mixed results elsewhere [P] |
| Soil Association / Essex (2006) | Organic farms employ ~**32% more people per farm** [S, advocacy; per farm, not per hectare] |
| Defra-commissioned England study | Organic farms were 46% of the sample but employed 57% of its workers; 50% casual against 33% on non-organic farms [P] |
| Forestry | Hitting tree-planting targets needs a ~**70% bigger** forestry workforce [S Groundwork] |
| Nature restoration | Skills shortages flagged for ELM and biodiversity net gain (ecologists, rangers, foresters, horticultural trades). No UK 2030 gap estimate found. [S] |

### 6. Scale check [E]

- Gemini's "agricultural labour expanded by 300%" means roughly +1.34 m workers. At £25k each that is **~£33bn/yr**, about **4× total income from farming** (£8.4bn, 2025). Not credible without a large, permanent transfer of public money.
- GPT's £500m at £50–70k loaded cost per FTE gives **7,100–10,000 FTE**.
- A realistic range for *paid* additional land-based jobs over a decade is **tens of thousands, low hundreds of thousands at most**: horticulture, forestry, hedgerows, peat, agroecology advisers, food processing. Against up to 8 m AI-exposed jobs, that is at most a few per cent.
- The bigger, cheaper lever is *participation*, not employment: 8,500 green prescriptions on a pilot budget of ~£5.5m works out at roughly £650 per person. That is the scale at which "nature for wellbeing" works.

### 7. Precedents worth citing

- **US Civilian Conservation Corps (1933–42):** ~3 m young men in ~2,600 camps. Aizer, Eli, Lee & Lleras-Muney (NBER w27103) find **no short-term job or wage gains, but longer enrolment raised height, health, longevity and lifetime earnings**. This is the best causal evidence that a nature-work corps can change lives, and it came from nutrition, structure and health rather than from jobs per se.
- **Women's Land Army (WWII):** peak membership of about 80,000 is commonly cited [? not verified in this session].
- **Green New Deal UK proposal:** National Nature Service, 10,000 placements for ~£300m [S, advocacy].

### 8. Implications for the PDF (one page: "Work")
1. Lead with the defensible claim: structured nature work measurably improves mental health, and a conservation corps improved lives for decades.
2. Say plainly that land work cannot soak up AI job losses on its own. Pair it with income policy (e.g. universal basic services or income) and with jobs in food processing, local logistics and repair.
3. Design the jobs properly: year-round contracts that mix horticulture with hedgerows, woodland, flood work and community food; housing; skills ladders; part-time and civic tiers.
4. Use automation for the drudgery (picking robots) and people for judgement work: scouting, integrated pest management (IPM), grazing management, nature monitoring, teaching.

### Sources
- IPPR, up to 8m jobs at risk (2024): https://www.ippr.org/media-office/up-to-8-million-uk-jobs-at-risk-from-ai-unless-government-acts-finds-ippr
- Graduate jobs (Adzuna via press): https://e.vnexpress.net/news/news/education/uk-graduate-jobs-plunge-to-record-low-as-ai-reshapes-entry-level-employment-market-5127639.html
- techUK on entry-level jobs: https://www.techuk.org/insights/news/what-s-actually-happening-with-entry-level-and-graduate-jobs
- Employers cutting entry-level roles: https://www.globalbankingandfinance.com/one-three-uk-employers-cut-entry-level-jobs-survey-shows/
- Coventry et al. 2021: https://eprints.whiterose.ac.uk/id/eprint/178622
- Natural England NECR204 coverage: https://farminguk.com/news/connecting-with-nature-offers-a-new-approach-to-mental-health-care_38603.html
- NECR228: https://publications.naturalengland.org.uk/file/5863897012109312
- Green social prescribing evaluation: https://arc-yh.nihr.ac.uk/new-findings-green-social-prescribing-for-adults-with-mental-health-problems
- Social Prescribing Academy results: https://socialprescribingacademy.org.uk/what-is-social-prescribing/natural-environment/green-toolkit/
- Pick for Britain: https://www.farminguk.com/news/uk-residents-made-up-just-11-of-harvest-2020-workforce_56861.html ; https://www.aljazeera.com/features/2020/11/19/pick-for-britain-a-rather-fruitless
- Farm Safety Foundation: https://www.farmersguardian.com/news/4409724/mental-health-steadily-decreasing-farmers
- Robotics: https://www.futurefarming.com/crop-solutions/strawberry-picking-robot-dogtooth-ready-for-practical-use/ ; https://www.essex.ac.uk/news/2025/07/02/trial-begins-on-next-generation-of-strawberry-picking-robots
- Organic labour: https://orgprints.org/10178 ; https://www.soilassociation.org/media/4946/policy_report_2006_organic_works.pdf
- Nature skills gap: https://www.countryside-jobs.com/article/the-nature-skills-gap ; https://www.groundwork.org.uk/environmental-employer-resource-hub/
- CCC long-run outcomes: https://www.nber.org/papers/w27103


---

<a id="note-05"></a>

## 05 · Geopolitics, prices, social unrest and cultural change

Tags: `research:international-comparison`, `research:diets-livestock-externalities` and the new themes "geopolitical stability", "social unrest" and "cultural change".
Gap addressed: the briefings name the Hormuz shock but do not connect geopolitics, prices, household access and social stability, and none treats diet as culture.
Status: web-search research, 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**2026 has been a double external shock, and so far UK shop prices have absorbed it.** The Strait of Hormuz has been disrupted since late February 2026, and Black Sea grain exports have been hammered since July. Global food prices are at their highest since November 2022. Yet UK food inflation in August 2026 was only **1.3%**. The danger is *lagged*: the fertiliser shock hits *next* season's yields and costs, and the drought-hit 2026 harvest raises import needs. The social risk in the UK is not famine but **affordability**. Food insecurity is already rising (12.2% of households) while headline food inflation is low.

### 2. Geopolitical shocks in 2026

| Shock | What happened | Source |
|---|---|---|
| **Strait of Hormuz** (Iran war, from Feb 2026) | Tanker traffic fell >90% within days. The strait normally carries ~20% of LNG and **up to 30% of traded fertilisers**. Urea went from ~$400/t to **>$850/t in April**, then eased to $453 in June; potash barely moved. FAO projected fertiliser prices 15–20% higher in H1 2026. IFPRI: input costs rose but crop prices did not, so farmers face an "affordability crisis" and a risk of using less fertiliser and getting lower yields in the autumn 2026 sowings. | [P] FAO, WTO, IFPRI |
| **Black Sea** (escalation from Jul 2026) | Strikes on Odesa ports removed ~⅓ of Ukraine's grain export capacity. Ukraine's 2026/27 wheat exports forecast at **8.3 Mt, −53%**. Novorossiysk terminals suspended after drone attacks; the Kerch/Azov route carries ~28% of Russian wheat exports. Russia and Ukraine supply ~30% of world wheat exports. Wheat hit a two-year high in late July. | [S] S&P Global, Reuters-based reports |
| **FAO Food Price Index, Sep 2026** | **136.0**, highest since Nov 2022; cereals +17% y/y, vegetable oils +18% y/y; still ~15% below the March 2022 peak | [P] FAO via press |

**UK exposure:** the UK imports little Black Sea grain directly. The exposure comes through world prices, feed costs and fertiliser. The UK's tradable surplus in good years (barley, oats) is small, and the 2026 harvest was a record low (dossier). Gas-to-nitrogen is the deepest link: Hormuz carries LNG *and* fertiliser.

### 3. UK prices and access

| Item | Figure | Source |
|---|---|---|
| CPI, Aug 2026 | 3.1% headline; **food 1.3%**, its smallest contribution since Sep 2021 | [S] ONS via Trading Economics |
| Outlook | Bank of England expects food inflation at **3.5% by Dec 2026** | [S] |
| Spring 2026 warnings | FDF said food inflation "at least 9%" by year end; IGD worst case >8% by June 2026, baseline 3.8% | [S] These **have not happened so far** (see note below) |
| Household food insecurity | **12.2%** of households (6.5 m adults, 2.2 m children), up from 11.3% a year earlier; 35.9% of Universal Credit households; 27.1% of single parents | [P] Food Foundation tracker, Jul 2026 |
| Public concern | 60% "highly concerned" about food prices in Feb 2026, the highest since tracking began in 2023 | [P] Food Foundation |

**Correction for the existing Claude briefing:** its line that "the food industry warns it could reach 9% again this year" was a fair report in spring, but it is now overtaken. Food inflation ran at ~1–2% through the summer. Update it, or reframe it as "the price shock is still in the pipeline".

### 4. Social unrest: what the evidence says

| Evidence | Finding | Caveat |
|---|---|---|
| Lagi, Bertrand & Bar-Yam (2011, NECSI) | Food riots worldwide (2008, 2011) clustered when the FAO Food Price Index was above ~210 | Correlation in mostly low-income, food-importing countries. **The FAO index was rebased in 2020 (2014–16 = 100), so "210" cannot be compared with today's 136.** Not a UK model. |
| York / Anglia Ruskin (2023, and 2026 in *Sustainability*) | Expert scenario work: a major conflict could drive energy and food prices up, hit low-income households, erode trust and, in the worst case, lead to unrest. Wheat, bread, pasta and cereal shortages are the most likely triggers. | Scenario and expert elicitation, not a forecast. The often-quoted "80% of experts say food violence is possible within 50 years" comes from a poor-quality aggregator [?]. |
| UK precedent: fuel protests, Sep 2000 | Blockades stopped ~3,000 daily fuel deliveries; ~90% of filling stations ran dry; **Sainsbury's warned it would run out of food "within days"; Safeway rationed bread and milk**; government took emergency fuel powers | Best UK evidence that *logistics* fails before *farms* do |
| UK precedent: 2021–23 | CO₂ crisis, HGV driver shortage, salad-veg rationing (Feb 2023): shortages showed up as empty shelves and rationing, not unrest | Disruption was absorbed |

**Read:** in a rich country, unrest risk runs through *affordability, perceived unfairness and logistics breakdowns* (panic buying), not through absolute calorie shortage. That argues for (a) income protection for the bottom fifth, (b) visible, fair rationing rules prepared in advance, (c) local stocks and communications. The NAO's call to "engage households and communities" is the unrest-prevention lever.

### 5. Cultural change: diets are already moving

| Trend | Evidence | Source |
|---|---|---|
| Meat intake falling slowly | Average daily meat intake fell from 103.7 g to 86.3 g per person (2008–2019), −17%. Red meat −13.7 g, processed −7 g, white meat +3.2 g. Well short of the National Food Strategy's 30% target. | [P] Oxford, *Lancet Planetary Health* |
| How it is falling | Smaller portions explain 52% of the decline, ahead of meat-free days | [S] Feb 2025 analysis |
| Record low | 854 g meat per person per week in 2022, the lowest since records began in 1974, partly due to cost of living | [S] citing Defra Family Food |
| Supply-side caution | Correcting for a FAO method change turns a "−5.2% meat supply 2008–18" finding into **+4.9%** | [P] Edinburgh thesis. The trend depends on the dataset. |
| Ultra-processed meat substitutes stalling | UK plant-based retail £848 m in 2025 (−1.2%); plant-based *meat* volume **−9.4%**; Tesco dropped its 300% meat-alternatives target; tofu's share rose from 8.3% to 10.8% | [P] GFI Europe/Circana |
| Seafood culture | The UK prefers imported cod and haddock; "fall out of love with flaky white fish" (see note 02) | [P] |

**Read:** British diets are shifting by *eating less meat* and *eating more whole plant foods*, not by switching to processed substitutes. That favours the project's direction (pulses, oats, field veg, mackerel) and argues against relying on precision-fermentation "meat" as the cultural vehicle. "Less but better", smaller portions and good recipes are going *with* the grain of current behaviour.

### 6. Points for the PDF
- Geopolitics page: "Two chokepoints in one year. Hormuz carries a fifth of the world's LNG and up to 30% of its fertiliser trade; the Black Sea carries 30% of its wheat exports. Britain buys neither directly, and pays for both."
- Unrest page: "Britain's food risk is not hunger, it is fairness. One household in eight is already food-insecure while food inflation runs at 1%."
- Culture page: "The diet is already changing: meat −17% in a decade, by smaller portions, not fake burgers."

### 7. Still missing
- ONS food inflation for September 2026 (released mid-October; not found).
- Whether Hormuz is open as of October 2026.
- UK-specific polling on willingness to accept rationing or diet change in a crisis.

### Sources
- FAO, Hormuz warning: https://www.fao.org/newsroom/detail/fao-chief-economist-warns-of-severe-global-food-security-risks-from-disruption-to-strait-of-hormuz-trade-corridor/en
- WTO data blog, Jul 2026: https://www.wto.org/english/blogs_e/data_blog_e/blog_dta_10jul26_451_e.htm
- IFPRI, Iran war fertiliser to food crisis: https://www.ifpri.org/blog/iran-war-from-fertilizer-to-food-crisis/
- Oxford Agile Initiative on UK fertiliser: https://www.agile-initiative.ox.ac.uk/news/strait-of-hormuz-disruption-exposes-the-uks-fertiliser-vulnerability/
- S&P Global, Black Sea factbox: https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/082026-factbox-black-sea-grain-trade-strained-by-escalating-russia-ukraine-conflict
- Poultry Site, Ukraine exports at risk: https://www.thepoultrysite.com/news/2026/06/russian-strikes-threaten-to-cut-ukraine-grain-exports-by-a-third
- FAO FFPI Sep 2026: https://fastmarkets.com/insights/fao-food-price-index-rises-in-september-on-higher-cereal-vegoil-prices-and-benchmark-at-highest-since-november-2022
- UK CPI Aug 2026: https://tradingeconomics.com/united-kingdom/inflation-cpi/news/584098
- Food Foundation, Jul 2026: https://foodfoundation.org.uk/news/food-prices-tracker-july-2026
- Food Foundation, Feb 2026: https://foodfoundation.org.uk/news/food-prices-tracker-february-2026
- IGD forecast: https://www.retailgazette.co.uk/blog/2026/03/middle-east-conflict-risks-pushing-uk-food-inflation-above-8-warns-igd/
- Lagi et al. 2011: https://arxiv.org/pdf/1108.2455
- York/ARU 2026: https://cieh.org/ehn/food-safety-integrity/2026/march/study-shows-uk-is-vulnerable-to-future-food-crisis/
- York 2023: https://www.york.ac.uk/news-and-events/news/2023/research/risk-civil-unrest-food-shortages/
- 2000 fuel protests: https://www.pressandjournal.co.uk/fp/past-times/4057166/fuel-price-rises/ ; https://www.cnn.com/TRANSCRIPTS/0009/13/ee.10.html
- Oxford meat intake study: https://www.oxfordmartin.ox.ac.uk/news/reduction-in-uk-red-and-processed-meat-intake-but-more-needed-to-meet-our-climate-targets
- Smaller portions: https://www.thecattlesite.com/articles/smaller-portions-drive-fall-in-meat-consumption
- GFI Europe UK plant-based 2024–25: https://gfieurope.org/wp-content/uploads/2026/06/GFI-Europe_UK-plant-based-food-retail-market-insights-2024-2025.pdf
- Edinburgh thesis: https://era.ed.ac.uk/handle/1842/44519


---

<a id="note-06"></a>

## 06 · Food tech, energy and a power-cut stress test

Tags: `research:food-tech-energy`, `research:horticulture`
Gaps addressed: "Food-tech / alternative proteins" (energy intensity, scale-up, whether it *relocates* the soya and nitrogen problem) and "Energy system integration" (no single energy–food stress test).
Status: web-search research, 22 Oct 2026. Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**Food tech mostly moves the dependency; it rarely removes it.** Precision fermentation swaps land and soya for electricity, sugar and *ammonia*, so it re-enters the nitrogen fracture. Vertical farms swap sunlight for grid power, and UK operators have gone bust on energy costs. The technologies that genuinely *reduce* dependency are the boring ones: gene editing for disease resistance (less pesticide, fewer lost harvests), waste heat for glasshouses, and backup power for the cold chain. **The single most important energy fact is that food is now an electricity system**: over half of UK food is chilled or frozen, payments and ordering are digital, and grain needs drying. A long power cut breaks food faster than a bad harvest does.

### 2. Precision fermentation and alternative proteins

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

### 3. Vertical farming

| Item | Evidence |
|---|---|
| Jones Food Company (Ocado ~70%) | The UK's largest vertical farm operator entered **administration in April 2025**; 61 jobs lost; never profitable; ~£22m owed [S] |
| Infarm | Collapsed on energy costs and capital intensity; assets sold to a new entity for ~€40m [S] |
| Others | Vertical Futures (administration, >£10m losses in 2024), GrowUp Farms (pre-pack rescue), Upward Farms and Agricool [S] |

**Read:** vertical farms grow leafy greens and herbs, crops with almost no calories, using electric light. They are not a staple-security technology. Gemini's claim that they act as "grid stabilisers" is theoretical; no UK operator survived long enough to show it.

### 4. Glasshouses and waste heat (the useful middle)
- Tomato self-sufficiency is 17% and fresh fruit 14% (dossier). Glass needs affordable winter heat.
- UK projects: Humber Tech Park (N. Lincs) plans a **27,000 m² tomato glasshouse on data-centre waste heat** (~£3.5m/yr sales) [S, status ?]. Low Carbon Farming plans **41 glasshouse sites on waste heat** from wastewater and recycling sites [S, paywalled].
- Netherlands: Aalsmeer growers are switching from gas to data-centre heat networks [S].
- **Read:** the UK's data-centre build-out (AI) creates a large low-grade heat stream. Pairing new data centres with glasshouses is a concrete win across AI, energy and food, and fits the project's AI theme. Planning policy could *require* heat-use plans for large data centres.

### 5. Gene editing
- **The Genetic Technology (Precision Breeding) Regulations 2025 took effect on 13 Nov 2025** (England, plants only; animals deferred) [P via law-firm summaries].
- Pipeline: disease-resistant beet and potato (fewer fungicides), climate-resilient tomato, methane-reducing barley [S NIAB].
- [?] Whether any precision-bred variety is on the National List yet; one commentary says farmers cannot grow them until it is.
- **Read:** this is the most *resilience-relevant* biotech, because it cuts pesticide dependence (largely imported) and protects yields in wet years (blight). It does not fix nitrogen. Scotland and Wales have not adopted the regime: a devolution friction point (see note 08).

### 6. Energy dependencies in the food system

| Dependency | Figure | Source |
|---|---|---|
| Farm diesel | 98% of English farms use red diesel (2023/24). Implied UK farm volume ≈ **0.9 bn litres/yr** from the £384m rebate value at the 42.8p/L duty gap [E] | [P] Defra energy-use survey; [E] |
| Diesel price 2026 | 123.7p/L in April 2026, +79% on the 2025 average (69p); ECIU estimates **£337m extra** farm fuel cost this year | [S] EDM citing ECIU |
| Chilled and frozen share | >50% of UK food consumed | [S] Cold Chain Federation |
| CO₂ and nitrogen | Both tied to gas prices (note 01) | |

### 7. Stress test: a 7-day national power loss (structural reading, not a model)

Precedents: the **Iberian blackout of 28 April 2025** hit ~50–60 m people for 10–24 hours. Card payments failed, warehouse management systems stopped, refrigeration failed, and gas plants led the restoration [S]. The National Risk Register lists national power outage as a catastrophic-impact risk (dossier). The UK fuel protests of 2000 showed shelves emptying within days once deliveries stopped (note 05).

| Hours / days | What breaks first | Why |
|---|---|---|
| 0–6 h | Payments, ordering IT, store tills, traffic lights, fuel pumps | Everything electronic; few stores can trade for cash at scale |
| 6–24 h | Chilled retail stock, home fridges; milking parlours and dairy cooling (farms with generators continue) | No cooling; milk must be cooled or dumped |
| 1–3 days | Distribution centres on generator fuel only; water pumping and treatment pressure (water companies hold generators for key sites) | Generator autonomy unknown (data gap, note 01); diesel resupply needs working pumps |
| 3–7 days | Frozen stock at risk; poultry and pig units (ventilation, feed systems) at welfare crisis; bakeries and mills stop; dry goods and household cupboards become the food supply | The **household 72-hour kit** and dry stocks matter here |
| Recovery | Restart needs coordinated power, fuel and IT; spoiled chilled stock must be replaced through a supply chain that is itself restarting | |

**Implications:** (a) backup-power autonomy standards for food distribution and cold stores, plus a priority list for fuel; (b) cash and offline payment fallbacks; (c) household 72-hour guidance (the government's 2025 Resilience Action Plan and its preparedness website already push this); (d) dry staples (grain, pulses, oats) are the *power-independent* reserve. This strengthens the case for a grain and pulse reserve over a chilled or frozen one.

### 8. PDF lines
- "A fermenter needs sugar, power and ammonia. We import two of those."
- "Vertical farms grew lettuce and went bust. Data-centre heat can grow tomatoes."
- "Food is an electricity system now. Half of what we eat is chilled or frozen."

### Sources
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


---

<a id="note-07"></a>

## 07 · Climate, pests and correlated failure

Tag: `research:climate`
Gap addressed: "quantified yield sensitivity to consecutive wet autumns / dry summers, new pest and disease pressure, and correlated failure risk across eastern arable counties" (and, it turns out, across Europe).
Status: web-search research, 22 Oct 2026. Builds on dossier Part 6 (climate raw sources). Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**Single bad-weather events are absorbed; *combinations* within one season and *correlation* across Europe are the real risk.** UK wheat copes well with one extreme (a wet spell, a hot week). It fails when extremes stack across growth stages: a wet autumn that stops drilling, then a dry spring, then a wet harvest (2020). In 2026 the drought hit the UK, France, southern Germany, Italy and Hungary at the same time. So the "trade is insurance" argument is weakest in exactly the years we need it, because our nearest suppliers fail together with us.

### 2. Yield sensitivity: evidence

| Evidence | Finding | Source |
|---|---|---|
| Slater et al. 2022, *Earth System Dynamics* 13:1377 (Oxford, UKCEH, Met Office, Bristol) | UK wheat yields since 1990 show "substantial resilience" to **single** extremes. **Significant losses come from combinations of extremes within a season**: 2020 had a wet autumn, a dry spring and August downpours. To 2080 (high emissions, E & S Britain), warmer winters may offset wetter Oct–Apr, and warmer, drier June–July could *help* yields. | [P] |
| NERC/NORA paper (UKCP Local 2.2 km) | **Wheat yield volatility has increased significantly** in recent years, only partly explained by seasonal temperature and rainfall. Impacts strongest with **compound extremes across multiple growth stages** (e.g. frost plus heavy rain). The autumn-to-spring "foundation stage" is projected warmer and wetter. | [P] authors to confirm |
| Harvest record (dossier) | Four of the five worst harvests on record fall in this decade: 2020, 2024, 2025 and 2026. 2026 winter wheat 6.9 t/ha (−11% vs 5-yr average), spring barley −17%; key crops forecast at 18.5 Mt, a record low | [P/S] AHDB, ECIU |

**Interpretation:** the Slater projection that *mean* yields might hold up is not reassuring for food security, because resilience is about the *bad tail* (rising volatility, compound events), not the average. Recent experience (2020, 2024 wet; 2025, 2026 dry) is a run of opposite extremes within six years: a farm can be flooded and droughted inside the same 18 months.

### 3. Correlated failure across Europe in 2026

| Country | 2026 impact | Source |
|---|---|---|
| France | Cereal output ~**−8 Mt** vs 2025; grain maize ~−35%, a four-decade low | [S] European Commission via Carbon Brief |
| Germany | Possible total crop losses in some southern regions; grain shortfall up to ~3 Mt (~€600m) | [S] DBV/Raiffeisen |
| EU total | Soft wheat yields −7% vs 2025 (JRC MARS); EU wheat 133.8 Mt (USDA FAS). Lower planted area because of input costs **plus** adverse weather | [S] |
| Hungary | Worst drought since 1991 | [S] |
| UK | Wheat, barley and oat yields all down (see above) | [P] AHDB |

**Read [E]:** for the UK, "diverse imports" in practice means mainly France, Germany, the Baltic and Black Sea, and North America. In 2026 the first two failed alongside the UK, the Black Sea was under attack (note 05) and North America was dry. That is a *correlated* shock: different causes in the same season. A reserve is the hedge against correlation that trade cannot provide.

### 4. Pests and diseases

| Threat | Status | Source |
|---|---|---|
| Warming as the driver | 2025 was the UK's **warmest year on record** (since 1884). Pests that once could not survive here are establishing. The Met Office and Defra "UK Climate-Pest Risk" tool covers 9 insect pests (e.g. Colorado potato beetle, peach potato aphid). | [P] Met Office, Feb 2026 |
| Colorado potato beetle | Targeted eradication in Kent in 2025; rated high unmitigated risk in the Defra Plant Health Risk Register | [P/S] |
| Wheat stem rust | **Re-emerging in the UK and Ireland**; a major cereal threat absent for decades | [S] EPPO-hosted study |
| Bluetongue BTV-3 (livestock) | 160 cases in England (Aug 2024–May 2025); new season from 11 Jul 2025; cases through winter 2025/26 in Kent, Cheshire, Staffs, Derbyshire, Lancs, Cornwall, Devon and Powys; 31 new cases on one day (6 Aug 2026) | [P] GOV.UK bluetongue page. The season totals in one page version look garbled [?] |
| Ash dieback, Phytophthora, spruce bark beetle | Forestry (dossier) | |

**Read:** a vector-borne livestock disease spreading across England through *winter* is a direct climate signal, since midges are active longer. Pest pressure feeds back into input dependence: more pests mean more (imported) pesticide, unless there is resistant breeding (gene editing, note 06) and integrated pest management.

### 5. Flood and peat exposure (from the briefings, for completeness)
- 59.2% of Grade 1 land lies in river or sea flood-risk areas; ~1.12 Mha (13%) of English farmland sits in mapped flood zones (EA, Oct 2026, via the Grok briefing) [P, not re-verified].
- Fen peat loses 1–2+ cm a year; 25–50 years left under arable (dossier) [S].

### 6. What remains to model
- The probability of 2 consecutive bad UK harvests (the GPT stress test) needs a crop-model ensemble. A rough empirical proxy: 4 of the last 7 harvests (2020–26) were among the 5 worst on record [E, from dossier].
- Correlation coefficients between UK, French and German wheat yield anomalies: a doable data exercise with FAOSTAT or Eurostat. Not done here.

### 7. PDF lines
- "One bad week doesn't hurt British wheat. A bad autumn, then a bad spring, then a wet harvest does, and that is the pattern now."
- "In 2026 Britain, France and Germany lost their harvests together. Trade is insurance until your neighbours make the same claim."

### Sources
- Slater et al. 2022, ESD: https://esd.copernicus.org/articles/13/1377/2022/
- PreventionWeb summary: https://www.preventionweb.net/news/climate-change-testing-resilience-uk-wheat-yields
- NERC/NORA wheat volatility paper: https://nora.nerc.ac.uk/id/eprint/533430/1/N533430JA.pdf
- Carbon Brief on Europe's 2026 crops: https://carbonbrief.org/how-this-summers-heat-and-drought-impacted-crops-in-europe-in-six-charts
- MARS 2026 forecast cut: https://ukragroconsult.com/en/news/mars-lowers-harvest-forecasts-for-all-crops-in-the-eu-for-2026/
- World Grain on EU crops: https://www.world-grain.com/articles/23056-weather-input-costs-wreak-havoc-on-eu-crops
- German drought losses: https://cambodianess.com/article/german-farmers-warn-drought-will-spell-heavy-crop-losses
- Met Office pest risk, 2026: https://www.metoffice.gov.uk/about-us/news-and-media/media-centre/weather-and-climate-news/2026/met-office-science-helps-protect-uk-plants-from-rising-pest-risks
- Pest risk study (EPPO platform): https://pra.eppo.int/pra/c1804e50-2029-488f-b92f-d38429142e81
- Bluetongue latest situation: https://gov.uk/bluetongue


---

<a id="note-08"></a>

## 08 · Devolved policy, support schemes and tax

Tags: `research:subsidies-tax-incentives`, `research:governance-policy`
Gap addressed: "Devolved policy and implementation feasibility": support differs across the four nations, and no briefing tests how schemes change farm decisions. Also corrects outdated figures.
Status: web-search research, 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**Four nations, four schemes, and none of them pays for food *resilience* as such.** England's new **Farming Roadmap 2050** (24 June 2026) does put food production first in principle, but its main money flows through SFI26: a capped, oversubscribed, mostly environmental scheme. Wales pays a flat "social value" rate per hectare; Northern Ireland pays an area-based safety net with soil and carbon conditions; Scotland is mid-transition. None has a stockholding, storage or "resilience action" payment. The inheritance tax change has calmed rather than crashed land markets.

### 2. England

| Item | Detail | Source |
|---|---|---|
| **Farming Roadmap 2050: Growing England's Future** (24 Jun 2026) | "Primary purpose of the farming system is to produce food", profitably. Four pillars: profitable, productive, sustainable, resilient. Draws on the Batters Farming Profitability Review (government accepted 53 of 57 recommendations). No numeric production targets seen [?]. **ELM spending rises from £1.8bn (2025/26) to >£2bn by 2028/29.** | [S] Food Manufacture, FWI, RICS, TFA, Sustain |
| **SFI26** | Actions cut from 102 to 71; mostly 3-year; **cap £100k per business per year**; min 3 ha; **£240m for new agreements** (Window 1 up to £60m, opened 30 Jun 2026, small farms or no existing ELM; Window 2 base £180m, opened Sep 2026); ~£560m already committed to live agreements; **25% cap on actions that take land out of production**; management payment removed; herbal leys cut from £382 to £224/ha | [S] Andersons, NFU, FWI, Farmers Guardian |
| Window 2 closure | Closed within hours on 22 Sep 2026 (dossier: ~£253m) | [S] [?] £180m base + Window 1 rollover may explain the £253m |
| Precision breeding | Regulations in force 13 Nov 2025, England only (note 06) | [P] |

**Feasibility reading:** the 25% cap on land-out-of-production options is effectively a food-security guardrail. But a first-come-first-served window that closes in hours rewards farms with agents and paperwork capacity, not the farms whose resilience matters most. The herbal-ley rate cut works *against* the clover and legume fertility building the resilience case relies on (note 03): a concrete perverse signal.

### 3. Wales: Sustainable Farming Scheme (from 1 Jan 2026)

| Item | Detail |
|---|---|
| Structure | 12 Universal Actions (e.g. soil health plan), then Optional and Collaborative layers; carbon baseline in year 2 |
| Trees | The contested **10% tree-cover rule was dropped**; farms instead plan to raise cover towards a national aim of 17,000 ha new woodland by 2030 |
| 2026 rates | Whole-farm £70/ha on the first 70 ha (£2/ha after); **Social Value Payment £107/ha**; habitat maintenance £69/ha; woodland maintenance £62/ha; £1,000 one-off stability payment for joiners ≤100 ha |
| Capping | Taper from £25k; nothing above £300k |
| BPS exit | Non-joiners lose 40% in 2026, then 20% a year |

[S] FWI, Andersons, Brown & Co. [?] Uptake in 2026 not found.

### 4. Northern Ireland: Sustainable Agriculture Programme (from Jan 2026)
- **Farm Sustainability Payment**, an area-based safety net replacing BPS after a 2025 transition payment. Progressive capping above £60k (half-rate in 2026, full from 2027; maximum ≈ £79,600).
- Conditions: the Soil Nutrient Health Scheme, carbon benchmarking, a bovine genetics programme, and new farm sustainability standards replacing cross-compliance. [P] DAERA
- [?] Per-hectare FSP rate not found.

### 5. Scotland
- Agriculture and Rural Communities (Scotland) Act 2024 creates a four-tier framework (base, enhanced, elective, complementary). **Details of the 2026 tiers were not found in this session** [?]. Scotland has *not* adopted England's precision-breeding regime.
- Scotland has the most woodland (19%) and holds most of the UK's salmon farming and seed-potato strength (notes 02, 07).

### 6. Tax

| Item | Detail | Source |
|---|---|---|
| APR/BPR from 6 Apr 2026 | 100% relief on the first **£2.5m** per person (transferable, so ~£5m per couple); 50% relief above (an effective 20% IHT). Estates affected in 2026/27 halve from 375 to 185 under the revised plan. | [P] HMRC/Treasury via law firms |
| Land market | Bare land values roughly **flat in Q4 2025**, down just over 5% over 2025; ~£8,700/acre average (England & Wales); the U-turn "calmed" the market | [S] Knight Frank via FarmingUK |
| Red diesel | Duty 10.18p/L, cut to 6.48p from 15 Jun to end-2026; rebate worth ~£384m (2025); farm diesel price 123.7p/L (Apr 2026), +79% y/y | [P/S] dossier, EDM |

**Correction for the briefings:** the "old £1m" cap is outdated (the GPT notes already say so). The £2.5m figure is right, and the *land price* effect has been modest so far. Avoid claims that IHT reform is "pricing out" or "flooding" the market without 2026 evidence.

### 7. The resilience gap across all four nations [E]
None of the schemes pays for:
1. holding grain, seed or fertiliser stock on farm through the pre-harvest low (note 01);
2. on-farm winter water storage at scale (England has capital grants; no resilience-tier revenue payment);
3. keeping a protein crop (beans, peas) in rotation *for* feed-soya replacement. SFI has legume options, but they are being cut back;
4. backup power for livestock units and grain drying.

**Proposal for the PDF:** a UK-wide "Resilience Tier" (the Claude briefing's move 6), funded across the four nations, paying for these four things on multi-year contracts and not through first-come-first-served windows. Devolution means it needs a common framework, as the UK Internal Market and Common Frameworks process allows, not a single scheme.

### Sources
- Farming Roadmap 2050: https://www.foodmanufacture.co.uk/Article/2026/07/03/farming-roadmap-2050-defra-unveils-plans-to-boost-english-farming/ ; https://ww3.rics.org/uk/en/journals/land-journal/farming-roadmap-2050-defra-england.html ; https://tfa.org.uk/tfa-news/tfa-blog-355-farming-roadmap-2050-clarity-at-last-delivery-must-follow/ ; https://www.sustainweb.org/news/jun26-defra-farming-roadmap/
- SFI26: https://theandersonscentre.co.uk/sfi-update-feb-2026/ ; https://www.fwi.co.uk/business/payments-schemes/analysis-what-sfi26-means-for-farm-businesses ; https://www.farmersguardian.com/news/4531034/sfi-2026
- Wales SFS: https://www.fwi.co.uk/business/payments-schemes/welsh-sustainable-farming-scheme-all-you-need-to-know ; https://theandersonscentre.co.uk/sustainable-farming-scheme-wales2/
- NI FSP capping: https://www.daera-ni.gov.uk/news/farm-sustainability-payment-progressive-capping-payments
- IHT £2.5m: https://www.saffery.com/insights/news/planned-cap-on-apr-and-bpr-inheritance-tax-reliefs-raised-to-2-5m/
- Land market: https://www.farminguk.com/news/iht-rethink-calms-farmland-market-after-year-of-uncertainty_67816.html
- Red diesel EDM: https://edm.parliament.uk/early-day-motion/65676


---

<a id="note-09"></a>

## 09 · Diet shift, feed–food mass balance and waste

Tags: `research:calories-protein`, `research:diets-livestock-externalities`, `research:scale-up-emergency`
Gap addressed: "Diet-shift mass balance and waste": no briefing runs a monthly feed/food/waste balance, and "less but better meat" stays qualitative. This note adds a **first-cut monthly cereal model** (`research/model/cereal_balance.py`) and pulls together the dossier's Part 3 arithmetic.
Status: 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate or model, [?] unresolved.

---

### 1. Headline finding

**Grain is not the binding constraint in an import shock; protein feed, fats and next year's fertiliser are.** In the model, if imports stop on 1 July, the UK's own cereals cover food milling *and* today's full livestock feed for two years, **provided bioethanol and distilling grain use is cut and exports stop**. Without that policy response, cereal stocks run out within 12 months. Two poor harvests in a row (−15% each) need feed cut by about a fifth; a ~30-day reserve (1.5 Mt) reduces that cut. The problem is that pigs and poultry cannot run on grain alone: they need the ~2.3–2.5 Mt of imported soya meal. So the *monogastric herd contracts because of protein, not energy*. That is the "less meat" mechanism, and it would happen whether or not policy chooses it.

### 2. Model: monthly pooled cereal stock (wheat + barley + oats) [E]

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

### 3. The protein and nutrient side (from dossier Part 3, not yet re-verified)

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

### 4. Waste: the fastest lever

| Item | Figure | Source |
|---|---|---|
| Total UK food waste | 10.7 Mt (2021; total including households, hospitality, retail and manufacture), carrying ~18 MtCO₂e | [P] UKFSR via Grok briefing |
| Households | 6.4 Mt (2021) total; **4.4–4.5 Mt edible** (WRAP; ~£14bn/yr) | [P] WRAP |
| Trend | Food waste per person −7% over three years (WRAP C2025 milestone, 2018 data) | [P] |

[E] At 1,000–1,500 kcal/kg, 4.4 Mt of edible household waste ≈ **28–42 days of national energy need per year**. Halving it ≈ 2–3 weeks a year, without new land, fertiliser or ships. In a crisis, waste falls naturally (higher prices, rationing): WWII households wasted little. This is "the reserve already in our bins".

### 5. "Less but better" made concrete

A quantitative version of the briefings' qualitative position:
1. **Monogastrics (pigs, poultry, eggs)** are sized by the *domestic protein supply*: home-grown beans, peas, rapeseed meal and distillers' grains. Model this as a pulse-area target: replacing 1.1 Mt of soya protein needs ~4 Mt of field beans at ~27% protein, roughly 1 Mha at ~4 t/ha [E]. That is about **6× today's pulse area (0.68 Mt production)** and bumps into the one-in-five-to-six-year rotation limit (GPT notes). A realistic target is perhaps a third of soya replaced within a decade.
2. **Ruminants on grass** stay; their constraint is methane and land-sparing for trees on grade 4–5 land, not food security.
3. **Diets already moving:** meat −17% per person 2008–2019, driven by smaller portions (note 05). A crisis plan works *with* that trend.

### 6. Still missing (next modelling steps)
- Add a protein ledger (soya, rapeseed meal, beans, peas) and herd response to the model.
- Add milling and dehulling capacity as a monthly ceiling.
- Use AHDB's grade split (milling vs feed wheat) and the barley and oat closing stocks from the September 2026 final balance.
- Add oils (rapeseed 49% self-sufficiency) and a micronutrient check.

### Sources
- Model: `research/model/cereal_balance.py` (this repo)
- AHDB end-of-season balance, Sep 2026: https://ahdb.org.uk/end-of-season-uk-cereal-supply-and-demand-september-2026
- WRAP household waste: https://wrap.ngo/resources/report/courtauld-2025-baseline-and-restated-household-food-waste-figures ; https://www.circularonline.co.uk/news/food-waste-falls-by-7-per-person-in-three-years/
- Dossier Part 3 (calories, protein and feed) and its cited sources: Defra UKFSR 2024; FAO food balance sheets; SFT; Wilkinson 2011


---

<a id="note-10"></a>

## 10 · Household equity and local response

Tags: `research:supply-chain-reserves`, `research:governance-policy` and the new theme "social resilience".
Gap addressed: "Household equity and local response": no community-level plans, and nobody has costed or designed an affordable mix of national stocks, regional hubs and household preparedness.
Status: web-search research, 22 Oct 2026. Labels: [P] primary, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**The weakest link is local, not national.** The NAO found that **most Local Resilience Forums (LRFs) do not plan specifically for food disruption**, that their capability is "insufficient", and that the last national food-disruption exercise (2023) exposed limitations. Meanwhile one household in eight is already food-insecure, and a third of Universal Credit households are. A 72-hour household-kit policy does not help households that cannot afford a full cupboard. A fair design needs three layers: national dry stocks, local food partnerships with a statutory role, and targeted support so that preparedness is not a luxury.

### 2. Evidence

| Item | Figure | Source |
|---|---|---|
| LRF capability | "Insufficient"; LRFs unclear what Defra expects; **most do not plan specifically for food supply disruption** | [P] NAO, Sep 2026 |
| National exercise | Last severe food-disruption exercise in **2023**; found limitations | [P] NAO |
| Powers | Defra lacks a power to **direct businesses** to take emergency action | [P] NAO |
| Household food insecurity | **12.2%** of households (Jul 2026); 16.7% of households with children; 35.9% of UC households; 27.1% of single parents; 19.2% with a disabled member | [P] Food Foundation |
| Food banks | Trussell: **2.6 m parcels in 2025** (−12% vs 2024); 2.9 m in Apr 2024–Mar 2025 (+51% on five years earlier) | [P] Trussell |
| Household preparedness | Prepare website launched 22 May 2024; government urges households to plan for **72 hours** without outside help; retailers warned against panic buying | [S] |
| Household stocks (UK Public Survey of Risk Perception, Resilience and Preparedness 2026, n = 10,791, fieldwork Feb–May 2026) | **60%** have three days of food needing no cooking (down from 66%); 85% have three days of cupboard food; **4%** have three days of bottled water (3 L/person/day); 13% feel largely or totally prepared, 50% slightly or not at all | [P] Cabinet Office/Defra (found in dossier Part 8) |
| Local food partnerships | Sustain's 2026 "civil food resilience" briefing: local food partnerships are the proven vehicle; asks for food in local risk registers and a remit for resilience bodies | [S] Sustain |
| Expert letter (Oct 2026) | Calls for storage at national, regional, local **and community** level | [S] |

### 3. Design: an affordable three-layer system [E, proposal]

| Layer | What | Rough scale and cost logic | Who |
|---|---|---|---|
| **National** | Dry staples (milling wheat, oats, pulses, oils, sugar), fortificants, CO₂, infant formula, seed and fertiliser; held as rotating commercial stock under contract (the Swiss model) | 1.5 Mt grain ≈ 30 days energy-equivalent; GPT scenario: ~£0.37bn commodity value for 30 days, plus storage at roughly £15/t/yr ≈ £20–25m/yr (dossier estimate) | Defra / Cabinet Office; a "power to direct" in legislation |
| **Regional / local** | Each LRF holds a food plan: mapped distribution centres, cold stores and their backup power, community kitchens, school and hospital kitchens as feeding hubs, priority fuel lists | Mostly planning time, not stock; exercise every 2 years | LRFs + local food partnerships + retailers |
| **Household** | 72-hour kit, with **targeted provision**: households on means-tested benefits get a one-off kit or voucher, and food banks hold a crisis buffer | Illustrative [E]: ~3 m low-income households × ~£40 kit ≈ **£120m one-off**; most households already have several days of dry food | DWP / councils / food banks |

**Why targeting matters:** in a price or supply shock, better-off households buy ahead and poorer households cannot. Panic buying is a distribution problem, and it falls hardest on those without spare cash, storage or a car. A universal "stock up" message without targeted help *widens* inequality and can trigger the shortages it is meant to prevent (2000 fuel protests, March 2020).

### 4. Links to the other themes
- **Unrest (note 05):** fairness and visible rules prevent disorder more than tonnage does.
- **Work (note 04):** community kitchens, local food partnerships and growing projects are where "meaningful nature work" and resilience meet at low cost. Green social prescribing already funds some of this activity.
- **Power cut (note 06):** schools, hospitals and community centres with generators are natural feeding points; map them now.

### 5. Still missing
- Any UK figure for household preparedness (how many have 3 days of food and water).
- A worked LRF food plan example (search found none).
- The cost of a statutory "power to direct" and the business compensation model.

### Sources
- NAO report and summary: https://www.nao.org.uk/wp-content/uploads/2026/09/Resilience-of-the-food-supply-chain-to-disruptions-summary.pdf ; https://www.foodmanufacture.co.uk/Article/2026/09/04/the-nao-has-warned-defra-over-its-lack-of-readiness-in-the-face-of-potential-food-supply-chain-disruption/ ; https://www.thegrocer.co.uk/news/defra-must-do-more-to-build-resilience-to-food-shocks-nao/723211.article
- Food Foundation, Jul 2026: https://foodfoundation.org.uk/news/food-prices-tracker-july-2026
- Trussell 2025: https://www.trussell.org.uk/news-and-research/news/food-banks-provide-over-2.6-million-food-parcels
- Prepare / 72-hour guidance: https://www.logisticsmanager.com/retailers-warn-against-panic-buying-as-government-advises-gathering-emergency-supplies
- Sustain, civil food resilience briefing 2026: https://www.sustainweb.org/assets/civil-food-resilience-sfp-briefing-2026-1782920860.pdf


---

<a id="note-11"></a>

## 11 · Food as the foundation of social stability

Tags: `research:governance-policy`, `research:supply-chain-reserves` and the themes "social unrest" and "food as essential resource and source of stability".
Builds on note 05 (prices and unrest) and goes deeper: the "meals from anarchy" idea, the cross-country evidence, historical cases, ports and strikes, and how states use food reserves for stability.
Status: web-search research, 22 Oct 2026. Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. "Every society is three meals away from revolution": what's true in it

**Origin.** The saying traces to US journalist **Alfred Henry Lewis**: "the last nine meals" between people and anarchy (New York Journal, 1896), and "there are only nine meals between mankind and anarchy" (*Cosmopolitan*, March 1906) [P, Quote Investigator]. It has been echoed by Trotsky, Heinlein and many others. In the UK it is often attributed to Lord Cameron of Dillington (then head of the Countryside Agency) in the 2000s [? not verified here]. The "three meals" version is a later, punchier variant with no clear source.

**Status:** a rhetorical device, not an empirical finding. Use it as an epigraph, not as evidence.

**What the evidence supports instead:**
1. **Rising food price *levels* are followed by more unrest.** Bellemare (2015, *American Journal of Agricultural Economics* 97(1):1–21), using monthly international data for 1990–2011 and natural disasters to separate cause from effect, finds food price increases lead to more social unrest; **volatility does not**, and may even reduce it [P].
2. **Riots clustered around global price peaks** (2008, 2011) in food-importing, low-income countries (Lagi, Bertrand & Bar-Yam 2011). That is correlation, and the threshold value does not transfer to today's rebased index (note 05) [P].
3. **Food is usually the spark, not the fuel.** Egypt 2011 analysts disagreed on how much weight bread carried compared with governance, land and unemployment [S]. Unrest follows when a price shock meets an existing grievance and a perceived injustice.
4. **Rich-country version:** disruption shows up first as **panic buying and empty shelves**, not riots. UK cases: the 2000 fuel blockades (Sainsbury's warned it would run out of food "within days"; Safeway rationed bread and milk), March 2020, and salad rationing in Feb 2023 (note 05). The UK's realistic failure mode is a **loss of trust**: visible unfairness in who gets food, plus logistics paralysis.

**A defensible headline for the PDF:** "Lewis said in 1906 that mankind is nine meals from anarchy. The modern evidence is less dramatic and more useful: it is rising prices, not empty fields, that break the peace. And people forgive scarcity sooner than unfairness."

### 2. Historical cases: food, legitimacy and the state

| Case | What happened | Lesson | Source |
|---|---|---|---|
| **Egypt, Jan 1977** | Sadat cut the bread subsidy under IMF and World Bank pressure; riots in nearly every major city; scores killed; **reversed within two days** | Bread prices are a legitimacy contract | [S] |
| **Egypt, 2008–2011** | The world's largest wheat importer; wheat +60% in a year before 2011; subsidy bill >$3bn/yr by 2010; subsidised flour leaked to the black market at 5× the price | Import dependence plus subsidy leakage is fragile | [S] |
| **Sri Lanka, 2021–22** | Overnight ban on synthetic fertiliser and pesticide (Apr 2021); rice output down ~20% in six months (some reports say far more); ~$450m of rice imported; tea losses; ban reversed Dec 2021; then economic collapse and mass protests in 2022 | **A cautionary tale for "biology instead of chemistry": transition must be phased, with organic supply and farmer training in place first.** The economic crisis had other causes too (debt, tourism, FX). | [S] opinion-heavy; Reuters timeline more reliable |
| **Japan, 2024–25** | Rice shortage; prices ~¥5,000 per 5 kg; stocks at a record low of 1.53 Mt; government released reserves but **only ~10% reached shops** at first; the farm minister resigned (May 2025) after saying he "never had to buy rice" | Having a reserve isn't enough: **release mechanics and political tone matter** | [S] AP |
| **UK, 1940–54 rationing** | Fair shares, the National Milk Scheme and school meals; infant mortality fell from 58 to 45 per 1,000 (1937→1944); children got taller and heavier; nutrition gaps between classes narrowed | Rationing, done fairly, *raised* public health and trust. Hard to separate from milk and school-meal schemes. | [S] working paper citing Ministry of Health 1946 |

### 3. Reserves as stability infrastructure, not just insurance

| Country | Model | Source |
|---|---|---|
| **Finland (NESA)** | Law requires ≥6 months of normal grain consumption; raised to **9 months** in 2023 (top-up 64% oats, 36% wheat). Explicitly "long-term preparedness, not a response to shortage". Households are told to keep 72-hour kits. | [P] NESA |
| **Switzerland** | Compulsory private stocks (wheat, rice, oils, sugar, fertiliser), funded by a small levy on imports (dossier) | [P] |
| **China** | Sinograin runs state reserves of grain, oils, meat and sugar. Claims of ~700 Mt stocks (≈1 year) are **unverified**; ~650 Mt is *storage capacity* | [S] [?] |
| **UK** | None. The WWII stockpile was wound down in the 1990s (expert letter, Oct 2026). Written answer, 31 Mar 2026: "no national food stockpiles or plans to create these". In the Lords on 15 Oct 2026, a peer said there are "virtually no strategic food reserves". | [P] Hansard |

**Reading [E]:** states that treat food as a **stability asset** (Finland, Switzerland, China, Japan) hold public or compulsory stocks and rehearse release. The UK treats food as a **market good** and relies on trade diversity. The 2026 combination of correlated harvests, Hormuz and the Black Sea (notes 05, 07) is the scenario where that bet looks weakest.

### 4. Ports, dockers and strikes

**What was found (22 Oct 2026):**
- **No UK dock strike ballot or notice for autumn 2026 was found.** All UK hits were the 2022 Felixstowe and Liverpool disputes.
- **30 October 2026:** dockworker unions at ~40 ports in France, Greece (Piraeus), the Basque Country, Italy, Turkey and Morocco have called an international day of strikes and protests against war and militarisation [S, In These Times, WFTU]. Earlier, on 6 Feb 2026, walkouts hit at least 21 Mediterranean ports over arms shipments [S, LSE blog].
- **UK precedent:** Felixstowe, which handles about 40% of UK container trade (verify), struck for 8 days in Aug 2022 and again in September; Liverpool struck in autumn 2022. Disruption was absorbed without food shortages, because most fresh food comes via the Short Straits RoRo ferries (Dover, Eurotunnel), not container ports.

**Reading:** a one-day Mediterranean action has negligible direct UK food impact. The UK's food logistics chokepoint is **Dover and Eurotunnel**: ~42% of dairy and egg imports and ~39% of meat (note 01). A French port or ferry strike, Channel weather, or a cyber attack on border systems would matter far more than a container-port strike. [?] **If you have a source for the strike you heard about, send it and I'll assess it specifically.**

### 5. The FOI request (WhatDoTheyKnow)
- "Strategic food reserves and compound risk", to **Defra**, filed **21 Oct 2026** by Mars Robertson. Its title references multiple breadbasket failure, El Niño, and Red Sea / Strait of Hormuz disruption. Status: awaiting response (statutory deadline 20 working days, so around **18 Nov 2026**) [S, via search; the page itself was blocked from this session].
- Likely answer, based on the record: Defra repeats "no national stockpiles"; may cite the sectoral risk register (the NAO notes Defra reports a top-10 risk list to the Cabinet Office); may withhold detail under the s.24 (national security) or s.35 (policy formulation) exemptions [E].
- **Use in the PDF:** a box saying "We asked Defra…", with the date and the answer once it arrives.

### 6. Synthesis: food as a source of stability [E]
1. **Food is the one essential that cannot wait.** Energy can be rationed by the hour and money can be printed, but hunger runs on days. That is the true kernel in "nine meals".
2. **Legitimacy runs through price and fairness.** The state that cut the bread subsidy (Egypt 1977) and the minister who never bought rice (Japan 2025) show the political cost; fair rationing (UK 1940s) shows the political dividend.
3. **Transition shocks are self-inflicted risks.** Sri Lanka shows that a sudden input ban destroys both food and trust. The UK's path from chemistry to biology must be phased and measured.
4. **A reserve is a social contract made visible.** Its value is partly calories and partly *confidence*: it prevents the panic buying that empties shelves in a rich country.

### Sources
- Quote origin: https://quoteinvestigator.com/2022/05/02/nine-meals/ ; https://barrypopik.com/blog/every_nation_is_about_nine_meals_away_from_a_revolution
- Bellemare 2015: https://ideas.repec.org/a/oup/ajagec/v97y2015i1p1-21..html
- Lagi et al.: https://arxiv.org/pdf/1108.2455
- Egypt bread: https://www.npr.org/sections/money/2011/02/01/133403007/protests-and-the-price-of-bread ; https://www.voanews.com/a/high-food-prices-helped-spark-egypt-protests-116170879/160199.html ; https://newstatesman.com/politics/2013/07/what-price-bread-egypt
- Sri Lanka: https://www.tbsnews.net/node/381010 ; https://fwi.co.uk/farm-life/flindt-on-friday/flindt-on-friday-sri-lanka-fallout-a-warning-for-all
- Japan rice: https://www.foodmanufacturing.com/supply-chain/news/22941833/japans-rice-crisis-prices-soar-supplies-dwindle-and-minister-resigns
- UK rationing: https://arxiv.org/pdf/2301.09982 ; https://blogs.kent.ac.uk/history/?p=1054
- Finland NESA: https://www.huoltovarmuuskeskus.fi/en/a/national-emergency-supply-agency-boosting-finlands-emergency-grain-stockpiles ; https://huoltovarmuuskeskus.fi/en/a/procurement-of-additional-grain-for-emergency-stockpiles-completed
- China (unverified scale): https://janataweekly.org/articles/how-china-prepared-for-the-new-global-food-crisis-caused-by-the-us-war-on-iran
- Lords, Food Security, 15 Oct 2026: https://hansard.parliament.uk/Lords/2026-10-15/debates/1A83180F-4DDD-4033-B32A-CD71EFEB8FEA/FoodSecurity
- Written answer HL15829: https://questions-statements.parliament.uk/written-questions/detail/2026-03-20/HL15829/
- Dockworkers 30 Oct: https://inthesetimes.com/article/dockworkers-six-countries-announce-port-strikes-october-30 ; https://www.wftucentral.org/greece-piraeus-dockworkers-and-metalworkers-organise-strike-on-october-30/ ; https://blogs.lse.ac.uk/businessreview/2026/03/03/mediterranean-dockworkers-are-striking-to-protest-against-war/
- Felixstowe 2022: https://www.personneltoday.com/hr/felixstowe-docks-port-unite-strike-ballot/
- FOI request: https://www.whatdotheyknow.com/request/strategic_food_reserves_and_comp


---

<a id="note-12"></a>

## 12 · Carbon credits, nature markets and a new economy of food

Tags: `research:subsidies-tax-incentives`, `research:forestry`, `research:diets-livestock-externalities` and the theme "new economy".
Gap addressed: carbon credits were mentioned (Gemini's "unified global carbon market by 2030") but never tested. This note covers what UK carbon and nature markets actually pay, what pricing agriculture would mean, the integrity problems, and a "new economy" framing in which food is essential infrastructure.
Status: web-search research, 22 Oct 2026. Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Headline finding

**Carbon pricing is about to reach UK food from the outside, through the border tax on fertiliser, before it reaches farming from the inside.** The UK Carbon Border Adjustment Mechanism (CBAM) starts on **1 Jan 2027** and covers imported fertiliser, during a Hormuz price shock. Voluntary woodland and peat credits are real but small: ~£28–40 per tonne, a £1.2bn UK market in 2025. Soil carbon credits have serious integrity problems. Pricing farm emissions the Danish way is feasible, if revenue goes back to farmers and households. The principle behind Gemini's proposal (price all emissions) is mainstream economics; its "single global market with zero carve-outs by 2030" is not achievable and is not needed for the UK argument.

### 2. What carbon and nature markets pay UK land managers

| Market | Price / size | Notes | Source |
|---|---|---|---|
| **Woodland Carbon Code** | Pending Issuance Units averaged **£28.32 (2025)**, up from £26.85 in 2024; huge spread (£112 between lowest and highest) | PIUs are promises of future sequestration; verified units come later | [P] WCC |
| **Peatland Code** | **£39.57 (2025)**, up from £25.04; average skewed by three large deals | Pays for restoration and rewetting | [P] WCC / IUCN UK Peatland Programme |
| UK carbon credit sector | ~**£1.2bn** contribution to the UK economy in 2025 | City of London Corp / UK Carbon Markets Forum, Apr 2026 | [S] |
| **Biodiversity Net Gain** (England, statutory since 2024) | Statutory credits (last resort) **£42,000** per unit for most habitats, £48k woodland, £125k ponds; market units ~£20k (hedges, grassland) to £140k (watercourses); prices for common habitats softening | Defra originally expected £9–15k/unit. Developer-funded, 30-year habitat-bank obligations. | [P/S] gov.uk mirror, Savills, Carbon Pulse |
| **UK ETS** (compliance market) | UKA ~£58 (Nov 2025); analysts expected >£60 average in 2026; **UK–EU ETS linking** negotiations open, possible signing reported in Jul 2026 [?] | Agriculture is *not* covered | [S] S&P, Carbon Pulse |

**Read:** for a farmer, carbon and nature markets are a **side income on the right land** (peat, poor grassland for trees, habitat banks), not a business model. BNG units can be very valuable but depend on local housebuilding demand and lock land up for 30 years. All of these are *land-use* markets. They pay for taking land out of food or reducing intensity, so they need the "protect grade 1–3a" guardrail (Claude briefing move 8).

### 3. Integrity: why soil carbon credits are risky

| Evidence | Finding | Source |
|---|---|---|
| Mitchell et al., *Carbon Management* (2024) | Six Australian soil-carbon projects credited in 2023: most measured gains were explained by **unusually high rainfall**, not management, and did not persist. 25% withholding buffers are insufficient; recommend ≥5-year measurement periods. | [P] |
| Lötjönen et al. (2024) | Permanence, additionality and measurement are the core problems; farmers only sign *finite* contracts, which conflicts with permanence; proposes discounted "offset ratios" | [P] |
| Carbon Farming Summit (2025) | Offsetting is **not an appropriate instrument** for soil management; it can *raise* net emissions; prefer action- or result-based payments | [S] |
| Guardian / Die Zeit / SourceMaterial (Jan 2023) | >90% of Verra rainforest credits analysed were likely "phantom" credits; Verra disputes this | [S] |

**Read:** pay farmers for soil health through **public schemes (ELM, SFI) as an action payment**, not by selling soil carbon as offsets to polluters. Woodland and peat codes are more robust: measurable biomass, and water tables you can see. Even so, permanence (fire, storms, disease; note 07) and buffer pools matter.

### 4. Pricing agricultural emissions: what it would look like

| Item | Figure | Source |
|---|---|---|
| UK agricultural emissions | **47 MtCO₂e (2024), 12% of UK total**; 49% of methane, 59% of N₂O | [P] Defra (dossier) |
| **Denmark (Green Tripartite, Jun 2024)** | Livestock emissions tax from **2030**: 300 DKK/tCO₂e, rising to 750 DKK by 2035, with a **60% basic deduction**, so the effective rate is **120 DKK (2030) and 300 DKK (2035)**. Revenue is recycled into land conversion (10% of farmland to nature, incl. 140,000 ha of lowland soils). | [P/S] |
| **UK CBAM (from 1 Jan 2027)** | Covers imported fertiliser. Manufacturers say **+£50/t or more** on-farm in some cases; industry range +7–30%; AIC worst case **£152.5m/yr** levy on non-EU fertiliser imports; free-allowance details unclear; NFU and others want a delay because of Hormuz | [S] FWI, NFU, FarmingUK |

Scale [E]:
- Applying a UK ETS-level price (~£60/t) to all 47 Mt ≈ **£2.8bn/yr**, about a third of total income from farming (£8.4bn). Politically and economically impossible without recycling the money back.
- At Denmark's effective rates (~£14/t in 2030, ~£35/t in 2035) ≈ **£0.65bn/yr rising to £1.6bn/yr**, comparable to today's £1.8bn agri-environment budget. **A Danish-style tax recycled through ELM would be roughly revenue-neutral for the sector as a whole while changing what pays.**
- Two technical choices dominate the outcome. (1) Methane metric: under GWP100, a stable herd looks as bad as a growing one; under GWP*, a stable or falling herd adds little new warming. Ruminant farmers prefer GWP*; climate scientists disagree on its use for allocation. (2) Leakage: without a border adjustment on *food* imports, pricing UK livestock exports the emissions (the Grok briefing's point).

**On Gemini's "unified global carbon market by 2030, zero carve-outs":** the underlying idea, pricing externalities, goes back to Pigou and is economic orthodoxy. But one global price for CO₂ and methane by 2030 is not on any negotiating table. Treating methane "as the exact same commodity" ignores that methane is short-lived, and its effect depends on the metric. The UK argument does not need it: CBAM, UK–EU ETS linkage and a Danish-style domestic scheme are the realistic tools.

### 5. A "new economy" framing: food as foundational infrastructure

Ideas with real-world traction (not just theory):

| Idea | Status | Relevance |
|---|---|---|
| **Foundational (everyday) economy** (Manchester Foundational Economy Collective) | Adopted as "Everyday Economy" by **Greater Manchester Combined Authority** (Andy Burnham's former authority) and in Welsh policy | Treats food production and distribution as essential infrastructure, like water and power. A natural fit for a Burnham government. [S] |
| **Well-being of Future Generations (Wales) Act 2015** | 10 years on: ~80% of stakeholders understand it, 85% say it shaped their work; criticised for weak outcomes and funding | A legal duty to consider the long term, which is where reserves and soil belong [S] |
| **Wellbeing economy / doughnut economics** | Scotland and Wales in the Wellbeing Economy Governments network [? not re-verified] | Framing, not mechanism |
| **Food as critical national infrastructure** | NAO: no food assets in the CNI database; Cold Chain Federation lobbying for CNI status (note 01) | The concrete legal step |
| **Price externalities, recycle revenue** | Denmark (farm methane); fee-and-dividend models | Protects the poorest, which is the unrest link (note 11) |

**Synthesis: a new economy of food [E, proposal for the PDF]**
1. **Food is infrastructure.** Designate food logistics nodes as CNI; hold a public or compulsory reserve (Finland, Switzerland); give Defra a power to direct.
2. **Price what harms, pay for what protects.** CBAM on imported fertiliser (phased, with a hardship window during the Hormuz shock); a Danish-style livestock levy from the 2030s, recycled into a "resilience tier" (note 08) for legumes, storage, water and hedgerows.
3. **Credits only where they're measurable.** Woodland and peat codes on grade 3b–5 land and lowland peat; no soil-carbon offsets; BNG habitat banks kept off grade 1–3a.
4. **Share the dividend.** Return carbon revenue to low-income households and fund community food partnerships (note 10). Fairness is the stability mechanism (note 11).
5. **Work that matters.** The resilience tier and the woodland, peat and hedgerow programme create skilled land jobs, tens of thousands not millions (note 04). Pair with data-centre heat for glasshouses (note 06): the AI economy's waste heat grows the food.

### 6. Still missing
- Current UKA price (Oct 2026) and whether the UK–EU ETS link was signed.
- Final UK CBAM fertiliser rate and free-allocation design.
- How much of a carbon-credit price reaches landowners after developer fees.
- Peer-reviewed evaluation of foundational-economy policy outcomes.

### Sources
- WCC prices: https://www.woodlandcarboncode.org.uk/UK-carbon-prices ; https://www.woodlandcarboncode.org.uk/news-events/uk-woodland-and-peatland-carbon-prices-continue-increase-2025
- IUCN UK Peatland Programme prices: https://www.iucn-uk-peatlandprogramme.org/node/1961
- BNG statutory credit prices (mirror of gov.uk): https://govukdiff.njk.onl/update/2026-06-02T10:00:00+01:00/www.gov.uk/guidance/statutory-biodiversity-credit-prices ; Savills: https://www.savills.co.uk/research_articles/229130/377826-0 ; Carbon Pulse: https://carbon-pulse.com/482625/
- UK–EU ETS link: https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/111225-eu-council-greenlights-uk-carbon-market-linkage-negotiations ; https://carbon-pulse.com/531760/
- UK CBAM and fertiliser: https://www.fwi.co.uk/business/how-the-carbon-tax-on-fertiliser-will-impact-farm-businesses ; https://www.nfuonline.com/news/nfu-calls-for-delay-to-cbam/ ; https://www.farminguk.com/news/iran-linked-disruption-fuels-calls-to-delay-uk-carbon-border-tax_68373.html ; https://www.britishagriculturebureau.co.uk/updates-and-information/cbam-what-a-carbon-tax-on-fertiliser-means-for-farmers/
- Denmark livestock tax: https://www.thelocal.dk/20241118/denmark-confirms-plan-for-world-first-livestock-co2-tax-by-2030 ; https://farminguk.com/news/denmark-s-livestock-farmers-to-be-taxed-for-emissions-from-2030_65714.html
- Soil carbon integrity: https://doaj.org/article/caea2b9f2e8b4afa9934d7b36cbe5a7e ; https://jukuri.luke.fi/handle/10024/554824 ; https://ghginstitute.org/2025/01/17/making-soil-carbon-credits-work-for-climate-change-mitigation/ ; https://orgprints.org/id/eprint/55192/1/20250306__CarbonFarmingSummit_all_final.pdf
- Verra investigation: https://www.carbonbrief.org/daily-brief/revealed-more-than-90-of-rainforest-carbon-offsets-by-biggest-provider-are-worthless-analysis-shows
- Foundational economy: https://www.greatermanchester-ca.gov.uk/what-we-do/economy/the-everyday-economy/ ; https://theknowledgeexchangeblog.com/2021/02/22/the-infrastructure-of-everyday-life-has-the-time-come-for-the-foundational-economy/
- Wales Future Generations survey: https://futuregenerations.wales/news/stakeholder-survey-results-2025/


---

<a id="note-13"></a>

## 13 · How other countries store food: reserves, contingency plans and costs

Tags: `research:international-comparison`, `research:supply-chain-reserves`
Sources: dossier Part 8 (raw searches on Finland, Switzerland, Norway, Sweden, Germany, Japan, Singapore, Gulf and the EU), distilled here, plus new searches on India, Egypt, Israel, Singapore and costs (22 Oct 2026).
Labels: [P] primary or official, [S] secondary, [E] my estimate, [?] unresolved. Currency conversions are approximate.

---

### 1. Headline finding

**The UK is an outlier among comparable countries: it is the only one in this set with no public or compulsory food stock and no plan to create one.** The Nordic and Alpine countries hold **3–9 months of bread grain**. They fund it through small levies (Finland, on electricity; Switzerland, built into import prices) or the defence budget (Sweden, Norway), and keep it fresh by **rotating it through private firms** instead of building state silos. The running cost is small: **about £1 per person per year for six months of grain**, scaled to the UK [E]. The hard parts are the release rules, governance and keeping the stock in the right place. Japan's 2025 rice crisis shows that a reserve that is badly released, or not refilled, fails politically.

### 2. Country by country

#### Finland: the benchmark (NESA, Huoltovarmuuskeskus)
- **Storage:** legal minimum of **6 months** of normal human grain consumption (Government Decision 568/2024). Raised to **~8.5–9 months** in 2022–23 by buying domestic oats (64%) and wheat (36%); a 2025 plan to cut back to 6 months to save ~€20m (~£17m) caused a political row [P/S].
- **Also stores** seed grain (released 15,000 t of spring cereal seed and 50 t of rapeseed after the poor 2021 harvest; rebuilding takes 1–3 years), fertiliser inputs, feed and medicines [P].
- **Model:** NESA owns little stock directly. It contracts companies to hold stock that "keeps circulating through normal business"; there are also compulsory company stocks and agreement-based stocks. Critical firms must keep continuity plans. A legal backstop lets the state take temporary control of critical functions [P].
- **Cost and funding:** National Emergency Supply Fund of **~€2bn (~£1.7bn)**, mostly tied up in stocks. Funded by a **strategic stockpile fee on electricity**: ~€66m (~£57m) in 2026, ~€92m (~£79m) in 2027 under the new Security of Supply Act (in force 1 Apr 2026). Plus ~€25m/yr admin from the budget; can borrow up to €600m. This covers *all* security of supply, not only food: about **€16 (~£14) per person per year** [P].
- **Households:** 72-hour kit guidance.

#### Switzerland: compulsory private stocks (FONES / BWL)
- **Storage:** overall target **3–4 months** of average demand. 2019 figures: wheat **4 months (195,000 t target)**, sugar 3 months (59,000 t), rice 4 months (16,400 t); protein feed **93,000 t (2 months)**; nitrogen fertiliser ~17,000 t (one-third of a growing season); fuel ~4.5 months; antibiotics 5–6 months. Coffee was dropped in 2019 as "not vital" [P/S].
- **Model:** importers and processors are legally *obliged* to hold stock; five industry bodies run it (réservesuisse for food and feed, Agricura for fertiliser). The federal government provides loan guarantees (the CHF 540m credit was proposed to rise to CHF 750m over 10 years) [P/S].
- **Cost:** about **CHF 14 per person per year** (SRF, 2019) for the whole system, including fuel and medicines. Financed through the price of goods via industry guarantee funds [S] [? mechanism detail].
- **Live use, 2026:** on 31 Aug 2026, drought and low Rhine and Danube water stalled feed imports. The government **released up to 20% of protein-feed stocks (~16,000 t), Sept 2026 to Feb 2027.** It is only the second such release (the first was 2018). The farmers' union expects no consumer price impact [P/S]. **This is a reserve doing its job this year, in a shock similar to the UK's.**

#### Norway: rebuilding from zero
- **Storage:** old state grain stocks were dismantled (2003 [?]); now building **82,500 t of bread grain ≈ 3 months**, adding 15,000 t a year from 2024 to 2029. Last contracts signed Aug 2025 [P].
- **Model:** **the state owns the grain; millers and grain firms store and rotate it** under 25-year contracts won on price (first round: Norgesmøllene, Fiskå Mølle, Strand Unikorn, Lantmännen). Grain must be food quality and no older than 4 years [P].
- **Cost:** ~**NOK 300m to buy** the grain (~NOK 3,600/t ≈ £260/t); operating cost estimated at ~NOK 50m; NOK 63m in the first-year budget; authority to commit up to NOK 1bn in future years [P/S].

#### Sweden: total defence
- **Storage:** new law *Beredskapslager i livsmedelskedjan* (Prop. 2025/26:205), in force **1 July 2026**. State-owned stocks of grain and critical inputs (seed, fertiliser, feed, plant protection, spare parts, veterinary medicines), held by an agency or private contractors. The government sets quantities, and site locations are secret. The first stocks were tendered for the four northern counties in Oct 2025 [P].
- **Cost:** **SEK 575m** in the 2026 budget (~£43m, ~SEK 54 per person); SEK 2.1bn for food and drinking-water preparedness over 2026–28; up to SEK 50bn of loan-financed defence money may go to infrastructure and stockpiling [P].
- **Households:** the leaflet *Om krisen eller kriget kommer* ("If crisis or war comes") is sent to every household; officials claim 90–95% of people could live on grain for 3 months without deficiency [S].

#### Germany: an old reserve being modernised
- **Storage:** *Bundesreserve Getreide* **705,000 t** (582k soft wheat, 67k rye, 56k oats; end-2021) plus the *Zivile Notfallreserve* (~126,000 t rice, peas and lentils, plus 5,000 t condensed milk held at dairies). About **one month of bread** [P via top agrar, Bundestag answers].
- **Model:** ~150 private sites (2,000–8,000 t each) chosen by tender; BLE inspects every 4–6 weeks; stock rotated about every 10 years [P/S].
- **Reform:** Agriculture Minister Rainer wants to add **ready-to-eat canned meals** (the "ravioli reserve"), because raw grain needs working mills, bakeries and power. Cost **€80–90m (~£70–78m)**; prompted by the attack on Berlin's power grid (early 2026) [S].
- **Households:** 10-day stock advice (BBK) [S].

#### Japan: what goes wrong
- **Storage:** government rice reserve target **1 Mt** (~1.5–2 months of rice). Released **590,000 t** in 2025 to tame prices (rice nearly doubled, ¥2,023 → ¥3,688 per 5 kg); only ~10% reached shops at first; the minister resigned. The reserve stood at **320,000 t** in Sept 2026, with a 210,000 t buyback announced 1 Sept 2026 and criticised as "too late" [P/S].
- **Self-sufficiency:** 38% on a calorie basis (FY2024) [P].
- **Lesson:** release mechanics, the rule to buy back within a year, and refilling quickly all matter. A reserve run down for price management is not there for the next emergency.

#### Singapore
- **Rice Stockpile Scheme (since 1968):** importers must hold **2× their average monthly imports** as a condition of their licence; the state can acquire the stock in an emergency. A national stockpile of rice, frozen chicken and canned food exists, but its size is secret. Dropped "30 by 30"; new targets are 20% fibre and 30% protein from local production by 2035 [P].

#### Israel
- The state pays private suppliers to hold staples (oil, tea, legumes, baby food, sugar, grain for food and feed). Government-backed reserves were estimated at **~3 months** (INSS, Dec 2023), raised during the war. Weakest area: **animal-based foods** [S].

#### Egypt (the world's largest wheat importer)
- Strategic wheat reserves officially reported at **4 months** (Feb 2026), **~9 months** (June 2026, after the harvest) and "several months" (Oct 2026); procured ~5 Mt domestically in 2026 [S, official claims].

#### India
- **Central pool:** **92.6 Mt** wheat + rice on 1 July 2026 against a buffer norm of 41.1 Mt, more than twice the norm. Norms are set quarterly (operational stock + strategic reserve) [S].
- **Cost:** food and public distribution budget **₹2.35 lakh crore (2026–27)**, 97% of it the free-grain scheme for **813.5m people**; ~0.6% of GDP [P PRS]. That is a welfare system and a reserve in one, so not comparable per tonne.

#### China
- Grain Security Guarantee Law in force 1 June 2024, with a dedicated reserve chapter; Sinograin runs central reserves; output 715 Mt (2025). Reserve size is a state secret. USDA-based estimates put China at **~44% of world wheat ending stocks** [S/E]. Claims of a "700 Mt / 1-year reserve" are unverified [?].

#### Gulf (Qatar, UAE)
- **Qatar:** after the 2017 blockade, near-self-sufficiency in dairy and poultry (98%); strategic reserves for storables (wheat, sugar, rice, oils, frozen poultry), privately managed and state-overseen [P].
- **UAE:** imports up to ~90% of its food; strategy based on 3–5 supply sources for each of 18 basket items [S].

#### EU
- Preparedness Union Strategy (Mar 2025): households should be able to manage **72 hours**; an EU stockpiling strategy followed in 2025 [? date] [S].

#### United Kingdom (for contrast)
- **No public or compulsory food stock**; "no current plans" (written answer, 31 Mar 2026). The WWII stockpile was ended in the 1990s [P].
- Commercial wheat at the pre-harvest low ≈ 1 month of national calories (note 01).
- **Households (UK Public Survey of Risk Perception, Resilience and Preparedness 2026, Cabinet Office/Defra, n = 10,791):** **60%** have three days of food that needs no cooking (down from 66% in 2025); 85% have three days of cupboard food that may need cooking; **only 4% have three days of bottled water**; **13%** feel largely or totally prepared, and 50% slightly or not at all [P gov.uk].

### 3. Side-by-side summary

| Country | Grain / staple cover | Who holds it | Funding | Indicative cost |
|---|---|---|---|---|
| Finland | 6 months legal minimum, ~9 actual | Contracted firms, rotating; plus compulsory company stocks | Electricity levy → €2bn fund | ~€16 (~£14)/person/yr (all security of supply) |
| Switzerland | 3–4 months (wheat 4, sugar 3, rice 4, protein feed 2, N fertiliser ⅓ season) | Compulsory private stocks | Built into import prices; federal guarantees | ~CHF 14/person/yr (incl. fuel and medicines) |
| Norway | 3 months bread grain by 2029 (82,500 t) | State-owned, millers store | State budget | NOK 300m to buy + ~NOK 50m/yr to run |
| Sweden | Not disclosed; building 2026–28 | State-owned, contractors | Defence / civil-defence budget | SEK 575m (2026) |
| Germany | ~1 month bread grain + pulses and rice | State-owned, ~150 private sites | Federal budget | +€80–90m for ready-meal reserve |
| Japan | Rice, target 1 Mt (now 0.32 Mt) | State | Budget | — |
| Singapore | Rice ≥2 months' imports + secret state stock | Importers (licence condition) + state | Private / state | — |
| Israel | ~3 months staples | State-paid private suppliers | Budget | — |
| Egypt | 4–9 months wheat (official) | State | Budget | — |
| India | 92.6 Mt (2× norm) | State (FCI) | Budget | ₹2.35 lakh crore (incl. welfare) |
| **UK** | **None public; ~1 month commercial wheat at the June low** | **Private, uncommitted** | **—** | **—** |

### 4. What it would cost the UK [E]

Assumptions: grain at £200/t; storage £15/t/yr; financing 4%; rotation loss £5/t/yr; UK food-grain use ~6 Mt/yr.

| Option | Stock | One-off purchase | Annual running cost | Per person per year |
|---|---|---|---|---|
| **Norway-style** (3 months of bread grain, scaled: 14.7 kg/person) | ~1.0–1.5 Mt | £0.2–0.3bn | ~£30–42m | ~£0.40–0.60 |
| **Finland-style** (6 months of food grain) | ~3.0 Mt | ~£0.6bn | ~£84m | **~£1.20** |
| Finland actual level (9 months) | ~4.5 Mt | ~£0.9bn | ~£126m | ~£1.80 |
| **Swiss-style** (compulsory stocks of grain, oils, sugar, rice, protein feed, N fertiliser; fuel and medicines extra) | Wide basket | Mostly private capital | — | Swiss whole-system benchmark CHF 14 → ~£0.9bn/yr if applied to the UK, including fuel and medicines |
| **Germany-style ready meals** | Canned meals for power-cut scenarios | £70–80m | — | — |

**Read:** a six-month grain reserve costs roughly the price of **one loaf of bread per person per year** to maintain. The capital is a one-off purchase that is *recovered* when the grain is rotated and sold. The bigger costs are a broad Swiss-style basket (oils, feed protein, fertiliser) and the governance: release rules, regional placement and a power to direct.

### 5. What the UK can copy

1. **Ownership by the state, storage by the market** (Norway, Sweden, Germany): no new state silos; contracts with millers and merchants.
2. **Compulsory stock duty on importers** for oils, sugar, rice, protein feed and fertiliser (Switzerland, Singapore). The cost lands in prices, at a few pounds per person.
3. **Dedicated, ring-fenced funding** (Finland's electricity levy): the reserve can't be raided in a budget squeeze, as nearly happened in Finland in 2025.
4. **Store inputs, not just food:** seed, nitrogen and protein feed (Finland, Switzerland, Sweden). The Swiss feed release in 2026 is the proof.
5. **Ready-to-eat layer for power cuts** (Germany).
6. **Clear release and buy-back rules** (the Japan lesson); publish them in advance so release doesn't trigger panic.
7. **Household layer with targeting:** every Nordic country mails a guide. The UK survey shows only 4% hold three days of water.

### Sources
- Finland NESA: https://www.huoltovarmuuskeskus.fi/en/organisation/funding ; https://huoltovarmuuskeskus.fi/en/security-of-supply/methods-and-tools ; https://huoltovarmuuskeskus.fi/en/a/procurement-of-additional-grain-for-emergency-stockpiles-completed ; https://www.huoltovarmuuskeskus.fi/en/a/ministry-of-economic-affairs-and-employment-state-emergency-stockpiles-to-release-spring-cereal-and-rape-seeds-for-sowing-to-secure-sufficient-supply ; MTV Uutiset 6 Feb 2025: https://www.mtvuutiset.fi/artikkeli/keskusta-huolestui-viljan-varmuusvarastojen-vahenemisesta-ymmartaako-hallitus-taysin-mista-on-kyse/9096310
- Switzerland: https://www.bwl.admin.ch/en/range-of-compulsory-stocks ; SRF 2019: https://www.srf.ch/news/schweiz/schweizer-vorratskammer-kein-kaffee-im-krisenfall ; feed release 2026: https://www.cash.ch/news/notreserven-fur-protein-tierfutter-werden-freigegeben-964808
- Norway: https://www.regjeringen.no/no/aktuelt/staten-ber-om-tilbod-pa-beredskaplagring-av-korn/id3028355/ ; https://www.regjeringen.no/no/aktuelt/nye-kontraktar-for-beredskapslagring-av-matkorn/id3061307/ ; https://www.tu.no/artikler/norge-oppretter-beredskapslager-for-korn-vi-ma-tenke-det-utenkelige-sier-vedum/535884
- Sweden: https://regeringen.se/pressmeddelanden/2025/10/de-forsta-beredskapslagren-for-spannmal-etableras-i-norra-sverige/ ; https://data.riksdagen.se/dokument/HD01MJU25.html ; https://data.riksdagen.se/dokument/HD03205.html
- Germany: https://www.topagrar.com/panorama/news/das-ist-uber-deutschlands-getreidevorrate-bekannt-20020375.html ; https://www.topagrar.com/management-und-politik/news/krisenvorsorge-agrarminister-rainer-will-staatsreserve-mit-fertigprodukten-20017575.html
- Japan: https://www.thedailystar.net/business/global-economy/news/japan-release-emergency-rice-reserves-fight-inflation-3825041 ; https://english.adnkronos.com/2026/09/01/japan-govt-to-buy-back-210000-tons-of-rice-after-stockpile-release/ ; MAFF self-sufficiency: https://www.maff.go.jp/j/press/kanbo/anpo/251010.html
- Singapore: https://www.mti.gov.sg/newsroom/written-reply-to-pq-on-stockpiling-of-key-food-items ; https://britcham.org.sg/news/singapore-drops-30-30-farming-goal-sets-revised-targets-fibre-and-protein-2035
- Israel: https://www.inss.org.il/publication/food-supply-chains/ ; https://jpost.com/israel-news/article-857784
- Egypt: https://english.ahram.org.eg/News/578762.aspx ; https://www.egypttoday.com/Article/1/149996/Cabinet-strategic-wheat-reserves-secure-citizens-needs-for-several-months
- India: https://www.businesstoday.in/latest/economy/story/global-food-security-faces-fresh-risks-but-indias-grain-buffer-offers-a-cushion-560357-2026-10-08 ; https://prsindia.org/budgets/parliament/demand-for-grants-2026-27-analysis-food-and-public-distribution
- China: dossier Part 8 (USDA WASDE via secondary; Grain Security Guarantee Law)
- Qatar: https://www.freshplaza.com/asia/article/9759318/qatar-targets-higher-food-self-sufficiency-by-2030/ ; UAE: https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/strategies-plans-and-visions/environment-and-energy/national-food-security-strategy-2051
- EU 72 hours: https://www.shelflife.ie/eu-citizens-urged-to-stockpile-enough-essentials-for-three-days
- UK household survey 2026: https://www.gov.uk/government/statistics/uk-public-survey-of-risk-perception-resilience-and-preparedness-2026/uk-public-survey-of-risk-perception-resilience-and-preparedness-2026-headline-findings-html


---

<a id="note-14"></a>

## 14 · Who has food reserves, why "six months", and is it enough?

Tags: `research:international-comparison`, `research:supply-chain-reserves`, `research:scale-up-emergency`
Follows note 13. Status: 22 Oct 2026, web search + model (`research/model/cereal_balance.py`, `reserve_table()`). Labels: [P] primary, [S] secondary, [E] my estimate or model, [?] unresolved.

---

### 1. Can we actually know which countries have food reserves?

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

### 2. Why "six months"? There is no magic number

The figures cluster at **3–4 months** (FAO/World Bank rule of thumb, Switzerland, Norway, Israel) and **6–9 months** (Finland, Egypt after harvest). The logic behind them:

1. **Time to organise an alternative.** FAO's classic guidance sizes a reserve to give "adequate lead time for government to … assess the size of the shortfall and initiate measures": find new suppliers, finance imports, reroute ships. That takes **weeks to a few months**, which is where the **3–4 month** benchmark comes from (plus a *cash* reserve for imports) [P FAO; S encyclopedia summary of the FAO/World Bank figure].
2. **Distance to the next harvest.** One growing season, from spring sowing to harvest, is **~5–6 months** in northern Europe. A reserve that bridges six months lets a country plant and harvest its way out of a shock that starts in winter [E].
3. **History and geography.**
   - **Finland**: in 1917–18, with grain self-sufficiency at ~60%, Russian imports stopped and there was no reserve to fall back on. Both world wars brought embargo-driven hunger. The security-of-supply system grew out of that. The legal minimum is **6 months**; it was raised to **~9 months** in 2022–23, and a 2025 attempt to cut back to 6 months to save ~€20m (~£17m) became a political row [P NESA; S].
   - **Switzerland** stored for 6 months, cut to 4 months in 2003 (and lowered its planning ration from 3,300 to 2,300 kcal/day). It then consulted in 2023 on **12 months at a reduced ration**: cereals +50%, oils +25%, feed stocks *down*. Outcome not confirmed [?] [S].
4. **Cost and spoilage.** Grain keeps 4–10 years with good storage (Norway requires ≤4-year-old grain; Germany rotates at ~10 years). The carrying cost rises in proportion to size, while the benefit falls once alternatives can be organised. **Six months is a political compromise between insurance value and holding cost**, not a scientific optimum [E].

### 3. Is six months enough to take emergency action?

*(Read here as "enough time to put emergency measures in place". If you meant medical treatment, tell me.)*

#### What can be done, and how fast (UK) [E]

| Time after shock | Emergency measures available | Needs |
|---|---|---|
| Days 1–14 | Release stocks; ration fairly; stop grain-to-ethanol and distilling; ban grain exports; prioritise fuel for food logistics; household guidance | Legal powers (Defra lacks a "power to direct", note 10) |
| Weeks 2–12 | Divert feed grain to milling; cut pig and poultry numbers (they run short of *soya* anyway); find alternative import routes and suppliers; waste reduction | Milling capacity (~5–5.5 Mt/yr wheat today) |
| 3–6 months | Spring sowing (Mar–Apr) of cereals, potatoes and pulses on temporary grass and extra land; WWII-style tillage drive | Seed, nitrogen, diesel, labour, machinery |
| 6–13 months | First harvest from the expanded area (Aug–Sep) | Weather |
| 1–3 years | Pulses replace soya; new storage; on-farm water | Investment |

**So six months is enough to reach the first emergency *spring* harvest only if the shock starts in autumn or winter.** A shock that starts in spring, after the sowing window, needs up to **~12 months** of bridging to the next harvest. That is why Finland went to nine and Switzerland is considering twelve.

#### But the UK is different from Finland or Switzerland: it grows most of its own grain

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

### 4. Bottom line for the PDF
- "About 30 countries actively use public food reserves. The UK is not one of them."
- "Six months is a rule of thumb: the time it takes to find new suppliers, or to sow and harvest a spring crop. It is a compromise between insurance and cost, not a scientific number."
- "Because Britain grows most of its own grain, a reserve's job is to buy *time and choice*: a month covers the calories if we cut animal feed by a fifth; four to five months avoids forcing that choice in a nitrogen or double-harvest shock. But grain alone isn't enough. Store seed, nitrogen, oils and protein too."

### Sources
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


---

<a id="note-15"></a>

## 15 · From feed to food: can people eat "animal" grain, and what would a full system restructure look like?

Tags: `research:calories-protein`, `research:diets-livestock-externalities`, `research:supply-chain-reserves`, `research:agroecology-biology`
Prompted by: FAO feed figures supplied by the project lead; the idea of a rotating reserve that becomes animal feed when it ages; fewer animals; full-cost accounting including CO₂; carbon-negative cropping.
Status: 22 Oct 2026, web search + arithmetic. Labels: [P] primary or peer-reviewed, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Check of the FAO figures supplied

| Claim | Verdict |
|---|---|
| ~⅓ of global cereals go to animal feed; 86% of global livestock feed is not human-edible; grains are 13% of feed dry matter; 2.8 kg (ruminants) and 3.2 kg (monogastrics) of human-edible feed per kg boneless meat; ~6 bn t DM feed/yr | **Confirmed**: Mottet, de Haan, Falcucci, Tempio, Opio & Gerber (2017), *Global Food Security* 14:1–8 [P]. The authors flag the ~3 kg figure as lower than older estimates and needing confirmation. |
| FAOSTAT 2023: ~35% of cereals and ~24% of pulses to feed; ~45% of cereals eaten directly | Plausible and consistent with FAOSTAT; not re-verified this session [?] |

**Two cautions before using these in a UK argument:**
1. **The 86% is a *global* average driven by grazing ruminants** in low-input systems (grass, leaves, crop residues). **UK pigs and poultry eat mostly human-edible feed**: wheat, barley and ~2.3–2.5 Mt of soya meal (note 09). In the UK **~52% of wheat, barley and oats goes to feed** (Defra, 2023, dossier), well above the global ⅓. The UK's own feed–food competition is *higher* than the global figure suggests.
2. **"Only 3 kg of grain per kg meat" still means a big calorie loss** [E]. 3 kg of grain ≈ 9,900 kcal; 1 kg of boneless meat ≈ 1,500–2,500 kcal. That is **~4–6× fewer calories out than in** (meat protein is higher quality, so the protein loss is smaller). Ruminants on grass that cannot be cropped are the exception: there the "feed" competes with nothing (Wilkinson 2011: UK milk and upland suckler beef return more human-edible protein than they consume, dossier).

### 2. Can humans eat grain grown for animals?

**Mostly yes, and the dividing line is a quality grade, not a different crop.** "Feed wheat" is usually the same species, often a soft, lower-protein variety (UK Group 3/4) or a milling variety that missed its specification. "Feed" is a *contract* label.

| Issue | What it means | Source |
|---|---|---|
| **Baking quality** | Feed wheat makes poor *bread* (low protein, low Hagberg falling number) but is fine for **biscuits, cakes, flatbreads, porridge-type and wholegrain uses**, and blends with stronger flour. Only a minority of UK wheat meets bread specification; most is fed. Price gap in Nov 2025 only ~£14/t (feed £166/t, milling £180/t). | [P] study via search; [S] FWI |
| **Mycotoxins (the real safety limit)** | EU food limit for DON in unprocessed cereals **cut from 1,250 to 1,000 µg/kg** (Reg. 2024/1022, from 1 Jul 2024; durum and maize 1,500). Feed guidance values are much higher, ~8,000 µg/kg for cereals (EU Rec. 2006/576) [? not re-verified]. **In wet harvest years some feed grain will fail food limits. Test before diverting.** UK retained limits not confirmed [?]. | [P/S] |
| **Storage hygiene** | Food grain needs food-grade storage (pest control, no contaminants). Most UK merchant stores are assured for both food and feed. On-farm feed stores may not be. | [E] |
| **Barley and oats** | Feed barley → pearled barley, barley flour and flakes. Oats are the same crop for food or feed (oat milling is the constraint). | [E] |
| **Field beans and peas** | UK field beans are fed to animals *and* exported to Egypt for ful medames: the same beans. Marrowfat and feed peas are edible. | [S] dossier |
| **Imported maize, soya meal, rapeseed meal, distillers' grains** | Not direct human foods (meals are de-oiled press cake) | [E] |
| **Processing capacity** | UK flour millers mill ~5–5.5 Mt of wheat a year. **Diverting several Mt more needs more milling, dehulling and baking capacity**, or simpler foods (whole-grain cooking, porridge, flatbreads) | [S] |

**Bottom line:** in a crisis, most UK feed wheat, barley, oats and beans *can* become human food, *after* mycotoxin testing, with less bread and more porridge, flatbread and biscuits, and if milling capacity can be raised. That makes the 13–14 Mt of feed cereals the UK's **largest hidden food reserve**, as a flow rather than a stock.

### 3. The rotating-reserve idea: yes, and it already exists

**Proposal (project lead):** keep a food reserve; when it ages, rotate it out to animal feed.

**Precedent: Japan does exactly this.** The government holds ~1 Mt of rice, buys ~200,000 t a year, holds each lot for **five years**, then sells unused rice **as animal feed**. It is sized for "a once-in-a-decade bad harvest or two poor harvests in a row" [S]. Germany rotates its grain reserve about every 10 years and sells it on the market. Norway requires reserve grain to be no older than 4 years. Finland and Switzerland keep stocks moving through normal trade [P/S, note 13].

**UK design sketch [E]:**
- **Stock:** ~3 Mt of food-grade grain (≈6 months of food grain; note 13 costing ~£0.6bn to buy, ~£84m/yr to hold) + pulses + oils + seed + nitrogen.
- **Specification at intake:** food-grade mycotoxin limits, moisture ≤14.5%, assured storage.
- **Rotation:** ~⅓ to ⅕ replaced each year (3–5-year life). Outgoing grain goes to **millers first if it still meets food spec, otherwise feed**. Feed is the safety valve that makes rotation almost loss-free.
- **Interaction with "fewer animals":** a smaller herd shrinks the feed market that absorbs rotated stock, but even a halved UK feed demand (~6–7 Mt) easily absorbs 0.6–1 Mt a year.
- **Political lesson from Japan:** release rules and refilling must be pre-agreed. And don't call released reserve food "animal feed" in public: in 2025 a Japanese opposition leader had to apologise for doing so.

### 4. Repurposing production toward human-edible food: the size of the prize [E]

Illustrative scenario: halve the monogastric herd (pigs, poultry, eggs) and divert half of domestic feed cereals (~6 Mt) to human food.
- Grain diverted: 6 Mt × 3.3 m kcal/t ≈ **19.8 trillion kcal**.
- Lost animal food: about half of the ~6 trillion kcal from pigs, poultry and eggs ≈ 3 trillion kcal (dossier Part 3 estimate).
- **Net gain ≈ 16.8 trillion kcal/yr ≈ 107 days of national energy ≈ 29% of annual need.**

In *normal* times people won't eat 6 Mt more grain. So the restructure is not "eat more bread". It is:
1. **Grow less feed grain** and use the freed arable land for pulses (replace soya; note 09), vegetables and fruit (14% fruit self-sufficiency), and trees and hedges on the poorest land.
2. **Hold the difference as a reserve and as surge capacity**: the system *can* switch back to grain-for-people in a crisis.
3. **Feed animals on what people can't eat**: grass, by-products, and safe heat-treated food waste.

**Food waste to pigs:** the UK banned swill in 2001 after the foot-and-mouth outbreak (£8bn cost); the EU followed in 2002. **Japan ("Ecofeed") and South Korea** heat-treat food waste (≥70 °C for 30 min or 80 °C for 3 min) and recycle **~36% and ~43%** of food waste as feed, with no swill-linked outbreaks reported. Zu Ermgassen et al. (2016, *Food Policy*) estimate that legalising treated swill in the EU would save **~1.8 Mha of land** (incl. >0.25 Mha of Brazilian forest and savannah), cut pork's land use **~21.5%** and roughly **halve feed costs** [P model]. **Risk:** African swine fever is now in Europe, so this needs centralised licensed treatment, not farm-level swill.

### 5. Fewer animals: what the official advice already says
- **Climate Change Committee, Seventh Carbon Budget (Feb 2025):** **cattle and sheep −27% by 2040, −38% by 2050**; **meat consumption −25% by 2040** (−35% by 2050); **dairy −20% by 2040**; freed land goes to woodland, peat restoration and bioenergy crops. **Government says this is not policy**; farm groups object [S multiple].
- **Gap in the CCC framing for resilience [E]:** the CCC targets *ruminants* (methane). For *food security*, the bigger lever is **monogastrics on imported soya** (note 09). A resilience-led plan cuts pigs and poultry first (feed competition and import dependence), and keeps grass-fed ruminants on unploughable land while trimming numbers for methane. Both lenses agree on "fewer, better".
- Diets are already moving: meat −17% per person 2008–19, mainly through smaller portions (note 05).

### 6. Full-cost accounting including CO₂ (links note 12)
- **Hidden costs:** FAO SOFA 2023 put global agrifood hidden costs at **≥$10 trillion a year**, ~70% from unhealthy diets [P via dossier]; SOFA 2024 refines this [? figure not re-verified]. Sustainable Food Trust (2017): ~£1 of hidden cost per £1 spent on UK food (methods contested).
- **Mechanism that exists:** Denmark's livestock levy from 2030 (effective ~£14/t CO₂e rising to ~£35/t by 2035), recycled to land conversion. Scaled to UK agriculture's 47 MtCO₂e that is **~£0.65–1.6bn/yr**, about the size of today's agri-environment budget (note 12).
- **Fairness condition:** recycle revenue to low-income households and farmers, or full-cost pricing becomes a food-poverty and unrest risk (notes 10, 11).

### 7. "Carbon-negative crops": what is real

Crops are carbon-neutral within a year (they absorb CO₂ and release it when eaten or rotted). **Removal requires carbon stored for decades or more.** The UK options, ranked by evidence:

| Option | Evidence | Read |
|---|---|---|
| **Rewetting farmed lowland peat** | Avoided emissions; Peatland Code credits ~£40/t (2025) | Large per hectare, but costs food output on Grade 1 Fen land; choose field by field (notes 07, 12) |
| **Hedgerows, agroforestry, woodland on grade 3b–5** | Measurable woody biomass; WCC credits ~£28/t | Robust; also shelter, biodiversity, timber |
| **Enhanced rock weathering** (spreading crushed basalt on fields) | Models: UK arable ERW could remove **6–30 MtCO₂/yr by 2050** (Goldschmidt 2025 abstract). UNDO/Newcastle first-year trial: **crop yields +15%** on average (+9.3% ploughed, +20.5% direct-drilled), soil pH +0.2–0.29 in a dry 2022. Long-term Leverhulme/Sheffield field trials are measuring actual removal; per-hectare UK figures not found [?] | **The most interesting "food + carbon" lever**: it may raise yields *and* remove CO₂, and it replaces lime. Needs verified measurement, quarry energy and haulage counted, and heavy-metal checks |
| **Biochar** | Stable carbon; needs biomass and pyrolysis energy. UK field data not found this session [?] | Niche; good with waste biomass |
| **Soil carbon from leys and cover crops** | Real but slow, saturating and reversible; credit integrity poor (Australian rainfall artefact, note 12) | Pay as soil-health *actions*, don't sell as offsets |
| **BECCS / energy crops** | CCC includes bioenergy on freed land; Drax and imported wood are contested | Competes for land with food and trees; lowest priority for this project |

**For the PDF:** ERW is a *possible* new pillar ("farms that capture carbon and grow more"), but it is still at the trial-evidence stage. Present it as a research and early-deployment priority, not a solved technology.

### 8. A full system restructure: the blueprint in one table [E, synthesis]

| Pillar | Move | Evidence anchor | Timescale |
|---|---|---|---|
| **Store** | 3 Mt rotating food-grain reserve + pulses, oils, seed, N; rotated stock goes to millers or feed | Japan, Finland, Norway, Switzerland (notes 13, 14) | 1–3 yrs |
| **Re-purpose** | Grow less feed grain; pulses replace ~⅓ of soya within a decade; freed land to veg, fruit and trees | Notes 09, 15 | 2–10 yrs |
| **Fewer, better animals** | Cut pigs and poultry first (soya and grain competition); ruminants on grass, −27% by 2040 per CCC | CCC 7CB; Mottet 2017; Wilkinson 2011 | 5–15 yrs |
| **Close loops** | Licensed heat-treated food waste to pigs (Japan/Korea model); P recovery from sewage | Zu Ermgassen 2016; note 03 | 2–5 yrs |
| **Price the truth** | CBAM on fertiliser (phased); Danish-style livestock levy recycled through ELM and to households | Notes 12, 08 | 2027–2035 |
| **Draw down carbon** | Peat rewetting where right; hedges and trees on poor land; ERW trials scaled if verified | Note 12; ERW trials | 1–30 yrs |
| **People** | Skilled land jobs, community food, fair rationing rules | Notes 04, 10, 11 | Now |

**Risks to name honestly:**
- **Sri Lanka:** sudden input or livestock shocks destroy trust. Phase everything.
- **Leakage:** cutting UK livestock while importing meat exports the emissions. Pair with diet change and border measures.
- **Rural livelihoods:** upland grazing farms get 42% of income from support (dossier). The transition must pay them for nature *and* food.
- **Disease:** swill feeding without strict treatment risks ASF and FMD.

### Sources
- Mottet et al. 2017: https://research.wur.nl/en/publications/livestock-on-our-plates-or-eating-at-our-table-a-new-analysis-of- ; FAO/ILRI summary: https://www.ilri.org/news/fao-sets-record-straight-86-livestock-feed-inedible-humans
- DON limits 2024: https://www.nfuonline.com/news/eu-changes-to-maximum-limits-for-mycotoxins/ ; https://www.food-safety.com/articles/print/9382-eu-sets-new-limits-for-mycotoxin-deoxynivalenol-in-unprocessed-grains-among-other-foods
- UK milling vs feed wheat: https://www.fwi.co.uk/business/markets-and-trends/crop-prices/wheat-quality-improves-in-2025-despite-regional-challenges ; https://ahdb.org.uk/news/10-year-high-imported-wheat-milled-grain-market-daily ; https://researchportalplus.anu.edu.au/en/publications/balancing-quality-with-quantity-a-case-study-of-uk-bread-wheat/
- Japan rotating rice reserve (5 years → feed): https://asianews.network/japanese-government-criticised-for-slow-response-to-soaring-rice-prices/ ; https://www.feedstrategy.com/business-markets/company-news/article/15437406/japan-rice-stockpiles-down-as-surplus-bought-for-livestock-feed
- Swill / Ecofeed: https://www.cambridgenetwork.co.uk/news/feeding-food-waste-pigs-could-save-vast-swathes-threatened-forest-and-savannah ; https://www.feedipedia.org/node/21259 ; zu Ermgassen et al. 2016, Food Policy, doi:10.1016/j.foodpol.2015.11.001
- CCC Seventh Carbon Budget: https://www.farminguk.com/news/uk-livestock-numbers-must-fall-climate-change-committee-says_66183.html ; https://sustainweb.org/news/feb25-seventh-carbon-budget-climate-change-committee ; https://www.fwi.co.uk/news/environment/farmers-reject-cccs-call-for-livestock-reduction-targets
- ERW: https://goldschmidtabstracts.info/2025/32039.pdf ; https://goldschmidtabstracts.info/2025/31077.pdf ; https://www.agriland.co.uk/?p=381736 ; https://remineralize.org/rem_publications/co2-sequestration-by-enhanced-weathering-of-agricultural-soils-in-norfolk-uk/ ; https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2025.1606574/epub
- Dossier Part 3 (feed volumes, Wilkinson 2011) and notes 09, 12, 13, 14 in this folder


---

<a id="note-16"></a>

## 16 · Can we store a complete diet, not just grain? And is a rotating reserve really "no downside"?

Tags: `research:supply-chain-reserves`, `research:calories-protein`, `research:scale-up-emergency`
Question (project lead): can fats and protein be stored as well as grain, giving a fully functional diet that bridges an emergency until the economy and farming can switch within a season? And can it be framed as "no downside", because rotation means nothing is wasted?
Status: 22 Oct 2026. Model: `research/model/reserve_basket.py`. Labels: [P] primary, [S] secondary, [E] my estimate or model, [?] unresolved. Nutrient values and shelf lives are typical figures, to be checked by a nutritionist.

---

### 1. Short answer

**Yes, a nutritionally complete diet can be stored.** It costs more than grain alone, but not much: **about £6.50 per person per year for six months of a full ration for the whole population** [E]. Every item can be rotated through normal trade, public catering or animal feed, so **almost nothing is wasted**. But it is **not literally "no downside"**. It has a small insurance premium, it ties up capital, it can move markets while it is being built, and it needs honest governance. The defensible framing is: **"No waste, low cost, high insurance: a fire extinguisher we eat every few years."**

### 2. What can be stored, and for how long

| Food group | Storable form | Typical good-storage life [E/S] | Who already stores it |
|---|---|---|---|
| Starch / energy | Wheat and barley grain (milled on release) | 5–10 years as grain | Finland, Norway, Germany, Switzerland (wheat 4 months) |
| | Rice (white) | 5+ years | Japan (5-year rotation), Germany, Switzerland (4 months), Singapore |
| | Oats | ~1–2 years (stabilised); the fat goes rancid sooner | Finland (64% of its 2023 top-up) |
| **Protein** | Dried peas, beans, lentils | 2–4 years before "hard-to-cook" ageing | Germany (24k t peas, 18k t lentils) |
| | Skimmed milk powder | ~2–3 years | Germany holds condensed milk via dairy contracts |
| | Canned oily fish or meat | ~3–5 years | Military rations; Germany's planned ready-meal reserve |
| **Fats** | Edible oils in tanks | **Several years in tanks and large containers** (Swiss practice); rapeseed is polyunsaturated and oxidises, so keep it cool, dark and nitrogen-blanketed | **Switzerland: 35,000 t of oils and fats = 4 months**, in tanks, rotated through company sales [P] |
| Sugar | Dry sugar | Effectively indefinite if dry | Switzerland (3 months) |
| **Micronutrients** | Vitamin C and D tablets, iodised salt, flour fortificants (calcium carbonate, iron, B1, B3) | 2–3+ years; cheap and tiny | Not stored by the UK; the calcium carbonate for flour has come from a single French quarry (note 01) |
| Special diets | Infant formula, medical foods | ~1–2 years | Israel's state-paid stocks include baby food |
| **Farm inputs** | Seed grain; nitrogen fertiliser | Seed 1–2 years; fertiliser years, but ammonium nitrate is a **security hazard** | Finland (seed), Switzerland (N for ⅓ of a season), Sweden (inputs) |

Not storable in bulk: fresh fruit and vegetables (vitamin C), fresh dairy, fresh meat. These come from **domestic production**, which keeps running in most scenarios: milk 105%, lamb 103%, potatoes 71%, field veg 56%. Tablets fill the vitamin C gap.

### 3. A complete storable ration (per person per day) [E]

| Item | g/day |
|---|---|
| Wheat (milled to fortified flour) | 350 |
| Oats | 60 |
| Rice | 50 |
| Dried pulses | 80 |
| Rapeseed oil | 35 |
| Sugar | 25 |
| Skimmed milk powder | 30 |
| Canned oily fish | 30 |
| Vitamin C 40 mg + vitamin D 10 µg tablet; iodised salt | — |

**Result (model):** 660 g dry weight; **~2,450 kcal; ~89 g protein** (needs ~2,250 kcal, ~46 g); fat ~53 g (19% of energy, low but adequate for an emergency); **calcium ~1,060 mg** (need ~700); **B12 ~3.9 µg** (need 1.5). Cereals plus pulses balance the amino acids (pulses supply the lysine wheat lacks). Oily fish and rapeseed oil supply omega-3. **Cost ~£0.42 per person per day at wholesale.**

It is monotonous, not luxurious, and close to the WWII diet (~2,400 kcal, ~73 g protein), which improved the population's health (note 11). A nutritionist should check it for vitamin A, folate, zinc and iron bioavailability, and cover infant and medical needs separately.

### 4. Size and cost (whole UK population) [E]

Assumptions: wholesale prices (wheat and oats £200/t, rice £500, pulses £350, oil £1,000, sugar £500, milk powder £2,500, canned fish £5,000); storage £15–80/t/yr by item; 4% financing; ~¼ of stock rotated each year at a 5% discount.

| Reserve | Tonnes | Stock value (bought once, recovered on rotation) | Annual carrying cost | **Per person per year** |
|---|---|---|---|---|
| Full ration, 30 days | 1.4 Mt | £0.87bn | £75m | **£1.08** |
| Full ration, 90 days | 4.1 Mt | £2.6bn | £225m | **£3.24** |
| **Full ration, 6 months** | **8.3 Mt** | **£5.3bn** | **£455m** | **£6.55** |
| Full ration, 12 months | 16.7 Mt | £10.6bn | £913m | **£13.14** |

**Cross-check:** 12 months at ~£13 per person per year matches Switzerland's ~CHF 14 per person per year for its whole compulsory-stock system (note 13).

**Does the UK need a full ration for everyone? No.** Domestic farming keeps producing most calories, milk and meat (notes 09, 14). A smarter design:
- **90 days of the complete ration**: the bridge for a power-cut, logistics or import shock while the economy switches (feed diversion, ethanol cut, new import routes). ~£3.2 per person per year.
- **plus 6 months of the import-dependent items**: oils (UK ~53% fat self-sufficiency), rice, pulses (soya replacement), vitamins and fortificants, infant formula.
- **plus seed and part of a season's nitrogen** (the Swiss "⅓ of a season" rule), so *next* year's harvest is protected.

The cost is roughly **£4–7 per person per year**: about the price of two loaves a year, or a weekly coffee for one month [E].

### 5. "Bridge to a new season": does this buy enough time?

With domestic production continuing (cereal model, notes 09 and 14):
- **Days 0–90:** the reserve feeds people while the state stops grain-to-ethanol, diverts feed wheat to mills, cuts pig and poultry numbers as soya runs out, and finds new import routes.
- **Months 3–6:** spring sowing of cereals, potatoes and pulses on extra land (temporary grass, set-aside), using **stored seed and nitrogen**.
- **Months 6–13:** first harvest from the switched system.

**A 90-day complete ration plus 6 months of the import-dependent items plus inputs covers a shock that starts at any time of year**, because the UK's own harvest refills the grain. Countries without that harvest (Singapore, the Gulf) need much more.

### 6. Rotation: where everything goes, so nothing is wasted

| Item | Normal-times rotation outlet |
|---|---|
| Wheat, barley, oats | Millers (if still food-grade), otherwise animal feed (Japan sells 5-year-old reserve rice as feed) |
| Rice, sugar, oils | Food manufacturers and retail through contracted firms (the Swiss model); out-of-spec oil to biodiesel |
| Pulses | Canners, feed compounders |
| Milk powder, canned fish, ready meals | **Public catering**: school meals, NHS, armed forces, prisons, food banks. The reserve's oldest stock feeds the nation's institutions. |
| Seed | Sown in the last year of its life; next year's seed bought in |
| Nitrogen fertiliser | Used on farms in the normal season; replaced annually |

**Elegant design point:** rotating canned and powdered stock through public procurement turns the reserve into a **year-round social good**: cheaper school meals and food-bank supply. That links resilience to the equity agenda (note 10).

### 7. Honest downsides (and how to shrink each one)

| Downside | Evidence | Mitigation |
|---|---|---|
| **A real premium** | ~£75m–£0.9bn a year depending on size [E] | Ring-fenced levy (Finland: on electricity) or built into import prices (Switzerland) |
| **Capital tied up** | £0.9–5.3bn of stock | Recovered at rotation; can be held by contracted firms with state guarantees (Swiss CHF 540–750m guarantee model) |
| **Moves prices when building** | Japan's 2026 buyback was criticised as "too late", and buying big stocks in a tight market raises prices | Buy gradually over 3–5 years, at harvest, in surplus years |
| **Spoilage through mismanagement** | India: CAG found 4.72 lakh t of wheat (₹700 crore) deteriorated in Punjab 2011–16 (open storage, first-in-first-out not followed) | Covered storage, FIFO, independent audit, published stock reports |
| **Political raiding** | Finland's 2025 attempt to cut from 9 to 6 months to save €20m (~£17m); Japan ran its reserve down from 1 Mt to 0.32 Mt managing prices | Statutory minimum; release rules set in law; refill obligation within 12 months (Japan's rule) |
| **Hazardous inputs** | Ammonium nitrate stores are an explosion and security risk (Beirut, 2020) | Dispersed, regulated sites; store as safer products or hold contracts for supply rather than bulk |
| **Crowding out private stocks** | If the state holds stock, firms may hold less | Contract existing firms to hold extra on top of their working stock (Finland, Norway) |
| **Monotonous diet** | Acceptability in a long crisis | Recipes and public communication planned in advance; rationing that people see as fair (note 11) |

**Framing recommendation:** don't claim "no downside". Opponents will find the costs, and the claim will cost credibility. Claim instead: **"Zero waste, small premium, large insurance. About £5 per person per year to make sure no shock can empty the shelves."**

### 8. PDF lines
- "We can store a complete diet: grain, pulses, oil, milk powder, fish and vitamins. Switzerland already does most of it."
- "Ninety days of a full ration for every person in Britain costs about £3 each a year. Six months costs about £6.50."
- "Nothing is wasted. Old stock goes to school dinners, hospitals, food banks, millers or animal feed."

### Sources
- Swiss oils in tanks, 35,000 t = 4 months; rotation through company sales: https://www.bwl.admin.ch/en/range-of-compulsory-stocks ; https://bwl.admin.ch/en/organisation-strategic-reserves ; https://www.ge.ch/document/emergency-provisions-and-national-economic-supplies
- Swiss 12-month proposal (oils +25%): https://swissinfo.ch/eng/politics/swiss-government-proposes-expanding-national-food-stockpiles/48446798
- General shelf-life guidance: https://ccfruitandnuts.ucanr.edu/sites/default/files/2020-09/335597.pdf
- India FCI losses (CAG): https://www.tribuneindia.com/news/punjab/wheat-worth-rs-600-cr-allowed-to-rot-cag-48189 ; https://www.tribuneindia.com/news/haryana/80000-mt-wheat-stock-damaged-in-2017-2021-cag ; https://www.deccanherald.com/business/avoidable-outgo-rs-375-cr-2259383
- Japan rotation to feed and buyback: note 15 and note 13 sources
- Germany pulses and condensed milk; Israel baby food; Finland seed: note 13 sources
- Model: `research/model/reserve_basket.py`


---

<a id="note-17"></a>

## 17 · Insurance framing: from the £2 entry tier to the £10 Natural Insurance

> **Update (23 Oct 2026):** the headline policy is now **the Natural Insurance (not National Insurance): £10 per person per year**, a complete programme including 5 Mt of multi-purpose grain. See `draft/briefing_full_context.md` §2 and chapter 9. £2 remains the entry tier described below.

Purpose: the PDF's central message, with each number traceable to a model, so the framing survives hostile scrutiny.
Status: 22 Oct 2026. All figures are [E] from `research/model/reserve_basket.py` and `cereal_balance.py` (assumptions in notes 13 and 16). All amounts in GBP.

---

### 1. The message

> **For £2 per person per year, Britain could hold eight weeks of complete food for every citizen, or ten months of bread grain. Old stock goes to school dinners, hospitals, millers and farms, so nothing is wasted. Minimal downside, nothing to lose, a lot to gain.**

### 2. What £2 actually buys (whole UK population)

| £/person/yr | What it buys | Stock held once (recovered on rotation) |
|---|---|---|
| **~£1.10** | **30 days** of a complete ration (grain, pulses, oil, milk powder, fish, vitamins) | ~£12.50 per person (£0.9bn) |
| **~£1.20** | **6 months of food grain** (Finland's legal minimum) | ~£9 per person (£0.6bn) |
| **~£2.00** | **~8 weeks (55 days) of a complete ration**, *or* **~10 months of food grain** | ~£15–23 per person |
| ~£3.25 | 90 days of a complete ration | ~£38 per person |
| ~£4–7 | Full "smart backup": 90-day complete ration + 6 months of imported items (oils, rice, pulses, vitamins) + seed and part of a season's nitrogen | ~£40–75 per person |

**Be precise in the PDF.** "£2" buys the first tier, *not* the full backup. Use "**from £2 a year**" and show the ladder. A critic then cannot say the number was inflated, and readers see that the gold-standard version still costs less than a coffee a month.

### 3. Return on investment: when does it pay off?

Premium: £0.12–0.46bn a year (from the £2 tier to the 6-month complete ration).
Avoided loss: assume a severe national food disruption costs 1–2% of GDP (~£29–58bn on a ~£2.9trn economy). That is illustrative; for scale, the one-day Iberian blackout cost Spain ~$1.8bn (note 06).

| Annual premium | Loss avoided | Pays for itself if a severe shock happens with annual probability of… |
|---|---|---|
| ~£0.14bn (£2 tier) | £29–58bn | **0.2–0.5%** (about once in 200–400 years) |
| £0.23bn (90-day ration) | £29–58bn | 0.4–0.8% |
| £0.46bn (6-month ration) | £29–58bn | 0.8–1.6% (about once in 60–125 years) |

**Read:** the National Risk Register already lists catastrophic food-disruption pathways (national power outage, pandemic, CBRN). The 2020s have delivered COVID, the 2021 CO₂ crisis, 2022 energy and fertiliser shocks, the 2023 salad rationing, the 2025 retail cyber attacks and the 2026 Hormuz and Black Sea disruption. The odds of a severe shock are **well above** the break-even line. The policy pays for itself if disaster strikes **once every few centuries**, and the recent record suggests something far more frequent.

### 4. Economies of scale: why the state should do it, not just households
- Government advice asks each household to keep **3 days** of food and water. The 2026 survey found only 4% have three days of water and 60% have three days of no-cook food (note 13).
- A household buying 3 days of shelf-stable food at retail spends roughly **£15–20 per person** [E, retail ~3× wholesale].
- The state can hold **30 days** of complete food per person for **~£12.50 of stock and ~£1 a year**, because it buys at wholesale, stores in bulk, borrows cheaply and rotates through existing trade.
- **Pooling is ~10× more efficient than household stockpiling**, and it is fair: it covers the people who cannot afford to stockpile (12% of households are food-insecure, note 10).

### 5. WIN–WIN–WIN (each "win" with its evidence)

| Win | For whom | Evidence |
|---|---|---|
| **Security** | Everyone | A buffer of one to six months vs ~1 month of commercial wheat at the June low (note 01); Switzerland used its feed reserve in Aug 2026 (note 13) |
| **Farmers** | UK growers | Steady state demand for grain, pulses and oil; buying at harvest supports prices in surplus years |
| **Public services** | Schools, NHS, food banks | Rotated stock supplies public catering below market cost (note 16) |
| **Fairness and stability** | Low-income households | Pooling covers those who can't stockpile; visible fair rules prevent panic buying and unrest (note 11) |
| **Climate and nature** (if paired with the restructure) | Society | Reserve plus feed-to-food flexibility allows fewer, better animals and land for pulses and trees (note 15) |

### 6. "Minimal downside": the honest footnote
Keep one line in the PDF so critics have nothing to "expose": *"Risks (the premium, market impact while building, mismanagement and political raiding) are managed by buying gradually, independent audit and a statutory minimum, as in Finland, Switzerland and Japan."* (Details: note 16 §7.)

### 7. Slogans to test
- "**£2 a year. The cheapest insurance Britain will ever buy.**"
- "**Eight weeks of food for everyone, for less than a cup of coffee.**"
- "**Nothing wasted: yesterday's reserve is today's school dinner.**"
- "**A reserve isn't a cost. It's what lets us change the system without fear.**"


---

<a id="note-18"></a>

## 18 · Nature's gift: how the UK really stacks up as a place to grow food

Tags: `research:baseline-self-sufficiency`, `research:soils-land`, `research:climate`, `research:international-comparison`
Question (project lead): a mild, moist climate, good soils and flat land should mean the UK grows huge amounts of food, and soils can improve with the right approach. Is that true?
Status: 22 Oct 2026, web search + dossier Parts 4–6. Labels: [P] primary, [S] secondary, [E] my estimate, [?] not re-verified this session.

---

### 1. Verdict

**Half right, and the right half is powerful.** Per hectare, the UK is one of the most productive places on Earth to grow cereals and grass. Its climate gives a long, mild, moist season, and the world wheat-yield record was set in Lincolnshire. **But it is land-poor per person.** The UK has roughly a third of France's arable land per head and is about 2.3× as densely populated. So the honest headline is not "Britain could be a breadbasket for the world". It is: **"Britain could feed itself well, with calories and protein to spare, if it grew food for people rather than feed for animals, stored some, and rebuilt its soils."**

### 2. What nature gives: the strengths

| Factor | Evidence | Source |
|---|---|---|
| **Climate** | Köppen Cfb: mild, rain in every month, no dry season; long growing season (250–290 days >5 °C in lowland England, 330+ on Atlantic coasts); fewer frosts than in 1961–90 | [P] Met Office (dossier Part 6; Claude briefing) |
| **Yields per hectare** | UK wheat averages ~**7.8 t/ha** (5-year average implied by AHDB's 2026 figure of 6.9 t/ha, −11%). **That is about double the world average (~3.5–3.7 t/ha)** and on a par with France, Germany and the Netherlands; far above Ukraine (~4), Russia (~3) and the US (~3) [? FAOSTAT country figures not re-verified]. Scotland's 10-year wheat average is **8.6 t/ha** (9.2 in 2023). | [P] AHDB, Scottish Government; [?] |
| **Yield ceiling** | **World record 17.95 t/ha**, Tim Lamyman, Louth, Lincolnshire, 10 Aug 2022 (in a drought year), more than twice the UK average | [P] Guinness World Records |
| **Grass** | World-class temperate grassland: ~71% of farmland (permanent grass 9.5 Mha, temporary grass 1.3 Mha, rough grazing 1.2 Mha) | [P] Defra (dossier) |
| **Water** | Rain-fed farming almost everywhere; ~10× Kuwait's rainfall; no desalination needed | [P] Met Office (briefings) |
| **Best land** | England's best and most versatile (BMV) land, grades 1–3a, ≈ **42%** of agricultural land; deep silts and loams in the Fens, Lincolnshire, the Vale of Evesham and the Vale of York | [S] Natural England (dossier) |

### 3. What nature withholds: the limits

| Limit | Evidence | Source |
|---|---|---|
| **Land per person** | Arable land ≈ **0.09 ha per person** in the UK vs ≈ **0.27–0.29 ha** in France (FAO arable totals ÷ population) and ~0.18 ha world average [?] | [S/E] |
| **Population density** | UK ~**285 people/km²** vs metropolitan France ~**120** [E] | [E] |
| **Not all flat or arable** | Croppable land 6.1 Mha of 16.8 Mha farmed; most of the north and west is upland, wet or steep, suited only to grass and trees | [P] Defra |
| **Water in the wrong place** | The dry east grows the crops. In 2026: 1,412 abstraction restrictions and 50% cuts to East Anglian spray-irrigation licences | [P] EA (dossier) |
| **Volatility** | 4 of the 5 worst harvests on record in 2020–26; compound extremes (note 07) | [P/S] |
| **Light and heat** | Cool summers and short winter days limit fruit, tomatoes and high-value veg without glass (fruit 14%, tomatoes 17% self-sufficient) | [P] Defra |
| **Soil degradation** | Costs **~£1.2bn/yr** in England and Wales (range £0.9–1.4bn; 2010 prices): **organic matter loss 47%, compaction 39%, erosion 12%**; 80% of the cost falls off-farm (floods, water quality) | [P] Graves et al. 2015, *Ecological Economics* 119:399–413 |
| **Fen peat** | Shrinks 1–2+ cm a year; 25–50 years left under arable | [S] (dossier) |

**Comparison with the Gemini briefing's claim** that the UK "ranks alongside Ukraine's chernozem": **not supported.** The UK out-yields Ukraine per hectare (more rain, more inputs) but has a fraction of its land per person. The two are strong in different ways.

### 4. Could soils get better? Yes, slowly and up to a ceiling

| Evidence | Finding |
|---|---|
| **Rothamsted/Woburn ley-arable experiment** (Johnston et al. 2017, 70 years, sandy loam) | A 3-year grazed grass-clover ley in a 5-year rotation **raised topsoil organic carbon from 0.98% to 1.23% in 28 years**, then levelled off (~1.3% looks like the equilibrium). **Continuous arable declined.** |
| **Broadbalk** (Rothamsted since 1843) | Manure plots built soil organic matter over a century; unfertilised plots still yield ~1.6 t/ha; fertilised ~7–8 t/ha (dossier) |
| **Rock dust (ERW)** | First-year UK trial: crop yields +15% (+20.5% under direct drilling), soil pH +0.2–0.29 (note 15) |
| **Avoided degradation** | The £1.2bn a year cost of compaction, erosion and organic-matter loss is largely avoidable with cover crops, controlled traffic, leys and reduced tillage on vulnerable soils |

**Read:** soils can improve measurably within **one farming generation (20–30 years)**. That is a real "regenerative" story backed by Britain's own long-term experiments. But gains plateau, they need land in grass-clover for part of the rotation (which costs some cereal output), and they cannot replace phosphorus (note 03).

### 5. How much more food could the UK grow? [E, from notes 09 and 15]
- **Calories:** UK crops eaten directly ≈ 115–140% of physiological need in a normal year (dossier Part 3). Diverting half of feed grain to people adds ~29% of annual need.
- **Protein:** pulses could replace ~⅓ of imported feed-soya within a decade; full replacement needs ~1 Mha of beans (6× today).
- **Fruit and veg:** the biggest *gap*. Glass on waste heat (data centres), orchards and better storage could lift 14% and 56% substantially. This is where "growing much more" is most realistic and most valuable.
- **Export potential:** strong in specific products: malting barley, oats, seed potatoes, grass-fed lamb and dairy, salmon, genetics, agronomy know-how. **Not** a bulk grain exporter on France's scale; there isn't the land per person.

### 6. PDF lines
- "Per hectare, Britain is one of the best places on Earth to grow food. The world wheat-yield record was set in Lincolnshire."
- "Per person, we are land-poor: a third of France's arable land per head. That's why what we grow, and who eats it, matters more than how much land we have."
- "Our own soils prove they can recover. Rothamsted's grass-clover leys raised soil carbon by a quarter in 28 years."

### Sources
- AHDB 2026 harvest (dossier Part 1, Part 6): https://ahdb.org.uk/news/final-harvest-report-confirms-cereal-yields-are-below-historic-averages-across-the-uk
- Scottish wheat yields 2023: https://gov.scot/publications/cereal-and-oilseed-rape-harvest-2023-final-estimates/pages/wheat-yield-and-production-remain-high-despite-small-decreases
- Wheat yield world record: https://guinnessworldrecords.com/world-records/highest-wheat-yield ; https://www.fwi.co.uk/arable/wheat-wolds-broke-yield-world-record
- Arable land totals (FAO-based table) and land-use context: https://www150.statcan.gc.ca/n1/pub/16-201-x/2009000/t230-eng.htm ; https://rural.struttandparker.com/publication/agrifrance-rural-report-2019/
- Soil degradation cost: https://ideas.repec.org/a/eee/ecolec/v119y2015icp399-413.html ; https://cranfield.shorthandstories.com/re-focusing-national-policy-and-local-management-to-protect-soils-our-most-neglected-ecosystem/index.html
- Ley-arable soil carbon: https://repository.rothamsted.ac.uk/item/8v42x/changes-in-soil-organic-matter-over-70-years-in-continuous-arable-and-ley-arable-rotations-on-a-sandy-loam-soil-in-england
- Country yield comparison: FAOSTAT (to be pulled directly; not accessible this session)


---

<a id="note-19"></a>

## 19 · The big picture: carbon markets, geopolitics, culture, and regenerative farming in an AI economy

Tags: `research:subsidies-tax-incentives`, `research:international-comparison`, `research:labour-jobs`, `research:agroecology-biology`, `research:governance-policy`
Extends notes 04, 05, 11, 12 and 15. Answers the request for *more* on carbon credits, full system change, cultural shifts, how regenerative agriculture fits technological unemployment, and the geopolitical frame.
Status: 22 Oct 2026, web search. Labels: [P] primary, [S] secondary, [E] my estimate, [?] unresolved.

---

### 1. Carbon markets: where the money is going (2026–2030)

| Development | What it means for UK land and food | Source |
|---|---|---|
| **UK ETS will take carbon removals by end-2029** (legislation by 2028) | Engineered removals (DACCS, BECCS, biochar) enter the compliance market with a **200-year minimum storage** rule and buffer pools. **Woodland removals: not yet decided**; the CCC advised against, Defra pushed back | [S] Sustainability Magazine, ESG News |
| **UK–EU ETS linking** (negotiations open; reported near signing Jul 2026) [?] | One carbon price across Europe; UKAs ~£58–60/t | [S] note 12 |
| **UK CBAM from 1 Jan 2027** | Imported fertiliser pays a carbon price: +£50/t or more on-farm; NFU wants a delay because of Hormuz | [S] note 12 |
| **EU Carbon Removals and Carbon Farming Certification (CRCF, Reg. 2024/3012)** | **Carbon-farming methodologies adopted July 2026**: agriculture and agroforestry on mineral soils, **peatland rewetting**, afforestation; additionality tests, liability rules, **≥10% uncertainty deduction**. A separate act (2026/285, in force 7 May 2026) covers DACCS, BioCCS and **biochar** | [S] LexisNexis, HSF Kramer |
| **UK voluntary codes** | Woodland Carbon Code ~£28/t, Peatland Code ~£40/t (2025); UK carbon credits worth ~£1.2bn to the economy in 2025; soil and hedgerow codes in development [?] | [P/S] note 12 |
| **Biodiversity Net Gain** | Statutory credits £42k–125k per unit; market units £20k–140k | [P/S] note 12 |

**Read [E]:** the direction is clear. *Durable* removals (trees, peat, biochar, possibly rock weathering) are moving into regulated, higher-value markets, with permanence and liability rules. *Soil carbon* stays in the low-trust voluntary tier. For UK land managers, that points to:
1. Trees and hedges on poor land, peat rewetting where right, biochar from farm and forestry waste, and **verified** ERW as future income lines.
2. Soil health paid through public schemes, not offsets.
3. **A UK carbon-farming standard aligned with the EU's CRCF**, so British farmers can sell into a linked European market after ETS linking. That alignment has not been announced [E].

**System-change logic:** a carbon price on fertiliser (CBAM) plus payments for removals together *re-price* the farm. Synthetic nitrogen gets dearer, and clover, leys, trees and peat earn more. This is the market mechanism behind "biology instead of chemistry", but it needs phasing (Sri Lanka, note 11) and revenue recycled to farmers and households (note 12).

### 2. Geopolitics: food is a weapon, a lever and a shield

| Pattern | Evidence | Source |
|---|---|---|
| **Export bans spread fast** | In 2022, **32 countries imposed 77 export restrictions**. At the late-May peak, **~17% of globally traded food and feed calories** were restricted (Indonesia's palm-oil curbs were ~⅓ of that). Only 19% of measures were notified to the WTO. | [P] IFPRI Food & Fertilizer Export Restrictions Tracker |
| **Chokepoints are being used** | 2026: Hormuz (LNG and up to 30% of traded fertiliser); Black Sea (Ukraine wheat exports forecast −53%) | [P/S] note 05 |
| **Inputs as leverage** | Phosphate rock (Morocco, China, Russia), potash (Russia, Belarus), ammonia from gas | [P] note 03 |
| **States are stockpiling** | China (~44% of world wheat stocks), India (2× buffer norm), Indonesia (record 5.3 Mt rice), Sweden and Norway rebuilding, Switzerland weighing 12 months | [S] notes 13, 14 |
| **Alliances** | Singapore's government-to-government rice and food deals with Vietnam and New Zealand (Oct 2025) | [S] note 13 |

**Read [E]:** when a crisis hits, the world market contracts *towards* the countries that hold stock and *away from* those that rely on "just in time". **A reserve is foreign policy**: it stops the UK from panic-buying in a tight market (which harms poorer importers) and gives it room to help allies. A UK with a reserve, a protein crop and its own fertiliser options is a *more reliable partner*: it can say "we won't ban exports and we won't hoard".

### 3. Culture: what blocks system change, and what helps

**The backlash is real and recent:**
- **UK:** thousands of farmers and tractors in Westminster (Nov 2024, Feb 2025) over the inheritance tax change ("tractor tax"); the government scaled it back to a £2.5m threshold in Dec 2025 [S].
- **EU:** farmer protests in 2024 led the Commission to **withdraw the pesticide-halving regulation (SUR)**; the Nature Restoration Law passed only in weakened form; fallow rules were delayed. Organisers themselves partly blamed cheap imports rather than green policy [S].

**What is moving with the grain:**
- Diets: meat −17% per person (2008–19), mostly smaller portions; plant-based *meat* sales falling while tofu and pulses rise (note 05).
- Farmers: in Barclays' customer survey, **56% report adopting some regenerative practices** and 24% plan to; the main motive is cutting input costs (a lender's customers, so not representative) [S].
- Economics: Deloitte/WBCSD modelling across Europe finds regenerative practices **profitable for farmers after 3–5 years**, but with **€2,000–5,000/ha upfront** (≈ £1,700–4,300/ha) and a funding gap [S, modelled].

**Lesson for framing [E]:** system change fails when it is *done to* farmers (EU 2024, UK 2024) and works when it *pays* them and protects their identity as food producers. Lead with **"food security and fair prices for farmers"**, not "fewer cows". The CCC's −27% livestock pathway (note 15) is technically sound but politically toxic without that frame. A food reserve is a rare idea that farmers, environmentalists and security hawks can *all* support.

### 4. Regenerative farming in an AI economy: how the pieces fit

| Link | Evidence | Read |
|---|---|---|
| **AI cuts chemical inputs** | Peer-reviewed robotic spot-spraying (sugarcane, Australia, 2025): **−35% herbicide** at 97% efficacy, −65% in low-weed strips. UK eyeSpot research (Reading, ~2016) showed −74% to −95% in leeks and cabbages (prototype stage). Vendor claims of 10–20% less fertiliser are unverified. | AI and robotics are the *enabler* of lower-chemical farming. They make "biology plus precision" practical. |
| **AI automates drudgery** | Strawberry-picking robots: ~50 units in use in 2026, 4,000 targeted by 2029 (note 04) | Picking jobs shrink. Skilled jobs (scouting, integrated pest management, grazing planning, soil monitoring, robot fleet management) grow. |
| **AI needs heat sinks and land** | Data-centre waste heat → tomato glasshouses (Humber Tech Park plan; Dutch heat networks) (note 06) | The AI build-out can *grow food*: require heat-use plans for new data centres. |
| **AI displaces office work** | Graduate vacancies −46% y/y (Jul 2026); youth unemployment 16%; up to 8m jobs exposed (IPPR, worst case) (note 04) | Land and nature work offers *some* of those people meaningful, health-improving work, at the scale of tens of thousands of jobs, not millions. |
| **Nature work is good for people** | Meta-analysis: structured outdoor activity reduces depression and anxiety (SMD −0.64 / −0.94); CCC alumni lived longer and earned more (note 04) | The wellbeing case is strong if the jobs are well designed (pay, housing, year-round contracts). |

**The synthesis [E]: a "regenerative transition corps" (working name).**
- **Who:** young people and mid-career people displaced by automation, part-time and full-time.
- **What:** hedgerows, trees on poor land, peat rewetting, soil monitoring (with AI tools), community food growing, glasshouses on data-centre heat, and the *rotation logistics of the national food reserve* (school-meal supply).
- **Paid by:** carbon and nature markets (removal credits, BNG, Peatland Code), ELM, CBAM revenue, and a share of the economic gains from AI.
- **Why it's credible:** each element has a UK precedent or evidence base. The integration is the new idea.
- **Honest limits:** tens of thousands of quality jobs, not a mass solution; it needs income policy alongside (note 04).

### 5. Full system change in one picture [E]

```
 STORE ───────────► rotating reserve (£2/person/yr) ──► school meals, NHS, food banks, millers, feed
   │
 GROW FOR PEOPLE ─► less feed grain, more pulses, veg, fruit (glass on AI waste heat)
   │
 FEWER, BETTER ───► pigs and poultry sized to UK protein; ruminants on grass
 ANIMALS
   │
 PRICE THE TRUTH ─► CBAM on fertiliser + livestock levy, recycled to farmers and households
   │
 PAY FOR CARBON ──► trees, hedges, peat, biochar, verified rock dust (UK ETS removals from 2029; EU CRCF)
   │
 PEOPLE ──────────► regenerative transition corps; AI tools; fair rationing rules; local food plans
   │
 GEOPOLITICS ─────► a reliable partner: no hoarding, no export bans, reserve as foreign policy
```

### Sources
- UK ETS removals 2029: https://sustainabilitymag.com/news/how-the-uk-gov-is-aiming-to-integrate-carbon-removal-by-2029 ; https://esgnews.com/?p=37302
- EU CRCF carbon farming methodologies 2026: https://www.lexisnexis.co.uk/legal/news/commission-adopts-delegated-regulation-establishing-crcf-carbon-farming-certification-methodologies ; https://www.hsfkramer.com/notes/energy/2026-posts/a-new-eu-framework-for-carbon-removals-and-carbon-farming ; https://transition-pathways.europa.eu/agri-food/legislation/commission-adopts-certification-methodologies-carbon-farming-under-crcf
- IFPRI export restrictions 2022: https://www.ifpri.org/blog/food-export-restrictions-have-eased-russia-ukraine-war-continues-concerns-remain-key/ ; https://www.cgiar.org/news-events/news/from-bad-to-worse-how-russia-ukraine-war-related-export-restrictions-exacerbate-global-food-insecurity-2
- UK farmer protests: https://www.businessday.co.za/bd/world/europe/2024-11-19-thousands-of-british-farmers-protest-against-tractor-tax ; https://thecattlesite.com/news/farmers-protest-in-central-london-in-protest-of-tractor-tax
- EU rollback: https://www.euronews.com/my-europe/2024/02/06/von-der-leyen-announces-withdrawal-of-contentious-pesticide-law-the-first-defeat-of-the-gr ; https://birdlife.org/news/2024/02/08/5-things-you-need-to-know-about-the-farmer-protests ; https://www.swissinfo.ch/eng/eu-parliament-passes-nature-law-despite-political-backlash/73084337
- Regenerative adoption and economics: https://farming.co.uk/news/barclays-more-than-half-of-uk-farmers-report-adopting-regenerative-practices-as-climate-volatility-and-cost-pressures-intensify ; https://www.wbcsd.org/resources/closing-the-gap-an-analysis-of-the-costs-and-incentives-for-regenerative-agriculture-in-europe/ ; https://gwct.org.uk/blogs/news/2026/september/from-risk-to-reward-modelling-the-cost-of-the-regenerative-transition/
- Spot spraying: https://researchonline.jcu.edu.au/89739 ; https://www.fwi.co.uk/arable/precision-spraying-reduce-herbicide-use-95
