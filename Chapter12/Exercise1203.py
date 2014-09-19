"""
Exercise 12.3

Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Find text samples from several different languages 
and see how letter frequency varies between languages. 

Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. 

"""
import string



# helper function; taken from my exercise 11.5
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
        
    return inverse

# helper function, to allow for large strings
# such as a novel
def string_maker(filename):
    """reads a file of words and consolidates the contents into one big string."""
    bigstring = ""
    badstring = string.punctuation + "0123456789"
    fin = open(filename)
    for line in fin:
        t = []
        line = line.strip()
        for char in line:
            if char in badstring:
                continue
            char = char.lower()
            t.append(char)
        for char in t:
            if char in badstring:
                t.remove(char)
        s = ""
        for item in t:
            s += item
        bigstring += s
    return bigstring

def most_frequent(filename):
    s = string_maker(filename)
    d = {}
    for char in s:
        if char not in d:
            d[char] = 0
        else:
            d[char] += 1
    inverse = invert_dict(d)
    t = inverse.items()
    t.sort(reverse=True)
    freqString = ""
    for item in t:
        for letter in item[1]:
                freqString += letter
    return freqString
            
# French: eastinrluodcmpvbhfqgxjyzwk
# This is similar but not exact when compared with wikipedia's writeup
print most_frequent("madamebovary.txt") 

# English: etaonishrdlumwcyfgbpvkxjqz; similar but not
# exact when compared with wikipedia's writeup
print most_frequent("emma.txt") 