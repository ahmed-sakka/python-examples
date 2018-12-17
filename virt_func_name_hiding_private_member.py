class Base(object):
        common = 100 #class variable

        def __init__(self):
            self.__x = 10
            self._y = 10
            self.z = 10
            self.common = 100

        def inherited_fn(self):
            print "Inherited function:", self.__x

        def virt_func(self):
            print "In base"

        def name_hiding(self, x):
            print "Base:", x

class Derived(Base):
        common = 1000

        def __init__(self):
            #super(Base, self).__init__()
            #super.__init__() #doesnt work
            Base.__init__(self)
            self.common = 200

        def access_base_members(self):
            print "Base private:", self._Base__x
            print "Base protected and public:", self._y, self.z
            print "Derived common (overriden var):", self.common
            print "Derived class variable:", Derived.common
            print "Base class variable:", Base.common
            #cant get to common since it is overriden in Derived

        def virt_func(self):
            print "In derived"
            
        def name_hiding(self):
            print "In derived"

x = Base()
x.virt_func() #virt_func of Base

y = Derived()
x = y
x.virt_func() #virt_func of Derived

x.inherited_fn() #call inherited fn through Derived
x.name_hiding() #OK
#x.name_hiding(10) #doesnt work due to name hiding

x.__class__.__base__.name_hiding(x, 10) #call overriden function from Base
print x.__class__.__base__.common             #overriden from Base
x.access_base_members()

print x.__dict__
