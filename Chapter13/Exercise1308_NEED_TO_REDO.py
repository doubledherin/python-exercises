"""
Exercise 13.8. 

Markov analysis:

1. Write a program to read a text from a file and perform Markov analysis. 
The result should be a dictionary that maps from prefixes to a collection of possible suffixes. 
The collection might be a list, tuple, or dictionary; it is up to you to make an appropriate choice. 
You can test your program with prefix length two, but you should write the program in a way that makes it easy
to try other lengths.

2. Add a function to the previous program to generate random text based on the Markov analysis. 
Here is an example from Emma with prefix length 2:

    He was very clever, be it sweetness or be angry, ashamed or only amused, at
    such a stroke. She had never thought of Hannah till you were never meant
    for me?" "I cannot make speeches, Emma:" he soon cut it all himself.

For this example, I left the punctuation attached to the words. The result is almost syntactically correct, 
but not quite. Semantically, it almost makes sense, but not quite. What happens if you increase the prefix 
length? Does the random text make more sense?

3. Once your program is working, you might want to try a mash-up: if you analyze text from two or more books, 
the random text you generate will blend the vocabulary and phrases from the sources in interesting ways.

"""
from __future__ import division
import random, string

# Taken from my exercise 13.5.
# Creates a list of words ("bookList")
# in the order they appeared in the file, with 
# whitespace and punctuation stripped out.
def process_file(filename):
    
    bookString = ""
    fin = open(filename)
    
    for line in fin:            
        line = line.lower()
        line = line.replace("--", " ")
        line = line.replace("\n", " ")

        #line = line.replace("-", " ")   #leaving in punctuation
        #for c in string.punctuation:    #leaving in punctuation
         #   line = line.replace(c, "")
        bookString += line
    
    bookList = bookString.split()
    return bookList


# Takes a processed file (see above) and returns a dictionary d
# where the key is a two-word combination found 
# in the file ("prefixes") and the value is a list
# of each word(s) that follows that prefix ("suffixes").       
def prefix_suffix(filename):
    d = {}
    listed_words = process_file(filename)
    num_words = len(listed_words)
    for i in range(0, (num_words - 2)):
        
        prefix = (listed_words[i], listed_words[i+1])
        

        suffix = (listed_words[i + 2])
        
        if prefix not in d:
            d[prefix] = [suffix]
        else:
            d[prefix].append(suffix)
    return d

# Get cumulative list of values, where final value is total no. prefixes
# Modified from my exercise 13.7
def cumulativeList(d):
    # helper
    def sublist(t, i):
        return t[0:(i)]

    prefix_frequencies = d.values()

    cumList = []
        
    for i in range(1, len(prefix_frequencies)+1):
        cumList.append(sum(sublist(prefix_frequencies, i)))
        
    return cumList
    
# do a binary search and return an index where found
def bisect(t, v):
    found = False
    start = 0
    stop = len(t)-1
    while start<=stop and not found:
        midpoint = (start+stop)//2
        if t[midpoint] == v:
            found = True
        elif t[midpoint] < v:
            start = midpoint + 1
        else:
            stop = midpoint - 1
    if found:
        return midpoint
    else:
        return midpoint + 1

def random_text_generator(filename):
    d = prefix_suffix(filename)
    
    # Change histogram back to a list of prefixes
    # Taken from my exercise 13.7
    list_of_prefixes = d.keys()
    num_prefixes = len(list_of_prefixes)
    
    for i in range(100):
        index = random.randint(0, num_prefixes-1)
        prefix = list_of_prefixes[index]
        no_of_suffixes = len(d[prefix])
        if no_of_suffixes == 1:
            print prefix[0], prefix[1], d[prefix][0],
        else:
            random_suffix = random.randint(0, no_of_suffixes-1)
            print prefix[0], prefix[1], d[prefix][random_suffix][0],
    return
            
        
    
#num_words = len(process_file("emma.txt"))    
#print random_text_generator("emma.txt")    
num_words = len(process_file("crime_and_punishment.txt"))    
print random_text_generator("crime_and_punishment.txt")