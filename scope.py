x = 0;

def f():
   return x;

def g():
   x = 1;
   return f();

print "%d" % g()
