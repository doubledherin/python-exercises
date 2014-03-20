"""
Rewrite exercise 8.5 so that instead of traversing the string, 
it uses the three-parameter version of 'find' from the ex8.4.py.


def count(s, l):
    counter = 0
    i = 0
    for letter in s:
        if l == s[i]:
            counter += 1
        i += 1
    print counter
"""    
    
def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
    
# find('lalapalooza', 'l', 3)

