import pandas as pd

df = pd.read_csv("data/spare_parts_budget_wide_example.csv")
df["rate_2024"] = df["actual_budget_2024"] / df["plan_budget_2024"]
rate = df.groupby("משק-בן")["rate_2024"].mean().sort_values(ascending=False)
print("אחוז ביצוע ממוצע ב-2024 לפי משק-בן:\n", rate)