class Base:
    def __init__(self, x):
        self.x = x

    def func(self):
        self.y = 10

b1 = Base(10)
#b1.func()

b2 = Base(100)
b2.func()

print b1.x#, b1.y
print dir(b1), dir(b2)
print b2.x, b2.y
