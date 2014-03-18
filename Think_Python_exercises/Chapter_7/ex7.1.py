"""Rewrite the funciton print_n from Sectin 5.8 using iteration instead of recursion.

Here's the recursive version:

def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)
"""

def print_n(s, n):
    while n > 0:
        print s
        n -= 1
        
# print_n('hello', 15)