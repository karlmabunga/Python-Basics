# This is a class of a zoo

# self refers to the specific instance of the Zoo class after we've intialized it
class Zoo:
    # __init__ is a special python initialization function
    def __init__(self, name):
        self.name = 'New Zoo of ' + name
        self.animals = []
    
    # We pass the self variable to this method so we have access to attributes or functions of this class
    def animalCount(self):
        print('The ' + self.name + ' currently has ' + str(len(self.animals)) + ' animals')

    def addAnimal(self, animal):
        self.animals.append(animal)
    
    def printAnimals(self):
        print(self.animals)

    def printName(self):
        print(self.name)


zoo = Zoo('Snakes')
zoo.printName()
zoo.animalCount()
zoo.printAnimals()
zoo.addAnimal('Anaconda')
zoo.addAnimal('Cobra')
zoo.animalCount()
zoo.printAnimals()

# Python will act as though the instance the method is being called on is the first argument
# These class instances are object
# The variables in the class are attributes
# The functions in the class are called methods
anotherzoo = Zoo('Birds')
anotherzoo.printName()
anotherzoo.addAnimal('Falcon')
anotherzoo.animalCount()
anotherzoo.printAnimals()
