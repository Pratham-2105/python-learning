"""
def decor(func):
    def inner():
        print("-----------")
        func()
        print("-----------")

    return inner

def msg():
    print("Python Programming")


out = decor(msg) # Parameter as a function!!
out()
"""

"""'

def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Calling function: {func.__name__}")

    return wrapper

@log_decorator
def greet():
    print("Hello")

# a = log_decorator(greet)
# a()
greet()

"""