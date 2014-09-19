"""
Exercise 10.11
To check whether a word is in the word list, you could use the in operator, 
but it would be slow, because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a 
bisection search (also known as binary search), which is similar to what you 
do when you look a word up in the dictionary.

You start in the middle and check to see whether the word you are looking 
for comes before the word in the middle of the list. If so, then you search 
the first half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 
113,809 words, it will take about 17 steps to find the word or conclude that 
it's not there.

Write a function called bisect that takes a sorted list and a target value 
and returns the index of the value in the list, if it's there, or None if it's not.
Or you could read the documentation of the bisect module and use that!
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
        
        

fin = open("words.txt")
t = []
for line in fin:
    word = line.strip()
    t.append(word)

print bisect(t, "zymurgy")


    

