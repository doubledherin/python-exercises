"""
Exercise 11.8

Exponentiation of large integers is the basis of common algorithms for public-key encryption.

Read the Wikipedia page on the RSA algorithm and write functions to encode and decode messages.

"""
import random, math

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for divisor in range(2, int(math.ceil(math.sqrt(n)))):
            if n % divisor == 0:
                return False
        return True

# the below function is taken from my exercise 6.8
# checks for greatest common divisor
def gcd(a, b):
    if b == 0:
        print a
        return a
    else:
        r = a % b
        return gcd(b, r)

# the below 3 functions are from stack overflow;
# I couldn't figure out how to do them myself.

# Euler's totient
def phi(n):
    y = n
    for i in range(2,n+1):
        if isPrime(i) and n % i == 0:
            y *= 1 - 1.0/i
    return int(y)

# preamble to figuring out the 
# modular multiplicative inverse
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# modular multiplicative inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
    
    
def keyGenerator():
    p = 1
    while not isPrime(p):
        p = random.randint(2**10, 2**20)
    q = 1
    while not isPrime(q):
        q = random.randint(2**10, 2**20)
    n = p * q
    totient = phi(n)
    e = random.randint(2, totient)      # public key
    
    while gcd(e, totient) != 1:
        e = random.randint(2, totient)
    d = modinv(e, totient)              # private key
    return e, d
    
#keyGenerator()  # this breaks everything








