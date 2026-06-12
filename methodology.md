# Methodology

## Climate Risk Exposure Index

---

## 1. Data Source

All hazard data were drawn from the **World Bank Climate Change Knowledge Portal (CCKP)**, the World Bank's designated climate data service. CCKP aggregates authoritative observational records — specifically the ERA5 reanalysis dataset produced by the European Centre for Medium-Range Weather Forecasts (ECMWF) — to national level and distributes them under a **CC-BY 4.0** licence.

This source was chosen deliberately over pre-assembled climate risk datasets for one reason: CCKP provides raw indicators in their natural units. That means all four steps of index construction — indicator selection, normalisation, weighting, and aggregation — are performed in this project rather than inherited from someone else's composite. That transparency is the core methodological requirement for CSRD (ESRS E1) and TCFD physical-risk assessment.

**Attribution:**
> The World Bank, Climate Change Knowledge Portal (CCKP). ERA5 0.25-degree observed historical data. CC-BY 4.0. https://climateknowledgeportal.worldbank.org

---

## 2. Country Selection

The index covers **21 countries** across three groups:

| Group | Countries |
|---|---|
| **European (14)** | Netherlands, United Kingdom, France, Germany, Belgium, Spain, Italy, Portugal, Denmark, Sweden, Norway, Poland, Greece, Ireland |
| **African (3)** | Nigeria, Kenya, South Africa |
| **Global anchors (4)** | United States, Australia, India, Brazil |

The set is Europe-weighted to reflect the CSRD regulatory context (EU-headquartered organisations with global operations). The African and global anchor countries serve two purposes: they widen the hazard range so that normalisation has genuine spread to work with, and they test whether the index produces results consistent with known physical geography (for example, India and Nigeria should rank highly on heat and drought; Norway and Ireland should rank low).

---

## 3. Temporal Scope

The index uses **observed historical data from 2000 to 2023** (24 years), aggregated annually. Each indicator is then averaged across this period to produce a single cross-sectional exposure value per country per hazard.

Projection data (which would extend to 2025 and beyond under CMIP6 emissions scenarios) was explicitly excluded. Physical-exposure screening requires a measure of where hazards stand today based on observed conditions, not a forecast conditional on future emissions pathways.

---

## 4. Indicator Selection

### 4.1 Candidate indicators

Three candidate indicators were downloaded, covering three distinct hazard dimensions:

| Indicator | Variable | Hazard dimension | Units | Direction |
|---|---|---|---|---|
| Maximum of daily maximum temperature | txx | Heat (thermal) | °C | Higher = more exposed |
| Average largest 5-day cumulative precipitation | rx5day | Flooding (water excess) | mm | Higher = more exposed |
| Maximum consecutive dry days | cdd | Drought (water deficit) | days | Higher = more exposed |

Rainfall is treated as a **flood-direction hazard only**: higher values indicate greater flooding exposure. Drought and water deficit are captured by a separate indicator (cdd) rather than being folded into the precipitation variable, consistent with the principle that opposite-direction hazards should not cancel each other out within a single indicator.

**Indicators excluded by design:**

- *Sea level* — available on CCKP only as EEZ-aggregated data via NASA servers, undefined for landlocked countries, and awkward to extract. Excluded from version 1 and noted as a limitation.
- *Emissions and renewable energy indicators* — these measure mitigation effort and transition risk, not physical exposure. Including them would conflate two distinct risk categories.
- *Mean annual temperature* — rejected in favour of txx because heat hazard is better represented by temperature extremes than by the average. A country where the mean temperature is moderate but peak temperatures are extreme presents real heat hazard.

### 4.2 Redundancy check

Because a drought index (consecutive dry days) is partly a function of precipitation, there is a risk that precipitation and drought double-count the same signal at opposite extremes. A Pearson correlation matrix was computed across the 21-country cross-sectional averages before finalising the indicator set:

|  | Temperature | Precipitation | Drought |
|---|---|---|---|
| **Temperature** | 1.000 | 0.461 | 0.818 |
| **Precipitation** | 0.461 | 1.000 | 0.513 |
| **Drought** | 0.818 | 0.513 | 1.000 |

**Decision rule:** a correlation of |r| ≥ 0.70 between two indicators was treated as evidence of redundancy, sufficient to justify dropping or combining one.

**Outcome:**
- Precipitation ↔ Drought: r = 0.513 — below the threshold. Drought adds distinct information and is retained.
- Temperature ↔ Drought: r = 0.818 — above the threshold and worth noting. Hotter countries also tend to have longer dry seasons (a real physical relationship driven by tropical seasonality). This overlap is acknowledged as a limitation; the sensitivity analysis tests whether it affects the robustness of the ranking.

All three indicators were retained for version 1.

