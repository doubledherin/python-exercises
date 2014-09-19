"""
Exercise 10.7

Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""

def is_anagram(s1, s2):
    
    if len(s1) != len(s2):
        return False
        
    s1_list = list(s1)
    s2_list = list(s2)
    
    for char in s1_list:
        if char in s2_list:
            s2_list.remove(char)
        else:
            return False
    return True

print is_anagram("12345", "13425")    #True
print is_anagram("12345", "1234")     #False
print is_anagram("", "abced")         #False
print is_anagram("santa", "satan")    #True