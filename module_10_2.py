# Потоки на классах

from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name='', power=0):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        # число  врагов
        num_v = 100
        days = 0
        # задержка по времени
        delay = 1
        print(f'{self.name}, на нас напали!\n')
        while num_v:
            sleep(delay)
            num_v -= self.power
            days += 1
            print(f'{self.name} сражается {days}, осталось {num_v} воинов\n')

        print(f'{self.name} одержал победу спустя {days} дней!\n')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')


