"""
Exercise 12.5

Two words form a "metathesis pair" if you can transform one into the other by
swapping two letters; for example, "converse" and "conserve." Write a program that finds all of the metathesis pairs in the dictionary. 

Hint: don't test all pairs of words, and don't test all possible swaps. 
"""

# Takes a word string and sorts it
# for later use as a baseline word
def baseline(s):
    t = list(s)
    t.sort()
    base = "".join(t)
    return base
    
# Creates a dictionary with the baseline
# as a key and the list of words that are anagrams 
# of that baseline as a value
def anagram_maker(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        base = baseline(word)
        if base not in d:
            d[base] = [word]
        else:
            d[base].append(word)

    for wordlist in d.values():
        if len(wordlist) > 1:
            print wordlist

def metathesis_checker(filename):
    t = anagram_maker(filename)
    return t
            
                    
            


print metathesis_checker("words.txt")
#print baseline("conserve")   