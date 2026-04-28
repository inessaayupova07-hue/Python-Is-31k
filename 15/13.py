from datetime import datetime, timedelta

date_obj = datetime.strptime(input("Дата (YYYY-MM-DD): "), "%Y-%m-%d")

days_ahead = (7 - date_obj.weekday()) % 7
if days_ahead == 0:
    days_ahead = 7

next_monday = date_obj + timedelta(days=days_ahead)
print(next_monday.date())
