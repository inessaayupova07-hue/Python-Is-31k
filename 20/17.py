class CachedValue:
    def __init__(self, func):
        self.func = func
        self.value = None
        self.computed = False
    def __get__(self, instance, owner):
        if not self.computed:
            self.value = self.func(instance)
            self.computed = True
        return self.value
