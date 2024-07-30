# Object Oriented Programming Concepts (OOPs)

# Classes : Blueprints/Prototypes according to which the objects/instances are created. For Example, Car, Laptop, etc.


class Car:

  def __init__(self, make, model, color, year):
    self.make = make
    self.model = model
    self.color = color
    self.year = year

  def __str__(self):
    return f"{self.make} {self.model} {self.color} {self.year}"


# Objects : Instances of a class. For Example, Toyota, Honda, etc.
car1 = Car("Toyota", "Camry", "Red", 2020)  # An object of the Car Class
car2 = Car(model="Civic", make="Honda", year=2022, color="Blue")
print(car1)
print(car2)

car3 = Car(model="Z4", make="BMW", year=2023, color="Black")
print(car3)
print(f"The Make of the Car '{car3}' is {car3.make}")

# OOPs 4 features: ABSTRACTION, ENCAPSULATION, INHERITANCE, POLYMORPHISM.
# ABSTRACTION: We show only the essential features of the object, and hide all the background details. We hide the implementation details of the object and expose only the essential features.
# ENCAPSULATION: We bind the data and the functions that operate on the data within a single unit. This data and functions are called as attributes and methods.
# INHERITANCE: We create a new class that inherits all the attributes and methods of the existing class.


class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species

  def sound(self):
    print("Sound")


class Dog(Animal):

  def __init__(self, name, species, breed):
    super().__init__(name, species)
    self.breed = breed

  def sound(self):
    print("Bark")


class Cat(Animal):

  def __init__(self, name, species, color):
    super().__init__(name, species)
    self.breed = color

  def sound(self):
    print("Meow")


dog1 = Dog("Max", "Dog", "Golden Retriever")
print(dog1.name, "is a", dog1.breed)

dash = Cat("dash", "Cat", "Ragdoll")
print(dash.name, "is a", dash.breed)
