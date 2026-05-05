class ListOfNumbers:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if not all(isinstance(x, (int, float)) for x in value):
            raise TypeError("Only numbers allowed")
        instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
