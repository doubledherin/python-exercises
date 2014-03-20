"""
The following functions are all *intended* to check whether a stirng contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
"""
# for each letter in 's', prints False if the letter is *not* a lowercase letter
# and True if it's a lowercase letter. White space, digits, and punctuation 
# and other characters return False.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            print True
        else:
            print False

# for each letter in the length of 's', prints 'True',
# because it's checking if the string 'c' is lowercase
# not if the letter in 's' is lowercase.            
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            print 'True'
        else:
            print 'False'

# for each letter in the length of 's', assigns 'True' to 'flag' if
# the letter is lowercase; 'False' to 'flag' if the letter is uppercase.
# because the value of 'flag' changes for each letter in 'c', the final value
# of flag is the only one that is printed/returned.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    print flag
    
# does the same as 'any_lowercase3' -- that is, it prints/returns only whether
# the last letter in 's' is upper- or lowercase -- but in a different manner. 
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    print flag

# for each letter in 'c', prints whether True if that letter is lowercase and 
# False if that letter is uppercase. Then prints True, for no reason.    
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            print False
    print True
    
#any_lowercase1("Hello! ")
#any_lowercase2("HELLO")
#any_lowercase3("HELLo")
#any_lowercase4("HELLo")
#any_lowercase5("HELLO")
