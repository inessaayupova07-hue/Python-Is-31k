class User:
    __slots__ = ('login', 'password')

    def change_password(self, new_password):
        self.password = new_password

u = User()
u.login = "admin"
u.password = "123"
u.change_password("456")
print(u.password)
