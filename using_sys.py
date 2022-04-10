import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PythonPATH содержит', sys.path, '\n')
