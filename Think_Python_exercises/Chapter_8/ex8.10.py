"""
A string slice can take a third index that specifies the "step size;" that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

>>> fruit = 'banana'
>>> fruit [0:5:2]
'bnn'

A step size of -1 goes through the word backwards, so the slice [::1] generates a reversed string.

Use this idiom to write a one-line version of is_palindrome from Exercise 6.6.

Here is Exercise 6.6's version: 

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
    
"""
str1 = "hannah"
str2 = "wendy"
print str1 == str1[::-1]
print str2 == str2[::-1]