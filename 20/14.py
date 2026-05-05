class SingleAssign:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise AttributeError("Cannot modify")
        instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
