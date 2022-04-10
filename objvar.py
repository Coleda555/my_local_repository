class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'.format(Robot.population))

    def syHi(self):
        print('Приветствую, мои хозяева называют меня {0}'.format(self.name))

    def howMany():
        print('у нас {0:d} роботов'.format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot('D1-D2')
droid1.syHi()
Robot.howMany()

droid2 = Robot('X1-Y2')
droid2.syHi()
Robot.howMany()

print('\n Здесь роботы могут проделать какую-то работу. \n')
print('Роботы закончили свою работу, давайте уничтожим их.')
del droid1
del droid2

Robot.howMany()
