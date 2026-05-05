class Animal:
    __slots__ = ('type', 'weight')

a = Animal()
a.type = "Cat"
a.weight = 4

# a.color = "Black"  # Ошибка: нельзя добавить новый атрибут
