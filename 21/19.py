class Order:
    __slots__ = ('items',)

    def total(self):
        return sum(self.items)

o = Order()
o.items = [10, 20, 30]
print(o.total())
