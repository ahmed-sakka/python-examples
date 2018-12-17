from dis import dis

class A(object):
  def __pick(self):
      print "1"

  def doitinA(self):
      self.__pick()

  def __xyz(self):
      print "A"

class B(A):
  def __pick(self):
      print "2"

  def doitinB(self):
      self.__pick()

  def __xyz(self):
      print "B"

b = B()
b._B__pick()
b._A__pick()
b.doitinA() # prints 1
b.doitinB() # prints 2
b._B__xyz()
b._A__xyz()

dis(A.doitinA)
print
dis(B.doitinB)
