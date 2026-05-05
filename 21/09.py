import math

class Circle:
    __slots__ = ('radius',)

    def area(self):
        return math.pi * self.radius ** 2

c = Circle()
c.radius = 2
print(c.area())
