# 20 · Adversarial review, round 1: what three AIs found and what we changed

Date: 23 October 2026. Reviewed: `draft/briefing_full_context.md` draft-3, the combined notes and both models.
Reviewers: ChatGPT ("adversarial audit"), Gemini ("structural audit and stress test"), Grok ("robustness memo v2"). All three ran or re-derived the models.

**How to read this note.** Agreement between AIs is not verification. Where a reviewer says it opened a primary source, we label the item **[R]** (reviewer-checked; we have not opened it ourselves). Where a reviewer gives a figure from memory, it stays [S] or [?]. Our own decisions are marked **Accepted**, **Partly accepted** or **Rejected (with reason)**.

---

## 1. The big findings (all three reviewers, or decisive on their own)

| # | Finding | Reviewer(s) | Decision | What changed |
|---|---|---|---|---|
| 1 | **The £10 total was a budget, not a cost.** Line F (operations, £158m) was `budget − (A…E)`, a plug. | GPT, Grok | **Accepted** | `reserve_basket.py` v2 costs every line bottom-up. Operations are itemised (£156m). The total is now an output: **£701m ≈ £10.08 per person**, with a published range (below). |
| 2 | **The 350 g wheat ration cannot be milled.** 350 g × 69.5 m = 24,300 t/day ≈ 1.8× what UK mills actually use (4.8–4.9 Mt/yr). Usage is not capacity, but no surge figure exists. | GPT, Grok | **Accepted** | Wheat cut to **180 g/day** (95% of demonstrated mill use). Calories moved to rice (already milled), oil and pulses. A grain stock is now described in **days of mill intake**, not "days of national calories". |
| 3 | **"Complete diet" was not shown.** Calcium only reaches ~1,060 mg if the flour is fortified at the mill; unfortified it falls to ~520–690 mg. Iodine via "iodised salt" is not how UK food works. | GPT, Grok, Gemini | **Accepted** | Renamed **survival ration**. Premix (calcium, iron, niacin, thiamin, folic acid) and potassium iodate are now stocked (line D). A dietitian-designed set of variants (children, infants, allergies, medical) is an open item. |
| 4 | **Flat 25% rotation contradicts the shelf lives in our own file** (oil and oats 1–2 years, milk powder 2–3). | GPT, Grok | **Accepted** | Rotation = 1 ÷ shelf life for each item. "Oils keep several years" is deleted. |
| 5 | **Seed was costed like grain.** Seed must be turned every year and loses its premium when sold as grain. 0.3 Mt is about half a season of cereal seed. | Grok | **Accepted** | Seed line costs the £100/t premium lost every year. Wording: "half a season of cereal seed, turned yearly". |
| 6 | **Storing ~1 Mt of ammonium nitrate is a Beirut problem.** COMAH, counter-terrorism, planning. | Gemini, Grok, GPT | **Accepted** | Nitrogen is held as **protected urea and UAN solution**, sized on a nutrient basis (~350 kt N, about a third of a season), and rotated through merchants. No ammonium-nitrate stockpile. See note 21 §4. |
| 7 | **The binding import is soya, yet the £10 table spent nothing on it.** | Grok | **Accepted** | New line P: **10 weeks of soya meal** (~460 kt) as a Swiss-style compulsory stock: ~£20m/yr. |
| 8 | **"No waste", "minimal downside", "shelves stay full", "no electricity", "106 days of national calories"** are claims a hostile reader will use. | All three | **Accepted** | Deleted throughout. Replacements: "designed to minimise losses through planned rotation"; "no refrigeration; low, interruptible power"; "a reserve buys time, if we can turn it into meals". |
| 9 | **Break-even assumed the reserve prevents 100% of a shock.** | GPT, Grok | **Accepted** | Break-even now shown against the share of loss prevented (table below). |
| 10 | **Week one of a blackout is not solved by grain.** Fuel, power, cyber, water and cooking fail first. | GPT, Grok, Gemini | **Accepted** | New line R (no-cook tranche for 10 m vulnerable people) and itemised fuel/backup power, offline operations and drinking-water contracts in F. Chapter 4 adds AdBlue, automated warehouses and grain-dryer fuel. |
| 11 | **One stock, three promises** (human backup, feed buffer, overseas aid) collide in a joint shock. | GPT | **Accepted** | Rule: **human food first**, a protected domestic minimum, aid and feed only from stock above it. |
| 12 | **Food *is* a critical-national-infrastructure (CNI) sector.** The NAO's point is narrower: Defra has not identified food-supply *assets* in the CNI Knowledge Base. | GPT [R], Grok [R] | **Accepted** | Chapters 4 and 12 reworded. |
| 13 | **Bundling the reserve with livestock, carbon and AI lets each lobby kill the other half.** | GPT, Grok | **Partly accepted** | We keep the big picture (it is the point of the project), but the briefing now states a **firewall**: the reserve case stands on its own; the system change is a companion argument. |
| 14 | **Drop the name "National Insurance (not National Insurance)"**, which collides with a tax. | GPT, Grok | **Rejected (deliberate)** | The irony is the hook and is meant to be noticed. For legal and technical text we add a plain working title: **National Food Resilience Reserve**. |
| 15 | **Put the agency under the Cabinet Office, fund it outside the annual Defra budget, write release and refill rules into law.** | Gemini, Grok, GPT | **Accepted** | Governance block in chapter 12. |
| 16 | **Promise the reserve will damp inflation and lower gilt yields.** | Gemini | **Rejected** | Reserves are poor price stabilisers, and release for prices competes with emergencies (World Bank/FAO/WFP 2025). We promise time and access, not prices. |
| 17 | **Upgraded headline: "eliminate the risk of empty shelves".** | Gemini | **Rejected** | Overclaims; the opposite of what reviewers 1 and 3 asked for. |

