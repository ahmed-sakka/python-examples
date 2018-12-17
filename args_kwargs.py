def kwargs_f(a):
    print a

def args_f(*args):
    sum = 0
    for x in args:
        sum += x
    avg = sum/len(args)
    return avg

kwargs_f(**{'a': 1}) #1
#kwargs_f(**{'b': 1}) #not ok

kwargs = {'a': 1}
kwargs_f(**kwargs) #1

print args_f(10, 20)
print args_f(10, 20, 30)
