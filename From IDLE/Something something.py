"""a = 123

r1 = a % 10 
q1 = a // 10
r2 = q1 % 10
q2 = q1 // 10
r3 = q2 % 10
q3 = q2 // 10

print("Sum of the numbers is :",r1 + r2 + r3)"""

"""
a = 2
b = 3

print(a ** b)
"""

x1 = int(input("Enter the value of x1 : "))
x2 = int(input("Enter the value of x2 : "))

y1 = int(input("Enter the value of y1 : "))
y2 = int(input("Enter the value of y2 : "))

d1 = (x1 - x2) ** 2
d2 = (y1 - y2) ** 2

d = (d1 + d2) ** 1/2
print("Distance between the points are {} units.".format(d))
