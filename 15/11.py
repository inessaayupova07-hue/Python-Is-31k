from datetime import datetime

date_obj = datetime.strptime("2024-12-31", "%Y-%m-%d")

print(date_obj.day)
print(date_obj.month)
print(date_obj.year)
