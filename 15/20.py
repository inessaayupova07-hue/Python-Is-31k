from collections import Counter

error_days = Counter()

with open("log.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
            date = line.split()[0]
            error_days[date] += 1

for date, count in error_days.items():
    print(f"{date}: {count}")
