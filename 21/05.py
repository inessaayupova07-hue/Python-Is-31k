class Book:
    __slots__ = ('title', 'author')

    def info(self):
        print(f"{self.title} by {self.author}")

b = Book()
b.title = "1984"
b.author = "Orwell"
b.info()
