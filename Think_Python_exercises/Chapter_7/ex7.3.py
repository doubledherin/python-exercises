"""
Write a function that prints a 4-column table.
--Column 1 should show a number, a
--Column 2 should show the square root of a according to
  the function defined in ex7.2.py
--Column 3 should show the square root of a according to 
  math.sqrt
--Column 4 should show the absolute value of the difference 
  columns 2 and 3."""

import math

def square_root(a):
    x = a / 2
    while True:
        # print "x equals", x
        y = (x + a/x) / 2
        # print "y equals", y
        if abs(y-x) < 0.0000001:
            # print y
            return y
        x = y  
          
def test_square_root(a):
    a = float(a)
    b = square_root(a)
    c = math.sqrt(a)
    d = abs(b - c)
    print a, b, c, d
    
test_square_root(2)
    
