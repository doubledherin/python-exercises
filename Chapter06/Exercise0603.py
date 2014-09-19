"""
Exercise 6.3. 

Write a function is_between(x, y, z) that returns True if x <= y <=z or False otherwise.
"""

def is_between(x, y, z):
    return x <= y and y <= z

print is_between(1,2,3) #True
print is_between(3,2,3) #False
print is_between(0,0,0) #True
print is_between(3,2,1) #False
print is_between(1,2,-4) #Fals
