# Climate Risk Exposure Index

A transparent, reproducible composite index of physical climate hazard exposure for 21 countries, built from publicly available observed data to demonstrate the physical-risk screening methodology required by **CSRD (ESRS E1)** and **TCFD**.

---

## What this project does

The index ranks 21 countries by their exposure to three physical climate hazards — temperature extremes, extreme precipitation, and drought — using a four-step methodology consistent with the **OECD/JRC Handbook on Constructing Composite Indicators**:

1. **Indicator selection** — three hazard indicators from ERA5 observed data, with a correlation-based redundancy check
2. **Normalisation** — min-max rescaling to a 0–1 range
3. **Weighting** — equal weights (1/3 each), with a five-scheme sensitivity analysis
4. **Aggregation** — linear weighted sum to a composite exposure score

Every methodological choice is documented with a rationale, making the output auditable and reproducible.

---

## Key findings

| Rank | Country | Composite Score | Primary driver |
|---|---|---|---|
| 1 | India | 0.878 | Heat + precipitation + drought |
| 2 | Nigeria | 0.785 | Drought + heat |
| 3 | Australia | 0.742 | Heat + drought |
| 4 | Portugal | 0.575 | Heat |
| 5 | Brazil | 0.570 | Heat |

The top-tier ranking is **robust to weighting assumptions** — India and Nigeria hold ranks 1 and 2 under all five weighting schemes tested. A clear regional divide separates tropical and semi-arid countries from the European sample, with Mediterranean countries (Portugal, Greece, Spain, Italy) forming a distinct mid-range group.

---

## Repository structure

```
├── 01_data_assembly.ipynb          # Load CCKP files → 504-row panel CSV
├── 02_index_construction.ipynb     # Normalise, weight, rank → outputs + charts
├── 03_dashboard.ipynb              # Interactive Plotly dashboard
├── rebuild_dashboard.py            # Standalone dashboard regeneration script
│
├── cckp_raw/
│   ├── cckp_[country].xlsx         # Raw CCKP downloads (21 files, one per country)
│   └── exposure_panel.csv          # Assembled panel: 504 rows × 5 cols
│
├── outputs/
│   ├── exposure_index_results.csv  # Final ranked results (21 rows)
│   ├── dashboard.html              # Interactive dashboard (standalone HTML)
│   ├── 01_composite_score.png
│   ├── 02_heatmap.png
│   ├── 03_driver_decomposition.png
│   ├── 04_sensitivity_analysis.png
│   ├── 05_scatter_correlations.png
│   └── 06_time_trends.png
│
├── methodology.md                  # Full methodology documentation (9 sections)
├── results.md                      # Results with tables and numbers
├── discussion.md                   # Interpretation against 4 research questions
├── conclusion.md                   # Summary, limitations, future extensions
│
├── CCKP_data_acquisition_checklist.md
└── Climate_Risk_Exposure_Index_Project_Brief.md
```

---

## How to reproduce

### Requirements

```
python >= 3.11
pandas
numpy
matplotlib
plotly
openpyxl
```

Install with:

```bash
pip install pandas numpy matplotlib plotly openpyxl
```

### Run order

1. **`01_data_assembly.ipynb`** — loads the 21 CCKP Excel files from `cckp_raw/` and assembles `exposure_panel.csv`
2. **`02_index_construction.ipynb`** — builds the index, runs the sensitivity analysis, and saves all charts to `outputs/`
3. **`03_dashboard.ipynb`** or **`rebuild_dashboard.py`** — generates the interactive dashboard at `outputs/dashboard.html`

All three notebooks can be run sequentially with a standard Jupyter installation. `rebuild_dashboard.py` can be run directly with `python rebuild_dashboard.py` if you prefer not to use the notebook.

---

## Data source

All hazard data come from the **World Bank Climate Change Knowledge Portal (CCKP)**, using ERA5 0.25-degree observed historical data aggregated to national level.

> The World Bank, Climate Change Knowledge Portal (CCKP). ERA5 observed historical data, 2000–2023. CC-BY 4.0.
> https://climateknowledgeportal.worldbank.org

**Indicators:**

| Indicator | Code | Hazard | Units |
|---|---|---|---|
| Maximum of daily maximum temperature | txx | Heat | °C |
| Largest 5-day cumulative precipitation | rx5day | Flooding | mm |
| Maximum consecutive dry days | cdd | Drought | days |

---

## CSRD and TCFD context

CSRD (ESRS E1) requires organisations to assess and disclose physical climate risk in a systematic, documented manner. TCFD asks for identification of physical risks affecting assets, operations, and supply chains — current and forward-looking. This index demonstrates the **country-level screening stage** of that process: a transparent, auditable first-pass identification of high-exposure geographies that would then be followed by asset-level and scenario-based analysis.

---

## Limitations

- Country-level aggregation masks sub-national variation (particularly relevant for the United States, India, Brazil)
- Sea-level and river-discharge hazards are not included — this understates flood exposure for low-lying European countries (Netherlands, Belgium, Denmark)
- Historical data only (2000–2023); no forward-looking scenario projections
- Temperature and drought indicators are positively correlated (r = 0.818), which partially double-weights the hot-and-dry profile of tropical countries

See [methodology.md](methodology.md) for the full limitations table.

---

## Licence

Code and methodology: MIT  
Data: CC-BY 4.0 (World Bank CCKP)
