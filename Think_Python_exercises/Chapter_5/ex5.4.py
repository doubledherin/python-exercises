# EXERCISE 1
"""Takes 3 integers and prints 'Yes' or 'No' depending on whether
you can or cannot form a triagle from sticks with those lengths.

Based on the law that if any of the three lengths is greater than the sum of the other two, then a triangle cannot be formed."""
def is_triangle(a, b, c):
    if a > b + c:
        print 'No'
        return
    if b > a + c:
        print 'No'
        return
    if c > a + b:
        print 'No'
        return
    print 'Yes'
    return

#TESTS    
#is_triangle(1, 2, 2)
#is_triangle(12, 4, 2)

# EXERCISE 2
"""Run is_triangle based on user inputs, which are converted to integers.""" 
def prompt_triangle():
    a = int(raw_input("Enter a (positive integer) value for side A: "))
    b = int(raw_input("Enter a (positive integer) value for side B: "))
    c = int(raw_input("Enter a (positive integer) value for side C: "))
    print "Checking to see whether those sides can form a triangle ... "
    print "The answer is: "
    is_triangle(a, b, c)   
    
#TEST
prompt_triangle()