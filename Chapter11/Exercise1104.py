"""
Exercise 11.4

Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none.

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError
    
"""


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
    
def reverse_lookup(d, v):
    t = []
    for k in d:
        if d[k] == v:
            t.append(k)
    if t == []:
        raise ValueError
    return t
    
    
s = "brontosaurus"

print reverse_lookup(histogram(s), 2) # ["r", "o", "s" "u"]

