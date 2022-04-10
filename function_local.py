x = 50


def funcLocal(x):
    print('x равен', x)
    x = 2
    print('Замененный х равен', x)


funcLocal(x)
print('х попрежнему равен', x)
