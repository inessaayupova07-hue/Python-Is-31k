from datetime import datetime, timedelta

start = datetime.strptime(input("Начальная дата (YYYY-MM-DD): "), "%Y-%m-%d")
end = datetime.strptime(input("Конечная дата (YYYY-MM-DD): "), "%Y-%m-%d")

workdays = 0
current = start

while current <= end:
    if current.weekday() < 5:
        workdays += 1
    current += timedelta(days=1)

print(workdays)
