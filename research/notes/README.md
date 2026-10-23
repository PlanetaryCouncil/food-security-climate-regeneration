# Research notes: UK food security, climate and regeneration

Research phase for a ~12-page PDF (one page per chapter). Date: 22 October 2026.
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
| 6 | **Geopolitics and prices:** Hormuz, Black Sea, export bans, food as foreign policy | 05, 19 |
| 7 | **Food and stability:** "nine meals", unrest evidence, fairness, local plans | 10, 11 |
| 8 | **How other countries prepare:** Finland, Switzerland, Norway, Japan… and the UK's empty shelf | 13, 14 |
| 9 | **The National Insurance (not National Insurance), £10 per person per year:** a storable full diet + multi-purpose grain, rotation, no waste, ROI | 16, 17 |
| 10 | **Work, wellbeing and the AI economy:** a regenerative transition corps | 04, 19 |
| 11 | **A new economy of food:** carbon markets, full-cost accounting, culture, the four nations | 08, 12, 19 |
| 12 | **The plan:** store, grow for people, rebalance, close loops, draw down carbon | 15, 17, 19 |

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
| 17 | Insurance framing: from the £2 entry tier to the £10 National Insurance |
| 18 | Nature's gift: how the UK really stacks up |
| 19 | The big picture: carbon markets, geopolitics, culture, regenerative farming and AI |

Draft briefing for fact-checking: `draft/briefing_full_context.md` (the National Insurance, £10 per person per year; downsides integrated as proactive criticism).

Models: `research/model/cereal_balance.py` (month-by-month grain stocks) and `research/model/reserve_basket.py` (cost of a complete storable diet). Run with `python3`.

## Key findings

1. **About one month of wheat at the pre-harvest low**, privately owned and not earmarked. Wheat, barley and oats together ≈ 2 months of calories. (01)
2. **Grain isn't the binding constraint; protein feed and fertiliser are.** Pigs and poultry shrink when soya stops. (09)
3. **2026: the UK, France and Germany lost harvests together.** Trade insurance fails when the neighbours claim too. (07)
4. **Two chokepoints in one year**, Hormuz and the Black Sea; in 2022, export bans covered 17% of traded calories. (05, 19)
5. **The risk is affordability:** food inflation ~1.3% (Aug 2026), yet 12.2% of households are food-insecure. (05, 10)
6. **The UK is an outlier:** no public or compulsory food reserve; Finland holds 6–9 months, Switzerland 3–4. (13, 14)
7. **A complete diet can be stored and rotated with near-zero waste.** The headline policy is **the National Insurance (not National Insurance): £10 per person per year** (~£695m): a 90-day complete ration for everyone, 6 months of oils/rice/pulses, seed and nitrogen, 5 Mt of multi-purpose grain (human backup / feed buffer / overseas aid) and the operations to run it. (£2 buys ~8 weeks of complete food.) (16, 17; `ten_pound_package()`)
8. **Per hectare, Britain is world-class** (wheat-yield world record, Lincolnshire); **per person, it is land-poor** (~⅓ of France's arable per head). Soils can recover: +25% soil carbon in 28 years with clover leys. (18)
9. **Carbon money is shifting to durable removals** (UK ETS from 2029, EU carbon-farming rules from 2026); soil-carbon offsets remain low-trust. (12, 19)
10. **Nature work helps people and resilience at the scale of tens of thousands of jobs, not millions.** AI is the enabler (precision spraying, robots, data-centre heat), not the enemy. (04, 19)

## Corrections to the earlier briefings
- Claude PDF: "food inflation could reach 9% this year" has been overtaken (1.3% in Aug 2026).
- All: protein "194%" is not closed-loop; imported soya carries about the population's whole protein need.
- Gemini: "+300% farm labour", "precision-fermentation patriotism", "vertical farms as grid stabilisers", "global carbon market by 2030" and "UK ranks with Ukraine's chernozem" are unsupported.
- The Lagi "210" riot threshold doesn't apply to today's rebased FAO index.
- SFI26 Window 2: £180m base (+ rollover) vs the dossier's "~£253m"; reconcile.

## Open items
1. Verify the key [P] figures against originals (NAO report, AHDB Sep 2026 tables, ONS CPI, Food Foundation, Swiss stock figures, FAOSTAT yields and land per person).
2. Add a protein ledger and milling-capacity limit to the cereal model.
3. Scotland's 2026 support tiers; NI per-hectare rate.
4. Salmon feed import share; mussel and oyster production.
5. A worked local resilience forum (LRF) food plan example.
6. Defra's reply to the FOI request (due ~18 Nov 2026).
