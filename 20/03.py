class LoggingSetDescriptor:
    def __init__(self):
        self.value = None
    def __set__(self, instance, value):
        print("Setting value")
        self.value = value
    def __get__(self, instance, owner):
        return self.value
