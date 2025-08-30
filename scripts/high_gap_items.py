import pandas as pd

df = pd.read_csv("data/spare_parts_budget_wide_example.csv")
df["gap_2024"] = (df["actual_budget_2024"] - df["plan_budget_2024"]).abs()
high_gap = df[df["gap_2024"] > 10000]
print("פריטים עם חריגה גבוהה (>10,000 ש"ח) בין תכנון לביצוע ב-2024:")
print(high_gap[["item_id", "משק-אב", "משק-בן", "plan_budget_2024", "actual_budget_2024", "gap_2024"]])