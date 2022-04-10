try:
    text = input('Введите что-нибудь')
except EOFError:
    print('НУ зачем вы мне сделали EOFE?')
except KeyboardInterrupt:
    print('Вы отменили операцию')
else:
    print('Вы ввели {0}'.format(text))
