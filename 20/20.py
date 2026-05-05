class ComplexDescriptor:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Only int")
        if not (0 <= value <= 100):
            raise ValueError("Out of range")
        print(f"Setting {value}")
        instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        print("Getting value")
        return instance.__dict__.get(self.name)
    def __delete__(self, instance):
        raise AttributeError("Cannot delete")
