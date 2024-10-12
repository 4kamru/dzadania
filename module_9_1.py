# Задача "Вызов разом"
# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)

# Эта функция должна:
# Вызвать каждую функцию к переданному списку int_list
# Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.

def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        result[i.__name__] = i(int_list)

    return result

# ПРОВЕРКА
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
