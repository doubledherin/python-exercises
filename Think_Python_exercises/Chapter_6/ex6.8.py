"""
The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is Euclid's algorithm, which is based on the observation that if r is the remainder when a is divided by b, then 
gcd(a,b) = gcd(b,r). As a base case, we can use gcd(a,0) = a

Write a function called gcd that takes a and b and returns the GCD.
"""

def gcd(a,b):
    if b == 0:
        print a
        return a
    else:
        return gcd(b, a%b)
        
gcd(12, 8)  # 4
gcd(8, 12)  # 4
gcd(5, 13)  # 1
gcd(6, 136) # 2
gcd(0, 12)  # 12
gcd(120, 0) # 120
gcd(-2, 0)  # -2
gcd(1, 4)   # 1



