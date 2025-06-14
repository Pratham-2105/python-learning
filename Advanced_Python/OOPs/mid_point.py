class Mid:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoint(self, other):
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Mid(mid_x, mid_y)

    def length(self, other):
        return((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f'Mid({self.x}, {self.y})'

p1 = Mid(1, 5)
p2 = Mid(6, 7)

mid = p1.midpoint(p2)
dist = p1.length(p2)

print("Point 1: ", p1)
print("Point 2: ", p2)
print("Distance: ", dist)
print("Midpoint: ", p1.midpoint(p2))