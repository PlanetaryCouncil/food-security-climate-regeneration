# 01 · Stocks, days of cover and single points of failure

Tag: `research:supply-chain-reserves`
Gaps addressed: "no audited days-of-cover figure" and "processing, packaging, fortification and retail concentration".
Status: researched 22 Oct 2026 by web search only. The session's network blocked direct fetches of gov.uk, nao.org.uk and others, so every figure below comes from search-result extracts. **Check against the primary page before final publication.**

Evidence labels used in all gap notes:
- **[P]** figure attributed to a primary source (official statistics, the organisation's own release); seen via search extract
- **[S]** secondary report (trade press, news, NGO)
- **[E]** my own calculation; method shown
- **[?]** unresolved or conflicting

---

## 1. Headline finding

**Nobody publishes a whole-population days-of-cover figure, but grain gives a usable floor.** At the annual low point (end of June 2026, before harvest) UK wheat stocks held about one month of the whole population's calories, and wheat plus barley about two months. That covers energy only, not diet. After harvest the figure is many times higher. So the risk is seasonal: the system is thinnest in early summer.

## 2. What is known

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

## 3. Days-of-cover calculation [E]

Method: tonnes × energy density ÷ population daily need.
- Wheat: 1.514 Mt × 3.27 m kcal/t = 4.95 trillion kcal.
- Need: 69.5 m × 2,250 kcal = 156 bn kcal/day. On the GPT scenario of 70 m × 2,400 kcal it is 168 bn kcal/day.
- **Wheat at its annual low ≈ 29–32 days of total population energy.**
- Barley at ~1.31 Mt ≈ another 26–28 days, but most of it is feed or malting grade and much less usable as human food.
- Against current human and industrial wheat demand (6.56 Mt/yr), the same stock is ≈ **84 days**.

Caveats: the stock is mixed in grade, partly feed wheat and partly imported. It is privately owned and already committed to buyers, held at farms and ports, and needs milling, power and transport before it becomes food. This is the *upper bound* of what grain alone could do at the worst time of year. It is not a ration plan. The GPT briefing's 30-day / 1.48 Mt reserve scenario lines up almost exactly with this, so a "30-day reserve" largely duplicates existing June stocks in tonnage. What it would add is ownership, grade, location and release rights.

**What to say in the PDF:** "At its lowest point each year, Britain's wheat in store equals about a month of the nation's calories. It belongs to private firms, much of it is feed grade, and none of it is earmarked for an emergency."

## 4. Single points of failure

| Node | Evidence | Risk reading |
|---|---|---|
| **Food-grade CO₂** | By-product of ammonia and bioethanol. CF Billingham historically supplied ~60% of UK food-grade CO₂ [S, 2021–23]. Ensus (Teesside bioethanol) stopped in autumn 2025; the government backed a **£100m three-month restart** and the plant was kept on standby. Government call for evidence on CO₂ supply resilience closed 20 Aug 2026. Supply tightens each summer when plants do maintenance; ammonia becomes uneconomic above ~€60/MWh TTF gas [S]. | HIGH. CO₂ is used to stun pigs and poultry, in modified-atmosphere packaging and in drinks. It is a gas-price-linked chokepoint with no strategic stock. Status after the restart window: **[?]** |
| **Cyber / IT** | May 2025: ransomware at Peter Green Chilled (supplies Tesco, Sainsbury's, M&S, Waitrose, Aldi, Co-op and others) halted order processing; M&S and Co-op were hit in the same wave [S]. The NAO names cyber as a rising risk. | HIGH-frequency, short duration. Attacks stop the *order* systems while the lorries still run. |
| **Cold chain** | ~450 temperature-controlled warehouses and ~100,000 refrigerated vehicles; **over 50% of food consumed in the UK is chilled or frozen** (Cold Chain Federation letter, older) [S]. The CCF's 2026 strategy asks for critical national infrastructure (CNI) status and energy resilience. No public figure exists for backup-generator autonomy (hours of run time). | HIGH under a long power cut. This is a data gap. |
| **Short Straits (Dover/Folkestone)** | ~18% of food, feed and drink imports, but ~42% of dairy & eggs, 39% of meat and 29% of fruit & veg (UKFSR, early 2020s) [P via Grok briefing] | MED–HIGH for perishables |
| **Fortificants** | Calcium carbonate for flour fortification has relied on tanker deliveries from a single French quarry [Grok briefing, not re-verified] [?] | Low cost to fix: store 90 days |
| **Retail concentration** | ~10 retailers handle ~95% of shop-bought food (dossier) | The concentration is also a strength: few actors to coordinate in a crisis |

## 5. What is still missing (honest gaps)
- Barley, oats, oilseed and pulse closing stocks from the September 2026 final balance. The AHDB tables need downloading.
- Stocks held by manufacturers, cold stores and wholesalers, by category. The NAO says these exist; no public number was found.
- Backup-power autonomy for distribution centres and cold stores.
- CO₂ supply after the Ensus standby period ends.

## Sources
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
