class AccessCounter:
    def __init__(self):
        self.count = 0
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        self.count += 1
        return instance.__dict__.get(self.name)
