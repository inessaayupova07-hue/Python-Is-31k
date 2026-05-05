class Message:
    __slots__ = ('text', 'author')

    def format(self):
        return f"{self.author}: {self.text}"

m = Message()
m.text = "Hello"
m.author = "User"
print(m.format())
