class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def move(self):
        print("Moving")

    def eat(self):
        print("Eating")

class Mammal(Animal):
    def __init__(self, weight, height, fur_color):
        self.fur_color = fur_color
        super().__init__(weight, height)

class Human(Mammal):
    def __init__(self, weight, height, fur_color, name, age):
        self.name = name
        self.age = age
        super().__init__(weight, height, fur_color)

    def move(self):
        print("Walking")

    def talk(self):
        print("Talking")

joao = Human(70, 1.80, "brown", "João", 50)

joao.move()
joao.eat()
joao.talk()
print(joao.__class__.__mro__)
