global_variable = 24

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)



r = int(input("Enter the range: "))
for i in range(r):
    print(fib(i), end = ' ')