"""
Exercise 5.3

Fermat's Last Theorem says that there are no integers a, b, and c such that 

    a**n + b**n = c**n

for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters, a, b, c and n, and
that checks to see if Fermat's theorem holds. If n is greater than 2 and it turns out 
to be true that
    
    a**n + b**n = c**n

the program should print, "Holy smokes, Fermat was wrong!' Otherwise the program should 
print, "No, that doesn't work."

2. Write a function that prompts the user to input values for a, b, c and n, converts them 
to integers, and uses check_fermat to check whether they violate Fermat's theorem.
"""

#Item no. 1
#----------

def check_fermat():
    a = int(input("Gimme an 'a' > "))
    b = int(input("Gimme an 'b' > "))
    c = int(input("Gimme an 'c' > "))
    n = int(input("Gimme an 'n' > "))
    
    if n <= 2:
        print("No, 'n' has to be greater than 2.")
        return
    
    left_total = str(a**n + b**n)
    right_total = str(c**n)
    
    print("a**n + b**n = " + left_total)
    print("c**n = " + right_total)
    
    if a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        
#check_fermat()     # remove comment from first part on the left to test.


#Item no. 2
#----------


#Oops! I already did no. 2 as no. 1.