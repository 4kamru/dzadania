# Задача "Мифическое наследование"

class Horse:
    """
    Класс Лошадь. Пройденный путь x_distance  увеличивается методом run на dx. Лошадь издает звук  sound = 'Frrr'
    """
    def __init__(self,*args):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*args)

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    """
    Класс Орёл. Сначала он на высоте y_distance = 0, поёт sound, а в полете fly поднимается на dy
    """
    def __init__(self,*args):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__(*args)

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    """
    Класс Пегас на основе классов Лошади и Орла.
    """
    def __init__(self, *args):
        super().__init__(*args)

    # перемещение по горизонтали и вертикали(благодаря родителям)
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # получаем позицию
    def get_pos(self):
        return self.x_distance, self.y_distance

    # Какой будет звук ? Если переставить родителей - будет петь иначе
    def voice(self):
        print(self.sound)


# Проверка
h1 = Horse()
h1.run(10)
print(h1.x_distance, h1.sound)
e1 = Eagle()
e1.fly(20)
print(e1.y_distance, e1.sound)
p0 = Pegasus
print(p0.mro())

print()
print('Главная проверка:')

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()