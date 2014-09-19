"""
Exercise 10.6

Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. 

You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.

For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.
"""

def is_sorted(t):
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True
    
    
print is_sorted([1,2,2])      #True
print is_sorted(['b','a'])    #False