## 2. The model after review (v2), in one table

`research/model/reserve_basket.py`. All prices and fees are assumptions, not quotes.

| Line | Component | Stock | Stock value | Annual cost | £/person/yr |
|---|---|---|---|---|---|
| A | 90-day survival ration for everyone (mill-feasible basket + vitamin tablets) | 3.50 Mt | £2.54bn | £225m | 3.24 |
| B | Rice and oil extended to 6 months (the import-dependent items) | 1.18 Mt | £0.77bn | £72m | 1.04 |
| C1 | Cereal seed, ~half a season, turned yearly | 0.30 Mt | £0.09bn | £38m | 0.55 |
| C2 | Nitrogen ~350 kt N as protected urea + UAN (no ammonium nitrate) | 0.90 Mt product | £0.31bn | £36m | 0.51 |
| P | Protein feed: 10 weeks of soya meal (compulsory stock) | 0.46 Mt | £0.21bn | £20m | 0.29 |
| Q | High-protein milling wheat tranche (gluten for the loaf) | 0.15 Mt | £0.04bn | £4m | 0.06 |
| R | No-cook tranche: 7 days ready-to-eat for 10 m vulnerable people | 0.07 Mt | £0.17bn | £24m | 0.34 |
| D | Formula, flour premix, iodine, feed amino acids, yeast (allowances) | – | £0.08bn | £11m | 0.16 |
| E | Food-grade grain, 3 Mt, in new stores (human first; feed and aid above the floor) | 3.00 Mt | £0.63bn | £115m | 1.65 |
| F | Operations, itemised: agency £40m, local plans £36m, priority fuel and backup power £40m, offline ops and exercises £10m, security and testing £15m, last mile and water £15m | – | – | £156m | 2.24 |
| | **Total** | **~9.6 Mt** | **~£4.8bn** | **~£701m** | **~£10.08** |

**Range (sensitivity, not a confidence interval):** gilt-guaranteed finance £9.19 · central **£10.08** · prices +30% £11.49 · stress (finance 6%, storage +50%, rotation losses doubled) £16.06 · severe stress (stress plus prices +30%) £18.46. Keeping 5 Mt of grain instead of 3 Mt: £11.18.

**How to say it:** "£10 per person per year is our funding envelope. Our bottom-up estimate is about £10; under stress it could reach £16–18. If quotes come in higher, grain tonnage shrinks first; protein, seed, premix and the no-cook tranche do not."

**Cash, not just cost:** the stock (~£4.8bn, ~£70 per person) and new stores (~£0.6bn, ~£9 per person) are bought up front. Inventory is an asset, but the cash is spent while the reserve stays full, and refilling after a release needs its own funding rule.

**Daily survival ration:** 560 g of listed commodities (wheat 180, oats 30, rice 130, pulses 90, rapeseed oil 55, sugar 25, skimmed milk powder 25, canned mackerel or herring 25), plus vitamin C and D tablets. That gives ~2,240 kcal, ~70 g protein, ~27% of energy from fat, and calcium ~740 mg if the flour is fortified (~520 mg if not). About £0.41 per day at wholesale.

**Break-even, honestly:**

| Shock (share of GDP) | Share of loss the reserve prevents | Pays for itself if the shock happens once every… |
|---|---|---|
| 1% | 100% | 41 years |
| 1% | 25% | 10 years |
| 1% | 10% | 4 years |
| 2% | 50% | 41 years |
| 2% | 25% | 21 years |

These are thresholds, not probability estimates. A fuel or cyber shock is mostly *not* prevented by grain; an import or harvest shock is.

## 3. Factual corrections by chapter

