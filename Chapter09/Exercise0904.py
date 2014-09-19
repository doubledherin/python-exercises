"""
Exercise 9.4

Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. 

Can you make a sentence using only the letters acefhlo? 
Other than 'Hoe alfalfa?'

"""
def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True
    
fin = open("words.txt")

for line in fin:
    word = line.strip()
    if uses_only(word, "acefhlo"):
        print word

#All cochleae leech fecal fleece.