class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
                # коль съел - будет жить
                self.alive = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.fed = False
                # не насытился - не жилец он...
                self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True
class Mammal(Animal):
    pass
class Predator(Animal):
    pass

# ПРОВЕРКА

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

