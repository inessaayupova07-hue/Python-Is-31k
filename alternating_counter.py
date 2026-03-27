class AlternatingCounter:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.turn_a = True

    def count(self):
        if self.turn_a:
            self.a += 1
        else:
            self.b += 1
        self.turn_a = not self.turn_a
        return (self.a, self.b)

    def reset(self):
        self.a = 0
        self.b = 0
        self.turn_a = True
