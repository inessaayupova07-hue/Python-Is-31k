class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = "Anna"
p.age = 20

print(p.name, p.age)
