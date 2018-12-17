import re
s = "##hey there"
re.search(r'##([A-Za-z ]+)', s).group(1) #'hey there'

