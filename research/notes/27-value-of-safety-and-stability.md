# 27 · The value of safety and stability

**Question:** what is safety worth, and what is stability worth? The plan's benefits are mostly losses that never happen, which makes them easy to ignore. This note sets out how to value them honestly.

## 1. Why safety is underpriced [I]

- **Invisible when it works:** a reserve that is never released looks like waste (the "preparedness paradox"; Y2K is the usual example).
- **Tragedy of the horizon:** Mark Carney (Lloyd's, 29 Sep 2015) described how costs arrive now while the losses they prevent arrive later, beyond political and business horizons. Food reserves have the same problem.
- **Rare events are underinsured:** people and governments discount low-probability, high-impact events until just after one happens (Finland, Switzerland and Norway hold reserves because they remember).
- **Contrast:** private markets price hope generously. A 16 Oct 2026 report quoted Elon Musk saying SpaceX will be worth over $100 trillion within ten years [S/?, a forecast by an interested party, not a valuation]. Public safety has no share price, so it is priced by its cost alone.

## 2. Five ways to value it: break-even thresholds [E]

From `benefits()` in `research/model/reserve_basket.py`. Store = £718m a year; both pillars = £1,028m.

| Currency | Basis | Store | Both pillars |
|---|---|---|---|
| Insurance premium | Agri-food sector GVA £153.2bn (2023), 4.1 m jobs (2025): Defra, *Food statistics in your pocket* [P] | 0.47% of output; ~£175 per food job a year | 0.67%; ~£250 |
| Peace of mind | HM Treasury Green Book wellbeing guidance (2021): £13,000 per WELLBY (range £10–16k), 2019 prices [P] | +0.0008 life-satisfaction points per person a year (~55,000 WELLBYs) | +0.0011 (~79,000) |
| Lives | DfT value of preventing a fatality £1.8m (2016 prices) [P/S], uprated ~40% to ~£2.5m [E] | ~290 deaths a year, or ~11,500 once in 40 years | ~410, or ~16,400 |
| The economy | GDP ~£2.9trn; one week ≈ £56bn | A week at 10% lower output ≈ 7.8 years of cost; a 1%-of-GDP shock avoided once in ~40 years | ~5.4 years |
| Defence comparison | ~£68bn a year ≈ £980 per person | £10.33 | £14.79 |

Sources: https://gov.uk/government/statistics/food-statistics-pocketbook/food-statistics-in-your-pocket ; https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1005388/Wellbeing_guidance_for_appraisal_-_supplementary_Green_Book_guidance.pdf ; DfT value of preventing a fatality (TAG data book; current-price value to confirm).

## 3. Benefits not priced [I]

- Security and sovereignty (food as leverage), bargaining power in a crisis, protection of the next harvest, rural jobs (~3,500 funded), soil, water and climate co-benefits, health (tablets, fortified flour), trust and fairness (Bellemare 2015; the 2000 fuel blockade).

## 4. Honesty rules

- Thresholds show how small a benefit is enough; they are not forecasts of benefit.
- Do not add the rows together: they overlap (lives, wellbeing and output partly count the same loss).
- Uprating the 2019 WELLBY and 2016 fatality values to 2026 prices lowers the thresholds further.
- The reserve does not stop inflation; its stability value is time, access and fairness.
- Open: the current DfT fatality value in 2026 prices; any UK estimate of the economic cost of a multi-week food disruption.
