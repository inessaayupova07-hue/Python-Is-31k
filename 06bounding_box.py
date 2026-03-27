class BoundingBox2D:
    def __init__(self):
        self.xs = []
        self.ys = []

    def add_point(self, x, y):
        self.xs.append(x)
        self.ys.append(y)

    def width(self):
        return max(self.xs) - min(self.xs)

    def height(self):
        return max(self.ys) - min(self.ys)

    def bottom_y(self):
        return min(self.ys)

    def top_y(self):
        return max(self.ys)

    def left_x(self):
        return min(self.xs)

    def right_x(self):
        return max(self.xs)
