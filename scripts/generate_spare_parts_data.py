import pandas as pd
import random

main_categories = [
    "רק\"ם", "צמ\"ה", "ניוד", "נשק", "תקשוב", "מערכות מיוחדות", "אנרגיה", "אחר"
]
sub_categories = {
    "רק\"ם": ["מרכבה סימן 4", "נמר", "נגמ\"ש זלדה", "נגמ\"ש אכזרית", "מרכבה סימן 3"],
    "צמ\"ה": ["שופל CAT 950", "באגר VOLVO EC210", "שופל JCB 4CX"],
    "ניוד": ["משאית DAF", "משאית MAN", "משאית איסוזו"],
    "נשק": ["M16", "M4A1", "MINIMI"],
    "תקשוב": ["רחפן EVO II", "רחפן AVATA"],
    "מערכות מיוחדות": ["פנדה"],
    "אנרגיה": ["גנרטור 60KVA"],
    "אחר": ["מערכת בקרה", "חומרי תחזוקה"]
}
statuses = ["בוצע", "חלקי", "נדחה", "ביצוע חריג", "השלמה עקב מבצע", "תוספת רכש חרום"]
remarks = [
    "אין חריגות", "אספקה סדירה", "החלפה מואצת", "צריכה מוגברת", 
    "פעילות מבצעית", "מבצע 'חרבות ברזל'", "פיילוט", "שילוב יחידות נוספות"
]
years = list(range(2019, 2025))
rows = []

for i in range(1, 301):
    main = random.choices(main_categories, weights=[65,12,5,5,5,4,2,2])[0]
    sub = random.choice(sub_categories[main])
    item_id = 1000 + i
    desc = f"{sub} - חלק {random.randint(1, 10)}"
    row = [item_id, main, sub, desc]
    for year in years:
        plan_qty = random.randint(10, 100)
        plan_budget = plan_qty * random.randint(800, 30000)
        actual_budget = int(plan_budget * random.uniform(0.9, 1.1))
        status = random.choice(statuses)
        remark = random.choice(remarks)
        row += [plan_qty, plan_budget, actual_budget, status, remark]
    rows.append(row)

columns = ["item_id","משק-אב","משק-בן","תיאור פריט"]
for year in years:
    columns += [f"plan_qty_{year}", f"plan_budget_{year}", f"actual_budget_{year}", f"status_{year}", f"remarks_{year}"]

df = pd.DataFrame(rows, columns=columns)
df.to_csv("data/spare_parts_budget_wide_example.csv", index=False)