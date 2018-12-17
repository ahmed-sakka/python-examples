def fiboi(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

def fibor(n):
    if n == 0: return 0
    if n == 1: return 1

    return fibor(n - 1) + fibor(n - 2)

for i in range(10):
   print (fiboi(i), fibor(i))

print

def factr(n):
    if n <= 1: return 1

    return n * factr(n - 1)

def facti(n):
    prod = 1

    for i in range(2, n+1):
        prod *= i

    return prod

for i in range(10):
   print (facti(i), factr(i))
