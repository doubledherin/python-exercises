"""
Exercise 11.9. 

If you did Exercise 10.8, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates. 

def has_duplicates(t):
    sorted_list = sorted(t)
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return True
    return False
"""

def has_duplicates(t):
    d = {}
    for item in t:
        if item in d:
            return True
        else:
            d[item] = None
    return False
    
    

print has_duplicates([1, 2, 3, 4]) # False
print has_duplicates([1, 2, 3, 4, 1]) # True