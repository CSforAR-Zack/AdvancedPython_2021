
class Animal:
    """ This is an animal class. """

    # Class variables
    generalType = 'Lifeform'

    def __init__(self, name):
        self.name = name

    def makeSound(self, sound):
        print(f'{self.name} makes the sound "{sound}"!')

    def __str__(self):
        return f'This is an animal with the name {self.name}.'

    def __add__(self, other):
        return f'{self.name} and {other.name}'

class Horse(Animal):
    
    def __init__(self, name, coatColor):
        super().__init__(name)
        self.coatColor = coatColor

    def makeSound(self):
        print("I changed makeSound")