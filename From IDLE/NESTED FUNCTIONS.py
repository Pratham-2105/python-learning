"""
#x = 20
def outer():
    x = 10
    print(x)
    def inner():
        x = 5
        print(x)

    return inner()

y = outer()
"""
# Sum of elements in the list:
"""
def sum_list(x):
    add = 0
    for i in x:
        add += i
    return add
        

list1 = [1, 2, 3, 4, 5]
y = sum_list(list1)
print(list1)
print(y)
"""

# Even numbers in list:
"""
def even_num(x):
    for i in x:
        if (i % 2 == 0):
            print(i)
            
            


list1 = [1, 2, 5, 6, 8, 3, 10]
y = even_num(list1)
print(y)
"""
"""
def name():
    return 'Something'

def outer(nam):
    def inner():
        x = nam()
        print('Hi', x)
    return inner()

y = outer(name)
print(y)
"""
"""
def myname():
    return 'Pratham'

def output(name1):
    def inner():
        x = name1()
        print("* * * *")
        print(x)
        print("* * * *")
    return inner()
y = output(myname)
print(y)
"""
"""
def one(msg):
    return msg + ' 1'
def two(msg):
    return msg + ' 2'
def three(fun):
    x = fun("Message Inside")
    print(x)
three(one)
three(two)
   """
# Factorial
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


number = int(input("Enter the number: "))
print(f"The factorial of {number} is {factorial(number)}")
"""


