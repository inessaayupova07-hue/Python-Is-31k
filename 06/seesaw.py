class SeeSaw:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_left(self, weight):
        self.left += weight

    def add_right(self, weight):
        self.right += weight

    def balance(self):
        if self.left == self.right:
            return "="
        elif self.right > self.left:
            return "R"
        else:
            return "L"
