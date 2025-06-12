# Pass Function:
"""
num = int(input("Enter a number: "))

if(num > 5):
    pass
else:
    print("Hello")
"""
# Continue Statement:
"""
for a in range(1, 11):
    if(a == 5 or a == 7):
        continue # Program moves back to for loop
    print(a, end = ' ')
"""

# Break Statement:
"""
for i in range(1, 10):
    if(i >= 5):
        break
    print(i)
"""
# Prime Numbers
"""
number = int(input("Enter a number: "))
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

"""
# Range in Prime Numbers
"""
low = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
print(f"Prime numbers between {low} and {upper} are:")
for num in range(low, upper):  
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
"""

# Print sum of prime numbers
"""
start = int(input("Enter the start range: "))
end = int(input("Enter the end of the range: "))

prime_sum = 0
print("The Prime numbers are: ")

for num in range(start, end + 1):
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                is_prime = False
                break
        if is_prime:
            print(num)
            prime_sum += num

print("Sum of prime numbers:", prime_sum)

"""

