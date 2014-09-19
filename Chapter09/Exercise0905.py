"""
Exercise 9.5

Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. 

How many words are there that use all the vowels aeiou? How about aeiouy?
"""

def uses_all(word, required):
    for char in required:
        if char not in word:
            return False
    return True


fin = open("words.txt")

count_aeiou = 0
count_aeiouy = 0

for line in fin:
    word = line.strip()
    if uses_all(word, "aeiou"):
        count_aeiou +=1
    if uses_all(word, "aeiouy"):
        count_aeiouy +=1
        
print count_aeiou
print count_aeiouy    

