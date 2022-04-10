import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да',
           'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
           'Спроси позже',
           'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай',
           'Мой ответ - нет',
           'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
flag_game = True

print('Привет, Мир! Я магический шар и я знаю ответ на любой твой вопрос.')
print('А как зовут тебя, мой друг?')
name = input()
print('Привет, {}'.format(name))

while flag_game:
    print('Что ты хочешь узнать?')
    question = input()
    print(random.choice(answers))
    print('Хочешь еще что-нибудь узнать, {} ? (y/n) '.format(name))
    answer = input()
    flag_answer = True
    while flag_answer:
        if answer not in ('y', 'n'):
            print('Введите корректный ответ!')
            answer = input()
        elif answer == 'y':
            flag_answer = False
        elif answer == 'n':
            print('Возвращайся, {}, если возникнут вопросы!'.format(name))
            flag_answer = False
            flag_game = False
