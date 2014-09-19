"""
Exercise 10.9
Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original. 

Hint: they don't have to be in the same order.
"""

def remove_duplicates(t):
    bad = []
    good = []
    while len(t) != 0:
        x = t.pop(0)
        if x in t:
            bad.append(x)
        elif x in bad:
            continue
        else:
            good.append(x)
    return good
            

    
print remove_duplicates([4,4,4,5,5,6,6,8,99,99,9]) # [8,9]
