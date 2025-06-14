# A method with same name can have multiple methods

# 1. Duck Type Isomorphism:

"""
class Duck:
    def quack(self):
        print("Quack Quack")

class Human:
    def quack(self):
        print("Hi")

duck = Duck()
person =  Human()
duck.quack()
person.quack()


class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swin in sea")

class Dog:
    def bark(self):
        print("dog fly?")

for obj in Bird(), Airplane(), Fish():
    obj.fly()

"""
# 2. Method Overriding:

"""
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
"""

# 3. Method Overriding:

"""
class Add:
    def sum(self, a = None, b = None, c = None):
        s = 0

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s

s = Add()
print(s.sum(1))
print(s.sum(2, 3))
print(s.sum(12, 14, 15))
"""

# 4. Operator Overloading:

