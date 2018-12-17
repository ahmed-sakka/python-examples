def enforce(*types):
    def check_accepts(f):
        def new_f(*args, **kwargs):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), "arg %r does not match %s" % (a,t)            
            return f(*args, **kwargs)
        return new_f
    return check_accepts

@enforce(int, (int,float))
def func(arg1, arg2):
    return arg1 * arg2

print func(3, 2) # -> 6.0
#print func('3', 2) # AssertionError!
#print func('three', 2) # AssertionError!

def bounds_check(f):
    def inner(*args):
        for i, e in enumerate(args):
            assert args[i] >= 0, "arg %r is negative" % (i,)
        return f(*args)
    return inner

@bounds_check
def func(arg1, arg2):
    return arg1 * arg2    

print func(3, 2)
#print func(-1, 2) # AssertionError!
print func(1, -2) # AssertionError!
