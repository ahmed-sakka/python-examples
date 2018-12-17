class Base:
    A = 10
    #self.x = 20 #self is not defined

    #def __init__(self):
    #    self.x = 20
    #    self.y = 100

    def nonstatic_func1(self):
        self.x = 30
        return self.x
    
    def nonstatic_func2(self):
        abc = 100 #local variable with function-scope
        self.y = 50
        return self.y
    
    print "Hey there"

    def static_func():
        A = 40
        #self.x = 50 #self not defined
        return A

    static_func = staticmethod(static_func)

b = Base()
print Base.A
print b.nonstatic_func1()
print b.x#, b.y
#print b.abc
#print b.nonstatic_func2.abc
print b.static_func()
print Base.static_func()
print id(b)

print "Diff objects of the same class in Python have diff properties"
b = Base()
print Base.A
print b.nonstatic_func2()
print b.y
print b.static_func()
print id(b)
