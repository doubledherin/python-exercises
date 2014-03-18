# EXERCISE 1
"""checks to see if Fermat's Last Theorem (that for all integers, 
a to the nth power + b to the nth power can never equal c to the 
nth power, where n is greater than 2)"""
def check_fermat(a, b, c, n):
    if type(a) != int or type(b) != int or type(c) != int or type(n) != int:
        print "Error: Only integers allowed."
        return
    if a**n + b**n != c**n:
        print "No, that doesn't work. Fermat was right."
        return
    print "Holy smokes, Fermat was wrong!"
    
# check_fermat(1, 2, 3, 4)


# EXERCISE 2
"""prompts user for values a, b, c, and n; converts them to integers, 
and runs the check_fermat function"""

def prompt_check_fermat():
    print "\nFermat's Last Theorem states that for all integers:\n"
    print "a to the nth power + b to the nth power != equal c to the nth power,"
    print "where n is greater than 2."
    print "Let's check!"
    a = int(raw_input("Please enter an integer value for a: "))
    b = int(raw_input("Please enter an integer value for b: "))
    c = int(raw_input("Please enter an integer value for c: "))
    n = int(raw_input("Please enter an integer value for n: "))
    check_fermat(a, b, c, n)
    
prompt_check_fermat()
    
        
    