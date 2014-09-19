"""
Exercise 13.6

Python provides a data structure called set that provides many common set operations. Read the documentation at http://docs.python.org/2/library/stdtypes.html#types-set and write a program that uses set subtraction to find words in the book that are not in
the word list. 
"""

import string



def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist
    
def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def weirdWordFinder(d1, d2):
    s1 = set(d1)
    s2 = set(d2)
    s3 = s1 - s2
    return s3
    
    


bookDict = process_file("crime_and_punishment.txt")
wordDict = process_file("words.txt")
print weirdWordFinder(bookDict, wordDict)


    