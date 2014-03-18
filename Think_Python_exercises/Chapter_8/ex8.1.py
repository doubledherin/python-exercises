"""
Write a function that takes a string as an argumetn adn displays the letters backward, one per line
"""

def reverse_string(s):
    newstring = ""
    index = -1
    for iter in range(len(s)):
        newstring += s[index]
        index -= 1
    print newstring
        
reverse_string('hello')
        