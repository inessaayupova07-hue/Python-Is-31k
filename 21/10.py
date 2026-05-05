class Employee:
    __slots__ = ('name', 'salary')

    def raise_salary(self, percent):
        self.salary *= (1 + percent / 100)

e = Employee()
e.name = "Max"
e.salary = 1000
e.raise_salary(10)
print(e.salary)
