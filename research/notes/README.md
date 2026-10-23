# Research notes: UK food security, climate and regeneration

Research phase for a ~12-page PDF (one page per chapter). Date: 23 October 2026 (after adversarial review rounds 1 and 2, notes 20 and 24).
Built on: four AI briefings (Claude, GPT, Gemini, Grok), the Claude research dossier, the GPT evidence notes and the cross-briefing gap analysis.

**How to read the labels:** **[P]** primary source · **[S]** secondary · **[E]** our own calculation or model · **[?]** not yet verified.
**Limit:** this session could search the web but not open gov.uk, nao.org.uk and similar pages directly. Check [P] figures against the originals before publication.

---

## The PDF, chapter by chapter (and which notes feed each page)

| # | Chapter | Notes |
|---|---|---|
| 1 | **Can Britain feed itself?** Resilient on paper, fragile in practice | 09, dossier Part 1 |
| 2 | **Nature's gift:** world-class yields per hectare, land-poor per person, soils that can recover | **18**, dossier Parts 4–6 |
| 3 | **Climate is changing the odds:** compound extremes, Europe failing together, new pests | 07 |
| 4 | **Hidden dependencies:** nitrogen, phosphorus, potash, diesel, CO₂, cyber, cold chain | 01, 03, 06 |
| 5 | **Protein, livestock and the sea:** soya, feed-to-food, fewer and better animals, fish | 02, 09, 15 |
| 6 | **Geopolitics and prices:** Hormuz, Black Sea, export bans, food as foreign policy, stabilising neighbours | 05, 19, 22 |
| 7 | **Food and stability:** "nine meals", unrest evidence, fairness, local plans | 10, 11 |
| 8 | **How other countries prepare:** Finland, Switzerland, Norway, Japan… and the UK's empty shelf | 13, 14 |
| 9 | **The UK Strategic Food Reserve, £10 per person per year:** survival ration, protein feed, seed, safe nitrogen, food-grade grain, fuel and plans; rotation; honest break-even | 16, 17, 20, 24, 25 |
| 10 | **Work, wellbeing and the AI economy:** a regenerative transition corps | 04, 19, 23 |
| 11 | **A new economy of food:** one carbon price, full-cost accounting, culture, the four nations | 08, 12, 19, 23 |
| 12 | **The plan:** store, the contingency ladder (rationing, livestock, nitrogen), grow for people, close loops, draw down carbon, governance | 15, 17, 19, 21 |
| 13 | **Running it:** a lean (~60), open, automated agency; port hubs, district stores, local points | 26 |

## All notes

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
| 17 | Insurance framing: from the £2 entry tier to the £10 Strategic Food Reserve |
| 18 | Nature's gift: how the UK really stacks up |
| 19 | The big picture: carbon markets, geopolitics, culture, regenerative farming and AI |
| 20 | Adversarial review round 1 (ChatGPT, Gemini, Grok): findings, decisions, corrections |
| 21 | The contingency ladder: rationing, the livestock destocking order, safe nitrogen |
| 22 | Stabilising the region, trade and mutual support (earning without gouging) |
| 23 | Our position: one carbon price, work in nature after AI, the consciousness shift |
| 24 | Adversarial review round 2: the hybrid redesign (market sizing, debt, week one, destocking, rationing) |
| 25 | Human food first, food for everyone, and the jobs |
| 26 | Running it: a lean, open, automated agency and a decentralised network |

Draft briefing for fact-checking: `draft/briefing_full_context.md` (draft-5: the Strategic Food Reserve, about £10 per person per year, hybrid design; downsides integrated as proactive criticism).

Models: `research/model/cereal_balance.py` (month-by-month grain stocks) and `research/model/reserve_basket.py` (v3: hybrid cost model, market check, sensitivity, priority schedule, break-even). Run with `python3`.

## Key findings

