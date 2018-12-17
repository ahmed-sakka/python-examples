import inspect

class A:
    pass

print issubclass(A, A)
print issubclass(A, object)

class B(object):
    pass

print issubclass(B, B)
print issubclass(B, object)

class C(B):
    pass

print issubclass(C, B)
print issubclass(C, object)

print inspect.getmro(C)

#classC = C()
#print inspect.getmro(classC)
