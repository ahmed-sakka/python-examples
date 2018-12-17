fh = open('trash', "r")

#reads in the entire file in the form of a str
print "Doing read()..."
print fh.read().rstrip()
print type(fh.read())

#reads in a line in the file in the form of a str
fh.seek(0, 0)
print "Doing readline()..."
print fh.readline()

#reads in the whole file at once and splits it by line -- outputs a list
fh.seek(0, 0)
print "Doing readlines()..."
print fh.readlines()

fh.seek(0, 0)
print "Doing readlines() with rstrip()..."
print [line.rstrip() for line in fh.readlines()]

#reads in each line in the file using generators
fh.seek(0, 0)
print "Doing xreadlines()..."
print fh.xreadlines().next().rstrip() #'file' object has no attribute 'xreadline'
print fh.xreadlines().next().rstrip() #'file' object has no attribute 'xreadline'
print fh.xreadlines().next().rstrip() #'file' object has no attribute 'xreadline'

#iterating over xreadlines()  
print "Iterating over xreadlines()..."
fh.seek(0, 0)
for line in fh.xreadlines():
    print line.rstrip()

#treat the file object as an iterable
print "Iterating over the file object..."
fh.seek(0, 0)
for line in fh:
    print line.rstrip()

fh.close()
