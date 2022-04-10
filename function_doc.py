def printMax(x, y):
    ''' Выводит максимальное из двух чисел
    оба значения должны быть целыми'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'большее число')
    else:
        print(y, 'большее')


printMax(3, 5)
print(printMax.__doc__)
