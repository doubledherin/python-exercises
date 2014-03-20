"""
ROT13 is a weak form of encryption that involves "rotating" each letter in a word by 13 places.
To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, 
so 'A' shifted by 3 is 'D' and 'Z' shifted by 1 is 'A'.

Write a function called rotate_word that takes a string and an integer as parameters, and that returns
a new string that contains the letters from the original string "rotated" by the given amount.

For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed".

You might want to sue the built-in functions 'ord', which convernts a character to a numeric code, 
and 'chr', which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13.
If you are not easily offended, find and decode some of them.
"""
import string

def rotate_word(s, i):
    
    encrypted = []
    
    for c in s:
        if c.islower():
            encrypted += string.lowercase[((string.lowercase).find(c) + i) % 26]
        elif c.isupper():
            encrypted += string.uppercase[((string.uppercase).find(c) + i) % 26]
        else:
            encrypted += c
    
    newstring = ''.join(encrypted)
    
    print newstring



def rot13_encoder(s):
    print rotate_word(s, 13)
    
def rot13_decoder(s):
    print rotate_word(s, -13)
    
    
# rotate_word("CHEERCHEER#$@%%!!!", 7)
# rot13_encoder("In the elevators, the extrovert looks at the OTHER guy's
# shoes.")
# rot13_decoder("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")