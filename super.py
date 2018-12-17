class AA(object):
 def __init__(self):
   print "world"

class A(AA):
 def __init__(self):
   super(A, self).__init__()
   print "world"

class B(A):
 def __init__(self):
   print "hello"
   super(B, self).__init__()

if __name__ == "__main__":
    b = B()
