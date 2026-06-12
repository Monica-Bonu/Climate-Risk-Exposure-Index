# Data Acquisition Checklist: Climate Risk Exposure Index

A step-by-step guide for pulling country-level hazard data from the World Bank
Climate Change Knowledge Portal (CCKP) and assembling it into one clean CSV.

Work through it top to bottom. The goal is to come away with one tidy
country-by-year table you can load straight into your notebook.

---

## 0. Before you start

**Source:** CCKP download page
`https://climateknowledgeportal.worldbank.org/download-data`

**Key decisions already made (keep these fixed):**

- Data type: **observed / historical only** (NOT projections). Projections pull in
  emissions scenarios you do not want for a physical-exposure screening tool.
- Time window: **2000 to 2023** (observed coverage; exact end year may vary
  slightly by country). Do not chase 2025; that only exists as projection data.
- Hazards: aim for **3 to 4**, all readily available for your country list.
  Suggested set below. Three clean hazards beat four where one fights you.
- Rainfall is treated as **flood-direction only** (higher = more exposed).
  Drought is a separate hazard if you include an aridity index.

**Licence / attribution (note now, use later):**
CCKP data is CC-BY 4.0. Cite as:
`The World Bank, Climate Change Knowledge Portal (CCKP). Data source: [dataset name].`

---

## 1. Country list (21 countries)

Paste or select these in the country picker. Europe-weighted, with global anchors.

**European (14):**
Netherlands, United Kingdom, France, Germany, Belgium, Spain, Italy, Portugal,
Denmark, Sweden, Norway, Poland, Greece, Ireland

**African (3):**
Nigeria, Kenya, South Africa

**Other anchors (4):**
United States, Australia, India, Brazil

> Note: CCKP often limits you to 1 to 3 countries per extraction. If so, you will
> repeat each variable download in country-batches and stack them later. Annoying
> but mechanical. The naming convention in Step 4 keeps this from becoming chaos.

---

## 2. Target variables (three candidate indicators)

On the **Spatially Aggregated Data** download tab, choose **Country** level.

**Important framing:** download all three indicators below as *candidates*. You are
NOT committing to all three being in the final index yet. After cleaning, you will
run a **correlation check** (see Step 6a) to test whether the drought index is too
redundant with precipitation to justify keeping both. The data settles that decision,
not a guess made in advance. Downloading all three is what makes the redundancy check
possible, so even if drought is later dropped, the download is not wasted: the check
itself is part of the methodology.

Each indicator has two layers worth recording: the **variable** (what you pull) and
the **hazard** it represents (why it is in the index).

| Variable (what you pull) | Hazard it represents | Code (verify on site) | Notes |
|---|---|---|---|
| Temperature (mean annual, or a heat-extreme measure) | Heat | `tas` (mean) or `txx` (extreme) | Mean is simpler and fine for v1; an extreme measure is a truer heat-hazard proxy. Pick one and record which. |
| Precipitation (annual total, or a heavy-rain index) | Flooding (wet direction) | `pr` (total) or an ETCCDI wet-day index (e.g. `r95p` / `rx5day`) | Treated as flood-direction only: higher = more exposed. Pick one and record which. |
| Drought index (SPEI / aridity type) | Drought (dry direction) | see Data Dictionary, drought/aridity group | Built largely from precipitation + evapotranspiration, which is exactly why it may overlap with precipitation. Note its exact name and what it is built from. |

**Why these three and not more:** they cover three *distinct* hazard dimensions
(thermal, water-excess, water-deficit), which is good coverage. The one to watch is
the precipitation/drought relationship: a drought index is partly a function of
precipitation, so the two can double-count the same signal at opposite extremes. The
correlation check in Step 6a is there to catch this.

**Sea level: scoped out of v1.** It is available on CCKP only as EEZ-aggregated data
via NASA servers (awkward to extract, undefined for landlocked countries). It is left
out of the first finishable version and noted as a limitation. Revisit only as an
extension once the three-candidate index works end to end.

**Recording rule:** for temperature and precipitation, decide mean vs extreme as you
download, and write down exactly which measure you took. The documentation must match
the data: do not label a mean as if it were an extreme.

**Settings to apply for every variable:**

- Collection / dataset: **observed historical** (e.g. `cru` or `era5`), NOT a
  CMIP6 scenario
