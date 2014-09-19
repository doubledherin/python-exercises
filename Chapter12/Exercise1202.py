"""
Exercise 12.2

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    
    res = []
    for length, word in t:
        res.append(word)
    return res

In this example, ties are broken by comparing words, so words with the same length appear in reverse alphabetical order. 

For other applications you might want to break ties at random.
Modify this example so that words with the same length appear in random order. 

Hint: see the random function in the random module. 
"""
import random

def sort_by_lengthModified(words):
    t = []
    for word in words:
        t.append((len(word), random.randint(0, len(words)), word))
    t.sort(reverse=True)

    res = []
    for length, randy, word in t:
        print length, randy, word
        res.append(word)
    return res
            
            
t = ["apple", "no", "yes", "bag", "banana", "chuckle", "doggie", "eatery", "French", "french", "pickle"]

print sort_by_lengthModified(t)