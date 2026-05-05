with open("input.txt", "r") as src, open("clean.txt", "w") as dst:
    for line in src:
        if line.strip():
            dst.write(line)
