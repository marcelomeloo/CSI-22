from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f'{self.name} speaks: Au Au')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f'{self.name} speaks: Miau Miau')

for animal in [Dog('Zeus'), Cat('Garfield')]:
    animal.speak()
