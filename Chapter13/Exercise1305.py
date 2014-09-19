"""
Exercise 13.5

Write a function named choose_from_hist that takes a histogram as defined in
Section 11.1 and returns a random value from the histogram, chosen with probability in proportion to frequency. For example, for this histogram:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> print hist
{'a': 2, 'b': 1}

your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
"""
from __future__ import division
import random, string


# taken and modified from my work in Exercise 11.2
def histogram(t):
    d = dict()
    for item in t:
        d[item] = d.get(item, 0) + 1
    return d
        
def choose_from_hist(d):
    # change histogram back to list
    t = []
    for k in d:
        for i in range(d[k]):
            t.append(k)
      
    n = random.randint(0, (len(t)-1))
    
    selection = t.pop(n)
    probability = d[selection] / (len(t) + 1)
    return "We selected '%s' with a probability of %g." % (selection, probability)


# taken and modified from my work in Exercise 11.2
def histogramFile(filename):
    t = stripdown(filename)
    d = dict()
    for item in t:
        d[item] = d.get(item, 0) + 1
    return d

# takes a file of words and creates a list of words
# in the order they appeared in the file
def stripdown(filename):
    
    bookString = ""
    fin = open(filename)
    
    for line in fin:            
        line = line.lower()
        line = line.replace("--", " ")
        line = line.replace("-", " ")
        line = line.replace("\n", " ")
        for c in string.punctuation:
            line = line.replace(c, "")
        bookString += line
    
    bookList = bookString.split()
    return bookList

print choose_from_hist(histogramFile("emma.txt"))
print choose_from_hist(histogramFile("crime_and_punishment.txt"))


    
    
    
    
    