- Product: **timeseries** (you want the yearly series, not a single climatology)
- Aggregation period: **annual**
- Statistic: **mean** (or max where it makes sense for an extreme index)
- Time period: the historical option covering **2000 to 2023**
- Output format: **CSV** (or XLSX, then save as CSV)

---

## 3. Extraction loop

Repeat this for each variable (and each country-batch if limited to 3):

1. Open the Spatially Aggregated Data download tab.
2. Set spatial level = **Country**.
3. Select your country (or batch of up to 3).
4. Select the variable (one hazard).
5. Apply the fixed settings from Step 2 (observed, annual, timeseries, 2000-2023).
6. Download as CSV.
7. Rename the file immediately using the convention in Step 4. **Do this before
   the next download** or you will end up with a folder of `download(3).csv`.

---

## 4. File naming convention

Name every file the same way so they merge predictably:

```
hazard_variablecode_countrybatch.csv
```

Examples:
```
temp_tas_batch1.csv
temp_tas_batch2.csv
precip_pr_batch1.csv
drought_spei_batch1.csv
```

Keep all files in one folder, e.g. `cckp_raw/`.

---

## 5. What each file should contain

A good extract has, at minimum:
- a **country** column
- a **year** column (2000 to 2023)
- a **value** column (the hazard variable, in its real units)

If a file has months instead of years, you will aggregate to annual in the
notebook (mean for temperature-type, sum or mean for precipitation-type).
If a file is "wide" (years as columns), you will reshape to long in the notebook.
Either is fine; just note which shape you got.

---

## 6. Assembly plan (done later, in the notebook, not on the site)

You do NOT merge by hand. The notebook will:

1. Load each CSV.
2. Standardise country names (e.g. "United Kingdom" vs "UK" vs "Great Britain").
   Build a small name-mapping dictionary; this is the #1 source of merge bugs.
3. Reshape each to long format: `country, year, hazard, value`.
4. Average each hazard across 2000-2023 to get one value per country per hazard
   (this is your cross-sectional exposure profile).
5. Pivot to one row per country, one column per hazard. That table is the input
   to your four-step index.

---

## 6a. Indicator selection check (the redundancy step)

Before the three candidates become the final indicator set, run a correlation
check on the cleaned country-by-hazard table. This is where "three candidates"
becomes "the chosen indicators."

The notebook will:

1. Compute the correlation matrix between temperature, precipitation, and the
   drought index across the 21 countries.
2. Look specifically at the precipitation vs drought correlation. A strong
   (inverse) correlation means they largely carry the same signal at opposite
   extremes, i.e. the index would double-count precipitation.
3. Decide and document the outcome:
   - **Low/moderate overlap** -> keep all three; the drought index adds distinct
     information.
   - **Strong overlap** -> drop the drought index (or combine), and keep a clean
     two-indicator index, with the correlation result as the documented reason.

Either outcome is defensible because the *decision rule* is principled and
empirical, not a guess. Record the correlation values and the decision in the
notebook and the brief; this is exactly the indicator-selection reasoning an
interviewer wants to see.

Selection criteria applied throughout (from composite-indicator best practice):
relevance to the concept (physical hazard exposure), validity (does the variable
capture the hazard), non-redundancy (the check above), data quality/availability,
coverage of distinct hazard dimensions, and interpretability.

---

## 7. Sanity checks before you trust the data

- [ ] All 21 countries present in every hazard file (or note who is missing).
- [ ] Year coverage is roughly 2000-2023 for each (note gaps).
- [ ] Values are in plausible real units (spot-check 2 or 3 countries you know).
- [ ] Netherlands, Denmark, Belgium show up as expected on flood-direction rain.
- [ ] African countries: check how many missing years (data completeness varies;
      this is a legitimate limitation to report, not a reason to exclude them).

---

## 8. If CCKP proves too fiddly

Fallback without abandoning the project:
- Temperature anomaly and precipitation anomaly are available clean and
  country-level from **Our World in Data** (ERA5 / Copernicus, CC-BY, covers
  2000 to near-present). Two real hazards is thin but valid as a starting index;
  you can layer CCKP hazards on top once the method runs end to end.

---

## Scope reminder

Resist the 70-variable buffet. Pull only your chosen 3 to 4 hazards for your 21
countries across 2000-2023. The richer the pull, the longer the cleaning, and
cleaning-that-never-ends is exactly how the last project stalled. Get a working
index on a small clean set first; expand only after "done".
