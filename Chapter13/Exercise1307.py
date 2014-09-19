"""
Exercise 13.7

An obvious improvement on exercise 13.5 is to build the list once and then make multiple selections, 
but the list is still big.

An alternative is:
1. Use keys to get a list of the words in the book.           # did that already
2. Build a list that contains the cumulative sum of the word frequencies (see Exercise 10.3). The last 
item in this list is the total number of words in the book, n.
3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10.11) to find the index 
where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.

Write a program that uses this algorithm to choose a random word from the book. 

"""
from __future__ import division
import random, string


#Gets a histogram of word frequencies
def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

#Helper function for process_file
def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


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


    
# get cumulative list of values, where final value is total no. words
def cumulativeList(d):
    # helper
    def sublist(t, i):
        return t[0:(i)]

    word_frequencies = d.values()

    cumList = []
        
    for i in range(1, len(word_frequencies)+1):
        cumList.append(sum(sublist(word_frequencies, i)))
        
    return cumList
            




def choose_from_hist(d):
    t = d.keys()
    c = cumulativeList(d)
    n = c[-1]
    r = random.randint(0, n)
    index = bisect(c, r)
    result = t[index]
    probability = (emma.get(result))/n
    print probability

    print "The word '" + result + "' was chosen randomly with a probability of %g." % probability
    
emma = process_file("emma.txt")

print choose_from_hist(emma)


    
    
    
    
    