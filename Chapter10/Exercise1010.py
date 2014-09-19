"""
Exercise 10.10

Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. 

Which one takes longer to run? Why?

Hint: use the time module to measure elapsed time. 
"""
import time

def list_builder1(filename):
    fin = open(filename)
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    #print t
    return t

def list_builder2(filename):
    fin = open(filename)
    t = []
    for line in fin:
        word = line.strip()
        t += [word]
    #print t
    return t
    
t0 = time.clock()    
list_builder1("words.txt")
print time.clock() - t0, "seconds process time for list_builder1"

t0 = time.clock()
list_builder2("words.txt")
print time.clock() - t0, "seconds process time for list_builder2"


# Using the .append() idiom is significantly faster: 0.047351 seconds, 
# versus 73.706331 seconds for the += idiom. Reason: the += idiom 
# involves reassignment, so the list is rebuilt from scratch with
# each iteration. I think that means O(n**2). Bad news bears.

