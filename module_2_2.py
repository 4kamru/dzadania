first = int(input('Введите 1-е число: '))
second = int(input('Введите 2-е число: '))
third = int(input('Введите 3-е число: '))
a = 4
if first == second and second == third:
    a = 3
elif first == second or first == third or second == third:
    a = 2
else:
    a = 0
print(a)
