import os

path = ".."

for (path, dirs, files) in os.walk(path):
    for curr_file in files:
         print os.path.join(path, curr_file)
