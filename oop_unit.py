class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Привет, меня зовут', self.name)


p = Person('Kaliada')
p.say_hi()
