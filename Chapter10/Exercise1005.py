"""
Exercise 10.5

Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
"""

def chop(t):
    t = t[1:-1]
    print t # to verify: [2,3,4,5,6,7]
    return 


listy = [1,2,3,4,5,6,7,8]
 
result = chop(listy)   # None
print result

