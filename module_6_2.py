class Vehicle:
    # общий атрибут неизменяемый - набор цветов
    # __COLOR_VARIANTS = ['red', 'white', 'yellow', 'green', 'magenta', 'black', 'gray']
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        # owner - ИЗМЕНЯЕМЫЙ атрибут
        self.owner = owner
        # НЕИЗМЕНЯЕМЫЕ атрибуты (модель, цвет, мощность)
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    # получим модель (строка с названием)
    def get_model(self):
        return f'Модель: {self.__model}'

    # получим лошадиные силы :) мощность
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    # получим цвет
    def get_color(self):
        return f'Цвет: {self.__color}'

    # вывод данных об авто
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Изменение цвета, если цвет есть в списке допустимых. Если нет, то сообщение
    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()