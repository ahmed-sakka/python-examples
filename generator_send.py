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

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

def print_successive_primes(iterations=3, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes()

#another generator
def generator(num):
    while True:
        num = yield num

def generator_send():
    g = generator(1)
    g.send(None) #print g.send(None) outputs a 1
    print g.send(1)
    print g.send(2)
    print g.send(3)

generator_send()
