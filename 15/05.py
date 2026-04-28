import csv

with open("data.csv", newline="", encoding="utf-8") as infile, open("filtered.csv", "w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if int(row["age"]) > 25:
            writer.writerow(row)
