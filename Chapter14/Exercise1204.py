"""
Exercise 12.4

1. Write a program that reads a word list from a file and prints all the sets of words that are anagrams.

Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a set of letters to a list of words that 
can be spelled with those letters. The question is, how can you represent the set of letters in a way 
that can be used as a key?

2. Modify the previous program so that it prints the largest set of anagrams first, followed by the 
second largest set, and so on.

3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, 
to form an eight-letter word. What set of 8 letters forms the most possible bingos?
Hint: there are seven.

"""

##############Question 1###################

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
    return d
    
#print anagram_maker("words.txt")

##############Question 2###################
    
# Creates a dictionary with the baseline
# as a key and the list of words that are anagrams 
# of that baseline as a value

# Then sorts the sets of anagrams according to their 
# word length
def anagram_makerModified(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        base = baseline(word)
        if base not in d:
            d[base] = [word]
        else:
            d[base].append(word)

    sortedAnagramSets = []
    allAnagramSets = d.values()
    for anagramSet in allAnagramSets:
        sortedAnagramSets.append((len(anagramSet), anagramSet))
    sortedAnagramSets.sort(reverse=True)
    
    for item in sortedAnagramSets:
        if item[0] > 1:
            print item[1]
           
#anagram_makerModified("words.txt")

##############Question 2###################
"""
3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, 
to form an eight-letter word. What set of 8 letters forms the most possible bingos?
Hint: there are seven.
"""
  
def bingoBuster(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        if len(word) != 8:
            continue
        base = baseline(word)
        if base not in d:
            d[base] = [word]
        else:
            d[base].append(word)

    sortedAnagramSets = []
    allAnagramSets = d.values()
    for anagramSet in allAnagramSets:
        sortedAnagramSets.append((len(anagramSet), anagramSet))
    sortedAnagramSets.sort(reverse=True)
    
    max = 2
    eightLetterAnagramMax = []
    for item in sortedAnagramSets:
        if item[0] > max:
            max = item[0]
            eightLetterAnagramMax.append(item[1])
    return eightLetterAnagramMax[0]

print bingoBuster("words.txt")
# ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest']        