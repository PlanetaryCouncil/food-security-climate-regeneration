# 23 · Running it: a lean, open, automated agency and a decentralised network

Date: 23 October 2026. Status: author design [I] with costed assumptions [E], implemented in `reserve_basket.py` (`AGENCY`, `jobs()`). Briefing chapter 11.

## 1. Principles (common sense)

1. **Lean.** About 65 people, never more than 100 even in a crisis surge. Every person has an essential role.
2. **Three deep.** Every function has a lead and two trained deputies, and every person can do at least three roles. Anyone can be on leave, ill or leave the job without a function stopping.
3. **Automate the manual work.** No routine hand sampling. Sensors, automatic samplers and AI watch the stock; people decide, check and answer for it.
4. **Open by default.** You cannot hide a programme that builds warehouses, moves millions of tonnes through ports and employs ~1,000 people, and it is not a secret nuclear programme. So the reserve publishes:
   - where it is;
   - how much it holds, by region, every month;
   - what it buys and when;
   - what went wrong.

   Only live security details (alarm codes, guard rotas, real-time per-site stock levels) are withheld, as for any public building.
5. **Protected by spread, not by secrecy.** Many sites in many districts, near ports and near people, with different operators, power feeds and software. Losing one site loses a small fraction.
6. **Human food first** (note 22), **food for everyone**.
7. **Always learning.** An innovation department keeps cutting cost and waste, and the public is invited to find weaknesses.

## 2. The agency: 18 functions, about 65 people

**Rule of three:** each function has a lead + 2 deputies drawn from neighbouring functions. Each person has one **primary** role and is a trained **deputy** in two others, so each function has at least three people able to run it. Deputies run their secondary function for real in quarterly drills, and roles rotate every ~2 years.

| # | Function | People | AI and automation do | People do |
|---|---|---|---|---|
| 1 | **Leadership and accountability**: chief executive (statutory accounting officer), deputy, board secretary | 3 | Draft reports, track decisions | Answer to Parliament; sign releases (two-person rule) |
| 2 | **Situation room and duty desk** | 6 | Watch prices, weather, shipping, stock sensors and news around the clock; raise alerts | On-call rota (1 week in 6), judge alerts, start the contingency ladder |
| 3 | **Market and risk intelligence** | 3 | Forecasts, scenario runs, purchase-timing signals | Buying strategy, risk register |
| 4 | **Stock data and automated sampling** | 4 | A digital twin of every store; sensor and auto-sampler data; anomaly detection | Run and fix the sensing network, data quality |
| 5 | **Quality and food safety** | 3 | Flag lots near limits; schedule rotation | Set standards; manage lab contracts; release certificates |
| 6 | **Contracts and compulsory-stock obligations** | 4 | Track obligations, deliveries, invoices | Negotiate; set and audit the commercial baseline (additionality) |
| 7 | **Audit and integrity** | 3 | Fraud and "paper stock" analytics; satellite and sensor cross-checks | Commission unannounced independent checks; report |
| 8 | **Finance and treasury** | 3 | Payments, hedging signals, refill-fund tracking | Budget, hedging decisions, refill rule |
| 9 | **Legal and regulation** | 3 | Draft and compare texts | Food Security Act, CCA, WTO, subsidy control, data protection |
| 10 | **Four nations and local resilience** | 4 (one per nation) | Local dashboards | Work with resilience forums, councils and devolved governments |
| 11 | **Logistics, ports and fuel priority** | 4 | Route planning, fleet and fuel tracking | Port and haulage contracts; priority fuel list |
| 12 | **Nutrition and special diets** (registered dietitians) | 3 | Ration optimisation | Specification and variants for infants, children, older people, medical needs |
| 13 | **Public engagement and open data** | 3 | Publish dashboards; sort public feedback | Open conversation: citizens' panel, public meetings, answering every serious question |
| 14 | **International, trade and aid** | 3 | Monitor export bans, partner needs | Partner agreements, WFP sales, export and aid decisions |
| 15 | **Cyber, security and offline operations** | 4 | Intrusion detection | Keep a paper-and-radio fallback; test it; physical security standards |
| 16 | **People, training, exercises, volunteers** | 3 | Scheduling, e-learning | Run drills; manage the Food Reserve Volunteers |
| 17 | **Innovation department** | 6 | Most of the analysis | Improve nutrition, storage, transport, sampling, data retention and AI tools |
| 18 | **Domestic production and soils** (the grow pillar) | 3 | Read soil-moisture sensors, satellite crop and soil data, seed and fertiliser stocks | Track soil health, water storage, seed security and nutrient independence with Defra and the devolved governments |
| | **Total** | **~65** | | |

