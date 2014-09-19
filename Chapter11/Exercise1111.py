"""
Exercise 11.11

Here's another Puzzler from Car Talk: This was sent in by a fellow named Dan O'Leary. 
He came upon a common one-syllable, five-letter word recently that has the following 
unique property. When you remove the first letter, the remaining letters form a homophone 
of the original word, that is a word that sounds exactly the same. Replace the first letter, 
that is, put it back and remove the second letter and the result is yet another homophone 
of the original word. And the question is, what's the word?

... there is, however, at least one word that Dan and we know of which will yield two 
homophones if you remove either of the first two letters to make two, new four-letter 
words. The question is, what's the word?

Write a program that lists all the words that solve the Puzzler. 
"""

# Downloaded from http://thinkpython.com/code/pronounce.py.
def make_dictionary(filename):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d
# Taken from my results of Exercise 11.1
def dict_maker(filename):
    d = dict()
    t = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        t.append(word)
    for item in t:
        d[item] = len(item)
    return d

def isHomophone(word1, word2, phoneticDict):
    if word1 not in phoneticDict or word2 not in phoneticDict:
        return False
    return phoneticDict[word1] == phoneticDict[word2]

def parameterChecker(word, regularDict, phoneticDict):
    word2 = word[1:]
    if word2 not in regularDict:
        return False
    if not isHomophone(word, word2, phoneticDict):
        return False 
    word3 = word[0] + word[2:]
    if word3 not in regularDict:
        return False
    if not isHomophone(word, word3, phoneticDict):
        return False
    return True



    
phoneticDict = make_dictionary("pronouncingDictionary.txt")
regularDict = dict_maker("words.txt")

for word in regularDict:
    if len(word) != 5:
        continue
    if parameterChecker(word, regularDict, phoneticDict):
        print word, word[1:], word[0] + word[2:]


