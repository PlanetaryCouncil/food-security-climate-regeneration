# Page 13 · The honest downside, and why it is still the reasonable thing to do

**Standalone page** (does not modify chapters 1–12 in `draft/briefing_full_context.md`). Draft 22–23 October 2026.
**For the reviewing AI:** same rules as the main briefing. Check every numbered claim (CORRECT / WRONG / OUTDATED / UNVERIFIABLE / MISLEADING), give primary sources, and list counter-evidence. Labels: **[P]** primary (via search extract) · **[S]** secondary · **[E]** authors' estimate or model · **[?]** unverified.

---

**Headline:** A food reserve costs money, needs warehouses and must be guarded. So does an army. This one defends against hunger.

**Narrative:**
A strategic food reserve is not free. It needs warehouses, materials, staff, security and money tied up in stock. It can be mismanaged, raided by politicians or targeted by saboteurs. We say so plainly.

But look at what it is: a **stabilising force**, held in readiness the way a nation holds an army. You hope never to use it. If supply chains break — a war at sea, a cyber attack, a failed harvest across Europe, a week without power — it kicks in, keeps shelves stocked and prices calm, and buys the weeks the country needs to adapt. No government wants its citizens going hungry, queuing outside empty shops, or watching anger turn into looting. A reserve is the precaution that makes that far less likely.

The costs are modest and largely recovered. Dry grain, pulses, oils, powders and tins need **no refrigeration**: stores run on a little ventilation, not a power-hungry cold chain. Stock is rotated before it ages into school meals, hospitals, food banks, mills and animal feed, so nothing is wasted. Building and running it creates skilled jobs across the country, a bonus rather than the reason. At **£10 per person per year, under 3p a day**, it costs about **1% of what Britain spends on defence**. It is the reasonable, grown-up thing to do.

---

## A. The honest downside (included claims)

1. **It costs money.** The £10 policy costs ~**£695m a year** (£10 × 69.5 m people); the stock (~11.5 Mt) is worth ~**£4.7bn**, tied up but recovered as it is rotated and sold. `research/model/reserve_basket.py` [E]
2. **It needs new warehouses.** About 5 Mt of the multi-purpose grain needs new storage at an assumed ~£200 per tonne of capacity (~**£1bn capital**), amortised over 25 years. Existing merchant and farm stores can take part of the rest under contract [E; capex per tonne to be checked]
3. **It needs materials and land:** silos, sheds, tanks for oils, pallets, packaging for powders and tins, and secure sites near mills and distribution centres [E]
4. **Rotation sells older stock at a discount** (modelled at 5% on ~¼ of stock a year) [E]
5. **Building it can push up prices** if bought too fast; Japan's 2026 rice buyback was criticised as "too late", and large purchases in tight markets raise prices for others. https://english.adnkronos.com/2026/09/01/japan-govt-to-buy-back-210000-tons-of-rice-after-stockpile-release/ [S]
6. **It can be mismanaged.** India's auditor found **4.72 lakh tonnes of wheat (₹700 crore) deteriorated** in Punjab in 2011–16 through open storage and not using stock oldest-first. https://www.tribuneindia.com/news/punjab/wheat-worth-rs-600-cr-allowed-to-rot-cag-48189 [S]
7. **It can be raided by politicians.** Finland tried in 2025 to cut its reserve from 9 to 6 months to save ~€20m (~£17m); Japan's rice reserve fell to **320,000 t against a 1 Mt target** after being used to manage prices. https://www.mtvuutiset.fi/artikkeli/keskusta-huolestui-viljan-varmuusvarastojen-vahenemisesta-ymmartaako-hallitus-taysin-mista-on-kyse/9096310 [S]
8. **It can be a target for sabotage, theft or attack.** Sweden keeps the locations of its new grain stores secret for this reason. https://www.thelocal.se/20251014/sweden-to-establish-emergency-grain-stocks-in-north [S]
9. **Grain stores carry physical hazards:** dust explosions (ignition from overheated bearings, slipping belts, hot work) and fires from self-heating grain. https://www.fireengineering.com/firefighting/an-overview-grain-dust-explosions/ [S]
10. **Stored fertiliser is dangerous:** ammonium nitrate is an explosion and security risk (Beirut port, 2020) [S]
11. **Quality must be maintained:** insects, rodents, moulds and mycotoxins; pulses become "hard to cook" after 2–4 years; oils oxidise without good storage [S/E]
12. **Complacency risk:** firms might hold less stock of their own if the state holds some (crowding out) [E]

