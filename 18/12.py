with open("input.txt", "r") as src, open("filtered.txt", "w") as dst:
    for line in src:
        if len(line.strip()) > 5:
            dst.write(line)
