"""
Encapsulate the following code in a function and generalize it so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count
"""
from sys import argv
print argv

def count(s, l):
    counter = 0
    i = 0
    for letter in s:
        if l == s[i]:
            counter += 1
        i += 1
    print counter

count('apple', 'p')