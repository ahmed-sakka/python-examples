class MyClass:
    def f(self):
        print "f()"

def monkey_f(self):
    print "monkey_f()"

MyClass.f = monkey_f
obj1 = MyClass()
obj2 = MyClass()
obj1.f()
obj2.f()
