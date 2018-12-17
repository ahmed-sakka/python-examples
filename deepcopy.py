import copy

class Foo(object):
    def __init__(self, val):
         self.val = val

    def __repr__(self):
        return str(self.val)

foo = Foo(1)

print "*" * 50
print "List copy"
print "*" * 50

a = ['foo', foo]
b = a[:]
c = list(a)
d = a
e = copy.copy(a)
f = copy.deepcopy(a)

#edit orignal list
a.append('baz')
a[1] = 10
foo.val = 5

print('original: %s\nslice: %s\nlist(): %s\ndirect assignment: %s\nshallow copy: %s\ndeepcopy: %s' % (a, b, c, d, e, f))

print "*" * 50
print "Dict copy"
print "*" * 50

d = {'a': 1, 'b': 2}
d2 = d
d3 = copy.copy(d)
d4 = copy.deepcopy(d3)

#edit orignal dict
d['c'] = 1
d['b'] = 1
print "original: %s\ndirect assignment copy: %s\nshallow copy: %s\ndeep copy: %s" % (d, d2, d3, d4)
