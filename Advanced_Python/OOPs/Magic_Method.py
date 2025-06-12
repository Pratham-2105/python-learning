class Rect:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def disp(self):
        return self.r * self.h


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2 # other is used for another object

        if r1 > r2:
            return True
        else:
            return False


class Dog:
    species = "Canine"
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def display_details(self):
        print(f"Name: {self.Name}, Age: {self.Age}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return F"The name is {self.name}, the age is {self.age}"


"""

p = Person("Ritik", 20)
print(p) # This prints the conversion of object; Implicitly

out = p.__str__()
print(out) # This called the __str__ function; Explicitly

print(p.__dict__)



d1 = Dog("Charlie", 4)
d2 = Dog("Bob", 5)

print(d1.species)
print(Dog.species)
d1.Name = "Hollow"
d1.display_details()



x = Rect(12, 12)
print(x.disp())
print(dir(int))

a = 10
b = 10
c = a + b

print(c)
print(a.__add__(b)) # Dunder Function
print(dir(int))

str1 = "Hello "
str2 = "World"

new_str = str1.__add__(str2)
print(new_str)
print(len(new_str))

str3 = new_str.__len__()
print(str3)


st1 = Student(58, 69)
st2 = Student(60, 65)

if st1 > st2:
    print("st1 is greater")
else:
    print("st2 is greater")


if st1.__gt__(st2):
    print("st1 is greater")
else:
    print("st2 is greater")

"""