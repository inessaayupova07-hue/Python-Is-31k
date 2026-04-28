seen = set()

with open("input.txt", "r", encoding="utf-8") as infile, open("unique.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        if line not in seen:
            seen.add(line)
            outfile.write(line)
