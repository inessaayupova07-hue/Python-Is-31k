import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

shapes = [Rectangle(3, 4), Circle(2), Shape()]

for s in shapes:
    print(s.area())
