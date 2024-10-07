# Домашнее задание по уроку "Try и Except"
# если оба аргумента числа, то складываем и оставляем 3 знака после запятой (ну или точки...)
# если один аргумент строка - то оба преобразуем в строки и склеиваем их
def add_everything_up(a,b):
    try:
        res = a + b
    except TypeError:
        res = str.format('{}{}',a,b)
    else:
        # оставляем 3 знака
        res = str(f'{res:.3f}')
    finally:
        return(res)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
