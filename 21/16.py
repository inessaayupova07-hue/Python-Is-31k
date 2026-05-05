class Temperature:
    __slots__ = ('value',)

    def to_fahrenheit(self):
        return self.value * 9/5 + 32

t = Temperature()
t.value = 0
print(t.to_fahrenheit())