## B. Why the downside is manageable (included claims)

13. **No refrigeration, little electricity.** Dry grain, pulses, oils in sealed tanks, milk powder and tins are stored at ambient temperature. Grain cooling by aeration uses roughly **0.3 kWh per tonne over six months** in trials. https://doaj.org/article/2bfcbd50940640bf804c8ee2f94c2a61 [P]
14. At ~1 kWh per tonne per year, the whole ~11.5 Mt reserve would use ~**11.5 GWh/yr (~£3m)** of electricity, under 0.5% of its running cost, and well-dried grain keeps safely for weeks without fans in a power cut [E]
15. **Proven management tools:** covered storage, first-in-first-out rotation, temperature probes, independent audit and published stock reports (the opposite of India's failures) [E]
16. **Buy gradually, at harvest and in surplus years,** over 3–5 years, as Finland did with domestic oats and wheat in 2022–23. https://huoltovarmuuskeskus.fi/en/a/procurement-of-additional-grain-for-emergency-stockpiles-completed [P]
17. **Put the minimum in law** with release and refill rules: Finland's reserve rests on a government decision setting a 6-month minimum, and Japan must buy back released rice within a year [P/S]
18. **Disperse and protect sites:** many contracted sites rather than a few big targets. Germany uses ~**150 private sites** of 2,000–8,000 t, inspected every 4–6 weeks. https://www.topagrar.com/panorama/news/das-ist-uber-deutschlands-getreidevorrate-bekannt-20020375.html [S]
19. **Hold fertiliser as supply contracts or safer products,** not giant ammonium-nitrate stockpiles [E]
20. **Contract existing firms to hold *extra* stock on top of their normal working stock** (Finland, Norway, Switzerland), so the state reserve adds to private stock rather than replacing it [P/S]

## C. What the nation gets for it (included claims)

21. **Stability when supply chains break:** today, commercial wheat stocks at the June low cover ~**1 month** of national calories and retailers hold ~**10 days** of stock; the reserve adds **3 months of complete food** for everyone plus 5 Mt of grain [P/E]
22. **Calm instead of panic:** in the 2000 fuel blockade, Sainsbury's warned it would run out of food "within days" and Safeway rationed bread and milk, from a logistics failure, not a harvest failure. https://www.pressandjournal.co.uk/fp/past-times/4057166/fuel-price-rises/ [S]
23. **Rising food prices are followed by unrest** across countries (1990–2011); a reserve that holds prices and shelves steady reduces that risk. Bellemare 2015, *AJAE*: https://ideas.repec.org/a/oup/ajagec/v97y2015i1p1-21..html [P]
24. **Fairness protects the poorest:** 12.2% of households are already food-insecure (35.9% of Universal Credit households) and cannot stockpile; a national reserve covers them. Food Foundation, Jul 2026: https://foodfoundation.org.uk/news/food-prices-tracker-july-2026 [P]
25. **It works in practice:** Switzerland released up to 16,000 t of protein feed from its reserve in Sept 2026 when drought stalled river imports, with no consumer price impact expected. https://www.cash.ch/news/notreserven-fur-protein-tierfutter-werden-freigegeben-964808 [S]
26. **No waste:** rotated stock feeds school meals, hospitals, the armed forces, food banks, millers and livestock. Japan already sells 5-year-old reserve rice as feed [E/S]
27. **Jobs (a bonus, not the reason):** the operations budget (~£158m/yr) could fund roughly **2,000 direct jobs** in stock management, inspection, logistics and local food planning, plus contracted storage work and a ~£1bn construction programme for new stores [E]
28. **Overseas stabilisation:** multi-purpose grain can support allies and humanitarian relief in a crisis, as the 787,000 t ASEAN+3 emergency rice reserve did after Typhoon Haiyan (2013). https://www.asean.org/wp-content/uploads/images/2015/October/outreach-document/Edited%20APTERR-2.pdf [P]
29. **Support for farmers:** steady demand for grain, pulses and oilseed, bought at harvest [E]

## D. The defence comparison (included claims)

30. UK defence spending is ~**2.36% of GDP** (NATO definition, 2025–26), rising to ~2.6% by 2027–28: roughly **£68bn a year** [P/E]. Institute for Government: https://www.instituteforgovernment.org.uk/explainer/uk-defence-spending
31. The £10 food reserve (~£0.7bn) ≈ **1% of defence spending** [E]
32. NATO allies committed to **3.5% of GDP on core defence plus up to 1.5% on defence-related resilience** (civil preparedness, critical infrastructure) by 2035. https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/chart-of-the-week-defence-spending [S]
33. 1.5% of UK GDP ≈ **£43bn a year**; the food reserve would use about **1.6%** of that resilience allowance. **A strategic food reserve is a natural candidate for NATO-counted civil resilience spending** [E, proposal; eligibility to be checked]
34. Peer precedent: **Sweden funds its food stockpiles from its total-defence budget** (SEK 575m in 2026; up to SEK 50bn of loan-financed defence money may go to infrastructure and stockpiling incl. food). https://data.riksdagen.se/dokument/HD01MJU25.html [P]
35. **Finland** treats food, energy and medicine stocks as one security-of-supply system funded by a levy, at ~**€16 (~£14) per person per year**. https://www.huoltovarmuuskeskus.fi/en/organisation/funding [P]

## E. Cost–benefit in one table [E]

| | Annual cost | What it buys or avoids |
|---|---|---|
| £10 food-security insurance | ~£695m (≈ 0.02% of GDP; ≈ 1% of defence) | 3 months of complete food for all; 6 months of oils, rice and pulses; seed and nitrogen; 5 Mt multi-purpose grain; plans, people and backup power |
| Severe national food disruption (illustrative) | £29–58bn one-off (1–2% of GDP) | Empty shelves, price spikes, emergency imports at peak prices, health harm, loss of public order |
| **Break-even** | | The reserve pays for itself if such a disruption occurs **about once every 40–85 years**. The 2020s have already brought COVID, the CO₂ crisis, the energy and fertiliser shock, salad rationing, retail cyber attacks and the 2026 Hormuz and Black Sea disruption. |

## F. Context and excluded material (for the reviewer)

- "No electricity exposure" is overstated: grain stores need some aeration (fans) and handling equipment. The accurate claim is **no refrigeration and very low, interruptible electricity use**.
- The capex figure (£200/t of new storage) and storage fee (£15/t/yr for grain) are assumptions; UK quotes for new flat stores and silos should be gathered.
- Job numbers are rough. The policy should not be justified mainly by jobs.
- The break-even depends on the assumed cost of a severe disruption (1–2% of GDP), which is an illustrative assumption, not a modelled estimate.
- Whether NATO's 1.5% resilience category can include food stockpiles needs checking against the NATO Hague Summit (2025) text and UK reporting rules.
- The link from food prices to unrest is strongest in lower-income, import-dependent countries. In the UK the realistic failure mode is panic buying, empty shelves and loss of trust, not mass riots. Present unrest as a risk that a reserve reduces, not a prediction.

## G. Lines for the page
- "An army defends the border. A food reserve defends the dinner table."
- "Under 3p a day per person, about 1% of the defence budget, for a nation that never runs out of food."
- "Yes, it needs warehouses, guards and good management. So does every insurance worth having."
- "No fridges, no waste, no panic."
