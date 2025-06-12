"""
# Palindrome String

s1 = input("Enter the string: ")
s2 = s1[ : : -1]

if (s1 == s2):
    print("Is Palindrome")
else:
    print("Not Palindrome")
"""    
"""
s1 = input("S: ")
order = ord(s1)

if (65 <= order <= 90):
    print("UPPER CASE")
    
else:
    print("lower case")
"""

"""
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
branch = input("Branch : ")
case = branch.upper()

percentage = ((m1 + m2 + m3) / 300) * 100
print("Percentage = {:.2f}".format(percentage))


if(percentage > 90 and case == 'IT' or case == 'DS'):
    print("Eligible for AKTU site.")

else:
    print("Not Eligible for AKTU site.")
"""
#List check
""" 
l = ['Hi', 'Hello', 'He', 'Not']
item = l[2]
s1 = 'string'
    ##if (type(l[2]) == str):
if (type(item) == type(s1)):
    print(l[0] + l[1] + l[2] + l[3])

else:
    print("NOT A STRING")

"""