| Ch. | Claim | Verdict | Correction | Source |
|---|---|---|---|---|
| 1 | 60% production-to-supply | Correct; context | The fall from 65% is mostly an **import-price** effect; volume barely changed. Never imply farms produced 5% less. | Defra AUK ch.14 [R]; FarmingUK / Farmers Weekly, Jul 2026 [S] |
| 1 | 101% of energy need | Correct; sharpen | 2,150 kcal produced vs 2,119 required = **101.5%**, a margin of **31 kcal** per person per day. | Defra nutritional supply 2025 [R] |
| 1 | 190–195% of protein | Inconsistent inside source | Use "about 1.9 times". | Defra [R] |
| 1 | Soya carries the population's protein need | Arithmetic correct; misleading | 2.39 Mt × ~47% ≈ 1.12 Mt protein vs ~1.17 Mt reference need, but it is **upstream, inside animals, not edible**. 77% goes to pigs and poultry. | AIC 2024 imports [S] |
| 1 | Livestock use 85% of farmland | Update | Defra now says **84% of UAA and ~56% of croppable area** feed livestock (stated assumptions). | Defra AUK 2025 ch.2 [R] |
| 1–9 | Calorie denominators | Inconsistent | Defra requirement 2,119 kcal; our planning figure 2,250 kcal. Label which one is used; never mix them in a sentence. | — |
| 2 | 71% of farmland is grass | Correct | 71.3% from table 2.1; do not add sole-right rough grazing twice. | Defra table 2.1 [R] |
| 2 | World-record wheat yield | Correct; misleading as system proof | One field. The system claim is a national average ~8 t/ha, about twice the world average. | — |
| 2/12 | Soil carbon +25% | Misleading | +0.25 percentage points (0.98% → 1.23%), ≈25% relative *concentration*, one sandy loam, then a plateau. Not a stock change, not UK-wide. | Johnston et al. 2017 |
| 4/12 | "No food assets in the CNI database" | Partly verified | Food **is** one of 13 CNI sectors. The NAO says Defra should identify food-supply assets in the CNI Knowledge Base. Quote the PDF before using the stronger sentence. | NAO, 4 Sep 2026 [R] |
| 4 | Single French quarry for flour chalk | Unverified | Keep [?]; the action (stock premix) does not depend on it. | — |
| 5 | Mills process 5–5.5 Mt | Outdated | **4.8 Mt wheat milled, 3.8 Mt flour (2025)**; ~15% of the grist imported (largely for gluten strength). | UK Flour Millers [R] |
| 5 | Feed wheat can feed people | Correct for porridge, flatbreads, wholegrain; **not for the Chorleywood loaf** without blending | High-speed bread needs ~13% protein and a Hagberg falling number of ≥250 s. Hold a high-protein tranche (line Q) and publish an emergency grist / flatbread standard. | Gemini [S] |
| 5 | Beans replace soya | Misleading | Faba beans are short of methionine and contain anti-nutritional factors (vicine/convicine, tannins). Replacing soya needs synthetic amino acids (imported) and low-vicine varieties. 1 Mha of beans ≈ 16% of croppable land, at the rotation ceiling. | Gemini, Grok [S] |
| 5 | Mackerel is "the protein we already have" | Misleading | Pelagic catches are concentrated in autumn–winter; the UK has little fish-canning capacity. Contract winter canning/pouching or buy canned stock. | Gemini [S] |
| 6 | Food inflation 1.3% (Aug), CPI 3.1% | Update | **Sep 2026: food 1.3%, CPI 3.5%.** | ONS [R] |
| 6/11 | CBAM on fertiliser | Correct; qualify | Covers named commodity codes, not every product; indirect emissions delayed to at least 2029; no universal £50/t. | HM Treasury factsheet [R] |
| 8 | "Britain alone among its peers" | Unsupported comparison | "Several comparable countries maintain reserves; Britain has none." | — |
| 8 | Finland ~€16 per person | Funding flow, not cost | €66m levy revenue plus ~€25m budget; fund ~€2bn, much of it inventory. | NESA [R] |
| 8 | Switzerland 3–4 months | Overgeneralised | **2–4 months depending on product**; actual stocks can differ from targets. | FONES [R] |
| 8/13 | Switzerland dropped coffee (2019) | Wrong | 2019–20 was a **proposal**; the official list still shows coffee at three months. | FONES search extract [R], swissinfo [S] |
| 9 | 1.514 Mt ≈ 1 month | Correct with label | ≈32 days of raw-wheat energy (3.27 Mcal/t, 2,250 kcal). The same AHDB balance has a **794 kt unexplained residual**: print both facts; it is not a range. Merchant stocks of home-grown wheat were 451 kt (Jun 2026). | AHDB [R] |
| 9 | Pooled opening stock 2.95 Mt | Rounded | 3.006 Mt (wheat 1.514 + barley 1.337 + oats 0.155). | AHDB [R] |
| 9 | NATO 1.5% counts food reserves | Unestablished | The Hague 2025 text lists "civil preparedness and resilience". Whether food stocks count is a case to make, not an accounting fact. | Gemini [S] |
| 9 | Household kit vs state "tenfold efficiency" | Withdrawn | Mixed retail ready-to-eat with wholesale raw ingredients, and stock with carrying cost; omitted the last mile. | GPT |
| 9 | 2,000 jobs from operations | Inconsistent | 2,000 posts at ~£60k would use £120m of a £156m operations line. Now: ~400 agency staff plus jobs inside storage contracts, construction and local plans: "around 1,000–2,000 jobs, most inside contracts". | GPT |
| 11 | Danish-style tax on UK = £0.65–1.6bn | Over-broad | Applies to livestock emissions (enteric + manure, ~30 MtCO₂e [E]), not all 47 Mt: **~£0.4bn (2030 effective rate) to ~£1bn**. | GPT; our recalculation [E] |
| 12 | Household food waste = 28–42 days of energy | Unverified as stated | True only at 1.0–1.5 kcal per gram of mixed waste; show the density. It is a demand reduction, not a reserve. | Grok; our check [E] |
| model | Scenario D fails "month 25" | Wrong label | Was month 13; with corrected opening stock it is month 24. Scenario B already assumed exports stop (renamed). The unused `start` parameter was removed. | GPT |

