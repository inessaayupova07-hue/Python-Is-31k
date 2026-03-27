class NumberDivider:
    def __init__(self):
        self.div3 = []
        self.not_div3 = []

    def add_number(self, n):
        if n % 3 == 0:
            self.div3.append(n)
        else:
            self.not_div3.append(n)

    def divisible(self):
        return self.div3

    def not_divisible(self):
        return self.not_div3
