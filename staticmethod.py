class A:
   total = 0

   def __init__(self, name):
     print "In the Ctor"
     self.name = name
     A.total += 1

   def status():
      print "Total number of instance of A : ", A.total
   
   print "I'm here"
   status = staticmethod(status)

if __name__ == "__main__":
    a1 = A("A1")
    a2 = A("A2")
    a3 = A("A3")
    a4 = A("A4")

    A.status()
