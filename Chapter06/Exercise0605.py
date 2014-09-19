"""
Exercise 6.5. 
The Ackermann function, A(m, n), is defined:

A(m, n) =   n + 1                   if m = 0
            A(m - 1, 1)             if m > 0 and n = 0
            A(m - 1, A(m, n - 1))   if m > 0 and n > 0.
            
See http://en.wikipedia.org/wiki/Ackermann_function. 

Write a function named ack that evaluates Ackermann's function. Use your function to evaluate ack(3, 4), which should be 125. 

What happens for larger values of m and n? 
"""

def ack(m, n):
    if m < 0 or n < 0:
        return "You can only use non-negative integers for this function."
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
        
#ack(-1, 2)
#ack(0, 1)
print ack(3, 4)
print ack(2, 1)

# for larger values of m and n, we get at runtime error: maximum recursive depth exceeded.