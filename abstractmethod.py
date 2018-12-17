from abc import ABCMeta, abstractmethod

class Abstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass

#Abstract() #cant instantiate

class B(Abstract):
    pass

#B() #cant instantiate

class C(Abstract):
    def foo(self):
        return 7

print (C()).foo()
