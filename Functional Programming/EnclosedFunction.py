# Closures

"""

def outer_func(text):
    def inner_funct(): # Enclosed Function;
        print(text)

    return inner_funct

my_funct = outer_func("hello")
my_funct() # Output: Hello

"""
from idlelib.squeezer import count_lines_with_wrapping

"""

def greet(name):
    def say_hello():
        print(f"Hello, {name}")

    return say_hello

greeting = greet("Alice")
greeting() # Output: Hello, Alice

"""

"""

def outerFunction(text):
    text1 = text

    def innerFunction():
        print(text1) # uses the variable;
        print(text) # uses the parameter;
    return innerFunction

myFunction = outerFunction('Hey!')
myFunction()

"""

"""
def make_counter():
    count = 0

    def counter():
        nonlocal count
        # nonlocal tells the inner function that this
        # particular variable has already been declared!!
        # so it can be modified
        count += 1
        return count

    return counter

counter1 = make_counter()
counter2 = make_counter()

for i in range(5):
    print("Counter-1:", counter1())
print()
for i in range(6):
    print("Counter-2:",counter2())


# print(counter1())
# print(counter1())
# print(counter1())
#
#
# print(counter2())
# print(counter2())
#
# print(counter1()) # The first counter is independent of the second counter;
"""

