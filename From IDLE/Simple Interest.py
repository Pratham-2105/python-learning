p = float(input("Enter the Principle amount : "))
r = float(input("Enter the Rate-of-interest : "))
t = int(input("Enter the time in months : "))

si = (p * r * t) / 100
total = p + si

print("Simple Interest gained in", t, "months is", si)
print("Total amount after", t, "months is", total)
