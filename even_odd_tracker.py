class EvenOddSumTracker:
    def __init__(self):
        self.even = 0
        self.odd = 0

    def add_number(self, n):
        if n % 2 == 0:
            self.even += n
        else:
            self.odd += n

    def even_sum(self):
        return self.even

    def odd_sum(self):
        return self.odd
