"""
Exercise 8.5. 

The following program counts the number of times the letter a appears in a string:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count

This program demonstrates another pattern of computation called a counter. 
The variable count is initialized to 0 and then incremented each time an a is
found. When the loop exits, count contains the result--the total number of a's.

Encapsulate this code in a function named count, and generalize it so that it
accepts the string and the letter as arguments.

"""

def count(s, l):
    count = 0
    for char in s:
        if char == l:
            count += 1
    print count
    return count
    

count("happy birthday to you.", "p")
count("happy birthday to you.", "o")
count("happy birthday to you.", "x")