class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input("Введите что-нибудь")
    if len(text)<3:
        raise ShortInputException(len(text),3)

except EOFError:
    print('НУ зачем вы мне сделали EOF?')
except ShortInputException as ex:
    print('ShortInputException: длина введеной строки -- {0} \
          ожидалась, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений')