"""
In 1939 Ernest Vincent Wright published a 50,000 word novel called 
Gadsby that does not contain the letter 'e'. Since 'e' is the most 
common letter in English, that's not easy to do.

Write a function called has_no_e that returns True if the given word 
doesn't have the letter 'e' in it.

Modify your program from the previous section (ex9.1) to print only 
the words that have no 'e' and computer the percentage of the words 
in the list that have no 'e'.

***
Here is my program from ex9.1:

fin = open('words.txt')
words = fin.readlines()

for word in words:
    if len(word.strip()) > 20:
        print word
        
"""

def has_no_e(s):
    print s.count("e") == 0

#has_no_e("hello1")
#has_no_e("zymurgy1")

def wordlist_e_crawler():
    
    fin = open('words.txt')
    words = fin.readlines()

    newlist = []
    for word in words:
        if word.count("e") == 0:
            newlist += [word.strip()]

    print "%d percent of the words in the wordlist have no 'e'." % (float(len(newlist)) / len(words) * 100)


wordlist_e_crawler()
    

    