class Parent(object):
    def _protected(self):
        pass

    def __private(self):
        pass

class Child(Parent):
    def foo(self):
        self._protected()

    def bar(self):
        self._Parent__private()

p = Parent()
p._protected()
p._Parent__private()


c = Child()
c._protected()
c._Parent__private()
