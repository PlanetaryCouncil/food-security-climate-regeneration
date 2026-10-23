# 16 · Can we store a complete diet, not just grain? And is a rotating reserve really "no downside"?

> Background research on storable diets. The final reserve design (a mill-feasible approach, bread and a no-cook ration for everyone, compulsory commercial stocks sized to UK markets) is in the briefing, chapter 9.


Tags: `research:supply-chain-reserves`, `research:calories-protein`, `research:scale-up-emergency`
Question (project lead): can fats and protein be stored as well as grain, giving a fully functional diet that bridges an emergency until the economy and farming can switch within a season? And can it be framed as "no downside", because rotation means nothing is wasted?
Status: 22 Oct 2026. Model: `research/model/reserve_basket.py`. Labels: [P] primary, [S] secondary, [E] my estimate or model, [?] unresolved. Nutrient values and shelf lives are typical figures, to be checked by a nutritionist.

---

## 1. Short answer

**Yes, a nutritionally complete diet can be stored.** It costs more than grain alone, but not much: **about £6.50 per person per year for six months of a full ration for the whole population** [E]. Every item can be rotated through normal trade, public catering or animal feed, so **almost nothing is wasted**. But it is **not literally "no downside"**. It has a small insurance premium, it ties up capital, it can move markets while it is being built, and it needs honest governance. The defensible framing is: **"No waste, low cost, high insurance: a fire extinguisher we eat every few years."**

## 2. What can be stored, and for how long

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

## 3. A complete storable ration (per person per day) [E]

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

## 4. Size and cost (whole UK population) [E]

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

## 5. "Bridge to a new season": does this buy enough time?

With domestic production continuing (cereal model, notes 09 and 14):
- **Days 0–90:** the reserve feeds people while the state stops grain-to-ethanol, diverts feed wheat to mills, cuts pig and poultry numbers as soya runs out, and finds new import routes.
- **Months 3–6:** spring sowing of cereals, potatoes and pulses on extra land (temporary grass, set-aside), using **stored seed and nitrogen**.
- **Months 6–13:** first harvest from the switched system.

**A 90-day complete ration plus 6 months of the import-dependent items plus inputs covers a shock that starts at any time of year**, because the UK's own harvest refills the grain. Countries without that harvest (Singapore, the Gulf) need much more.

## 6. Rotation: where everything goes, so nothing is wasted

| Item | Normal-times rotation outlet |
|---|---|
| Wheat, barley, oats | Millers (if still food-grade), otherwise animal feed (Japan sells 5-year-old reserve rice as feed) |
| Rice, sugar, oils | Food manufacturers and retail through contracted firms (the Swiss model); out-of-spec oil to biodiesel |
| Pulses | Canners, feed compounders |
| Milk powder, canned fish, ready meals | **Public catering**: school meals, NHS, armed forces, prisons, food banks. The reserve's oldest stock feeds the nation's institutions. |
| Seed | Sown in the last year of its life; next year's seed bought in |
| Nitrogen fertiliser | Used on farms in the normal season; replaced annually |

**Elegant design point:** rotating canned and powdered stock through public procurement turns the reserve into a **year-round social good**: cheaper school meals and food-bank supply. That links resilience to the equity agenda (note 10).

## 7. Honest downsides (and how to shrink each one)

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

## 8. PDF lines
- "We can store a complete diet: grain, pulses, oil, milk powder, fish and vitamins. Switzerland already does most of it."
- "Ninety days of a full ration for every person in Britain costs about £3 each a year. Six months costs about £6.50."
- "Nothing is wasted. Old stock goes to school dinners, hospitals, food banks, millers or animal feed."

## Sources
- Swiss oils in tanks, 35,000 t = 4 months; rotation through company sales: https://www.bwl.admin.ch/en/range-of-compulsory-stocks ; https://bwl.admin.ch/en/organisation-strategic-reserves ; https://www.ge.ch/document/emergency-provisions-and-national-economic-supplies
- Swiss 12-month proposal (oils +25%): https://swissinfo.ch/eng/politics/swiss-government-proposes-expanding-national-food-stockpiles/48446798
- General shelf-life guidance: https://ccfruitandnuts.ucanr.edu/sites/default/files/2020-09/335597.pdf
- India FCI losses (CAG): https://www.tribuneindia.com/news/punjab/wheat-worth-rs-600-cr-allowed-to-rot-cag-48189 ; https://www.tribuneindia.com/news/haryana/80000-mt-wheat-stock-damaged-in-2017-2021-cag ; https://www.deccanherald.com/business/avoidable-outgo-rs-375-cr-2259383
- Japan rotation to feed and buyback: note 15 and note 13 sources
- Germany pulses and condensed milk; Israel baby food; Finland seed: note 13 sources
- Model: `research/model/reserve_basket.py`
