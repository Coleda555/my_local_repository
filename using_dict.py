ab = {'swopoop': 'swopoor@nvf.ru',
      'Larry': 'larry@bob.com',
      'Dmitry': 'dmitry@mail.ru',
      'Pirat': 'blak@list.ny'
      }
print('Адрес swopoop -', ab['swopoop'])

del ab['Pirat']
print('\n В адресной книге {0} контакта\n'.format(len(ab)))
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
ab['Guido'] = 'guido@pyton.ru'
if 'Guido' in ab:
    print('\n Адрес Guido:', ab['Guido'])
