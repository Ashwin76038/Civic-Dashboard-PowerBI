# Civic Issue Reporting Analysis

A supporting BI case study for understanding issue volumes by area, type and severity.

## Dataset and grain

The reviewed file contains **919 unique report records** after removing **49 exact duplicate rows** from 968 input rows. Names and ages were removed; report IDs were replaced with artificial issue keys. Data origin and real-versus-synthetic status remain unverified. Do not describe it as measured municipal operations.

## Business questions

- Which issue types account for the largest report volumes?
- Where are reports concentrated by ward and area?
- How does reported severity vary across issue types?

The data has no reliable resolution timestamps or status history. It cannot establish response time, backlog or service improvement.

## Privacy and dashboard status

The public CSV excludes citizen names and ages. The original PBIX and screenshot were quarantined outside the checkout because imported model data could retain names and the visual predates deduplication. Rebuild Power BI from the sanitized CSV, validate totals, and export a new image before featuring this project. Historical Git objects may still contain the originals.

## Reproduce

```bash
python -m pip install pandas
python scripts/validate.py
```

Import `civic dasboard/civic_issues.csv` into Power BI. Retain this legacy folder name for path compatibility. Set Submission_Date to date with the source locale verified, Report_ID to text and Ward_Number to category. Use distinct Report_ID for report counts; create a date dimension for date filtering.

See [verified counts](docs/validated_metrics.json). No production impact or model accuracy is claimed.
