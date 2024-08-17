# раскрытие вложенного списка - в 1-й день сам не додумался, поэтому
# https://stackoverflow.com/questions/973568/convert-nested-lists-to-string
# только преобразовал в str
def get_list_values(data_structure, temp=[]):
    for item in data_structure:
        if type(item) == list:
            temp = get_list_values(item, temp)

        else:
            temp.append(item.__str__())

    return temp


def opros():
    while 1 > 0:
        v1 = int(input("Выберите число от 3 до 20 :"))
        if v1 >= 3 and v1 <= 20:
            f1 = v1
            break
        else:
            print("Выбранное число не подходит. Повторите ввод")
    return (f1)


# определяем число из 1-й вставки - можно было бы сделать через random (там ведь камни случайно появляются)
# но для контроля ситуации будем задавать явно
first = opros()
# матрица границ перебора по i и j - для перебора по предполагаемым значениям 1-го и 2-го элемента пар
minmax = []
if first % 2 == 0:
    minmax.append([1, first // 2 - 1])
    minmax.append([2, first - 1])
else:
    minmax.append([1, first // 2])
    minmax.append([2, first - 1])

paar = []
for i in range(minmax[0][0], minmax[0][1] + 1):
    # перебор для 2-го элемента пары
    for j in range(minmax[1][0], minmax[1][1] + 1):
        if j != i and first % (j + i) == 0 and j > i:
            paar.append([i, j])

# лучше бы тут всё же какие-то разделители были б, но делаю, как по заданию
result = ''.join((get_list_values(paar)))
print(f'{first} - {result}')
