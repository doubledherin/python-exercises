"""
Exercise 13.1
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.

Hint: The string module provides strings named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters. 

Let's see if we can make Python swear:
>>> import string
>>> print string.punctuation
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
Also, you might consider using the string methods strip, replace and translate.
"""
import string

def stripdown(filename):
    fin = open(filename)
    for line in fin:            
        line = line.strip().lower()
        line = line.replace("--", " ")
        for c in string.punctuation:
            line = line.replace(c, "")
        print line


stripdown("emma.txt")


