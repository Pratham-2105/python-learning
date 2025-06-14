# 1. Single Inheritance (Parent -> Child Classes)
# 2. Multiple Inheritance (Grandfather -> Father -> Son Classes)
# 3. Hierarchical Inheritance (Parent --> 1. Class1
                                          #2. Class2
                                          #3. Class3)

from abc import ABC, abstractmethod

# 1. Single Inheritance:
"""
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak() # Inheritance
d.bark()  # Child's own method

"""

# 2. Multi Inheritance:

"""
class Grandfather:
    def values(self):
        print("Wisdom")

class Father:
    def skills(self):
        print("Developer")

class Child(Father, Grandfather):
    def interests(self):
        print("Java")

c = Child()

c.skills()
c.interests()
c.values()

# f = Father()
#
# f.values
# f.interests

"""

# 3. Hierarchical Inheritance:
"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def barks(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.speak()
d.barks()

c = Cat()
c.speak()
c.meow()

"""

# Constructor overriding: Priority of last defined constructor is higher than previous;

"""

class Animal:
    def __init__(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()

class Animals:
    def __init__(self):
        print("Animal Constructor")


class Dogs(Animals):
    def __init__(self):
        #super().__init__()
        print("Dogs Constructor")

D = Dogs()


class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__() # Calls the Parent constructor
        print("Dogs Constructor")

d = Dog()
"""
"""
class Person:
    def __init__(self, name):
        self.name = name
        print("Person:", name)

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        print("Student Grade:", grade)

st1 = Student("Alice", "A")
st2 = Student("Bob", "B")
"""

"""

class Parent:
    def __init__(self, name):
        print(f"Parent: {name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        print(f"Child: {age}")

onj = Child("Alice", 20)

"""

"""

class Parent:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

    def show_vars(self):
        print("Inside Parent Class:")
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        print("Private:", self.__private_var)


# usage
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("\nInside Child Class:")
        print("Accessing Public:", self.public_var)       # allowed
        print("Accessing Protected:", self._protected_var) # allowed (by convention)

        # Trying to access private directly will cause an error:
        # print("Accessing Private:", self.__private_var)  # AttributeError

c = Child()

print("\nOutside Class Access:")
print("Public:", c.public_var)
print("Protected:", c._protected_var)
#print("Private:", c.--private_var)
print("Private (via mangling):", c._Parent__private_var)

"""

class Payment(ABC):

    @abstractmethod # Blueprint of Bluprint

    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")

pay_method1 = CreditCardPayment()
pay_method1.pay(100)

pay_method2 = UpiPayment()
pay_method2.pay(1000)

pay_method3 = PayPalPayment()
pay_method3.pay(1500)
