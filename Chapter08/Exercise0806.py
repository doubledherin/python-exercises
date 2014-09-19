"""
Exercise 8.6 

Rewrite the below count function so that instead of traversing the string, 
it uses the three-parameter version of the find function.

def count(s, l):
    count = 0
    for char in s:
        if char == l:
            count += 1
    print count
    return count
    
def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            print index
            return index
        index += 1
    print("-1")
    return -1

"""

def count(s, l, i):
    count = 0
    while i < len(s):
        if s[i] == l:
            count += 1
        i += 1
    print count

count("aaaaa", "a", 3)      # 2
count("aaaaa", "b", 2)      # 0
count("zzzaa.", "z", 2)     # 1