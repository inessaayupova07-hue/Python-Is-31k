with open("input.txt", "r") as src, open("numbered.txt", "w") as dst:
    for i, line in enumerate(src, 1):
        dst.write(f"{i}: {line}")
