"""Use incremental development to write a function called 'hypotenuse' that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go."""

# first iteration: skeleton with parameters and return value sketched out
"""# this function will take two arguments and return a float. 
def hypotenuse(x, y):
    return 0.0

we're good there."""

# second iteration: adding the code to the body 
# (and importing required math module)

import math

def hypotenuse(x, y):
    z = math.sqrt(x**2 + y**2)
    print z


hypotenuse(3, 4) # should yield the result '5' -- and it does!