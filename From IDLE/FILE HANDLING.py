"""
file = open(r'D:\Programming\Python\FileHandling.txt', 'r')
"""
"""
p = file.read()
print(p)
"""
# Counting chars in a file:
"""
modified = p.replace(" ", "").replace(".", "")
print(modified)
count = 0

for i in modified:
    if (type(i) == str):  #if (i != ' ' and i != '.'): 
        count += 1
    else:
        count = count
print(count)
file.close()
"""
# Counting words in a file
"""
count = 0
modified1 = p.split()
for i in modified1:
    if(type(i) == str):
        count += 1
print(count)
"""

# Counting lines in a file:
"""
count = 0
modified2 = p.split("\n")
for i in modified2:
    if(type(i) == str):
        count += 1
print(count)
"""
##############################################


# Readline:
"""
s1 = file.readline()
print(s1)
"""
# Readlines:
"""
s2 = file.readlines()
print(s2)
print(type(s2)) # List 
"""

### WRITING IN A FILE ### w mode overwrites the data, a mode adds new data...

"""file1 = open(r'D:\Programming\Python\FileHandling.txt', 'a')
file1.write("Pyton is very simple. \n This is a very low level language")
file1.close

file1 = open(r'D:\Programming\Python\FileHandling.txt', 'r')
s = file1.read()
print(type(s))
print(s)
file1.close"""

# Copying form one file to another:

"""file1 = open(r'D:\Programming\Python\FileHandling.txt', 'r')
p = file1.read()

file22 = open(r'D:\Programming\Python\FileHandling1.txt', 'a')
file22.write(p)
file22.close

print()


file22 = open(r'D:\Programming\Python\FileHandling1.txt', 'r')
s = file22.read()
#print(s)
file22.close

file33 = open(r'D:\Programming\Python\FileHandling3.txt', 'a')
file33.write(p + s)
file33.close

file33 = open(r'D:\Programming\Python\FileHandling3.txt', 'r')
q = file33.read()
print(q)
file33.close
"""

"""f = open(r'D:\Programming\Python\FileHandling4.txt', 'w')
f.write("Hello1")
f.write("Hello2")
f.close

file44 = open(r'D:\Programming\Python\FileHandling4.txt', 'a')
t = file44.read()
print(t)
f.close"""

# File A with binch of numbers. Create two files one with even and other with odd create the file as well
# Create a file with a bunch of numbers
"""with open(r'D:\Programming\Python\FileWithNumbers.txt', 'w') as file:
    for i in range(1, 21):
        file.write(f"{i}\n")

# Read the file and separate even and odd numbers into two different files
with open(r'D:\Programming\Python\FileWithNumbers.txt', 'r') as file:
    numbers = file.readlines()

with open(r'D:\Programming\Python\EvenNumbers.txt', 'w') as even_file, 
     open(r'D:\Programming\Python\OddNumbers.txt', 'w') as odd_file:
    for number in numbers:
        if int(number.strip()) % 2 == 0:
            even_file.write(number)
        else:
            odd_file.write(number)

# Print the contents of the even numbers file
with open(r'D:\Programming\Python\EvenNumbers.txt', 'r') as even_file:
    print("Even Numbers:")
    print(even_file.read())

# Print the contents of the odd numbers file
with open(r'D:\Programming\Python\OddNumbers.txt', 'r') as odd_file:
    print("Odd Numbers:")
    print(odd_file.read())"""
    
"""lst1 = ['1-SAN\n', '2-BAN\n', '3-MAN\n']
f = open(r'D:\Programming\Python\EvenNumbers.txt', 'w')
f.writelines(lst1)
f.close()

f = open(r'D:\Programming\Python\EvenNumbers.txt', 'r')
s = f.read()
print(s)
f.close"""
