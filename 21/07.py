class Point:
    __slots__ = ('x', 'y')

    def to_string(self):
        return f"({self.x}, {self.y})"

p = Point()
p.x = 1
p.y = 2
print(p.to_string())
