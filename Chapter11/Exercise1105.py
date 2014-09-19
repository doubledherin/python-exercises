"""
Exercise 11.5
Read the documentation of the dictionary method "setdefault" and use it to write a more concise version of invert_dict. 

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
    
Documentation on setdefault:

setdefault(key[, default])

If "key" is in the dictionary, return its value. 
If not, insert "key" with a value of "default" and return "default." 
"default" defaults to "None."

"""
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
        
    return inverse
    
d = {'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
print invert_dict(d)

