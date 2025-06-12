"""
for j in range(1,6): # ROWS
    for i in range(1, 6): # COLUMNS
        print("*", end = '')
    print()
"""
#Using i for output
"""
for i in range(1, 6): 
    for j in range(1, 6): 
        print(i, end = '')
    print()
"""
#Using j for output
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end = '')
    print()
"""
#Alphabets
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(chr(i + 64), end = ' ')
    print()
"""
    
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(chr(j + 64), end = ' ')
    print()
"""

#Pyramid
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = ' ')
    print()
"""

"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end = ' ')
    print()
"""
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()
"""
#Alphabet Pyramid
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(j + 64), end = ' ')
    print()
"""

"""
for i in range(1, 6): #ROW VALUE IS SAME = PRINT OUTER LOOP
    for j in range(1, i + 1): #COLUMN VALUE IS SAME  = PRINT INNER LOOP
        print(chr(i + 64), end = ' ') 
    print()
"""
# Reverse Pyramid
"""
for i in range(1, 5):
    for j in range(1, 6 - i): # for j in range(5 - i):
        print("*", end = ' ')
    print()

"""
"""
for i in range(1, 4):
    for j in range(1, 5 - i + 1):
        print(' ', end = '')
    for k in range(1, i + 1):
        print("*", end = ' ')
    print()

"""

"""
num = 1
for i in range(1, 10):  
    for j in range(1, i):  
        print(num, end=' ')
        num = num + 1 
    print()

"""
"""
num = 1
for i in range(1, 6):  
    for j in range(1, i):  
        print(chr(num + 64), end=' ')
        num = num + 1 
    print()
"""
"""
for i in range(1, 5):
    for j in range(1, 5 - i + 1):
        print(' ', end = '')
    for k in range(1, i + 1):
        print("*", end = ' ')
    print()
"""



