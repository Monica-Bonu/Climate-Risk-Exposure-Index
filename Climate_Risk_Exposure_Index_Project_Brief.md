# Project Brief: Climate Risk Exposure Index

*A transparent, reproducible country-level index of physical climate hazard
exposure, built to demonstrate CSRD (ESRS E1) and TCFD physical-risk assessment.*

---

## 1. Background (so what)

Companies are now legally required to assess and disclose their exposure to
physical climate hazards. Under the EU Corporate Sustainability Reporting
Directive (CSRD) and its climate standard ESRS E1, and under the Task Force on
Climate-related Financial Disclosures (TCFD) framework, organisations must
identify which of their operations and locations are exposed to acute hazards
(such as floods and storms) and chronic hazards (such as rising temperatures).

The problem is that many organisations, particularly mid-sized ones, do not yet
have a structured, transparent way to carry out this assessment. Physical risk is
inherently spatial: it depends on *where* assets are located. Before an
organisation can model financial loss at a specific site, it first needs to know
which locations warrant closer attention. That prioritisation step (screening
many places to find the few that matter most) is where physical-risk assessment
begins in practice, and it is often done inconsistently or not at all.

This project addresses that gap by building a small, transparent demonstration of
the screening step: a composite index that scores and ranks countries by their
exposure to physical climate hazards, and explains what drives the ranking.

## 2. Goal

To build a tool that evaluates how physical climate risk exposure is distributed
across regions, in line with TCFD and CSRD physical-risk requirements.

The verb is *evaluate* deliberately: the project does not only display the
distribution of exposure, it assesses it, identifies what drives it, and tests how
robust the conclusions are.

## 3. Objectives

**Overall:** Build a transparent, reproducible index that scores and ranks
countries by their exposure to physical climate hazards, demonstrating the kind of
physical-risk assessment CSRD and TCFD require.

**Specific objectives:**

1. Identify and select relevant physical climate hazards from authoritative data,
   with a documented rationale for inclusion and exclusion.
2. Assess exposure consistently across countries by normalising the hazard
   indicators onto a common scale and combining them into a composite exposure
   score.
3. Rank and prioritise countries by exposure, and present the results so a
   non-technical reader can interpret them.
4. Interpret the results: identify which hazards drive exposure in the
   highest-risk countries, and test how sensitive the ranking is to the weighting
   choices.

## 4. Questions

1. Which countries are most exposed to physical climate hazards, based on the
   selected indicators?
2. Which specific hazards drive the exposure of the highest-risk countries? Is a
   country high-risk because it is moderately exposed to everything, or extreme on
   one hazard?
3. How sensitive is the ranking to the choice of weighting? Does the order of
   high-risk countries hold up when the weights are changed?
4. Are there any counterintuitive or surprising results that point to either a
   real finding or a data limitation?

## 5. Methodology

### 5.1 Data source

The index is built from observed, country-level climate data from the **World
Bank Climate Change Knowledge Portal (CCKP)**, the World Bank's designated climate
data service. CCKP aggregates authoritative observational records (e.g. CRU and
ERA5) to national level and distributes them under a CC-BY 4.0 licence.

This is a deliberate move away from an earlier synthetic dataset (a Kaggle
"Climate Change Dataset") whose values were implausible and which had already had
its indicators combined. CCKP provides **raw indicators in their natural units**,
which is essential: it means all four steps of index construction are performed in
this project rather than inherited from a pre-built index.

**Scope of the data pull:**

- **Countries (21):** Netherlands, United Kingdom, France, Germany, Belgium,
  Spain, Italy, Portugal, Denmark, Sweden, Norway, Poland, Greece, Ireland
  (Europe); Nigeria, Kenya, South Africa (Africa); United States, Australia,
  India, Brazil (global anchors). The set is Europe-weighted for relevance to the
  Dutch/EU context, with global anchors to widen the hazard range so normalisation
  has real spread to work with.
- **Time window:** observed data, **2000 to 2023** (exact end year varies slightly
  by country). Projection data (which would reach 2025 and beyond) is deliberately
  excluded, as it depends on emissions scenarios and is not appropriate for an
  observed-exposure screening tool.
- **Aggregation:** each hazard is averaged across 2000-2023 to produce one
  cross-sectional exposure value per country per hazard.

### 5.2 Hazard selection

Physical hazard indicators are selected from CCKP. The working set:

- **Heat** — a temperature-extreme indicator (e.g. maximum of daily maximum
  temperature, or a hot-days index), chosen over mean temperature because heat
  *hazard* is better represented by extremes.
- **Heavy rainfall (flood direction)** — a heavy-precipitation index. Rainfall is
  treated as a **flood-direction hazard only**: higher values mean higher
  exposure, consistent in direction with the other hazards. Drought and water
  scarcity (the low-rainfall hazard) are out of scope unless captured by a separate
  drought indicator below.
- **Drought / aridity (optional)** — an aridity or SPEI-type drought index, added
  as a land-based hazard available for most countries. If included, it is treated
  as a distinct hazard, not folded into rainfall.
