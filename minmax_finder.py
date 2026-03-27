class MinMaxNumberFinder:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def min_numbers(self):
        if not self.numbers:
            return []
        m = min(self.numbers)
        return [x for x in self.numbers if x == m]

    def max_numbers(self):
        if not self.numbers:
            return []
        m = max(self.numbers)
        return sorted(list(set([x for x in self.numbers if x != min(self.numbers)])))
