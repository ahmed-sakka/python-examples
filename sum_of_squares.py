square = (i*i for i in range(1000000))

#add the squares
total = 0
for i in square:
    total += i

print total

#add the squares
total = 0
for i in (i*i for i in range(1000000)):
    total += i

print total
