"""
Exercise 10.3

Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list, where the ith element is the sum of the first i + 1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

"""

def cumulative(t):

    # Helper function that takes a list t and creates a sublist of the first 
    # i items.
    def sublist(t, i):
        return t[0:(i)]

    res = []
    for i in range(1, len(t)+1):
        res.append(sum(sublist(t, i)))
    return res
    
print cumulative([1,2,3,4,5,6,7,8,9])    