**Selection criteria applied** (consistent with OECD/JRC composite-indicator best practice):
- Relevance to the concept (physical hazard exposure)
- Validity (does the variable capture the intended hazard)
- Non-redundancy (correlation check above)
- Data quality and availability across all 21 countries
- Coverage of distinct hazard dimensions
- Interpretability for a non-specialist audience

---

## 5. Normalisation

Each indicator was rescaled to a **0–1 range using min-max normalisation**:

$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$$

where $x_{min}$ and $x_{max}$ are the minimum and maximum values across all 21 countries.

- A score of **0** indicates the country with the lowest observed exposure on that indicator.
- A score of **1** indicates the country with the highest observed exposure.

Min-max normalisation was chosen because it is transparent, interpretable, and widely used in composite indicators (including the UNDP Human Development Index). Its main limitation is sensitivity to outliers: a single extreme country compresses the remaining scores toward zero. In this dataset, India (precipitation) and Australia/Nigeria (temperature, drought) act as high-end anchors — a real feature of the data rather than a statistical artefact, and one that is visible in the heatmap.

---

## 6. Weighting

Each indicator was assigned an **equal weight of 1/3**, producing a symmetric composite:

$$\text{Composite Score} = \frac{1}{3} \cdot \text{Temperature}_{norm} + \frac{1}{3} \cdot \text{Precipitation}_{norm} + \frac{1}{3} \cdot \text{Drought}_{norm}$$

Equal weighting is the standard transparent default in composite-indicator construction. It reflects a deliberate methodological position: in the absence of empirically grounded evidence that one hazard dimension is more consequential than another for all 21 countries, unequal weights would introduce a hidden value judgement. The choice is explicit and open to challenge — which is precisely why the sensitivity analysis (Section 8) exists.

---

## 7. Aggregation

The weighted normalised indicators were summed to produce a single **composite exposure score** per country, ranging from 0 (least exposed) to 1 (most exposed). Countries were then ranked in descending order.

---

## 8. Sensitivity Analysis

To test whether the equal-weighting assumption materially affects the conclusions, the index was recalculated under five alternative weighting schemes:

| Scheme | Temperature | Precipitation | Drought |
|---|---|---|---|
| Equal (baseline) | 1/3 | 1/3 | 1/3 |
| Temperature-heavy | 0.50 | 0.25 | 0.25 |
| Precipitation-heavy | 0.50 | 0.50 | 0.25 |
| Drought-heavy | 0.25 | 0.25 | 0.50 |
| No drought | 0.50 | 0.50 | 0.00 |

**Finding:** India and Nigeria hold ranks 1 and 2 under all five schemes. Australia holds rank 3 or 4 in all schemes. The top tier of the ranking is robust. Mid-table positions (ranks 4–10) show some movement: Portugal shifts between ranks 4 and 6, Brazil between ranks 4 and 5, and Kenya between ranks 5 and 7 depending on the drought weight. These shifts are modest and do not alter the overall structure of the ranking.

---

## 9. Limitations

| Limitation | Implication |
|---|---|
| **Country-level, not asset-level** | The index identifies which countries warrant closer attention; it does not assess exposure at the site or asset level required for detailed TCFD/CSRD disclosure |
| **Observed data only, no projections** | The index captures current exposure. Forward-looking physical risk under different emissions scenarios requires CMIP6 projection data, which is out of scope for version 1 |
| **Sea level excluded** | A chronic coastal hazard is absent from the indicator set. Countries with significant coastal exposure (Netherlands, United Kingdom) may be underscored relative to their true physical risk profile |
| **Annual aggregates are coarse** | Averaging to annual values cannot capture within-year intensity, event timing, or compound hazards (e.g. heat and drought occurring simultaneously) |
| **Precipitation indicator and European flood risk** | rx5day measures rainfall intensity, in which tropical and monsoon countries (India, Brazil, Nigeria) rank highest. European countries such as the Netherlands, Belgium, and Denmark are well-known flood-risk countries but their exposure arises primarily from sea level, river flooding, and land drainage rather than from extreme precipitation events. This means rx5day understates flood exposure for low-lying European countries — a limitation that would be addressed in a more detailed analysis by adding a sea level or river discharge indicator |
| **African data completeness** | Observed climate records are generally more complete for Western Europe than for some African countries. Uneven data availability is an inherent feature of global climate-risk assessment and is reported rather than concealed |
| **Temperature-drought correlation (r = 0.818)** | The strong positive correlation between txx and cdd means the index partially double-weights the hot-and-dry hazard profile of tropical countries. The sensitivity analysis confirms this does not change the top-tier ranking, but it is a legitimate methodological constraint |
| **Min-max sensitivity to anchors** | India (precipitation) and Australia/Nigeria (temperature, drought) act as high-end anchors. Adding or removing one extreme country would shift all normalised scores |
