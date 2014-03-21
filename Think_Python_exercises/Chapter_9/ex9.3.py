"""
Write a function named 'avoids' that takes a word and a string of forbidden letters, and that returns True if the word doesn't use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don't contain any of them. 

Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
"""
import string


def avoids(word, letters):
    for c in letters:
        if c in word:
            print False
            return
    print True
    return
    
    
            
def avoids_modified():
    
    while True:
        print "Please enter a string of forbidden letters (no non-alpha characters): "
        forbidden = (raw_input()).lower()
        
        if forbidden.isalpha() == False:
            continue
        break
    
    fin = open("words.txt")
    words = fin.readlines()
    
    forbidden_list = []
    permitted_list = []
    
    for word in words:
        word = word.strip()
        for letter in forbidden:
            # print "trying letter", letter, "in", word
            if letter in word:
                # print word, "is forbidden because it contains", letter
                forbidden_list += [word]
                # print "forbidden list now contains", word
                break
            else:
                if letter == forbidden[-1]:
                    permitted_list += [word]
                    # print "permitted list now contains", word
                    break
    
    print permitted_list
    

# a function that finds a 5-letter string of 'forbidden' letters
# that excules the smallest number of words from teh wordlist
def rare_forbidden():
    
    fin = open("words.txt")
    words = fin.readlines()

    # populate an empty dictionary with each letter of the alphabet
    # as a key with a 0 value
    d = {}
    for c in string.lowercase:
        d[c] = 0

    # replace the 0 values with the number of times each key's letter
    # appears in the wordlist
    for c in string.lowercase:    
        for word in words:
            d[c] += word.count(c)
    
    # invert the key-value pairs
    inverse = {}
    for key in d:
        value = d[key]
        if value not in inverse:
            inverse[value] = key
        else:
            inverse[value].key(append)
        
    # turn the dictionary into a sorted list of tuples
    t = inverse.items()
    t.sort()
    
    # get the first 5 in the list
    short = t[0:5]
    
    # create a list of just the letters in the 5-item list
    forbidden = []
    for pair in short:
        forbidden += [pair[1]]
    
    # smash list into a string
    forbidden = ''.join(forbidden)
    
    # pasted chunk of code from the above 'avoids_modified' function,
    # which separates wordlist into forbidden and permitted words
    forbidden_list = []
    permitted_list = []
    for word in words:
        word = word.strip()
        for letter in forbidden:
            # print "trying letter", letter, "in", word
            if letter in word:
                # print word, "is forbidden because it contains", letter
                forbidden_list += [word]
                # print "forbidden list now contains", word
                break
            else:
                if letter == forbidden[-1]:
                    permitted_list += [word]
                    # print "permitted list now contains", word
                    break
    print len(forbidden_list)
    
rare_forbidden()    