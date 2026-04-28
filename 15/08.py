with open("input.txt", "r", encoding="utf-8") as f:
    count = sum(1 for line in f if line and line[0].isupper())

print(count)
