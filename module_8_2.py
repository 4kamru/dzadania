# ПЕРЕХВАТ ИСКЛЮЧЕНИЙ
import collections
import types
# принимаем коллекцию args, возвращаем сумму чисел и количество НЕчисел
def personal_sum(*args):
    result = 0
    incorrect_data = 0
    # перебор по коллекции
    for val in args:
        # перебор по членам коллекции ( иначе в случае ошибки выдаст 1, 2, 3  вместо требуемого в задании)
        for i in val:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
                # print(f"Ошибка! Ожидалось число, а передано:   Это уже {incorrect_data}-й параметр, не являющийся числом")
                print(f"Некорректный тип данных для подсчёта суммы - {i}")

    return (result, incorrect_data)

# Проверка
# numbers = [1, 2, 3, 4, '-', 'a', 'c', 5]
# print(personal_sum(numbers))


# расчет среднего арифметического, если аргумент - коллекция
def calculate_average(*numbers):
    res = 0
    # если в аргументе лишь одно число:  результат = None
    if isinstance(*numbers, int):
        res = None
        print(f'В numbers записан некорректный тип данных')
    else:
        try:
            # сумму чисел делим на длину коллекции минус количество некорректных данных
            # (это и есть число чисел в коллекции)
            psum = personal_sum(*numbers)
            res = psum[0]/(len(*numbers)-psum[1])
        except ZeroDivisionError:
            res = 0
        finally:
            return res



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать