"""
Exercise 11.10. 

Two words are "rotate pairs" if you can rotate one of them and get the other (see rotate_word in Exercise 8.12). Write a program that reads a wordlist and finds all the rotate pairs. 

def rotate_word(s, n):
    new = ""
    for c in s:
        new += chr(ord(c) + n)
    return new
        
"""

def rotate_pair_finder(wordlist, rotation):
    d = {}
    fin = open(wordlist)
    for line in fin:
        word = line.strip()
        d[word] = None
    newlist = []
    for key in d:
        newword = ""
        for char in key:
            newword += chr(ord(char) + rotation)
        if newword in d:
            newlist += [(key, newword)]
    return newlist

    

print rotate_pair_finder("words.txt", 13) 
print rotate_pair_finder("words.txt", 1)
            
    
        