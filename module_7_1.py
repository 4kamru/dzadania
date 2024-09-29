# Задача "Учёт товаров"
import os.path

# Продукт: название, масса, категория
class Product():
    def __init__(self, name = '', weight = 0.0, category =''):
        self.name = name
        self.weight = weight
        self.category = category

    # возвращаем полную строку продукта при выводе на печать объекта класса Product
    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

# Магазин
class Shop():
    __file_name = 'products.txt'
    # если такого файла нет - создадим
    def __init__(self, str_products = ''):
        self.str_products = str_products
        if not os.path.exists(self.__file_name):
            file = open(self.__file_name, 'w')
            file.close()


    # добавляем продукты в магазин - если их еще нет в файле products.txt. Если есть - выходит сообщение
    def add(self, *products):
        str_prod = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if not (str(i) in str_prod):
                file.write(f'{i}\n')
            else:
                print(f'Продукт {i} уже есть в магазине')
        file.close()

    # читаем список продуктов из файла и возвращаем строку с ним
    def get_products(self):
        file = open(self.__file_name, 'r')
        str_prod = file.read()
        file.close()
        return str_prod




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
