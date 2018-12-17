import operator

#x = {10: 1, 13: 4, 4: 3, 2: 1, 0: 10}
x = {1: 2, 2: 1, 3: 5, 100: 1, 4: 2}

#sort by value
print "SORT BY dict.items()"
print "Sorting by value..."
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

sorted_x = dict(sorted_x)
print sorted_x
print sorted_x.keys()

#sort by keys
print "Sorting by keys..."
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

sorted_x = dict(sorted_x)
print sorted_x
print sorted_x.keys()

print "SORT BY dict()"
for k in sorted(x, key=x.get):
  print k, x[k]

print 

for k in sorted(x, key=x.get, reverse=True):
  print k, x[k]
