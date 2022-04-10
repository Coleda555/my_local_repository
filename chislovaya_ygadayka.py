import random

count = 0
num_input = ''
border1 = 1
border2 = 100
num_random = 0
flag_game = True


def check_number(number, border1, border2):
    if number.isdigit():
        number = int(number)
        if border1 - 1 < number < border2:
            return True
        else:
            return False
    else:
        return False


def game ():
    print('Добро пожаловать в числовую угадайку')
    print('Введите границу поиска числа')
    border1, border2 = input(), input()
    flag = True
    while flag:
        if border1.isdigit() and border2.isdigit() :
            border1 = int(border1)
            border2 = int(border2)
            flag = False
        else:
            print('Вы ввели не число, введите натуральное число')
            border1, border2 = input(), input
    num_random = random.randrange(border1, border2)
    print('Введите число от {0} до {1}'.format(border1, border2))
    num_input = input()
    flag = True
    while flag:
        if check_number(num_input, border1, border2) == False:
            print('А может быть все-таки введем целое число от {0} до {1}?'.format(border1, border2))
            num_input = input()
        else:
            flag = False
    count = 1
    num_input = int(num_input)

    while num_input != num_random:
        if num_input < num_random:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            num_input = input()
            flag_check = True
            while flag_check:
                if check_number(num_input, border1, border2) == False:
                    print('Введите корректное число')
                    num_input = input()
                else:
                    flag_check = False

        elif num_input > num_random:
            print('Ваше число больше загаданного, попробуйте еще разок')
            num_input = input()
            flag_check = True
            while flag_check:
                if check_number(num_input, border1, border2) == False:
                    print('Введите корректное число')
                    num_input = input()
                else:
                    flag_check = False
        num_input = int(num_input)
        count += 1
    print('Вы угадали, поздравляем! Что бы угадать число вам понадобилось {} попыток'.format(count))

while flag_game:
    game()
    print('Хотите сыграть еще раз? (y/n)')
    answer = input()
    flag_answer = True
    while flag_answer:
        if answer in ('y', 'n'):
            if answer == 'y':
                flag_answer = False
                game()
            elif answer == 'n':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                flag_game = False
                flag_answer = False
        else:
            print('Введите корректный ответ!')
            answer = input()

