x = 50


def funcGlobal():
    global x
    print('x равен', x)
    x = 2
    print('заменяем глобальное значение х на', x)


funcGlobal()
print("x равен", x)
