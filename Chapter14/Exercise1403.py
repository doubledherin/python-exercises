"""
Exercise 14.3

If you download my solution to Exercise 12.4 from http://thinkpython.com/code/anagram_sets.py, 
you'll see that it creates a dictionary that maps from a sorted string of letters to the list 
of words that can be spelled with those letters. For example, 'opst' maps to the list 
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions: store_anagrams should 
store the anagram dictionary in a "shelf;" read_anagrams should look up a word and return a 
list of its anagrams. 
"""
import shelve
import sys

from Exercise1204 import *

# Note: This was mostly taken from the solution provide by the author.
# For this exercise, little preliminary explanation was given.
# I felt I could learn more by studying and implementing the author's solution.
def store_anagrams(filename, d):
    """Stores the anagrams in d on a shelf.
    
    filename: filename of shelf, formatted as a string
    d: dictionary that maps strings to a list of anagrams
    """
    
    shelf = shelve.open(filename, "c")
    for word, anagrams in d.iteritems():
        shelf[word] = anagrams

    shelf.close()
    
def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.
    
    
    filename: string file name of shelf
    word: word to look up
    
"""
    shelf = shelve.open(filename)
    base = baseline(word)
    
    try:
        return shelf[base]
    except KeyError:
        return []

dictionary_of_anagrams = anagram_maker("words.txt")
store_anagrams("shelved_anagrams.txt", dictionary_of_anagrams)
print read_anagrams("shelved_anagrams.txt", "converse")
    