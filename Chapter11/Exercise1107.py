"""
Exercise 11.7. 

Memoize the Ackermann function from Exercise 6.5 and see if memoization makes 
it possible to evaluate the function with bigger arguments. 

My Ackermann function from 6.5:

def ack(m, n):
    if m < 0 or n < 0:
        return "You can only use non-negative integers for this function."
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
        

print ack(4, 1) # return 125

# for larger values of m and n, we get at runtime error: maximum recursive depth exceeded.
"""
known = {}

def ack(m, n):
    if m < 0 or m < 0:
        return "You must use positive integers or 0."
    if m == 0:
        print m, n
        return n + 1
    if n == 0:
        print m, n
        return ack(m-1, 1)
    try: 
        return known[m, n]
    except KeyError:
        print m, n
        known[m, n] = ack(m - 1, ack(m, n-1))
        return known[m, n]
        
print ack(2, 1) #5