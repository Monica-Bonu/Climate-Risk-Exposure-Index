# Discussion

## Climate Risk Exposure Index

---

## 1. Overview

The goal of this project was to build a transparent, reproducible index that scores and ranks countries by their exposure to physical climate hazards — demonstrating the kind of physical-risk screening that CSRD (ESRS E1) and TCFD require. The index achieves that goal: it produces a full country ranking from publicly available observed data using a documented four-step methodology (indicator selection, normalisation, weighting, aggregation) consistent with the OECD/JRC composite-indicator framework. This section interprets the results against the four research questions the project set out to answer, considers what the findings mean for practical risk disclosure, and is honest about where the index falls short.

---

## 2. Research Question 1: Which Countries Are Most Exposed?

The index produces a clear and geographically coherent answer: **India, Nigeria, and Australia** are the three most exposed countries in this sample by a substantial margin, with composite scores of 0.878, 0.785, and 0.742 respectively. All three score more than twice the sample median (0.250). The next tier — Portugal, Brazil, and Kenya — sits in the 0.564–0.575 range, meaningfully separated from both the top three and the mid-table group.

The result is geographically consistent with known physical climate conditions. India sits at the intersection of monsoon rainfall intensity, heat extremes, and seasonal drought — the only country in the dataset to score above 0.9 on two indicators simultaneously. Nigeria and Australia are among the hottest and driest countries in the sample; their positions at the top of the ranking reflect structural climate conditions, not statistical accidents. That the index recovers this geography from raw observed data, without any prior knowledge of country rankings baked into the construction, is a positive validation of the methodology.

The **regional divide** is the most prominent structural feature of the results. European countries, taken together, average a composite score of 0.235 — less than half the mean of the African countries (0.609) and global anchors (0.609 averaged across India, Australia, Brazil, and the United States). Within Europe, a meaningful internal divide exists: the Mediterranean group (Portugal, Greece, Spain, Italy) scores substantially higher than the northern and western European countries. Portugal ranks 4th overall (0.575), and Greece 8th (0.449) — both higher than the United States (12th, 0.245) and France (11th, 0.250). This reflects the real climate gradient from the Atlantic fringe to the Mediterranean basin: sustained summer heat, reduced rainfall in the dry season, and longer drought windows are characteristics of southern European climate that the index picks up directly.

---

## 3. Research Question 2: Which Hazards Drive the Highest-Risk Countries?

The driver decomposition answers a question that a composite score alone cannot: **are high-ranking countries uniformly exposed, or do specific hazards dominate their score?** The answer differs by country, and the differences matter for risk management.

**India** is the clearest case of broad-spectrum exposure. It scores above 0.7 on all three indicators — the only country to do so. Its composite score is not inflated by one dominant hazard; it is high because India is genuinely highly exposed on every dimension measured. For CSRD and TCFD purposes, this signals that physical risk in India cannot be managed by addressing a single hazard type; all three require assessment.

**Nigeria** and **Australia** represent a different pattern: extreme on specific hazards. Nigeria's drought score (0.948) is the second highest in the dataset, and its temperature score (0.897) is near the top; but its precipitation exposure is moderate (0.509). Australia anchors the maximum value on both temperature and drought (1.000 each) while scoring relatively low on precipitation (0.227). These countries are not uniformly exposed — they are structurally exposed to heat and water deficit. A risk assessment that focused only on flooding would significantly underestimate their true physical risk profile.

The **Mediterranean European countries** tell yet another story. Portugal, Greece, and Spain all reach their mid-table composite scores primarily through temperature, with drought as a secondary contributor and precipitation as the weakest. Their hazard profiles resemble a scaled-down version of Nigeria's — dominated by heat and dry conditions — rather than the precipitation-heavy profile one might associate with flood risk. This is consistent with the drying trend in southern Europe observed in climate science and has real implications for organisations with agriculture, water-intensive manufacturing, or tourism assets in this region.

The **stacked driver decomposition** (available in the dashboard) makes this heterogeneity visible at a glance. A single composite number obscures whether a country is high-risk because of heat, flooding, drought, or all three. For corporate disclosure purposes, the decomposition is arguably more useful than the composite score itself: it tells a risk manager which hazard type to prioritise for site-level follow-up.

