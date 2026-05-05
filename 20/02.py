class LoggingGetDescriptor:
    def __init__(self, value=None):
        self.value = value
    def __get__(self, instance, owner):
        print("Getting value")
        return self.value
