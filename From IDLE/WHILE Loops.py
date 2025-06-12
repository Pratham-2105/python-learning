""" 
n = int(input("Enter the value of n: "))
i = 1

while(i <= n):
    print(i)
    i += 1
"""
"""
n = int(input("Enter the value of n: "))
i = n

while(i >= 1):
    print(i)
    i -= 1
"""

"""
n = int(input("Enter the value of n: "))
i = 0
add = 0

while(i <= n):
    add += i
    i += 1
print(add)
"""
"""
n = int(input("Enter the value of n: "))
i = n

while(i >= 5):
    print(i)
    i -= 1
"""
"""
n = int(input("Enter the value of n: "))
last_term = int(input("Enter the last value: "))
i = 1

while(i <= last_term):
    print(f"{n} x {i} =", i * n)
    i += 1

print("END OF PROGRAM")

"""
"""
n = int(input("Enter a number: "))
fact = 1
i = 1

while(i <= n):
    fact = fact * i
    i += 1
print(fact)
print("END OF PROGRAM")

"""
"""
num = int(input("Enter the number: "))
add = 0

while(num > 0):
    digit = num % 10
    add += digit
    num = num // 10
 
print(add)
print("END OF PROGRAM")

"""
"""
num = int(input("Enter the number: "))
num1 = num
s = 0

while(num > 0):
    r = num % 10
    q = num // 10
    s = s * 10 + r
    num = q
    
print("Reversed Number is:", s)

if(s == num1):
    print("Number is Palindrome.")
else:
    print("Number is not Palindrome.")

print("\nEND OF PROGRAM")
"""
"""
num = int(input("Enter the number: "))
count = 0

while(num > 0):
    num //= 10
    count += 1

print("The number of digits in the number are:",count)
print("\nEND OF PROGRAM")
"""
"""
num = int(input("Enter the number: "))
new_num = num
temp = len(str(num))
s = 0

while(num > 0):
    r = num % 10
    q = num // 10
    s = s + r ** temp
    num = q
    
if(new_num == s):
    print(f"{new_num} is Armstorng")
else:
    print("Number is not Armstrong")

print("\nEND OF PROGRAM")
"""
"""
limit = int(input("Enter the range: "))
print("Armstrong numbers are: ")

for i in range(1, limit):
    temp = len(str(i))
    a = i
    s = 0
    while(i > 0):
        r = i % 10
        q = i // 10
        s = s + r ** temp
        i = q
    
        if(a == s):
            print(a)

print("\END OF PROGRAM")
"""
"""
num = int(input("Enter a number: "))

num_str = str(num)
num_length = len(num_str)
sum_val = 0

for i, digit in enumerate(num_str):
    sum_val += int(digit) ** (i + 1)

if sum_val == num:
    print(f"{num} is a Daserium number.")
else:
    print(f"{num} is not a Daserium number.")
"""

