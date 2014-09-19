"""
Exercise 8.9. 

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1

    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    
    return True

Find and fix the  error in this function.

"""
#Answer: Line 10 should be: while j >= 0: