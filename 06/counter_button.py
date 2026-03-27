class CounterButton:
    def __init__(self):
        self.counter = 0

    def press(self):
        self.counter += 1

    def count(self):
        return self.counter

    def reset(self):
        self.counter = 0
