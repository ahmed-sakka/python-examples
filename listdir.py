#Print a list of file in a directory
#We want to print a list of files in a directory including the sub-directories. We may want to do it recursively.

import os

path = 'fn_pointers'

def file_list(dir):
    subdir_list = []
    for item in os.listdir(dir):
        fullpath = os.path.join(dir,item)
        if os.path.isdir(fullpath):
            subdir_list.append(fullpath)
        else:
            print fullpath

    for d in subdir_list:
        file_list(d)

file_list(path)

i = 0
for (path, dirs, files) in os.walk(path):
    for f in files:
        print os.path.join(path, f)
    #print dirs
    #print files
    #print "----"
    i += 1
    if i >= 4:
        break
