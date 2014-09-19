"""
Exercise 7.5. 

The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of pi. (Look it up.)

Write a function called estimate_pi that uses his formula to compute and return an estimate of pi. 

It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15 (which is Python notation for 10 to the power of -15). 

You can check the result by comparing it to math.pi.
"""
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n -1)
        result = n * recurse
    return result
    
def estimate_pi():
    k = 0
    total = 0
    
    while True:
        factor = 2 * math.sqrt(2) / 9801
        print "factor = %g" % factor
    
        num = factorial(4*k) * (1103 + 26390*k)
        print "num = %g" % num
    
        div = (factorial(k) ** 4) * (396 ** (4*k))
        print "div = %g" % div
    
        term = factor * (num / div)
        print "term = %g" % term
        
        total += term
        print "total = %g" % total

        if term < 1e-15:
            break
    
        k += 1
    
    print 1/total
    return 1/total
    
estimate_pi()


