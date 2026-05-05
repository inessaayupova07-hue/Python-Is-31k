class Rectangle:
    __slots__ = ('width', 'height')

    def area(self):
        return self.width * self.height

r = Rectangle()
r.width = 5
r.height = 3
print(r.area())
