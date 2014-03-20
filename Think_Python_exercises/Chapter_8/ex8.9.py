"""
Find and fix the index error in the below function:

def is_reverse(word1, word2):
    
    # guardian code
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1
    
    while j > 0:
        
        # check for indexing error(s)
        print i, j
        
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    
    return True
"""
def is_reverse(word1, word2):
    
    # guardian code
    if len(word1) != len(word2):
        print False
        return
    
    i = 0
    j = len(word2) - 1
    
    # change ">" to ">=" so that "j" can reach 0
    while j >= 0:
        
        ## check for indexing error(s)
        # print i, j
        
        if word1[i] != word2[j]:
            print False
            return
        else:
            i += 1
            j -= 1
            
    print True

        
# is_reverse("hellodolly", "yllodolleh")