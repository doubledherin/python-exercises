"""
Exercise 6.2. 

Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.

"""
import math

def hypotenuse(side1, side2):
    return math.sqrt(side1 ** 2 + side2 ** 2)

    
    
print hypotenuse(3,4)
print hypotenuse(30,40)
print hypotenuse(32,4)
print hypotenuse(3,-4)