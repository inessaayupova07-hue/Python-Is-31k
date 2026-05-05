class BankAccount:
    __slots__ = ('balance',)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Недостаточно средств")
        else:
            self.balance -= amount

b = BankAccount()
b.balance = 100
b.withdraw(150)
b.deposit(50)
print(b.balance)
