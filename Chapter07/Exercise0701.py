"""
Exercise 7.1. 
Rewrite the function print_n from Section 5.8 using iteration instead of recursion.

def print_n(s, n):
    if n <= 0:
        return

    print s
    print_n(s, n-1)
"""

def print_n(s, n):
    while n > 0:
        print s
        n -=1
   
print_n("Spam!", 5)

