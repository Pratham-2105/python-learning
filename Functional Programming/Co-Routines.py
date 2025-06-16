"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

ob  = MyNumbers()
myiter = iter(ob)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""

"""
def grep(pattern):
    print(f"Looking for {pattern}")

    while True:
        line = (yield)
        if pattern in line:
            print(f"Matched: {line}")


g = grep("python")
#next(g)

g.__next__()
g.send("hello world")
g.send("message1")
g.send("message2 is python")
g.send("python is awesome")

"""