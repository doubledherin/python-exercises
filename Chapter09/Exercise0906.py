"""
Exercise 9.6

Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). 

How many abecedarian words are there?
"""

def is_abecedarian(word):
    for i in range(len(word)-1):
            if word[i] > word[i+1]:
                return False
    return True
        

#print is_abecedarian("ace")   #True
#print is_abecedarian("hello") #False
#print is_abecedarian("zace")  #False

fin = open("words.txt")
count = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
print count

#Result: There are 596 words that are abecedarian.
    