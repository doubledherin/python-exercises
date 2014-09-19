"""
Exercise 11.3

Dictionaries have a method called "keys" that returns the keys of the dictionary, 
in no particular order, as a list.

Modify print_hist (below) to print the keys and their values in alphabetical order.

def print_hist(h):
    for c in h:
        print c, h[c]     
"""

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    t = h.keys()
    t.sort()
    return t
    
s = "brontosaurus"

print print_hist(histogram(s))

