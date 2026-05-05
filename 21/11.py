class Product:
    __slots__ = ('name', 'price')

    def set_price(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price

p = Product()
p.name = "Phone"
p.set_price(500)
print(p.price)
