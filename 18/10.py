with open("input.txt", "r") as src, open("upper.txt", "w") as dst:
    dst.write(src.read().upper())
