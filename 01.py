class SimpleDescriptor:
    def __init__(self, value=None):
        self.value = value
    def __get__(self, instance, owner):
        return self.value
