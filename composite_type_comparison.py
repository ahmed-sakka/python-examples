class Base:
    x = 10

    def __init__(self, y=7):
        self.y = y

    def __eq__(self, obj):
        return self.y == obj.y

b1 = Base()
b2 = Base()
b3 = Base(1)
b4 = Base(1)

print "b1 == b2", b1 == b2
print "b1 is b2", b1 is b2
print ""
print "b3 == b4", b3 == b4
print "b3 == b4", b3.__eq__(b4)
print "b3 is b4", b3 is b4
print ""
print "b1 == b1", b1 == b1
