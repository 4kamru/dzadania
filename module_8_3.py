# Класс Car - с атрибутами
# публичный: model (модель авто), приватные: __vin_number (вин - номер), __numbers (номер авто)
class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin_number = vin_number
        self.__numbers = numbers
        # готовимся ловить некорректные номера вин и авто, а также исключения
        self.__is_valid_vin(self.__vin_number)
        self.__is_valid_numbers(self.__numbers)

    # проверка корректности вин-номера. Это должно быть целое число в диапазоне от 1000000 до 9999999
    # если не целое - то некорретный тип, если вне диапазона - то некорректный диапазон
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number,int):
            if vin_number in range(1000000, 9999999):
                res = True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
                res = False
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')
            res = False
        return res

    # проверка корректности номера авто: это должен быть текст длиной ровно 6
    # в противном случае выдаем пользовательские исключения
    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            # res = True
            if len(numbers)==6:
                res = True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
                res = False
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            res = False
        return res

    # на всякий случай - получить номер авто
    def get_numbers(self):
        return self.__numbers

    # на всякий случай - получить вин-номер авто
    def get_vin_number(self):
        return self.__vin_number

# создаётся пользовательское исключение для обработки вин-номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


# создаётся пользовательское исключение для обработки номера авто
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# ПРОВЕРКА
try:
    first = Car('Model1',1000000,'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')


try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')



try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
