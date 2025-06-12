# Sample
"""
for i in range(1,11):
    print(i)
"""

# Table of any number
"""

a = int(input("Enter the number: "))
b = int(input("Enter the times to be muliplied: "))

for i in range(1, b + 1):
    print(f"{a} x {i} = {a * i}")

print("\nEND OF PROGRAM")

"""
# Pyramid 1

"""
for i in range(1, 6):
    print("* " * i)

print("\nEND OF PROGRAM")
"""
# Even natural numbers between 1 and n:
"""
num = int(input("Enter the value of n: "))
print(f"Even numbers between 1 and {num} are")

for i in range(1,num):
    if (i % 2 == 0):
        print(i, end = ' ')

print("\nThe numbers are-")

for i in range(1, num + 1):
    print(i)
    
print("\nEND OF PROGRAM")
"""

# Sum of n numbers:
"""
num = int(input("Enter the value of n: "))
s = 0

for i in range(1, num + 1):
    s = s + i

print(f"The sum of first {num} numbers is: {s}")

print("\nEND OF PROGRAM")

"""

# Factorial:
"""

n = int(input("Enter the value of n: "))
fact = 1
print(f"The factorial of {n} is: ")

for i in range(1, n + 1):

    fact = fact * i 

print(fact)
print("\nEND OF PROGRAM")

"""
# Printing a list:
"""
l = [1, 2, 3, 4]

for i in l:
    print(i)

print("\nEND OF PROGRAM")

"""
# Add all the elements of the list:
"""
l = [1, 2, 3, 4]
s = 0
        
print("The sum of the elements is: ")

for i in l:
    s = s + i
print(s)

print("\nEND OF PROGRAM")
"""

# Odd numbers in list
"""
list1 = []
num = int(input("Enter the number of elements: "))

for i in range(num):
    elements = int(input(f"Enter element {i + 1}: "))
    list1.append(elements)
                   
print("The odd numbers in the list are: ")

for i in list1:
    if(i % 2 == 1):
        print(i)

print("\nEND OF PROGRAM")

"""

# Length of string in list > 4:
"""
l = ['Hello', 'WHAT', 'WHERE', 'WHATEVER', 'HOW', 'CARE']
count = 0

print("The strings are: ")

for i in l:
    if(len(i) > 4):
        count = count + 1
        print(i)

print(f"The number of strings are : {count}")

print("\nEND OF PROGRAM")
"""

# Count strings in a list:
"""
list1 = []
num = int(input("Enter the number of elements: "))

for i in range(num):
    elements = input(f"Enter the elements {i + 1}: ") # ALL ELEMENTS BECOME A STRING***
    list1.append(elements)

print("The given list is: ", list1)

count  = 0
print("The strings in the list are: ")

for i in list1:
    if (type(i) == str):
        count  = count + 1
        print(i)

print("The total number of strings are: ", count)
"""

# Fibonacci Series:
"""
n = int(input("Enter the value of n: "))
        
a = 0
b = 1
print(a)

for i in range(1, n):
    c = a + b
    a = b
    b = c
    print(a)
    print(b)

print("\nEND OR PROGRAM")
"""

# Print a string vertically:
"""
a = input("Enter the string: ")

for i in a:
    print(i)

print("\nEND OF PROGRAM")
"""

# Vowels in a string:

a = input("Enter a string: ")
b = a.upper()
v = 'AEIOU'
count = 0

print("The vowels are: ")
for i in b:
    if(i == v):
        print(i)
        count = count + 1

print("The number of vowels are:",count)