**Crisis surge to ~100:** pre-agreed secondments from the civil service and the armed forces, plus trained Food Reserve Volunteers. These are named people trained in advance, not recruited on the day.

**Why not one person plus AI?** That would make one person and one AI the single points of failure the reserve exists to remove. Releasing public stock needs accountable humans. Audit cannot be self-audit. And in a blackout or cyber attack, cloud AI may be the first thing to fail. So the agency is AI-heavy but human-accountable, and it can run on paper.

## 3. Automated sampling and monitoring

- **In-store sensing:** temperature and moisture cables through every bulk store; CO₂ sensors (rising CO₂ signals insects or mould early). This is standard commercial technology.
- **Automatic samplers at intake and out-loading** at ~40 hubs, with near-infrared (NIR) analysers for moisture and protein, and rapid mycotoxin tests.
- **People only for exceptions:** an alert, a dispute, a release certificate, or an unannounced audit by a contracted independent inspector.
- **A digital twin:** every lot has an ID, origin, intake test, sensor history and planned rotation date.
- **Offline backup:** the ledger is printed and held regionally every week, so a cyber attack does not erase knowledge of where the food is.

**Cost [E]:** sensing ~£2 per tonne of capacity across ~6.8 Mt, plus auto-samplers and analysers at ~40 hubs at ~£250k each, ≈ £24m capex, ~£3m a year annualised over 10 years. Maintenance, data and AI ~£4m a year.

## 4. The agency budget [E]

| Item | £m a year |
|---|---|
| Staff: ~65 at ~£90k fully loaded | 5.8 |
| Innovation programme (pilots, university and start-up contracts) | 8.0 |
| Automated sampling and sensing (annualised capex) | 2.9 |
| Sensor maintenance, data platform, AI compute, offline backups | 4.0 |
| Confirmatory lab certificates on release | 3.0 |
| Open data and public feedback platform | 1.5 |
| Independent inspectorate: unannounced physical assay, additionality checks against registered commercial baselines | 8.0 |
| **Total** | **~33.3** |

**Package total: ~£718m ≈ £10.33 per person per year** (public £4.93 via taxes; compulsory stocks £5.40 via prices). Range £9.40–16.56; £18.34 under severe stress.

## 5. The decentralised network: near ports, near people

**Three layers [I/E]:**

| Layer | Where | What | Roughly |
|---|---|---|---|
| **Port hubs** | Bulk-grain ports and container ports | Imported staples (rice, oil, sugar, soya meal, strong wheat) where they land; export and aid outlets | ~8–10 hubs |
| **District stores** | Existing merchant, co-op and mill stores under contract, plus new stores, spread across every region of all four nations | Food-grade wheat, seed, pulses, oats, nitrogen | ~30 hubs plus many contracted farm stores |
| **Local points** | Schools, councils, depots, community centres | The 3-day no-cook ration, water, specialist food | Thousands |

**Which ports? A reality check [S/?, to verify]:**
- **Dover** is a roll-on/roll-off lorry port. It is vital for fresh food from Europe but does not handle bulk grain.
- **Felixstowe** is a container port. It suits containerised rice, canned goods and bottled oil.
- **Bulk grain** moves through ports such as **Tilbury, Liverpool, Immingham, Hull, Avonmouth (Bristol), Southampton, Ipswich and Belfast**, and through Scottish east-coast ports.

So: put grain hubs at bulk ports, put container staples near Felixstowe and other container ports, and plan Dover around fresh food and lorries.

**Ports are not enough on their own:**
- Many east-coast and estuary ports sit in flood-risk zones (the 1953 North Sea flood); flood-resilient sites are needed.
- Ports are natural chokepoints.
- Northern Ireland needs its own stock (a statutory minimum on the island of Ireland) because GB stores do not help if the ferries stop.

Hence the mix: port hubs for import and export, district stores for resilience, and local points for week one.

## 6. Open by default: why secrecy does not work here

**Sweden's choice.** Sweden keeps its new grain-store locations secret (chapter 8). That works for a small state-owned stock. It cannot work for a UK reserve spread across ~40 hubs, thousands of local points, ~1,000 workers, hauliers, port contracts and planning applications.

