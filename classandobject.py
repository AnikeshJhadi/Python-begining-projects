#defining lists containing info of employee
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]
#defining a class named Dog
class Dog:
    pass
#updating class Dog with __init__ function used for initialisation {constructor}
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Dog:
    # Class attribute update i.e. species
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
#class showing instance methods
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
#modifying the Dog class by adding a .breed attribute
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
#Parent class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
#Child classes of the Dog class
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
#override a method defined on the parent class, you define a method with the same name on the child class.
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
#changing the string returned by .speak() in the Dog class
class Dog:
    # Leave other attributes and methods as they are

    # Change the string returned by .speak()
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
#accessing the parent class from inside a method of a child class by using super()
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
