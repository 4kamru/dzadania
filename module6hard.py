import math

# класс Фигура с общими атрибутами и методами для потомков
class Figure:
    # атрибут класса - число сторон разное будет в зависимости от того, какая фигура
    sides_count = 0
    # судя  по Circle((200, 200, 100), 10) в проверках. на вход подается кортеж из r,g,b -
    # но потом это всё попадает в СПИСОК цветов
    # и ещё список сторон (они могут быть разными у треугольника)
    def __init__(self, color=(0, 0, 0), *sides):
        # clr = self.get_color()
        # Признак закраски " filled " мы не передаем - он True, если будут заданы корректные цвета
        self.filled = False
        # если заданы корректные цвета, то инициализация с их значениями, если нет - то с нулями (все черное..)
        if self.__is_valid_color(*color):
            self.__color = list(color)
        else:
            self.__color = [0,0,0]

        # если список сторон корректен, то инициализируем этим списком
        # если нет, - то оставляем список из элементов длиной 1 и число этих элементов = sides_count
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        # проблема с периметром:
        # надо принудительно установить длины сторон в 1, если число сторон больше, чем sides_count
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1)

    # проверка задаваемого цвета на корректность (r, g, b  > 0 и в диапазоне 0 - 255)
    def __is_valid_color(self, r, g, b):
        return ((isinstance(r, int) and 0 <= r <= 255) and (isinstance(g, int) and 0 <= g <= 255) and (
                    isinstance(b, int) and 0 <= b <= 255))

    # проверка задаваемого списка сторон на корректность.
    # если числа > 0 и оно равно sides_count (у треугольника там будет 3, у круга 1 и т.д. - то ИСТИНА
    # def __is_valid_sides(self, *sides):
    #     if (len(sides) == self.sides_count):
    #         return all(isinstance((i), int) and (i > 0) for i in sides)
    #     else:
    #         return(False)
    #
    # ЕЩЁ ОДНО: сумма 2-х сторон треугольника не может быть меньше третьей. Иначе у нас не получится треугольник...
    # Если расширять класс, то и для других фигур должна быть какая-то проверка...
    def __is_valid_sides(self, *sides):
        res1 = False
        res2 = True
        if (len(sides) == self.sides_count):
            res1 = all(isinstance((i), int) and (i > 0) for i in sides)
        else:
            res1 = False

        if (self.sides_count == 3):
            a = sides[0]
            b = sides[1]
            c = sides[2]
            if (a + b > c) and (a + c > b) and (c + b > a):
                res2 = True
            else:
                res2 = False
                print('Треугольник с такими сторонами невозможен. Стороны приводятся к 1')

        # res2 = True
        return(res1 and res2)

    # получаем список сторон ( там приватный атрибут - по другому никак)
    def get_sides(self):
        return self.__sides

    # задаем список сторон - если число сторон не равно sides_count - то ничего не изменится
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


    # получаем список цветов (по другому никак, т.к. __сolor приватный атрибут )
    def get_color(self):
        return self.__color


    # Задаём цвет. Если новые цвета корректны - то будут приняты они. Если нет - все останется как было
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True
        else:
            pass
            # self.__color = [0, 0, 0]
            # print('Некорректный цвет')  # пусть будет для проверки

    # расчет периметра
    def __len__(self):
        return(sum(self.__sides))


# Круг (наследник фигуры)
class Circle(Figure):
    # По сути - отличительный признак круга - одна сторона
    sides_count = 1
    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color,*sides)
        # расчет радиуса
        self.__radius = self.get_sides()[0]/(2 * math.pi)

    # радиус круга сделаем доступным для считывания
    def get_radius(self):
        return self.__radius
        # print(self.get_sides())

    # площадь круга через радиус
    def get_square(self):
        return math.pi * (self.get_radius()**2)

# Треугольник (наследник фигуры)
class Triangle(Figure):
    # Отличительный признак треугольника
    sides_count = 3
    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color,*sides)

    # площадь треугольника  по формуле Герона
    def get_square(self):
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        p = 1 / 2 * (a + b + c)
        return (math.sqrt(p * (p - a) * (p - b) * (p - c)))

# Куб (наследник фигуры)
class Cube(Figure):
    # Признак куба: 12 сторон
    sides_count = 12
    # передаем только 1 сторону, поэтому так
    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    # объем куба
    def get_volume(self):
        # рассчитать исходя из ПЕРИМЕТРА? - _len_
        vol = self.get_sides()[0]**3
        return vol


# fig = Figure((300,200,100),4)
# print('1:', fig.filled)
# fig.set_color(10,20,30)
# print('2:', fig.get_color())
# print('3:', fig.filled)
# print('4:', fig.get_color())
# print('5:', fig.get_sides())
#
# circle1 = Circle((200, 200, 100), 10, 20, 30)
# print('6:',circle1.get_color())
# circle1.set_color(55, 66, 77) # Изменится
# print('7:',circle1.get_color())
# print('8:', circle1.get_sides())
# circle1.set_sides(15,10) # длина окружности не изменится (1 параметр лишний)
# print('9:', circle1.get_sides())
#
# print('10:', len(circle1))
#
# circle1.set_sides(15) # длина окружности изменится
# print('11:',circle1.get_sides())
# print('12:',len(circle1))
# print('12 а - радиус:',circle1.get_radius())
#
t0 = Triangle((100,200,250),2,2,10)
print('13:', t0.get_color())
print('14:', t0.get_sides())
print('15:', t0.get_square())
t1 = Triangle((100,200,250),3,4,5)
print('16:', t1.get_color())
t1.set_color(256,200,-1)  # это должно быть проигнорировано
print('17:',t1.get_color())
t1.set_color(255,200,1)
print('18:',t1.get_color())
print('19:',t1.get_sides())
print('20:', t1.get_square()) # площадь должна быть равна 6 (там прямоугольный треугольник)
################################################################################################################
print()
print('------------------главная проверка------------------')
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

