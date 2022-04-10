number = 23
running = True
while running:
    guess = int(input("введите любое целое число"))
    if guess == number:
        print('Поздравляю, вы угадали число')
        running = False
    elif guess < number:
        print('Нет, вы загадали число немного меньше')
    else:
        print('Нет, вы загадали число немного больше')
else:
    print("Циккл while закончен")
print('Завершение')
