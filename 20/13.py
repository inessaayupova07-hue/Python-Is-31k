class RoundFloat:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        instance.__dict__[self.name] = round(value, 2)
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
