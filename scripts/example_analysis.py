import pandas as pd

# קריאה של הדאטה
df = pd.read_csv("data/spare_parts_budget_wide_example.csv")

# סיכום תקציב 2024 לפי משק-אב
summary = df.groupby("משק-אב")[['plan_budget_2024', 'actual_budget_2024']].sum()
print("סיכום תקציב 2024 לפי משק-אב:\n", summary)

# דוח חריגות: סטטוס 'ביצוע חריג' או 'תוספת רכש חרום' ב-2023/2024
mask = df["status_2024"].isin(["ביצוע חריג", "תוספת רכש חרום"]) | df["status_2023"].isin(["ביצוע חריג", "תוספת רכש חרום"])
print("\nפריטים עם חריגות במלחמה:\n", df.loc[mask, ["item_id", "משק-אב", "משק-בן", "תיאור פריט", "status_2023", "remarks_2023", "status_2024", "remarks_2024"]])

# השוואה: הפרשים בין תכנון לביצוע בפועל
df["gap_2024"] = df["actual_budget_2024"] - df["plan_budget_2024"]
print("\nפריטים עם חריגה שלילית/חיובית ב-2024:\n", df[["item_id", "משק-אב", "משק-בן", "תיאור פריט", "plan_budget_2024", "actual_budget_2024", "gap_2024"]].head())