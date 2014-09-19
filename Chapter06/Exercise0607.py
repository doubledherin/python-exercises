"""
Exercise 6.7. 
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. 
Note: you will have to think about the base case.
"""

def is_power(a, b):
    if a == 0 or b == 0:
        print "False"
        return False
    elif a/b == 1:
        print "True"
        return True
    elif a % b == 0:
        is_power(a/b, b)
    else:
        print "False"
        return False

is_power(8, 2)
is_power(5, 2)
is_power(8, 8)
is_power(0, 2)
is_power(8, 0)
is_power(8, -2)
is_power(-16, 8)
    