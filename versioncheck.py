import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы нужна как минимум 3-я версия Python",
                  RuntimeWarning)
else:
    print('Нормальное продолжение')
