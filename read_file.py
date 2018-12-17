#way 1
with open('monkey.py', 'r') as f:
    for line in f: #a file is a seqeunce of lines -- iterating over that sequence
        words = line.split()
        print words

#way 2: same as above
with open('monkey.py', 'r') as f:
    for line in f.readlines():
        words = line.split()
        print words

#way 
with open('monkey.py', 'r') as f:
    print f.read().splitlines()
    #for line in f.read():
    #    print line,
