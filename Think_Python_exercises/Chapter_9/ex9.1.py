"""
Write a program that reads words.txt (a complete list of 
legal crossword words) and prints only those that are 
longer than 20 characters (not including whitespace).
"""

fin = open('words.txt')
words = fin.readlines()

for word in words:
    if len(word.strip()) > 20:
        print word
