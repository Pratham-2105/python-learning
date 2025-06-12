# Adding two numbers
"""
def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    s = (a + b)
    print(f"The sum of {a} and {b} is {s}")

add()
"""
"""
def add(a, b):
    s = a + b
    print(s)

add(4, 7)         
"""

# Factorial of a number
"""
def fact(number):
    f = 1
    print("The factorial of the number is: ")
    for i in range(1, number + 1):
        f = f * i
    print(f)

user_input = int(input("Enter a number: "))
fact(user_input)
"""

# Input first and last name
"""
def user_name(name, RN):
    print(name)
    print(RN)

user = input("Enter your name: ")
roll_no = int(input("Enter your Roll No: "))

user_name(user, roll_no)
"""
# Length of variable [Variable Length Argument]
"""
def var_len(*a):
    s = 0
    for i in a:
        s = s + i
    print(s)

var_len(2, 3)
var_len(2, 5, 6, 1, 7)
"""
"""
def add(a, b):
    return(a + b)
    
y = add(4, 5)
print(y + 10)

"""

# Factorial
""" 
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

f1 = int(input("Enter n: "))
f2 = int(input("Enter r: "))
f3 = f1 - f2
n = fact(f1)
r = fact(f2)
difference = fact(f3)

nCr = (n/r * difference)
print(nCr)
"""

# Calculator
"""
def calc(a, b, ch):

    if (ch == '+'):
        return(a + b)
    elif (ch == '-'):
        return(a - b)
    elif (ch == '*'):
        return(a * b)
    elif (ch == '/'):
        return(a / b)
    else:
        print("INVALID")

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
choice = input("Enter your choice: ")

print(calc(n1, n2, choice))
"""
# Armstrong number:
"""
def armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            armstrong_numbers.append(num)
    return armstrong_numbers

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Armstrong numbers between {start} and {end} are: {armstrong_numbers_in_range(start, end)}")
"""

        
