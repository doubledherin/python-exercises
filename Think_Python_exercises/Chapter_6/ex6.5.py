"""
Write a function named ack that evaluates the Ackermann-Peter function. Use your function to evaluate (ack(3, 4), which should be 125. What happens for larger values of m and n?"""

def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
    return ack(m-1, ack(m,n-1))
    
ack(3, 4)