from datetime import datetime

dates = ["2024-12-31", "2023-01-15", "2025-06-20"]

sorted_dates = sorted(dates, key=lambda d: datetime.strptime(d, "%Y-%m-%d"))

print(sorted_dates)
