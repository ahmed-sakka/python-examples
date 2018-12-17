import re

#one match, searches from the beginning of the string
#no match
find = re.match(r'ABC_abc', '_ABC_abc_ABC_abc')
if find:
    print find.group()
#ok, match
find = re.match(r'ABC_abc', 'ABC_abc_ABC_abc')
if find:
    print find.group()

#list of matches -- no need to group()
#all matches, *anywhere* in the string
print re.findall(r'ABC_abc', '_ABC_abc_ABC_abc')

#one match, *anywhere* in the string
print re.search(r'ABC_abc', '_ABC_abc_ABC_abc').group()
#can be at the beginning of the string
print re.search(r'ABC_abc', 'ABC_abc_ABC_abc').group()
