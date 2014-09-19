"""
Exercise 13.3

Modify the program from the previous exercise to print the 20 most frequently used words in the book.
"""
import string

# taken and modified from my work in Exercise 11.2
def histogram(filename):
    t = stripdown(filename)
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
    
# Taken from my results for Exercise 11.5
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
        
    return inverse

def mostFrequentWords(filename, num=10):
    d = invert_dict(histogram(filename))
    t = d.items()
    t.sort(reverse=True)
    
    for i in range(num):
        print t[i][1]
    
        
    
mostFrequentWords("crime_and_punishment.txt", 20)
