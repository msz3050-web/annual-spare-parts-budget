import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/spare_parts_budget_wide_example.csv")
grouped = df.groupby("משק-אב")[[(f"actual_budget_{year}" for year in range(2019, 2025))]].sum().T
grouped.plot(kind="line", marker='o')
plt.title("מגמות תקציב בפועל לפי משק-אב (2019-2024)")
plt.ylabel("תקציב בפועל (ש"ח)")
plt.xlabel("שנה")
plt.legend(title="משק-אב")
plt.tight_layout()
plt.show()