class MaxLength:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if len(value) > 10:
            raise ValueError("Too long")
        instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
