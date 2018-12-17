def foo(x, y=0): # 1
    print x - y

foo(3, 1) # 2

foo(3) # 3

foo(y=1, x=3) # 5
