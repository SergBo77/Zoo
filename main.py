import pickle
# 1. Создание базового класса Animal
class Animal:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def make_sound(self):
       pass

   def eat(self):
       pass

# 2. Подклассы Bird, Mammal и Reptile
class Bird(Animal):
   def __init__(self, name, age, feather_color):
       super().__init__(name, age)
       self.feather_color = feather_color

   def make_sound(self):
       return "Чирик-чирик"

   def fly(self):
       return f"{self.name} летит"

class Mammal(Animal):
   def __init__(self, name, age, size):
       super().__init__(name, age)
       self.size = size

   def make_sound(self):
       return "Ррррр"

   def run(self):
       return f"{self.name} бежит"

class Reptile(Animal):
   def __init__(self, name, age, locomotion):
       super().__init__(name, age)
       self.locomotion = locomotion

   def make_sound(self):
       return "Шшш-Жжжж"

   def crawl(self):
       return f"{self.name} ползет"

# 3. Полиморфизм
def animal_sound(animals):
   for animal in animals:
       print(animal.make_sound())

# 4. Класс Zoo с использованием композиции
class Zoo:
   def __init__(self):
       self.animals = []
       self.staff = []

   def add_animal(self, animal):
       self.animals.append(animal)

   def add_staff(self, staff):
       self.staff.append(staff)

   def save_zoo(self, file_name):
       with open(file_name, 'wb') as file:
           pickle.dump(self.animals, file)
           pickle.dump(self.staff, file)

   def load_zoo(self, file_name):
       with open(file_name, 'rb') as file:
           self.animals = pickle.load(file)
           self.staff = pickle.load(file)

# 5. Классы сотрудников
class ZooKeeper:
   def __init__(self, name):
       self.name = name

   def feed_animal(self, animal):
       return f"{self.name} кормит {animal.name}"

class Veterinarian:
   def __init__(self, name):
       self.name = name

   def heal_animal(self, animal):
       return f"{self.name} лечит {animal.name}"

# 6. Создадим объекты классов
bird1 = Bird('Попугай', 5, 'зеленый')
bird2 = Bird('Конорейка', 3, 'желтый')
bird3 = Bird('Орел', 4, 'серый')

mammal1 = Mammal('Лев', 7, 'Большой')
mammal2 = Mammal('Слон', 10, 'Огромный')
mammal3 = Mammal('Волк', 6, 'Средний')

reptile1 = Reptile('Змея', 2, 'Ползает')
reptile2 = Reptile('Паук', 3, 'Ходит')
reptile3 = Reptile('Пчела', 1, 'Летает')

my_zoo = Zoo()

my_zoo.add_animal(bird1)
my_zoo.add_animal(bird2)
my_zoo.add_animal(bird3)
my_zoo.add_animal(mammal1)
my_zoo.add_animal(mammal2)
my_zoo.add_animal(mammal3)
my_zoo.add_animal(reptile1)
my_zoo.add_animal(reptile2)
my_zoo.add_animal(reptile3)

zookeeper = ZooKeeper('Иван')
veterinarian = Veterinarian('Марина')

my_zoo.add_staff(zookeeper)
my_zoo.add_staff(veterinarian)




