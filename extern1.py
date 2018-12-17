import sys
import extern2 
from extern2 import print_a
#from extern2 import print_b

a = 10
print a

extern2.a = 100

#print extern2.print_b.b #'function' object has no attribute 'b'

print_a()

#print_b()

sys.modules['extern2'].print_b()
print a
