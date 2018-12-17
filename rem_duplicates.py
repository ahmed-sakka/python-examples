import collections
from sets import Set

d = collections.defaultdict(int)

#extra space
l = [1,1,1,1,2,3,4,5,5]
res = []

for i in range(len(l)):
    if d[l[i]] == 0:
        d[l[i]] = 1
        res.append(l[i])

print res

#in place
j = 0
l = [1,1,1,1,2,3,4,5,5]
d = collections.defaultdict(int)

for i in range(len(l)):
    if d[l[i]] == 0:
        d[l[i]] = 1
        l[j] = l[i]
        j += 1

for i in range(j,len(l)):
    l.pop()

print l

#use set
l = [1,1,1,1,2,3,4,5,5]
res = list(Set(l))
res = list(set(l))
print res
