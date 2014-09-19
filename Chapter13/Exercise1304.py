"""
Exercise 13.4

Modify the previous program to read a word list (see Section 9.1) and then print 
all the words in the book that are not in the word list. 
How many of them are typos? 
How many of them are common words that should be in the word list, and how many of them are really obscure?
"""

"""
Exercise 13.3

Modify the program from the previous exercise to print the 20 most frequently used words in the book.
"""
import string

# take from results of previous exercise
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

# creates a list of words from a file 
# that contains all of the words
# permissible in a crossword
def wordlistList(filename):
    t = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

# takes a book file (filename1) and a 
# word list file (filename2) and prints the
# words in the book that are not in the list.
def weirdWordFinder(d1, filename2):
    book = stripdown(filename1)
    wordlist = wordlistList(filename2)
    for word in book:
        if len(word) > 1 and word not in wordlist:
            print word

weirdWordFinder("emma.txt", "words.txt")
     
