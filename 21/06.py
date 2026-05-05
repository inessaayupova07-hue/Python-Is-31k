class Student:
    __slots__ = ('name', 'grade')

    def change_grade(self, new_grade):
        self.grade = new_grade

s = Student()
s.name = "Ivan"
s.grade = 4
s.change_grade(5)
print(s.grade)