## 4. New risks added to the ledger (mostly from Gemini and Grok)

- **AdBlue.** Euro VI lorries need diesel exhaust fluid (urea solution). When it runs out, the engine-management system cuts power to a crawl (a "limp mode" of about 20 km/h under the Euro VI rules [S]). South Korea's 2021 urea shortage threatened its freight network. Add AdBlue to the fuel plan.
- **Automated distribution centres.** Robotic high-bay warehouses and cloud warehouse-management systems stop without power and data. Ask for 72-hour fuel at tier-1 depots and a "degraded mode" manual-picking plan.
- **Grain dryers.** British grain is often harvested at 16–20% moisture and must be dried below ~14.5% or it self-heats. In a wet autumn the queue is at the dryer, which runs on gas, diesel or electricity.
- **Phosphine** (stored-grain fumigant) and **food-grade CO₂** (stunning, packaging) are concentrated chemical inputs. Non-CO₂ stunning (electrical, inert gas) is the backup.
- **Synthetic amino acids** for pig and poultry feed are made by a handful of firms abroad. Stock is tiny in volume (line D).
- **Folic acid fortification** of non-wholemeal wheat flour becomes mandatory from **13 December 2026** (England regulations; check devolved equivalents) [S]. The premix stock must include it.
- **Devolution and Barnett.** If funded as a Defra programme, Barnett consequentials flow to Scotland, Wales and NI as general budget. A UK-wide civil-contingencies function avoids that, but needs agreement with the devolved governments, and **sites in all four nations** (eastern English silos do not feed Northern Ireland if the ferries stop).
- **Crowding out and additionality.** Contracts must be *on top of* a measured commercial baseline, or firms hold less and the public tonne just replaces a private one.
- **Insolvency and title.** Contracts must give the state clear title, access and quality liability, or a bankrupt contractor's warehouse receipts become a dispute.
- **Common-mode failure.** Ten stores on one power network, one contractor or one software platform are not ten independent safeguards.

## 5. New tests the reserve must pass (adopted from GPT §9)

July import stop before harvest · national power loss with fuel disrupted · cyber attack on the reserve contractor and retailers · floods hitting several stores and roads · two poor harvests plus less fertiliser · a wet harvest that downgrades grain to feed · livestock disease during a feed shock · reserve drained for prices just before a real emergency · a major stockholder goes bust · imported oil or formula fails while grain is plentiful · low-income households cannot pay or collect · the UK and aid partners need the same grain.

**Headline metric adopted:** *person-days of suitable nutrition delivered under the scenario.* It exposes what national tonnes and average calories hide.

## 6. Still open (not certified by any reviewer)

Flour-mill surge capacity; oat, rice and pulse processing capacity; fish canning capacity; infant-formula tonnage; Northern Ireland's ferry share of calories; British Survey of Fertiliser Practice nutrient tonnes; the NAO PDF's exact sentence on CNI assets; Finland's current months versus legal minimum; Swiss tonnages; ECIU harvest series definition; COMAH thresholds for UAN; shelf life of inhibitor-treated urea; Defra's FOI reply (~18 Nov 2026).