---

## 4. Research Question 3: How Sensitive Is the Ranking to Weighting?

The sensitivity analysis tests whether the ranking holds up when the equal-weighting assumption is relaxed. The short answer is yes — the top tier is robust, and the overall structure is stable.

**India and Nigeria hold ranks 1 and 2 under every scheme tested**, including when drought is removed entirely. This is the most important robustness finding. The top positions cannot be attributed to the choice of weights. Australia holds rank 3 in four of five schemes, dropping to 4 only when drought is removed (at which point Portugal rises to 3 because of its temperature score).

**Mid-table positions are less stable.** Portugal shifts between ranks 4 and 6, Brazil between 4 and 5, and Kenya between 5 and 7 depending on whether drought is weighted heavily or lightly. This instability is expected and interpretable: these countries score moderately across all three indicators rather than being extreme on one, so shifting the weights changes their relative ordering. The sensitivity analysis does not expose a weakness in the index — it exposes a genuine ambiguity in the underlying data that no weighting scheme can resolve without additional empirical justification for preferring one hazard over another.

The **three-tier structure** of the ranking — high-exposure tropical and semi-arid countries, mid-range Mediterranean countries, low-exposure northern European countries — holds under all five weighting schemes. No country from the bottom third of the ranking rises to the top third under any plausible weighting. This structural stability is what a credible composite index should demonstrate, and this one does.

---

## 5. Research Question 4: Counterintuitive or Surprising Results

Two results in this index warrant specific discussion because they appear, at first glance, inconsistent with widely held expectations about climate risk.

**The Netherlands ranks 16th (score: 0.200), below France, Belgium, and Germany.** The Netherlands is one of the world's most frequently cited examples of flood risk — much of the country lies below sea level and depends on an extensive system of dykes and water management infrastructure. Yet on this index, it ranks near the bottom. This is not an error. It reflects a specific methodological boundary: the precipitation indicator (rx5day) measures the intensity of extreme rainfall events, in which tropical and monsoon climates dominate. The Netherlands' flood risk arises almost entirely from sea-level rise, river flooding, and drainage capacity — physical mechanisms not captured by rx5day. The same applies to Belgium and Denmark. The exclusion of a sea-level or river discharge indicator from version 1 is the direct cause of this gap. It is documented as a limitation, and addressing it is the single most important extension for a version 2 of this index.

**The United States ranks 12th (score: 0.245), below Portugal, Brazil, and Kenya.** This is surprising for a country whose physical diversity includes Gulf Coast hurricanes, western drought and wildfires, and Mississippi basin flooding. The explanation is methodological: the index uses country-level averages across all 21 country-years. The United States is a large, climatically diverse country, and national averages mask the enormous internal variation in hazard exposure. A state-level or regional analysis would produce dramatically different results — Florida, California, and Texas would all score far higher than Maine or Oregon. This finding is a reminder that country-level composite indices are screening tools, not asset-level assessments. The appropriate response to the United States' mid-table ranking is to recognise that further disaggregation is needed, not to conclude that US physical risk is modest.

A third observation worth noting: **Norway scores the highest precipitation normalised value (0.293) among the Nordic countries**, even though Norway is not typically associated with extreme rainfall flood risk. This reflects Norway's Atlantic-facing climate — its annual precipitation levels are genuinely high relative to most European countries, and rx5day captures that. It does not make Norway a flood-risk country comparable to the Netherlands; it simply means that within the 21-country sample, Norway receives more intense short-duration rainfall than its northern European neighbours. The indicator is operating as designed; the finding is not counterintuitive once the indicator definition is understood.

---

## 6. Implications for CSRD and TCFD Physical-Risk Assessment

CSRD (ESRS E1) requires organisations to assess and disclose their exposure to physical climate hazards in a manner that is systematic, documented, and auditable. TCFD asks specifically for identification of physical risks that could affect the organisation's assets, operations, and supply chains — both on a current and forward-looking basis. This index addresses both frameworks at the country screening stage.

