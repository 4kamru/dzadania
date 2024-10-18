# Генераторы
def all_variants_v1(text):
    i = 0
    k = 0
    res = ''
    stroka = list(text)
    while i != len(text):
        res = stroka[i]
        yield res
        i += 1

def all_variants_v2(text):
    i = 0
    k = 0
    res = ''
    stroka = list(text)
    while i != len(text):
        res = stroka[i]
        stroka = list(text.lstrip())
        while k < i:
            res += stroka[k]
            yield res[::-1]
            k += 1
        i += 1

def all_variants_v3(text):
    #возвращаем разные срезы строки
    i = 0
    j = 0
    res = list(text)
    while i<len(text):
        str_ = res[i]
        while j<len(text):
            if i != 0 or j != 0:
                stroka = text[i:j]
                str_ = str(stroka)
            yield str_
            j += 1
        i += 1

def all_variants_v4(text):
    #возвращаем разные срезы строки
    i = 0
    j = 0
    while i <= len(text):
        while j <= len(text):
            res = text[i:j]
            j += 1
            yield res
        i+=1

def all_variants_v5(text):
    #возвращаем разные срезы строки
    i = 0
    j = len(text)
    while i <= j:
        while j != 0:
            res = text[i:j]
            yield res
            j -= 1
        i+=1

def all_variants_v6(text):
    #возвращаем разные срезы строки
    i = 0 # стартовый индекс среза
    j = 0  # сколько элементов берем за итерацию
    while i != len(text):
        while j != len(text)-1:
            yield list(text)[i]+text[i:j]
            # res = text[i:j]
            # yield res
            j += 1
        i+=1

def all_variants_v7(text):
    #возвращаем разные срезы строки
    i = 0 # стартовый индекс среза
    j = 0  # сколько элементов берем за итерацию
    while i != len(text):
        while j != len(text):
            yield text[i+j:]
            # res = text[i:j]
            # yield res
            j+=1
        i += 1

def all_variants_v8(text):
    # возвращаем разные срезы строки
    # i - начальный индекс среза, j - длина среза
    L = len(text)
    for j in range(1,L):
        i = 0
        while i < L and i+j <= L:
            res = text[i:i+j]
            yield(res)
            i += 1
    yield (text)




# def all_variants_v9(text):
#     #возвращаем разные срезы строки
#     j = 1 # стартовая длина среза
#     L = len(text)
#     i = 0
#     while i < L-1:
#         while (i+j <= L):
#             res = text[i:i+j]
#             yield(res)
#             while res != text:
#                 i+=1
#         if j < L:
#             j += 1
#         i = 0


# ПРОВЕРКА
# a = all_variants_v1("abc")
# for i in a:
#     print(i)
#
# print('Продолжение v 6')
# a = all_variants_v2("abc")
# for i in a:
#     print(i)
# a = all_variants_v6("abcd")
# for i in a:
#     print(i)
print('Продолжение v 8')
a = all_variants_v8("abc")
for i in a:
    print(i)