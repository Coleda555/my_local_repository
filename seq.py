shoop_list = ['Яблоко', 'Апельсин', 'Мандарин', 'Лимон']
name = 'swoorop'
# Операция индексирования
print('Элемент 0 -', shoop_list[0])
print('Элемент 1 -', shoop_list[1])
print('Элемент 2 -', shoop_list[2])
print('Элемент 3 -', shoop_list[3])
print('Элемент -1 -', shoop_list[-1])
print('Элемент -2 -', shoop_list[-2])
print('Символ 0 -', name[0])

# Вырезка из списка
print('Элемент с 1 по 3  -', shoop_list[1:3])
print('Элемент с 2 до конца  -', shoop_list[2:])
print('Элемент с 1 по -1  -', shoop_list[1:-1])
print('Элемент от начало до конца  -', shoop_list[:])

# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начало до конца:', name[:])
