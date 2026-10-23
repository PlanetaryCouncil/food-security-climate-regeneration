# 24 · Adversarial review, round 2: the hybrid redesign

Date: 23 October 2026. Reviewed: briefing draft-4, combined notes, both models (all three reviewers ran them).
Reviewers: fresh, unprimed sessions of ChatGPT, Gemini and Grok. ChatGPT and Grok opened many primary sources ([R] below); Gemini worked mostly from memory, so its single-source claims stay [S] or [?].

**Bottom line of round 2.** The arithmetic reproduces; the *design* did not survive. Three findings, shared by all three reviewers, forced a redesign:
1. **Rotation volumes swamp UK markets.** Draft-4 held ~1.64 Mt of rice (≈2.5 years of UK use, rotating ~329 kt/yr against ~670 kt/yr consumed) and ~0.70 Mt of rapeseed oil (rotating ~464 kt/yr against ~406 kt/yr used). There is no buyer for that.
2. **A state-owned stock adds ~£4.8bn to public sector net debt.** Inventory does not net off PSND; an extra-budgetary fund the government controls is still consolidated. "The stock is an asset" is commercially true and fiscally irrelevant.
3. **Week one was underpriced.** £2.50 per person-day for ready-to-eat food is below the only UK benchmark: ~£200m for ~4.7m COVID food boxes (~£43 a box) with power, data and roads working (NAO) [R]. £40m for fuel/power and £15m for water and the last mile are not service specifications.

**The redesign (model v3): a hybrid, as all three reviewers recommended.**
- **Tier 1, public crisis tranche** (owned by the state, paid from taxation): what markets will not hold and week one needs. That means no-cook food, infant formula, vitamin tablets, flour premix, sacks and packaging, bottled water, plus operations: the agency, local plans, priority fuel/AdBlue/backup power, the last mile and security.
- **Tier 2, compulsory commercial stocks** (Swiss/Singapore model): importers, millers, merchants and compounders must hold stock *additional* to their normal working stock. It rotates through their own trade, stays off the public balance sheet, and its cost is passed through food prices. Each line is sized against UK annual use.

## 1. Model v3 in one table

`research/model/reserve_basket.py` v3. Prices, fees and allowances are assumptions, not quotes. ChatGPT is right that "bottom-up" overstated it: this is an **illustrative carrying-cost model with explicit allowances**.

| Tier | Line | Stock | Annual cost | Rotation vs UK use |
|---|---|---|---|---|
| 2 | Food-grade milling wheat, 3 Mt (half in new stores at £350/t) | 3.0 Mt | £127m | 12% of milling |
| 2 | High-protein wheat (~90 days of the imported grist share) | 0.35 Mt | £12m | 7% |
| 2 | Rice, ~4 months of UK use | 0.22 Mt | £11m | 8% |
| 2 | Vegetable oil, ~4 months of rapeseed-oil use | 0.135 Mt | £12m | 16% |
| 2 | Sugar, ~2 months | 0.33 Mt | £14m | 4% |
| 2 | Pulses (UK-grown, food grade) | 0.30 Mt | £14m | 15% |
| 2 | Oats (stabilised) | 0.10 Mt | £5m | 13% |
| 2 | Skimmed milk powder | 0.05 Mt | £11m | 8% |
| 2 | Canned fish | 0.04 Mt | £14m | 7% |
| 2 | Soya meal, 10 weeks of imports | 0.46 Mt | £45m | in-flow (first in, first out) |
| 2 | Cereal seed: winter 0.2 Mt + **spring 0.1 Mt**, segregated | 0.30 Mt | £44m | annual turn |
| 2 | Protected urea, extra pre-season merchant stock (92 kt N) | 0.20 Mt | £13m | annual turn |
| 2 | UAN-28 in heated, recirculated tanks (70 kt N) | 0.25 Mt | £13m | annual turn |
| | **Tier 2 total** (held by firms; ~£2.0bn of stock) | **5.7 Mt** | **£333m ≈ £4.79/person** | |
| 1 | No-cook food: 7 days for 10 m vulnerable people at **£6/person-day** | £420m stock | £62m | via public catering |
| 1 | Infant formula ~7 kt standard powder + ready-to-feed | £84m | £9m | manufacturer-held |
| 1 | Specialised formula and medical foods | £30m | £4m | |
| 1 | Tablets: vitamins A, C, D + zinc, 90 days for everyone | £94m | £19m | |
| 1 | Flour premix (incl. folic acid), potassium iodate, feed amino acids, yeast | £24m | £3m | |
| 1 | Sacks, bottles, labels, pallets | £50m | £4m | |
| 1 | Bottled water, 90 m litres | £18m | £6m | |
| 1 | Operations: agency and testing £45m · local plans and exercises £46m · **priority fuel, AdBlue and backup power £100m** · **last mile and water £45m** · security and insurance £15m | – | £251m | |
| | **Tier 1 total** (public stock ~£0.72bn) | | **£357m ≈ £5.14/person** | |
| | **Total** | | **£690m ≈ £9.93/person** | |

Rotated tonnes now pay **£18/t for handling and haulage** (Camgrain publishes £9.90/t handling with haulage extra [R]). New-store finance follows the scenario rate.

**Range:** low £9.05 · **central £9.93** · no-cook at £8/day £10.21 · prices +30% £10.93 · stress (finance 6%, storage/ops +50%, losses doubled) £15.93 · severe stress £17.70.

**Priority schedule (what each pound buys, cumulative per person).** This answers ChatGPT's point that the £10 ceiling and the protected lines were incompatible under stress:

| Funding level | Buys |
|---|---|
| £1.53 | Week one: no-cook food, water, formula, tablets, premix, sacks |
| £5.14 | + operations: agency, local plans, priority fuel/power, last mile, security |
| £6.78 | + next season: seed (winter and spring), protected urea, UAN, soya meal |
| £7.48 | + imported staples: rice, oil, sugar, high-protein wheat |
| £8.10 | + pulses, oats, milk powder, canned fish |
| £9.93 | + 3 Mt food-grade grain |

**Fiscal honesty:** only Tier 1 (~£0.72bn of stock) sits on the public balance sheet. Tier 2's ~£2.0bn of stock and ~£0.5bn of new stores are financed by firms and paid for through prices (≈ £4.79 per person per year, a fraction of one percent of household food spend). A levy or a price pass-through moves the cost; it does not remove it.

## 2. What the 3 Mt of grain is for (cereal model, round 2)

`cereal_balance.py` now runs 36 months with a **1.0 Mt working-stock floor** (grain in mills, merchants and transit that cannot be drawn) and reports the minimum stock, as ChatGPT asked.

| Imports stopped 1 Jul; ethanol/distilling −75%; exports stopped | Feed level | Lowest stock | Extra reserve needed |
|---|---|---|---|
| Normal harvests | 100% | −1.28 Mt | **2.3 Mt** |
| Normal harvests | 90% | 1.43 Mt | 0 |
| Two −15% harvests, then normal | 80% | −1.54 Mt | **2.5 Mt** |
| Two −15% harvests, then normal | 70% | 1.25 Mt | 0 |
| Second harvest −35% (nitrogen), then normal | 80% | −2.52 Mt | **3.5 Mt** |

