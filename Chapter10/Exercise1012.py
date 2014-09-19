"""
Exercise 10.12

Two words are a "reverse pair" if each is the reverse of the other. 
Write a program that finds all the reverse pairs in the word list. 

"""

def bisect(t, v):
    found = False
    start = 0
    stop = len(t)-1
    while start<=stop and not found:
        midpoint = (start+stop)//2
        if t[midpoint] == v:
            found = True
        elif t[midpoint] < v:
            start = midpoint + 1
        else:
            stop = midpoint - 1
    if found:
        return midpoint

def reverse_pair_finder(t):
    for item in t:
        reverse = item[::-1]
        if reverse == item:
            continue
        x = bisect(t, reverse)
        if x:
            print item, t[x]    
    
fin = open("words.txt")
t = []
for line in fin:
    word = line.strip()
    t.append(word)

reverse_pair_finder(t)
    