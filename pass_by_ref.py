class Base():
    pass

def test(x):
    print id(x)    

print "Sending int which is immutable..."
a = 10
print id(a)
test(a) 

print "Sending float which is immutable..."
a = 10.5
print id(a)
test(a) 

print "Sending str which is immutable..."
a = "Hey"
print id(a)
test(a) 

print "Sending list which is mutable..."
a = []
print id(a)
test(a) 

print "Sending dict which is mutable..."
a = {}
print id(a)
test(a) 

print "Sending class object which is mutable..."
a = Base()
print id(a)
test(a) 
