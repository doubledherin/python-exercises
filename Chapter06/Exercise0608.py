"""
Exercise 6.8. 

The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder. 

One way to find the GCD of two numbers is Euclid's algorithm, which is based on the 
observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). 

As a base case, we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a and b and returns their greatest 
common divisor. If you need help, see http://en.wikipedia.org/wiki/Euclidean_algorithm.

Credit: This exercise is based on an example from Abelson and Sussman's Structure and 
Interpretation of Computer Programs.
"""


def gcd(a, b):
    if b == 0:
        print a
        return a
    else:
        r = a % b
        return gcd(b, r)
        
        
gcd(10, 5)  # 5
gcd(2, 5)   # 1
gcd(534, 0) # 534
gcd(0, 5)   # 5
gcd(64, 14) # 2
gcd(81, 45) # 9