1. **About one month of wheat at the pre-harvest low** (1.514 Mt ≈ 32 days of raw-wheat energy), privately owned and not earmarked; the AHDB balance has a 794 kt unexplained residual. Wheat, barley and oats together ≈ 2 months of raw-grain calories. (01, 20)
2. **In the tonnage model, grain balances stay positive; protein feed, fertiliser, milling and logistics are the likely binding constraints.** Pigs and poultry shrink when soya stops. (09, 20)
3. **2026: the UK, France and Germany lost harvests together.** Trade insurance fails when the neighbours claim too. (07)
4. **Two chokepoints in one year**, Hormuz and the Black Sea; in 2022, export bans covered 17% of traded calories. (05, 19)
5. **The risk is affordability:** food inflation 1.3% (Sep 2026; CPI 3.5%), yet 12.2% of households are food-insecure. (05, 10)
6. **Several comparable countries hold reserves; the UK holds none.** Finland 6–9 months of grain, Switzerland 2–4 months by product. (13, 14)
7. **The UK Strategic Food Reserve: about £10 per person per year (£10.24 central), human food first and food for everyone.** Bread from 4 Mt of food-grade wheat (~10 months of milling), a 3-day no-cook grain ration and vitamin tablets for all 69.5 m, specialist food for those who need it, plus seed, safe nitrogen, soya meal and imported staples. A public crisis tranche (~£5 via taxes) plus compulsory commercial stocks (~£5 via prices), rotated into mills, feed and export; ~1,000 permanent jobs and a lean ~60-person agency. (16, 17, 20, 24, 25, 26; `reserve_basket.py` v3.1)
8. **Per hectare, Britain is world-class** (wheat-yield world record, Lincolnshire); **per person, it is land-poor** (~⅓ of France's arable per head). Soils can recover: one Rothamsted clover-ley rotation raised topsoil carbon concentration by about a quarter in 28 years (one site). (18)
9. **Carbon money is shifting to durable removals** (UK ETS from 2029, EU carbon-farming rules from 2026); soil-carbon offsets remain low-trust. (12, 19)
10. **Nature work helps people and resilience at the scale of tens of thousands of jobs, not millions.** AI is the enabler (precision spraying, robots, data-centre heat), not the enemy. (04, 19)
11. **A contingency ladder above the reserve:** fair rationing principles, a livestock destocking order and safe nitrogen, written in advance (21). **Second-order:** the reserve can stabilise neighbours and earn modest income at fair, pre-agreed prices (22).
12. **Position:** one consistent carbon price, no free allowances, no subsidies for emitting, CO₂ as a commodity; a labour bridge from AI-disrupted work into low-carbon farming (23).

## Corrections to the earlier briefings
- Claude PDF: "food inflation could reach 9% this year" has been overtaken (1.3% in Aug 2026).
- All: protein "194%" is not closed-loop; imported soya carries about the population's whole protein need.
- Gemini: "+300% farm labour", "precision-fermentation patriotism", "vertical farms as grid stabilisers", "global carbon market by 2030" and "UK ranks with Ukraine's chernozem" are unsupported.
- The Lagi "210" riot threshold doesn't apply to today's rebased FAO index.
- SFI26 Window 2: £180m base (+ rollover) vs the dossier's "~£253m"; reconcile.

## Open items
1. Verify the key [P] figures against originals (NAO report PDF, AHDB Sep 2026 workbook, Food Foundation, Swiss stock figures, FAOSTAT yields and land per person).
2. Add a protein ledger and onset-month option to the cereal model; get flour-mill surge capacity.
2b. Quotes for storage, stores, fuel contracts; a dietitian-designed ration with variants; COMAH status of UAN; urea inhibitor shelf life (notes 20, 21).
3. Scotland's 2026 support tiers; NI per-hectare rate.
4. Salmon feed import share; mussel and oyster production.
5. A worked local resilience forum (LRF) food plan example.
6. Defra's reply to the FOI request (due ~18 Nov 2026).
