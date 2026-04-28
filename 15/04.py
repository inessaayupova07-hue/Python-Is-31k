import csv

with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ages = [int(row["age"]) for row in reader]

print(sum(ages) / len(ages))
