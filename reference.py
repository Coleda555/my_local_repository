print('Простое присваивание')
shoop_list = ['Яблоко', 'Апельсин', 'Мандарин', 'Лимон']
mylist = shoop_list
del shoop_list[0]
print('shoop_list:', shoop_list)
print('mylist:', mylist)

print('Копирование при полной вырезки')
mylist = shoop_list[:]
del mylist[0]

print('shoop_list:', shoop_list)
print('mylist:', mylist)
