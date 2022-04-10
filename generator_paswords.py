import string
import random

answers = []
count = 0
lengt_pasword = 0

dictionary = [string.digits, string.ascii_uppercase, string.ascii_lowercase, string.punctuation]


def generate_pasword(length, chars):
    pasword = ''
    for i in range(length):
        pasword += random.choice(chars)
    return pasword


def question():
    lengt_pasword = int(input('Длина одного пароля \n'))
    includ_dig = input('Включать ли цифры 0123456789? (y/n) \n')
    includ_up = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) \n')
    includ_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) \n')
    includ_chr = input('Включать ли символы !#$%&*+-=?@^_? (y/n) \n')
    includ_deferent = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) \n')

    answers = [includ_dig, includ_up, includ_lower, includ_chr]
    chars = ''

    for i in range(len(answers)):
        if answers[i] == 'y':
            chars += dictionary[i]
    return (lengt_pasword, chars)


flag_game = True
while flag_game:
    print('Для создания пароля ответьте на следующие вопросы: (ответ ввести: y = да, n = нет)  \n')
    count = int(input('Количество паролей для генерации \n'))
    x, y = (question())
    for i in range(count):
        print('Ваш {} пароль:  '.format(i +1), generate_pasword(x, y))
    flag_continue = True
    while flag_continue:
        print('Хотите создать новые пароли? (y/n) \n')
        answer = input()
        if answer == 'y':
            flag_continue = False
        elif answer == 'n':
            print('Пока, увидимся в следующий раз')
            flag_continue = False
            flag_game = False
        else:
            print('Введите корректный ответ')





