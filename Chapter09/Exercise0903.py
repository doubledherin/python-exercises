"""
Exercise 9.3

Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn't use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don't contain any of them. 

Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
"""
from string import ascii_lowercase

def avoids(word, forbidden):
    for c in word:
        if c in forbidden:
            return False
    return True
    
def avoids_modified():
    forbidden = raw_input("Enter a string of forbidden letters: ")
    count = 0
    
    fin = open('words.txt')
    
    for line in fin:
        flag = True
        word = line.strip()
        for c in word:            
            if c in forbidden:
                flag = False
        if flag:
            count += 1
    print count
"""
Below is the beginning of my attempt at the last question of this exercise. I find it really
difficult to solve without using lists or dictionaries or any fancy built-ins. I'd like to solve
it without that.
    
def five_rarest_forbidden():
    
    alpha = ascii_lowercase
    
    fin = open('words.txt')
    
    for i in range(len(alpha)):

        count = 0
   
        for line in fin:
            word = line.strip()
           
           
            for char in word:
                if char == alpha[i]:
                    print count
                    count += 1
                    print count
        #print "%s = %d" % (alpha[i], count)


five_rarest_forbidden()    

"""