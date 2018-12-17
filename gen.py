def simple_generator_function():
    yield 1
    yield 2
    yield 3

for value in simple_generator_function():
    print value

gen = simple_generator_function()
print next(gen)
print next(gen)
print next(gen)

gen = simple_generator_function()
print gen.next()
print gen.next()
print gen.next()

g = (x**3 for x in range(5))
print g.next()
print g.next()
print g.next()
