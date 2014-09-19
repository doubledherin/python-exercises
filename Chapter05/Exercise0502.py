"""
Exercise 5.2
Write a function called do_n that takes a function object and a number, n, as arguments, and that calls the given function n times.

"""

def do_n(f, n):
    for i in range(n):
        f()

def spammy():
    print "Spam!"

do_n(spammy, 5)