**Plain statement (Grok's challenge):** the 3 Mt does not replace a feed cut in a severe case. It **buys the choice not to cut feed by 10–30% at once**, which means not ordering a livestock destocking in year one of a shock. In a nitrogen shock it is not enough on its own (3.5 Mt needed at 80% feed). Earlier result corrected: draft-4's "normal harvests, full feed stays positive" had a minimum of only ~23 kt and failed in month 25 (ChatGPT).

## 3. Corrections accepted (by chapter)

| Ch. | Item | Correction | Source |
|---|---|---|---|
| 1, 3 | ECIU "four of the five worst harvests" | The 8 Oct 2026 ranking is **England, wheat + barley + oats + oilseed rape, by volume, since 1984** (pre-1999 estimated). 18.5 Mt is a separate 14 Aug "key crops" forecast. Say exactly that. | ECIU [R, Grok] |
| 1 | Livestock share of calories | **31%** in the Defra table (not 32%); land 84% of UAA | Defra [R] |
| 1 | Protein | §4.2 says **195%**; summary line 194%: keep "about 1.9×" | Defra [R] |
| 1 | 1984 peak | Defra narrative says "over 80% in the 1980s"; drop the exact 78% unless series named | Defra [R] |
| 2 | Fen peat "25–50 years left" | Not a national figure; use site-specific scenarios | ChatGPT |
| 2 | 7.8 t/ha | Derived (6.9/0.89), not a published mean: label [E] | — |
| 4 | NAO sentence | Now quotable: *"No specific food supply chain assets are currently included in the government's database of CNI assets."* (summary para 20). Defra had assessed no individual asset as sufficiently critical; first pass due by end-2026 | NAO, 4 Sep 2026 [R, both] |
| 4 | Single French quarry for flour chalk | **Recorded in UKFSR 2024 itself**: upgrade from [?] to [P] | UKFSR [R, ChatGPT] |
| 4 | AdBlue | 20 km/h is the **severe** inducement, after the tank is empty (or <2.5%) **and** a restart/refuel/park/time trigger; a torque cut comes first. Not an instant crawl. Cite Annex XIII **section 5** | Reg. 582/2011 [R] |
| 4 | Grain moisture | Safe storage depends on moisture **and** temperature, duration and condition; "above 14.5% self-heats" is too categorical | ChatGPT |
| 4 | Red diesel | Rebate £384m (2025) [R]; HMT said "almost £300m" in Mar 2026; a Jun–Dec 2026 duty cut changes it mid-year; 98% figure is 2024/25 | Grok |
| 4 | Peter Green Chilled ransomware | Gemini says Aug 2024; **rejected**: contemporary reporting dates it to **May 2025**, alongside M&S and Co-op | — |
| 5 | Imported grist | **~25% (Defra, UK 2025) to ~31% (UK Flour Millers 2024/25 table)**, not ~15%. High-protein tranche raised to 0.35 Mt | Defra, UKFM [R] |
| 5 | Feed wheat | Not automatically food grade: contaminants, assurance and variety matter, not only protein and falling number | ChatGPT |
| 8 | Swiss stocks | réservesuisse table, 1 Jan 2026: common wheat **160,000 t** + durum 20,000 t; sugar **50,000 t**; oils/fats **36,660 t**; rice 16,400 t; coffee **20,180 t (3 months, still compulsory)**; energy/protein feed **387,450 t** | réservesuisse [R, both] |
| 8 | Finland "about nine months" | The 2023 top-up is confirmed; nine months *held in Oct 2026* is not | NESA [R] |
| 8 | Singapore "since 1968" | Two months of imports confirmed; the year is not | MTI [R] |
| 9 | 1.514 Mt wheat | ≈ **39 days of all UK wheat use** (14.1 Mt/yr) or ≈ 32 days of national energy as raw wheat. Label the denominator | AHDB [R] |
| 9 | £420–830 per person shock | Label as an **illustration** (1–2% of GDP), not a measured loss | Grok |
| 9 | UAN "not Beirut" | UAN **contains** ammonium nitrate; UAN-32 can **salt out** near freezing into an AN-rich sludge; HSE warns AN–urea mixtures can be more sensitive. Hold **UAN-28, heated and recirculated**, get site-specific COMAH assessments | HSE [R]; Grok |
| 9 | "A third of a season" of N | BSFP 2025: UK N use **904 kt** (GB 817 kt). Draft-4's 350 kt was **39%**, and 0.5 Mt urea exceeded GB annual urea use (~0.38 Mt). Now **~162 kt N (~18% of a season)** as *extra pre-season merchant stock* that merchants can actually turn | BSFP [R] |
| 9 | Protected urea shelf life | Product-specific: BASF reports >12 months at 20 °C for its product; Gemini's 6-month rotation is not evidenced. Rotate annually, check each product's tested life | BASF [R] |
| 9 | Seed | Hold **spring** varieties separately: a wet autumn needs spring seed in March | Grok |
| 9 | Flour extraction | `EXTRACTION` was defined and unused. Now 85% (the 1942 "National Loaf" standard), bran to feed; illustrative survival day recomputed | ChatGPT |
| 9 | Refill within 12 months | Contradicts "never buy a stressed harvest". Now: **price-and-quality trigger, 36-month outer bound**, refill cash shown separately | Grok, ChatGPT |
| 9 | Formula | ~6–7 kt powder-equivalent for universal 90-day cover (~650,000 infants, ~100 g/day, +20%); split from medical foods; ready-to-feed for water/power loss | ChatGPT, Grok |
| 9 | Nutrition | Add **vitamin A and zinc** to the tablet; salt; part of the pulses pre-cooked/canned (90 g dry pulses a day is a gut problem). A dietitian-designed specification with variants is a **publication gate** | All three |
| 9 | NATO 1.5% | Declaration names "civil preparedness and resilience"; food is not named; accounting review in 2029. A bid, not income | NATO [R] |
| 11 | Agriculture's share of GHG | **~12–13%** depending on year (Defra AUK ch.11 says ~13% for 2024); 2022 agri-climate report: 47.7 Mt, **49% of methane, ~70% of N₂O** (draft said 59%) | Defra [R] |
| 11 | BNG statutory credits | **Two credits per unit**: £42,000 per credit means **£84,000 per unit** (£250,000 for the higher tier). Not market prices | GOV.UK [R] |
| 11 | "No free allowances" vs linking | The UK–EU common understanding requires **dynamic alignment**; "no free allowances now" is not compatible with linking on those terms. Reworded as advocacy for a **faster joint phase-out** | UK–EU summit text [R] |
| 11 | Carbon units | Separate **avoided emissions, temporary biological storage and durable removals**; they are not interchangeable tonnes | ChatGPT |
| 12 | FMD 2001 | Compensation ~£1.4bn; ~£8bn was the wider economic cost | PAC [R] |
| 12 | 2021 pig backlog | ~8,000 culled by late Oct 2021, ~40,000 by Feb 2022 (Lords Library); backlog 150,000–200,000 is not the number killed; **no compensation was paid** | Lords Library [R] |

## 4. Design changes beyond the model

1. **Destocking order rewritten** (note 21): stop births first; **bulk primal processing** instead of retail cuts; meat straight to public catering; **pre-agreed compensation** at a trailing-average deadweight price (2021 paid nothing, and farmers will not sign up to repeat it); rendering and animal-by-product capacity, with an anaerobic-digestion route pre-approved; a pre-drafted carcass-weight waiver; back-up electrical stunning kept serviceable; welfare killing kept separate from meat entering the food chain. Gemini adds that the UK has almost no red-meat canning left and that cold stores hold but do not freeze: blast-freezing is the bottleneck [S].
2. **Rationing reframed as a "Fair Shares Guarantee"** (note 21): purchase caps first, then statutory price caps on rationed lines, **paper ration books held in regional vaults** for a blackout, minimal personal data, appeals, and no documentation barrier to emergency food.
3. **Law:** the CCA 2004 *can* deliver rationing, price caps, directions and requisition (ChatGPT corrected our "cannot"), but regulations lapse after 30 days and need parliamentary approval. A **Food Security (Emergency) Act** builds the standing scheme; the CCA only switches it on.
4. **Governance:** the Cabinet Office holds the release key; Defra operates; Treasury and all devolved governments have formal roles. Seek an **ONS classification** before any financing claim. Barnett depends on spending classification, not on which department holds the budget.
5. **Northern Ireland:** NI grocery is still largely supplied from GB distribution centres [S, BBC Aug 2025]. A **statutory minimum stock on the island of Ireland** and NI-held no-cook stock.
6. **Trade (note 22):** call options and swaps work in calm markets and **fail in the export-ban case** the briefing cites. Option premiums need valuation, not a 3–5% guess. Paying firms' carrying costs can be a subsidy under the Subsidy Control Act 2022 unless structured as a uniform obligation. WTO Agriculture Annex 2 covers qualifying food-security stockholding. IEA oil "stock tickets" are a real contractual precedent, but they assume a working world market.
7. **Work after AI (note 23):** no evidence that displaced office workers move into land work (Pick for Britain is counter-evidence). Replace "tens of thousands" with a **costed pilot**: 10,000 jobs at ~£35k fully loaded ≈ £350m/yr.
8. **Headline acceptance test** (ChatGPT): *the share of people receiving a safe, appropriate ration and drinking water within 24, 72 and 168 hours, by locality and need group.*

## 5. Name

ChatGPT and Gemini recommend **UK Strategic Food Reserve** (clearest to Parliament; echoes the US Strategic Petroleum Reserve). Grok prefers **UK Food Resilience Reserve**, arguing "strategic" invites a price-stabilisation and WTO public-stockholding reading. **Decision: keep "UK Strategic Food Reserve"**, with the public explainer *"emergency food stocks, rotated through normal supply chains"*, and state in the text that it is not a price-support scheme.

## 6. Rejected or not adopted

- Gemini: "refill levy on post-crisis supermarket sales": it taxes food at the worst moment. We keep a refill rule funded from general taxation instead.
- Gemini: "state buys culled meat at 110% of the five-year average": over-compensation invites gaming. We use a trailing-average deadweight price.
- Gemini: EPOS purchase caps "by National Insurance number": a privacy and exclusion risk. We use offline paper entitlements with minimal data.
- Gemini: "mills run at 80–85% so 15–20% surge exists": no source. Grok and ChatGPT found no published surge figure. Still open.
- Gemini: Peter Green Chilled in Aug 2024: contradicted by contemporary reporting (May 2025).

## 7. New adversarial scenarios adopted

Refill rule meets a second bad, mycotoxin-hit harvest · UAN salts out in a cold snap · contractor sells the grain and fails (title found in the crisis) · cyber attack on the stock ledger in a heatwave · geomagnetic storm (transformers and GNSS, months not days) · 30% absenteeism at mills, abattoirs and HGV rosters · Irish Sea ferries stop while a GB retailer is offline · CO₂ and AdBlue fail together (both urea/gas chains) · export bans void partner options · wrong seed (winter in store, spring needed) · a devolved government rejects the release · water-treatment chemicals run out · single-national-flour allergen mis-pack · sterling falls during refill · phosphine-resistant insects across "independent" sites using one contractor · back-to-back crises · no-cook need exceeds 10 m when everyone's cooker is off · announcement-triggered panic.

## 8. Still open

Flour-mill surge capacity; site-specific COMAH status of UAN-28 tanks; ONS classification of Tier 2 obligations; Subsidy Control Act treatment; NI landbridge food-tonnage share; dietitian-designed ration and variants; UK rice, oil, SMP and canned-fish market absorption figures (the use figures in the model are rounded orders of magnitude: rice ~670 kt (USDA London Post forecast), rapeseed oil ~406 kt (market-research snippet), others [?]); a priced last-mile service; Defra's FOI reply (~18 Nov 2026).
