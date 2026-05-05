class A:
    __slots__ = ('x',)

class B:
    pass

a = A()
b = B()

a.x = 10
b.y = 20  # можно

# a.y = 5  # ошибка
