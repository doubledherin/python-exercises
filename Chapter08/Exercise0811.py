"""
Exercise 8.11

The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
"""
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
"""            
Incorrect.
The above returns False as soon as it see an uppercase letter. So even if there is a lowercase letter later on, it will never find it.
"""         
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
"""            
Incorrect.
The above checks to see if the letter 'c' itself is lowercase (as opposed to checking each character c in the string). It will always return True, no matter what string you give it.
"""         
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
"""            
Incorrect.
The above returns only the Boolean that applies to whether the last character in the string is lowercase.
"""
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
"""            
Correct.

The above initiates flag as False. While iterating, when we hit a lowercase
letter, flag gets set to True, and because the flag update uses an "or", it 
will be True until the end, even if we later hit uppercase letters.
"""        
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
"""            
Incorrect.
The above function checks to see whether ALL characters are lowercase.
"""
s = "HELlO"

print any_lowercase1(s)  # False; incorrect
print any_lowercase2(s)  # True; incorrect  
print any_lowercase3(s)  # False; incorrect
print any_lowercase4(s)  # True; correct
print any_lowercase5(s)  # False; incorrect