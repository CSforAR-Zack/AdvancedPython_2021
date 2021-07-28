from myClasses import Animal, Horse

animal1 = Animal('Trevor')
animal2 = Animal("Ethan")

print(animal1.name)
print(animal2.name)

animal1.makeSound("MOO")
animal2.makeSound("CROAK")

print(animal1)
print(animal2)

print(animal1 + animal2)

horse1 = Horse("Zack", "brown")
print(horse1.name)
print(horse1.coatColor)
horse1.makeSound()