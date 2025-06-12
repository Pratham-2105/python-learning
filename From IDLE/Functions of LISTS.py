integers = [1, 4, 6, 7, 3]
char = ['Hello', 'Hi', 'What', 'Where']
mixed = [3, 4, 'Hello', 3, 'What']
blank = []
python = ['P', 'Y', 'T' , 'H', 'O', 'N'] 
y = 'sequoia'

def mod(lst, add):
    return lst.append(add)

la = [] 
for i in range(1, 11):
    la.append(i)
print(la)

ls = []
for j in mixed:
    if (type(j) == str):
        ls.append(j)
print(ls)

# Extend - Concating two lists.
mixed.extend(integers)
print(mixed)

#Adding digits in list:
print(mixed)
count = 0

for i in mixed:
    if(type(i) == int):
        count += i
print(count)

# Vowels in a string --> List
vowels = []
for i in y:
    if(i in 'aeiouAEIOU'):
        vowels.append(i)
print(vowels)

# Insert --> Element at a specific index

integers.insert(2, 65)
print(integers)
mixed.insert(2, 54)
print(mixed)

# Printing string from a list

for i in python:
    print(i, end = '')
print()

# POP an element from the list

y = mixed.pop(2)
lst = [y]
print(mixed)
print(lst)

#use la = [1,..,10}
la = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = []
i = 0

while i < len(la):
    if la[i] % 2 == 0:
        new.append(la.pop(i))
    else:
        i += 1

print(la)
print(new)

# Clear

# Count --> Returns the number of occurences

print(la.count(3))

# Sort
# Reverse
# copy






