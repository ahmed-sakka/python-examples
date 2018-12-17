class Base(object):
    def __init__(self):
        self.x = 10
        self.y = 10
    
    def __init__(self, a):
        self.x = a
        self.y = 10

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def overloading_test(self):
        self.x = 10

    def overloading_test(self, a):
        self.x = a
    
    def overloaded_fn(self, *args):
        if len(args) == 0:
            self.x = 10
            self.y = 10
        elif len(args) == 1:
            self.x = args[0]
            self.y = 10
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]

if __name__ == "__main__":
      #Base1 = Base()     #doesnt work 
      #Base2 = Base(100)  #doesnt work
      Base3 = Base(100, 200)

      print Base3.x, Base3.y

      #Base3.overloading_test() #doesnt work
      Base3.overloading_test(100)

      Base3.overloaded_fn()
      print "No args", Base3.x, Base3.y
      Base3.overloaded_fn(100)
      print "X arg", Base3.x, Base3.y
      Base3.overloaded_fn(100, 200)
      print "Y arg", Base3.x, Base3.y
