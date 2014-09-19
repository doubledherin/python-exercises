"""
Exercise 11.1
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn't matter what the values are. Then you can use the in operator 
as a fast way to check whether a string is in the dictionary.

If you did Exercise 10.11, you can compare the speed of this implementation with the 
list "in" operator and the bisection search.
"""
import time

def dict_maker(t):
    d = dict()
    for item in t:
        d[item] = len(item)
    return d

def bisect(t, v):
    found = False
    start = 0
    stop = len(t)-1
    while start<=stop and not found:
        midpoint = (start+stop)//2
        if t[midpoint] == v:
            found = True
        elif t[midpoint] < v:
            start = midpoint + 1
        else:
            stop = midpoint - 1
    if found:
        return midpoint

fin = open("words.txt")
t = []
for line in fin:
    word = line.strip()
    t.append(word)



# processing time is 0.04 seconds
t0 = time.clock()
print "zymurgy" in dict_maker(t)
print time.clock() - t0, "seconds to look up 'zymurgy' in words.txt with dict_maker"

# processing time is 5.9e-05; much faster than the hash for this case
t0 = time.clock()
print bisect(t, "zymurgy")
print time.clock() - t0, "seconds to look up 'zymurgy' in words.txt with bisect (which uses the list 'in' operator)"

