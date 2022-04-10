class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создан SchoolMember {0} '.format(self.name))

    def tell(self):
        print('Возраст {0}, Имя {1}'.format(self.age, self.name), end=" ")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Создат Teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан студент {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: {0:d}'.format(self.marks))

t = Teacher('Petrovich', 55, 1200)
s = Student('Kaliada', 32, 9)

print()

members = [t,s]
for member in members:
    member.tell()