**What openness buys:**
- **Trust:** people do not panic-buy when they can see the stock.
- **Accountability:** paper stock and quiet raiding are harder when monthly figures are public.
- **Market calm:** published buying rules and quarterly volumes stop traders guessing, without exact dates that invite front-running.
- **Deterrence:** an adversary knows that disrupting one site achieves little.

**What is withheld:** live security operations (alarm systems, guard rotas, real-time stock per site). That is ordinary building security, not secrecy about the programme.

**Published exceptions.** Open by default does not mean everything: a short, public list of exceptions is withheld, namely exact sites and tank volumes of fuel, infant formula and nitrogen, live release routes, and precise purchase dates. Host towns and ports, regional stocks, costs, audits and incidents are all published.

**The counter-argument we take seriously:** published locations make targeting easier (sabotage, theft, protest). We answer it with dispersion, redundancy, ordinary physical security, insurance and quick replacement, not with secrecy.

## 7. Open conversation with the public

- **Live dashboard:** stocks by region and product (monthly), purchases, rotations, quality incidents and costs.
- **Feedback channel:** anyone can report a problem, suggest an improvement or ask a question, and every serious question gets a public answer.
- **Citizens' panel:** a rotating, randomly selected group that reviews the reserve each year.
- **Adversarial bounty:** small payments for anyone who finds a real weakness (a scenario we missed, a flaw in a store, a data error), like a software bug bounty. *Resilience through transparency* in practice.
- **Annual public stress test:** one exercise a year, with results published, including failures.

## 8. Global markets: buy calm, sell calm

- **Counter-cyclical buying:** buy in good-quality surplus years and when prices are below their recent average; never fill from a stressed, mycotoxin-risk harvest .
- **Published buying rules:** rules and quarterly volumes are announced in advance and spread over 3–5 years; exact purchase dates are not, so traders cannot front-run them.
- **Small share of the market:** the wheat stock is mostly UK-grown, bought at harvest. About 0.8 Mt a year rotates, roughly 17% of UK mill intake, and small next to world wheat trade.
- **Hedging:** the treasury function can hedge purchases and sales with ordinary futures (e.g. UK feed wheat futures) rather than taking price risk.
- **Rotation outlets:** UK mills, animal feed (a ~13 Mt market), and export or aid through the port hubs (note 20).
- **No price manipulation:** releases are triggered by supply emergencies, not to manage inflation.

## 9. Jobs [E]

| Work | Jobs (approx.) |
|---|---|
| Lean agency incl. innovation and domestic-resilience monitoring | ~65 |
| Grain and food stores (intake, drying, aeration, maintenance; automated, ~1 per 20 kt) | ~280 |
| Confirmatory labs | ~40 |
| Haulage of rotated stock (~3.4 Mt a year) | ~300 |
| Crispbread, biscuit and canning production for rotation | ~150 |
| Local food-plan officers (~45 resilience bodies) | ~135 |
| Exercises, training, delivery registers | ~100 |
| **Total permanent** | **~1,070** |
| Construction while ~£0.7bn of new stores are built over ~5 years | ~1,400 a year |
| Optional paid Food Reserve Volunteers (e.g. 10,000 on a ~£1,000 retainer) | part-time |

Automation trims jobs inside the agency and labs but leaves the physical work: stores, driving, baking and local planning. Those jobs are mostly rural and near ports.

## 10. Open questions

1. Is ~65 people enough for the 18 functions? Which function is missing or under-staffed?
2. Does the rule of three (lead + two deputies; three roles each) work under UK civil-service and employment rules? What does the 24/7 duty desk really need?
3. Can sampling and quality monitoring be automated to this degree (cables, CO₂ sensors, auto-samplers, NIR, rapid mycotoxin tests)? What regulators or contracts still demand manual sampling?
4. What legal form fits best: executive agency, non-departmental public body, or statutory corporation? Who holds the release key?
5. Open by default: what are the real security risks of publishing locations and regional stocks, and how do comparable open systems manage them (e.g. Switzerland's réservesuisse, the US Strategic Petroleum Reserve, Finland)?
6. Which UK ports actually handle bulk grain, rice, oil and sugar, and which are flood-exposed? Is the hub layout sensible?
7. Will a published purchase calendar and futures hedging avoid moving markets?
8. Does an adversarial bounty and citizens' panel create useful scrutiny or noise?
9. Are the agency costs (~£33m a year) and automation capex (~£24m) realistic?
