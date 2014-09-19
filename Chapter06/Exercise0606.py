"""
Exercise 6.6. 

A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider". 
Recursively, a word is a palindrome if the first and last letters are the same and the middle 
is a palindrome.

The following are functions that take a string argument and return the first, last, and middle letters:

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

We'll see how they work in Chapter 8.

1. Type these functions into a file named palindrome.py and test them out. 
What happens if you call middle with a string with two letters? 
One letter? What about the empty string, which is written '' and contains no letters?

2. Write a function called is_palindrome that takes a string argument and returns True if 
it is a palindrome and False otherwise. Remember that you can use the built-in function 
len to check the length of a string.
"""

"""
 Answers to #1: If you call middle with a two-letter string, you get an empty string. 
 Same with a one-letter string. If you middle with the empty string, you get a 
 runtime error: "IndexError: string index out of range."
"""

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        print True
        return True
    if s[0] == s[-1]:
        is_palindrome(s[1:-1]) 
    else:
        print False
        return False
            
is_palindrome("hello")
is_palindrome("amanaplanacanalpanama")
is_palindrome("hannah")
is_palindrome("a")
is_palindrome("aa")

    
    