"""
Exercise 10.4

Write a function called middle that takes a list and returns a new list 
that contains all but the first and last elements. 
So middle([1,2,3,4]) should return [2,3].

"""
def middle(t):

    return t[1:-1]
    

listy = [1,2,3,4,5,6,7,8] 

print middle(listy)   # [2,3,4,5,6,7]