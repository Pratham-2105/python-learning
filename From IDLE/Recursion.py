# Factorial
"""
def refact(x):
    if (x == 1):
        return 1
    return x * refact(x - 1)

num = int(input("Enter the number for factorial: "))
print(refact(num))
"""

# Sum of N natural numbers:
"""
def add(num):
    if (num == 1):
        return num
    else:
        return num + add(num - 1)

x = int(input("Enter the number: "))
print(add(x))
"""
# Power of any number:
"""
def power(a, b):
    if(b == 0):
        return 1
    else:
        return a * power(a, b - 1)

x = int(input("Enter the base: "))
y = int(input("Enter the power: "))

print(power(x, y))
"""


# Reverse a string:
"""
def rev(s): 
    if len(s) == 0: 
        return s
    else:
        return rev(s[1:]) + s[0]) 

s = input("Enter a string: ")
print(rev(s))
"""

# Sum of elements of a list:
"""
def recursive_sum(lst):
    
    if not lst:
        return 0

    else:
        return lst[0] + recursive_sum(lst[1:])


numbers = [1, 5, 7, 6, 8, 2]
result = recursive_sum(numbers)
print("The sum of the list is:", result)
"""

# Multiply using recursion:
"""
def multiply(a, b):
    if (a == 0 or b == 0):
        return 0
    else:
        return a + multiply(a, b - 1)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(multiply(x, y))
"""

# Find the occurence of a char in a string:
"""
def count(a, char):
    if len(a) == 0:
        return 0
    if a[0] == char:
        call = 1
    else:
        call = 0
    return call + count(a[1:], char)

st = input("Enter a string: ")
ch = input("Enter the character: ")
print(count(st, ch))
"""      

# fibonacci series:
"""
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10
print("Fibonacci series:")
for i in range(1, n_terms + 1):
    print(fibonacci(i), end=" ")

"""

