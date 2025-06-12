s = {1, 2, 3, 4, (1, 2, 3)}
#s2 = {1, 2, 3, [1, 2, 3, 4]} List is immutable
s1 = set()
s1 = {'What', 2, 1, 'Bat', 'Man'}
print(s1)
print(s)
#print(s2)

# List --> Set
L = [1, 2, 3, 4, 5, 5, 4, 3 ,2 ,1]
snew = set(L)
print(snew)
print(type(snew))

# Tuple --> Set
T = (1, 2, 2, 4, 4, 5)
snew1 = set(T)
print(snew1)

# add(element):

def addset(sets, elements):
    return sets.add(elements)

addset(s1, 7)
print(s1)

# remove(element):
def remset(sets, elements):
    return sets.remove(elements)

remset(s1, 7)
print(s1)

# discard(element): Removes an element if found and no error if not found.
def discardset(sets, elements):
    return sets.discard(elements)

discardset(s, 8)
print(s)

# pop(): removes and returns an arbitary element.
def popset(sets):
    return sets.pop()

print(popset(s1))
print(popset(snew))

# union(other_set):
def unionset(sets, sets1):
    return sets.union(sets1)

print(s1)
print(snew)
unionset1 = unionset(snew, s1)
print(unionset1)

# intersection(other_set):
def interset(sets, sets1):
    return sets.intersection(sets1)

IT = {"BatMan", "SuperMan", "BlackAdam", "Flash"}
CS = {"IronMan", "BatMan", "Flash", "Hulk"}

print(IT)
print(CS)
print(interset(IT, CS))

# difference(other_set): removes same elements from sets and sets1.
def diffset(sets, sets1):
    return sets.difference(sets1)

print(diffset(snew, s1))
print(diffset(s1, snew))

print(diffset(IT, CS))
print(diffset(CS, IT))

# symmetric_difference(other_set): take elements from 1 & 2 and puts them in 1:
def symdiff(sets, sets1):
    return sets.symmetric_difference(sets1)

print(s1)
print(s)
print(symdiff(s1, s))

# issubset(other_set):
def subset(sets, sets1):
    return sets.issubset(sets1)

print(s1)
print(s)
print(subset(s1, s))

# issuperset(other_set):
def superset(sets, sets1):
    return sets.issuperset(sets1)

print(s1)
print(s)
print(superset(s1, s))
############################
print()

Qs1 = {'A', 'B', 'C', 'D', 'E', 'F'}
Qs2 = {'B', 'E'}

something = subset(Qs2, Qs1)
print(something)

samething = superset(Qs1, Qs2)
print(samething)

print()
###########################

Cafe = {'A', 'B', 'N', 'T', 'U', 'I', 'O', 'P'}
Bakery = {'A', 'N', 'O', 'Z', 'Y', 'K'}

print(interset(Bakery, Cafe))
print()
###########################

Lst = [1, 1, 2, 3, 3 ,5, 3, 4, 7, 9, 10]
converter_set = set(Lst)
newlist = list(converter_set)
                                                         # def sqr(num): return num **  2  
lst = list(map(lambda i : i * i, newlist)) #list(map(sqr, newlist))
print("Old list:", newlist)
print("New list :", lst)

print()
###########################
add = 0

for i in newlist:
    add += i
    
print("Sum :", add)
print()
###########################
### REDUCE FUNCTION ###

from functools import reduce

def SumOfNum(a, b):
    return a + b

newlist.append(8)
newlist.append(6)

print(newlist)
add = reduce(SumOfNum, newlist)
print("Sum using Reduce :", add)

avg = add/len(newlist)
print("Average is :", avg)









