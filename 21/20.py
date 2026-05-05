class Student:
    __slots__ = ('name', 'age', 'grades')

    def add_grade(self, value):
        self.grades.append(value)

    def average(self):
        return sum(self.grades) / len(self.grades)

s1 = Student()
s1.name = "A"
s1.age = 20
s1.grades = [5, 4, 3]

s2 = Student()
s2.name = "B"
s2.age = 22
s2.grades = [4, 4, 5]

print(s1.average(), s2.average())
