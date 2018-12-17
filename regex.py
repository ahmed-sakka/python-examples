import re
from sets import Set
import string

input = []
input.append('0123.0123abc')
input.append('0123.abc0123')
input.append('0123.0123')

#for ip in [input1, input2, input3]:

for ip in input:
    res = re.findall(r'[\d]+[.]{1}[\w]+', ip)
    if(res):
        for idx, result in enumerate(res):
            #print "*"*50, "\nRegEx Results Master List", "\n", "*"*50 
            #print idx, result

            #to discard input[0] and input[1] as a valid result using another RegEx:
            res1 = re.findall(r'^[^A-Za-z_]+$', result)
            if(res1):
                print "*"*50, "\nRegEx 2", "\n", "*"*50 
                for idx, result in enumerate(res1):
                    print idx, result
    
            #to discard input[0] and input[1] as a valid result using Sets:
            letters = Set(string.ascii_letters)
            intersect = letters & Set(result)
            if not intersect:
                print "*"*50, "\nSets", "\n", "*"*50 
                for idx, result in enumerate(res):
                    print idx, result

