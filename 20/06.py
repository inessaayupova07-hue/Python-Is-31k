class PositiveInt:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Must be positive")
        instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
