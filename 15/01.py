with open("input.txt", "r", encoding="utf-8") as f:
    words = f.read().lower().split()

unique_words = set(words)
print(len(unique_words))
