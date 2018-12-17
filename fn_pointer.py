def func3():
    #print x #cant find x
    return func1()

x = 1

def func1():
    print x
    return 1

def func2():
    return func1()

print func3()
print func2()


####



def A_function(func, *args, **kargs):
        print "Func Ptr:", func(),
	return f(*args, **kargs)

def f(a, b, c, d, e):
	return a*b*c*d*e

print(A_function(func1, 10, 20, c=30, d=40, e=50))
