"""
Rewrite the following program to take a third parameter--the index in word where it should start looking.

def find(word, letter):
    index = 0
    while index < len(world):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
"""
def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
    
find('lalapalooza', 'l', 3)