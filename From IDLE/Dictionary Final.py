d = {'R' : 20, 'S' : 30, 'T' : 15}

# Key - Value pairs
# Keys are unique

dictempty = {} # Empty Dictionary

##############################################
# Using dict() to construct dictionary:

cons_dict = dict(name = 'ANY', age = 25)

d1 = {'RN' : [1, 2, 3, 4], 'Marks' : [20, 24, 23, 25]}
print(d1)
#d2 = {[1, 2, 3, 4] : 'RN', [20, 24, 23, 25] : 'Marks'}
d3 = {(1, 2, 3, 4) : 'RN', (20, 24, 24, 25) : 'Marks'}
print(d3)
print(d1['RN'])
print(d)
d['R'] = 13
print(d)
print()
###############################################

# ZIP method: 

list1 = ['one', 'two', 'three'] # Keys
list2 = [1, 2, 3]   # Values

new_dict = dict(zip(list1, list2))
print(new_dict)
print()
###############################################

# get(key, default): prints keys in dict:

print(d1.get("Marks")) 
print()

# keys(): returns all the keys:

print(list(d1.keys()))

# values(): returns all the values:

print(list(d1.values()))
print()

# items() : returns all the pairs:
print(d1)
print(list(d1.items()))

print(new_dict)
print(list(new_dict.items()))
print()

# ***Prints the occurenence of a letter in a stirng ***

dict12 = {}
for i in 'Hello':
    if i in dict12:
        dict12[i] = dict12[i] + 1
    else:
        dict12[i] = 1
print(dict12)

# Adding the values to print the sum:

dict13 = {'o' : 1, 't' : 2, 'th' : 3, 'fu' : 4}
add = 0

for i in dict13.values():
    add += i
print(add)

# clear() :




