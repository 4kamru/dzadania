# Очереди для обмена данными между потоками
from threading import Thread
from queue import Queue
import time
import random
class Table:
    """Столик в кафе. Атрибуты: number - номер стола, guest - гость, который сидит за эти столом"""
    def __init__(self, number):

        self.number = number
        self.guest = None

# Единственное для чего этот класс - задержка от 3 до 10 секунд
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # задержка от 3 до 10 секунд (в кафе ведь не мгновенно тебя обслуживают)
        delay = random.randint(3, 10)
        time.sleep(delay)

class Cafe:
    """Кафе, в котором есть определённое кол-во столов
    и происходит имитация прибытия гостей (guest_arrival)
    и их обслуживания (discuss_guests)"""
    # список потоков
    list_t = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    # если есть свободный стол - сажаем гостя (назначаем столу guests)
    # с запуском потока (фактически - с ожиданием обслуживания)
    def guest_arrival(self, *guests):
        list_guests = list(guests)
        list_tables = self.tables
        # число гостей
        num_of_guests = len(list_guests)
        # число занятых столов (если гостей мало, то оно может быть меньше числа столов в кафе)
        # если гостей больше, чем столов, то равно числу столов в кафе. Значит тут минимум из 2-х чисел
        num_z_tables = min(len(self.tables), num_of_guests)
        for i in range(num_z_tables):
            list_tables[i].guest = guests[i]
            # запуск потока гостя
            t = guests[i]
            t.start()
            # добавляем поток в список
            Cafe.list_t.append(guests[i])
            print(f'{list_guests[i].name} сел(-а) за стол номер {list_tables[i].number}')

        # Если свободных столов для посадки не осталось, то помещать гостя в очередь
        if num_of_guests > num_z_tables:
            for i in range(num_z_tables, num_of_guests):
                self.queue.put(guests[i])
                print(f'{list_guests[i].name} в очереди')

    # обслуживание гостей
    def discuss_guests(self):
        # проверяем, есть ли хоть один занятый стол
        for table in self.tables:
            if table.guest is not None:
                res = True

            res = False
        # если очередь не пустая или есть хотя бы один занятый стол
        while (self.queue.empty()==False or res):
            for table in self.tables:
                if not (table.guest is None) and not(table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    t1 = table.guest
                    t1.start()
                    Cafe.list_t.append(t1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


