"""
Write a function that takes a as parameter, chooses a reasonable estimate of the square root of a, and returns and better estimate of the square root of a (using Newton's method).
"""
def square_root(a):
    x = a / 2
    while True:
        # print "x equals", x
        y = (x + a/x) / 2
        # print "y equals", y
        if abs(y-x) < 0.0000001:
            print y
            return y
        x = y    
square_root(23.0)  # 8.0, 5.0, 5.0, 4.1, 4.1, 4.0012.., 