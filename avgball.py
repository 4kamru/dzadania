grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# тут бы цикл поставить, но не проходили мы их
grades_avg = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[0]), sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]
students_s = sorted(students) # метод sorted сортирует множество
# готовим словарь со средними оценками
dict_avg_grades = dict(zip(students_s, grades_avg)) # приходится преобразовывать в dict
print(dict_avg_grades)