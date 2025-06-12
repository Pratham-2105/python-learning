#import keyword

def check_pass(pwd):
    if len(pwd) < 8:
        return "Weak: Too short!"

    has_digit = any(ch.isdigit()for ch in pwd)
    has_upper = any(ch.isupper() for ch in pwd)
    has_lower = any(ch.lower() for ch in pwd)

    if not has_digit or not has_upper or not has_lower:
        return "Medium: Add digits/uppercase/lowercase"
    return "Strong"

'''
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = a+b
print(c)'''

#age = 19
#name = "Pratham"

'''Comment'''
# Also comment

#Different methods to print

'''print("Name is %s and age is %d" %(name,age))'''

# Using format specifier;

'''print("Hello {}" .format(name))'''

# Using f string;

'''print(f"hello {name}")'''

# Using file or stream
'''
#with open('output.txt', 'w') as f:
        print("This line is written in file.", file = f)
        f.close()
'''

# End-Points in Strings;

#end = '\n';
#seperate = ' ';

'''
print("Hello", end= " ")
print("World")
'''

#Elements of Python;
'''
1. Keywords and Identifiers
2. Variables
3. Data types and type conversion
4. Operators in Python
5. Expressions in Python

'''
# import keyword;
'''
print(keyword.kwlist)
print("Total keywords: ", len(keyword.kwlist))
'''

# Data - Types

# Strings and Integers

'''
a = input("Enter number: ") # by-default a string;
print(a)
print(type(a))

num = int(input("Enter num: "))
print(num)
print(type(num))
'''
# String : Collection of characters;
# Lists : Multiple Data-types;
# Tuple : Like lists but is immutable;

# Sets: Unordered collection of data-types; no indexing;


# Operations in Python;
'''
a = "Pratham"
b = "Srivastava"
c = a + b  # OPERATOR OVERLOADING ; '+' for String is different
                                         #'+' for Numbers is different
# d = a - b  --> ERROR

print(c)
'''

# Relational Operator;

'''
1. ==
2. !=
3. >    
4. <    
5. >=    
6. <=
7. !

'''

# Assignment operators

'''
1. +=
2. -=
3. *=
4. /=
5. //=
6. ^=
7. //=
8. **=
9. =

'''

# Loops
'''
for i in range(1, 6):
    print(i)
'''

#
'''
a = 5
b = 5
print(a is b)
'''

# GRADING SYSTEM
'''
name1 = input("Enter name: ")
roll = int(input("Enter roll-no: "))
sub1 = float(input("Enter marks of Sub 1: "))
sub2 = float(input("Enter marks of Sub 2: "))
sub3 = float(input("Enter marks of Sub 3: "))
sub4 = float(input("Enter marks of Sub 4: "))
sub5 = float(input("Enter marks of Sub 5: "))

marks = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print("\n")
print("Name of the student: ", name1)
print("Roll no: ", roll)
print("Marks of the student is: %d" %(marks))

if(marks >= 90):
    print("Grade: A")
elif(marks >= 70):
    print("Grade: B")
elif(marks >= 50):
    print("Grade: C")
elif(marks >= 40):
    print("Grade: D")
else:
    print("Grade: F")
'''

# Greatest Between 3 numbers;

'''
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

if(a > b):
    if(a > c):
        print("Greatest is a:", a)
    else:
        print ("Greatest is c:", c)
        
elif(b > a):
    if(b > c):
        print("Greatest is b:", b)
    else :
        print("Greatest is c:", c)
else:
    print("Greatest is c:", c)
'''

# Ternary if & else:
'''
a = float(input("Enter marks of the student: "))
res = "Passed" if a > 45 else "Failed"
print(f"The result is : {res}")

'''

# Selection(switch) statements:
'''
value = int(input("Enter value: "))

match(value):
    case 1: print("One")
    case 2: print("Two")
    case 3: print("Three")
    case 4: print("Four")
    case 5: print("Five")
    case _: print("INVALID INPUT")
'''
#Loops:

'''
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = "")
    print()
'''

'''
i = 1
#j = 1 
while(i <= 5):
    j = 1
    while (j <= i):
        print(j, end = "")
        j += 1
    print()
    i += 1
'''

# Even and Odd:
'''
num = int(input("Enter range: "))
print("EVEN: ")
for i in range(1, num+1):
    if(i % 2 == 0):
        print(i, end = " ")

print()
print("ODD: ")
j = 1
while (j <= num):
    if(j % 2 == 1):
        print(j, end = " ")
    j = j + 1
'''

# Password Strength Checker:
''' Check function '''

'''
print(check_pass("4Tyue"))
print(check_pass("ThisIEWrrg8"))
print(check_pass("ghtuitioert"))
'''

# Jump Statements:

'''
for i in range(1, 6):
    print(i, end = "")
    if(i == 3):
        continue
    else:
        print(i, end = "")
'''

# Strings:

'''
a = "Hello Every'one"
b = 'Hello Everyone'
c = """ 
    Double inverted commas,
    are used for multi-line,
    comments.
        """
print(a)
print(b)
print(c)
'''
# Repeatation of a String:
'''
str = "for test "
print(str * 5, end = "")

'''

# Slicing a String:
'''
a = "HELLO_WORLD!"

print(a[-2])
print(a[-8])
print(a[ : 7])
print(a[:  : 2])
print(a[-1 : : -1])
'''

# Functions for a String:

'''
a = "hello_world"

print(a.upper())
print(a.lower())
print(a.count("o")) # Counts the occurence of the letter
print(a.capitalize())
print(a.replace("hello", "hi"))
print(len(a))
print(a.title())
print(a.split("_"))
print(a.find("world"))
print(a.find("World")) # If not found i.e, case sensitive;
words = ["Hello", "World"]
print(", ". join(words))

s1 = "1234"
s2 = "HELLO"
s3 = "hello"

print(s1.isdigit())
print(s2.isalpha())
print(s3.islower())
print(s2.isupper())

'''

# List: Like an array but can have different data-types;

'''
fruits = ["apple", "orange", "banana"]
mod_fruits = ["apple", "orange", "banana"]

print(fruits)
print(mod_fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

mod_fruits[1] = "cherry"
print(mod_fruits)

mod_fruits.append("blueberry")
mod_fruits.insert(2, "mango")
print(mod_fruits)

mod_fruits.remove("cherry")
mod_fruits.pop(3)
print(mod_fruits)
print("apple" in fruits)
'''

# Tuples: Immutable list;
'''
a = 1,
b = () # Empty Tuple
tup = (1, 2, 3)
tup1 = (3, 4, 5)

print(tup[0])
print(tup[1])
print(tup1 + tup)
print(tup1 * 5)

'''
# Dictionary: {key : "value"} pairs


# Sets: Unique elements, unordered;

'''
fruits = {"apple", "orange", "banana"}
print(fruits)
fruits.add("cherry")
print(fruits)
'''