- **Sea level (under review)** — available via CCKP but only as EEZ-aggregated
  data accessed through NASA servers, awkward to extract and undefined for
  landlocked countries. Likely scoped out of the first version and noted as a
  limitation; included only if extraction proves quick.

Emissions, renewable energy share, and forest cover are excluded by design: these
are mitigation/emissions indicators, not measures of physical exposure.

### 5.3 Index construction (the four steps)

The index follows the standard four-step logic for composite indicators,
consistent with the OECD/JRC *Handbook on Constructing Composite Indicators*:

1. **Indicator selection** — choose the hazards above and document why each is
   included and what it represents.
2. **Normalisation** — rescale each indicator onto a common 0 to 1 range (min-max)
   so variables in different units become comparable.
3. **Weighting** — assign a weight to each hazard. Equal weighting is the
   transparent default; the choice is treated as an explicit, defensible judgement
   rather than a hidden assumption.
4. **Aggregation** — combine the weighted, normalised indicators into a single
   exposure score per country, then rank.

### 5.4 Interpretation and robustness

- **Driver decomposition:** the composite score is broken back down into its
  hazard contributions to show *why* each high-risk country ranks where it does.
- **Sensitivity analysis:** the index is re-calculated under alternative weighting
  schemes (e.g. equal weights vs an adjusted set) to test whether the ranking is
  robust or depends heavily on the weighting assumption. This is the standard,
  credible answer to the common criticism that composite-index weights are
  arbitrary.

### 5.5 Presentation

Results are delivered through a documented notebook (the full method) and a simple
interactive dashboard that lets a non-technical user view and filter the country
ranking.

## 6. Contributions

- **A worked demonstration** of physical-risk screening as required under CSRD
  (ESRS E1) and TCFD, translating an abstract regulatory obligation into a
  concrete, reproducible method.
- **A transparent methodology** in which every choice (hazard selection,
  normalisation, weighting, aggregation) is documented and open to challenge,
  addressing the criticism that composite indices hide value judgements inside a
  single number.
- **An interpretation layer** that moves beyond presenting data to evaluating it:
  identifying drivers of exposure and testing robustness, which is the step that
  turns information into a basis for decisions.
- **A reusable, auditable pipeline** built on authoritative open data, reflecting
  the data discipline increasingly expected in CSRD-era sustainability reporting,
  where disclosures are subject to external assurance.

## 7. References

- IFRS Foundation / TCFD: *Recommendations of the Task Force on Climate-related
  Financial Disclosures.*
- EFRAG: *European Sustainability Reporting Standards (ESRS),* in particular ESRS
  E1 Climate Change.
- OECD & European Commission Joint Research Centre: *Handbook on Constructing
  Composite Indicators: Methodology and User Guide.*
- World Bank: *Climate Change Knowledge Portal (CCKP)* — observed country-level
  climate data (CRU, ERA5 sources), CC-BY 4.0.
  https://climateknowledgeportal.worldbank.org
- IPCC: *Sixth Assessment Report* — definitions of acute and chronic physical
  climate hazards (for hazard framing).

## 8. Other relevant notes

### Scope boundaries (what this project is not)

- It is **country-level, not asset-level.**
- It uses **observed indicators, not forward-looking climate projections** or
  scenario analysis.
- It does **not estimate financial loss.**
- It captures **high-rainfall (flooding) exposure but not drought or water
  scarcity**, unless a separate drought indicator is included.

These boundaries are deliberate. They keep the project finishable and are the
honest limitations to state when presenting it.

### Limitations to note

- **Data completeness varies by country.** Observed climate records are generally
  more complete for Western Europe than for some African countries, where there
  may be more gaps and interpolation. Uneven data availability is itself a real
  feature of global climate-risk assessment and is reported rather than hidden.
- **Weighting involves judgement.** Equal weighting is a defensible default but a
  judgement nonetheless; the sensitivity analysis exists precisely to show how much
  that judgement affects the result.
- **Annual aggregates are coarse.** Averaging across 2000-2023 and using annual
  indicators cannot capture within-year intensity or the timing of events; the
  index measures broad relative exposure, not event-level risk.
- **Sea level may be excluded** for tractability; if so, a relevant chronic coastal
  hazard is absent from the first version and noted as such.

### Definition of done

A clean notebook that loads and prepares the CCKP data, builds the normalised and
weighted composite index, ranks the 21 countries, decomposes the drivers, and runs
one sensitivity analysis; plus a simple dashboard showing the ranking; plus a short
methodology write-up. No machine learning, no additional hazards beyond the chosen
set, no asset-level precision required.

### Possible extensions (only after "done")

- Use the 2000-2023 time dimension to show how exposure has shifted over time.
- Add EM-DAT extreme-event frequency as an acute-hazard indicator.
- Benchmark the index against the official ND-GAIN exposure ranking as a form of
  validation.
- Test alternative normalisation or aggregation methods.