The methodology used here — indicator selection with a documented rationale, normalisation to a common scale, explicit weighting with a sensitivity test, and aggregation to a composite — is the same structural approach a corporate sustainability team would apply to their own physical-risk screening. The difference is scope: this index covers 21 countries at a national level; a corporate application would focus on specific geographies (operating sites, supplier locations, customer concentrations) and would need to add more granular hazard indicators relevant to the assets in question.

Three findings have direct practical relevance for corporate disclosure work:

1. **Country-level screening is a starting point, not an endpoint.** The index correctly identifies India, Nigeria, and Australia as high-priority geographies for further analysis. For an organisation with operations or supply-chain exposure in those countries, the next step is to identify specific assets within those countries and assess exposure at site level — which requires hazard data at higher spatial resolution than national averages.

2. **The hazard decomposition is at least as important as the composite score.** An organisation managing heat risk in India faces a different set of interventions than one managing drought risk in Australia or flood risk in coastal Europe. The driver decomposition this index provides is the kind of output that translates directly into workstream prioritisation in a physical-risk programme.

3. **The limitations of country-level averages are particularly acute for large, diverse economies.** The United States example illustrates that national-average scores can significantly understate regional exposure. CSRD-aligned disclosure for a US or Brazilian operation requires sub-national assessment. The same logic applies to India and China, which are not in this sample but would face the same aggregation problem.

The index also demonstrates a principle that both CSRD and TCFD emphasise: **transparency of method matters as much as the output**. Every choice made in this project — which indicators to include, the correlation threshold used for the redundancy check, the normalisation formula, the weighting assumption — is documented with a rationale. That documentation is what makes the output auditable and credible. A climate risk number without a method is not a disclosure; it is an assertion.

---

## 7. Limitations in Context

The limitations documented in the methodology are real, but their materiality varies by use case.

The **absence of sea-level exposure** is the most significant gap for European-focused analysis. It causes a systematic underestimation of physical risk for low-lying coastal and riverine countries (Netherlands, Belgium, Denmark, United Kingdom) relative to their actual risk profile. Any organisation relying solely on this index to assess European flood risk would draw incorrect conclusions about those countries.

The **country-level aggregation** is an appropriate limitation for a v1 screening tool but becomes misleading if the results are used for anything more granular than country prioritisation. The corollary is positive: the index is well-suited for the task it was designed for — identifying which countries warrant closer attention — and should not be used beyond that scope without methodological extension.

The **historical basis only** of the index means it reflects where hazards stand based on 2000–2023 observed conditions. Climate projections consistently indicate that heat and drought hazards will intensify, particularly in the already high-scoring geographies. A forward-looking version of this index using CMIP6 scenario data would likely show a wider spread between the top and bottom of the ranking as tropical and Mediterranean hazards intensify relative to northern European ones. For TCFD disclosure purposes, which explicitly requires consideration of forward-looking physical risks, a scenario-based extension is not optional — it is a gap this version 1 leaves open.

The **temperature-drought correlation (r = 0.818)** is acknowledged as a partial double-weighting of the hot-and-dry hazard profile. The sensitivity analysis confirms it does not materially alter the top-tier rankings. It is nonetheless a methodological constraint that a more sophisticated version of the index could address through principal component analysis or by replacing one of the correlated indicators with a genuinely orthogonal hazard dimension.

---

## 8. Summary

The index successfully answers all four research questions. India, Nigeria, and Australia are the most exposed countries; their exposure is driven by different combinations of heat, precipitation, and drought, not a single shared profile. The top-tier ranking is robust to weighting assumptions; mid-table positions show modest sensitivity that reflects real ambiguity in the underlying data. The counterintuitive results — particularly the Netherlands and the United States — are explainable and methodologically informative: they point directly to the indicator gaps and aggregation limitations that future work should address.

The project demonstrates that a credible, reproducible physical-risk screening index can be built from publicly available observed data using a standard composite-indicator methodology. It also demonstrates that the transparency CSRD and TCFD require — documented rationale for every methodological choice, a correlation check, a sensitivity analysis, and an honest statement of limitations — is practically achievable and should be the baseline expectation for climate risk disclosure work.
