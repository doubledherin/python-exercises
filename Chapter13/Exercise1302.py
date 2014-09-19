"""
Exercise 13.2

Go to Project Gutenberg (http://gutenberg.org) and download your favorite
out-of-copyright book in plain text format.

Modify your program from the previous exercise to count the total number of words 
in the book, and the number of times each word is used.

Print the number of different words used in the book. 
Compare different books by different authors, written in different eras. 
Which author uses the most extensive vocabulary?
"""
import string

# taken and modified from my work in Exercise 11.2
def histogram(t):
    d = dict()
    for item in t:
        d[item] = d.get(item, 0) + 1
    return d


def stripdown(filename):
    
    bookString = ""
    fin = open(filename)
    
    for line in fin:            
        line = line.lower()
        line = line.replace("--", " ")
        line = line.replace("-", " ")
        line = line.replace("\n", " ")
        for c in string.punctuation:
            line = line.replace(c, "")
        bookString += line
    
    bookList = bookString.split()
    return bookList

def uniqueWords(filename):
    t = stripdown(filename)
    d = histogram(t)
    n = len(d.items())
    return n
    
print len(stripdown("crime_and_punishment.txt"))          #203,331 words total
print histogram(stripdown("crime_and_punishment.txt"))
print uniqueWords("crime_and_punishment.txt")             #9,456 unique words

print len(stripdown("emma.txt"))                          #160,991 words total
print histogram(stripdown("emma.txt"))
print uniqueWords("emma.txt")                             #7,158 unique words
