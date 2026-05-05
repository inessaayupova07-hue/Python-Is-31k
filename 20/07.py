class StringOnly:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Only string allowed")
        instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
