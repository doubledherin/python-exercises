"""
Write a function that takes a string and 
returns True if it is a palindrome and
False otherise."""

def is_palindrome(s):
    if len(s) <= 1:
        #print True
        return True
    if first(s) != last(s):
        #print False
        return False
    return is_palindrome(middle(s))
        
def first(word):
    return word[0]
    
def middle(word):
    return word[1:-1]
    
def last(word):
    return word[-1]
    

is_palindrome('hannah')

#is_palindrome('roller')