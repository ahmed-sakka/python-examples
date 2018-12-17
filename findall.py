def findall(L, value):
       # generator version
       i = 0
       try:
            while 1:
               i = L.index(value, i+1)
               yield i
       except ValueError:
           pass

L = [1,2,2,3,3,2]
value = 2
for index in findall(L, value):
   print "match at", index
