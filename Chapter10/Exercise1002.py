"""
Exercise 10.2

Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized. 

"""
# Takes a nonnested list of strings t and returns a new list res with each
# string initial capped.
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    #print res
    return res

# Takes a list and returns a Boolean as to whether
# it contains at least one nested list.
def is_nesty(nlist):
    for item in nlist:
        if type(item) == list:
            return True
    return False

# Takes a list that contains strings and/or nested lists
# of strings, and returns a new equivalently nested list
# with each string initial capped.
def capitalize_nested(nlist): 
    
    # if nlist is actually a string, return it capitalized.
    if type(nlist) == str:
        return nlist.capitalize()
        
    # if the list contains no nested lists, return that list
    # with each item (string) initial capped    
    elif not is_nesty(nlist):
        return capitalize_all(nlist)
    
    # if the list contains at least one nested list,
    # recurse for each element.
    else:
        result = []       
        for elem in nlist:
            result.append(capitalize_nested(elem))
        
    return result
    
test = ["hey.", "i'm", ["a", "nested", ["list", "of"]], "strings"]

print capitalize_nested(test)






