# РАСПАКОВКА

def print_params(a=1, b="'строка'", c=True):
    print(a, b, c)


print('Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов')
print_params()
print_params(30, 'буква Б')
print_params(40, False)

print()  # просто отступ

print('Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])')
print_params(b=25)
print_params(c=[1, 2, 3])

print()

print('РАСПАКОВКА ПАРАМЕТРОВ')
# типы, как в определении функции
value_list = ['икс', False, 10]
# а что будет? меняю местами параметры разных типов
values_list_2 = [54.32, 'Строка']
#  типы, как в определении функции
values_dict = {'a': 20, 'b': 'игрек', 'c': False}
# а что будет? меняю местами параметры разных типов
values_dict_2 = {'b': 'зет', 'c': True, 'a': 30}

print('передаем в функцию список - value_list')
print_params(*value_list)
print('передаем в функцию список - values_list_2 ')
print_params(*value_list)

print()

print('Проверьте, работает ли print_params(*values_list_2, 42)')
print_params(*values_list_2, 42)

print()
print('работа со словарем')
print_params(**values_dict)
print_params(**values_dict_2)

print()
print('работа со списком и словарем, в котором 1 пара')
values_dict_1 = {'c': False}
print_params(*values_list_2, **values_dict_1)

print()

print('работа со списком и словарем, если в словаре больше одной пары')
print_params(*values_list_2, values_dict['b'])