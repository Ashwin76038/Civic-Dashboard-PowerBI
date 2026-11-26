# Civic Issue Reporting Analysis

A supporting data-quality and BI case study for exploring reported issue volumes by type, ward and severity. The public deliverable is a sanitized CSV, a Python validator and a metric receipt; a current Power BI report is not included in this repository.

## Analytical questions

- Which issue types account for the largest share of reports?
- How are reports distributed across wards and areas?
- How much missing classification limits severity-based prioritization?

## Data preparation and verified findings

The reviewed input contained 968 rows. Removing 49 exact duplicates produced **919 unique reports**. Citizen names and ages were removed, and report IDs were replaced with artificial issue keys.

| Metric | Result |
|---|---:|
| Unique reports | 919 |
| High-severity reports | 184 |
| Reports with unknown severity | 400 |
| Reports with unknown issue type | 254 |

The missing categories are analytical findings, not values to silently impute. [Full count receipt](docs/validated_metrics.json).

**Source status:** origin and real-versus-simulated status are unverified. These counts describe the supplied dataset, not measured municipal performance. There are no reliable resolution timestamps or status history, so response time, backlog, closure rate and service improvement cannot be calculated.

## Implemented work and structure

| File | Role |
|---|---|
| `civic dasboard/civic_issues.csv` | Sanitized, deduplicated public input; legacy folder spelling retained for compatibility |
| `scripts/validate.py` | Checks 919 unique report IDs, key format, duplicate absence and removal of name/age columns |
| `docs/validated_metrics.json` | Recorded issue and severity counts |

## Reproduce the validation

```bash
python -m pip install pandas
python scripts/validate.py
```

Executed on 25 November 2026 against the reviewed public source: **passed**, reporting 919 unique records with no citizen-name/age columns and no duplicate rows.

## Build a Power BI view

Import the sanitized CSV, verify the source date locale, set `Submission_Date` to date, `Report_ID` to text and `Ward_Number` to a category. Use distinct `Report_ID` for counts and a date dimension for filtering. Reconcile the report totals and unknown categories against the receipt before exporting any preview.

A local report exists separately, but it is not part of this public delivery. No outdated screenshot is shown as evidence of the current sanitized data.

## Privacy and limitations

The original report and image predate deduplication and may retain identifying information in imported model data. They were excluded from the current checkout; historical Git objects may still contain originals. Source authenticity, historical privacy review and redistribution rights remain unresolved. No production deployment, model accuracy or citizen outcome is claimed.

## Author

[Aswin S](https://github.com/Ashwin76038)
