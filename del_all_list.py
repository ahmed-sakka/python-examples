L = [1,2,3,3,3,2,2]

try:
    while True:
        L.remove(3)
except:
        print "Done"

print L

#for i in (idx for idx in L if L[idx] == 2):
#    print i
#    del L[i]
#    #L.pop(i)

while True:
    try:
        i = L.index(2)
        #del L[i]
        L.pop(i)
    except:
        break

print "Done, again"

print L
