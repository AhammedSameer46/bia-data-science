# Assignment 2A — Global Air Pollution Dataset: Cleaning & Exploration Report

**Prepared by:** Suhana | MSc Computer Science (Data Analytics)

---

## 1. Dataset Dimensions

| Stage | Rows | Columns |
|---|---|---|
| Raw dataset | 23,463 | 12 |
| Cleaned dataset | 23,462 | 12 |

**Purpose of the dataset:** City-level air quality measurements for cities worldwide, expressed using the standard Air Quality Index (AQI) framework, enabling comparison of overall and pollutant-specific air quality across countries and cities.

---

## 2. Column Descriptions

| Column | Data Type | Description |
|---|---|---|
| Country | Text (string) | Country in which the monitored city is located |
| City | Text (string) | Name of the monitored city (unique per row) |
| AQI Value | Integer | Overall composite Air Quality Index score (0–500) |
| AQI Category | Text (categorical) | Severity label for the overall AQI (Good → Hazardous) |
| CO AQI Value | Integer | AQI sub-score for carbon monoxide |
| CO AQI Category | Text (categorical) | Severity label for the CO sub-score |
| Ozone AQI Value | Integer | AQI sub-score for ground-level ozone |
| Ozone AQI Category | Text (categorical) | Severity label for the Ozone sub-score |
| NO2 AQI Value | Integer | AQI sub-score for nitrogen dioxide |
| NO2 AQI Category | Text (categorical) | Severity label for the NO2 sub-score |
| PM2.5 AQI Value | Integer | AQI sub-score for fine particulate matter (PM2.5) |
| PM2.5 AQI Category | Text (categorical) | Severity label for the PM2.5 sub-score |

---

## 3. Missing Value Summary

| Column | Missing Values (raw) | % of Rows |
|---|---|---|
| Country | 427 | 1.82% |
| City | 1 | 0.004% |
| All other 10 columns | 0 | 0.00% |

---

## 4. Duplicate Summary

- **Full-row duplicates found:** 0
- Zero duplicate records were identified in the raw dataset; no rows were removed on this basis.

---

## 5. Complete Cleaning Log

1. **Initial shape:** 23,463 rows × 12 columns.
2. **Duplicate check:** 0 full-row duplicates found → no removal necessary.
3. **Missing City (1 row):** Dropped. City is a unique record identifier; imputing a fabricated name is inappropriate, and the loss (1 row, 0.004%) is negligible.
4. **Missing Country (427 rows):** Filled with the label `"Unknown"`. The associated AQI measurements in these rows were fully complete and valid, so dropping ~1.82% of the dataset would have discarded genuine pollution data unnecessarily. Mode/most-frequent imputation was avoided because assigning a specific real country to an unlabelled city without a verified lookup source would fabricate geographic information.
5. **Whitespace check (Country, City):** 0 leading/trailing whitespace issues found → no standardization required.
6. **Category label consistency check** (AQI Category, CO/Ozone/NO2/PM2.5 AQI Category): all six columns use a single consistent, standard set of AQI severity labels (Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, Hazardous) → no standardization required, none found.
7. **Negative/invalid numeric value check** (all 5 AQI value columns): 0 negative or out-of-range values found → no correction required.
8. **Final shape:** 23,462 rows × 12 columns. Net rows removed: **1**. Net rows re-labelled: **427**.

---

## 6. Three Key Trends

1. **PM2.5 dominates the overall AQI.** PM2.5 AQI Value correlates with overall AQI Value at **r ≈ 0.98**, far higher than CO (r ≈ 0.43), Ozone (r ≈ 0.41), or NO2 (r ≈ 0.23). Particulate matter — not gaseous pollutants — is the primary driver of a city's overall air quality rating in this dataset.
2. **Air quality is strongly regionalised.** Among countries with at least 20 monitored cities, Pakistan (mean AQI **178.8**), India (**153.0**), Senegal (**152.4**), and China (**127.0**) have the highest average AQI, while Bolivia (**23.8**), Uruguay (**26.7**), and Argentina (**28.2**) have the lowest — a gap exceeding 150 AQI points between the most- and least-polluted country averages.
3. **Most cities report acceptable air quality.** **81.7%** of cities fall into the "Good" (9,936 cities) or "Moderate" (9,231 cities) categories, while only **2.0%** (478 cities) fall into "Very Unhealthy" or "Hazardous" — pollution severity is concentrated in a relatively small share of locations.

---

## 7. Two Anomalies

1. **Seoul, Republic of Korea — single-city country sample.** Seoul is the only Korean city in the dataset and records an AQI of **421** ("Hazardous") with a PM2.5 AQI of **415**, far above the pattern implied by other large-sample East Asian countries such as China (mean 127.0). Because Korea's average is drawn from a single observation, it should not be interpreted as representative of the country's national air quality.
2. **Boundary mismatches between AQI Value and AQI Category.** 148 rows (0.63% of the cleaned dataset) carry a category label inconsistent with standard EPA AQI breakpoints applied to their numeric AQI Value — e.g., 95 rows with AQI Value = 150 are labelled "Unhealthy" rather than "Unhealthy for Sensitive Groups," and 52 rows with AQI Value = 100 are labelled "Unhealthy for Sensitive Groups" rather than "Moderate." All mismatches fall exactly on category boundary values (100, 150, 300), suggesting a differing inclusive/exclusive boundary convention in the source data rather than random data-entry error. These labels were left unmodified since the intended convention could not be confirmed.

---

## 8. Assumptions

- Missing Country values were assumed genuinely unrecorded (not erroneous) and labelled `"Unknown"` rather than inferred from city name, as no verified city-to-country reference was used.
- The single row missing a City value was assumed safe to drop given its negligible weight (0.004% of records) and City's role as a unique identifier rather than a measurable variable.
- Boundary mismatches between AQI Value and AQI Category were assumed to reflect a source-data boundary convention rather than corruption, and were left unmodified rather than reassigned.
