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