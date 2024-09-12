class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(1, new_floor + 1):
            if (new_floor > self.number_of_floors) or (new_floor < 1):
                print('Такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return('Название: '+ self.name + ', кол-во этажей: ' + str(self.number_of_floors))


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
