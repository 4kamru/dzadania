# Декораторы в Python

# обёртка (декоратор) для функции sum_three или любой другой, выдающей целые числа
# если результат sum_three - простое число, то печатаем "Простое"
# если нет - то "Составное". Ну и возвращаем результат оборачиваемой функции
def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        for j in range(2, x):
            if x % j == 0:
                res = False
                break
            else:
                res = True
        if res:
            print('Простое')
        else:
            print('Составное')
        return x

    return wrapper

# Функция суммирует числа.
@is_prime
def sum_three(*args):
    res = sum(args)
    return res

result = sum_three(2, 3, 6)
print(result)
# Если в аргументах передать строку - будет ошибка
# но с проверкой не заморочиваемся пока...