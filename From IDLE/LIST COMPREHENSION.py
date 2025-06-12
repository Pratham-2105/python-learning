### LIST COMPREHENSION ###
blank = []
for i in range(1, 11):
    blank.append(i)

integers = [i for i in range(1, 11) if i % 2 == 0]
print(integers)

tup = (1, 2, 3) # Packing
a, b, c = tup
print(tup)
print(a, b, c) # Unpacking

lst = [13, 21, 32] 
d, e, f = lst
print(d, e, f)




