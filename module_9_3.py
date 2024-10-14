# Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x[0])-len(x[1]) for x in zip(first,second) if len(x[0])-len(x[1])]

# так это выглядит с zip:
# second_result = [not(len(x[0])-len(x[1])) for x in zip(first,second)]

# без zip (чуть длиннее, но сложнее)
second_result = [not(len(first[i])-len(second[i])) for i in range(len(first))]

# а так это выглядит с zip (реально проще):
# second_result = [not(len(x[0])-len(x[1])) for x in zip(first,second)]


# Проверка
print(list(first_result))
print(list(second_result))
