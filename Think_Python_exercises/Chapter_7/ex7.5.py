"""
Write a function that uses Srinivasa Ramanujan's formula to estimate pi.

It should use a while loop to compute tersm of the summation until the last term is smaller than 1e-15 (which is Python notation for 10 to the -15th power). 

You can check the result by comparing it to math.pi.
"""

import math

def estimate_pi():
    total = 0
    k = 0
    a = (2 * math.sqrt(2)) / 9801
    while True:
        term1 = (factorial(4*k) * (1103 + 26390*k))
        term2 = (factorial(k)**4) * (396**(4*k))
        b = term1 / term2
        iteration = a * b
        total += iteration
        
        if abs(iteration) < 1e-15:
            break
        k += 1
    x = 1/total
    y = math.pi
    print "This pi is: ", x
    print "The math.pi pi is: ", y
    print "The difference is: ", abs(x-y)
        
        
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
estimate_pi()
        
