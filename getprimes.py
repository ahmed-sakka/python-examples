from math import sqrt

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
    
#print all primes whose sum doesnt exceed a given limit
def solve_number_10(next_prime_limit):
    total = 0
    for next_prime in get_primes():
        if next_prime < next_prime_limit:
            total += next_prime
        else:
            print(total)
            return

def get_primes(number=2):
    while True:
        if is_prime(number):
            yield number
        number += 1

#infinite loop -- print an infinite series of primes
#for n in get_primes():
#   print n,

solve_number_10(5)

#print the first 100 primes
def first_100():
    count = 0
    while count <= 100:
        if is_prime(count):
            yield count
        count += 1

for prime in first_100():
    print prime,
