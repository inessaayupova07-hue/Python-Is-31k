from collections import Counter

with open("input.txt", "r", encoding="utf-8") as f:
    words = f.read().lower().split()

counter = Counter(words)

for word, count in counter.most_common():
    print(word, count)
