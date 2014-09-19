"""
Exercise 8.1. Write a function that takes a string as an argument and displays the letters backward, one per line.
"""

def mirror(s):
    for i in range(1, len(s)+1):
        print s[-i]
    
mirror("holy moly schnestoly")