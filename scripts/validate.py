from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
d=pd.read_csv(root/'civic dasboard/civic_issues.csv')
assert len(d)==919 and d.Report_ID.is_unique
assert not {'Citizen_Name','Age'}.intersection(d.columns)
assert d.Report_ID.str.fullmatch(r'ISSUE_\d{5}').all()
assert not d.duplicated().any()
print('919 unique reports; no citizen names/ages; no duplicate rows.')
