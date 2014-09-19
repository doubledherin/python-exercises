"""
Exercise 11.6

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

known is a dictionary that keeps track of the Fibonacci numbers we already know. It starts with two items: 0 maps to 0 and 1 maps to 1.

Whenever fibonacci is called, it checks known. If the result is already there, it can return immediately. Otherwise it has to compute the new value, add it to the dictionary, and return it.

Run this version of fibonacci and the original with a range of parameters and
compare their run times.
"""
import time

known = {0:0, 1:1}

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
def fibonacciMemo(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


# processing time is 3.2e-05 seconds
t0 = time.clock()
print fibonacci(5)
print time.clock() - t0, "seconds to compute fibonacci(5)"

# processing time is 9e-06 seconds
t0 = time.clock()
print fibonacciMemo(5)
print time.clock() - t0, "seconds to compute fibonacciMemo(5)"

# processing time is 5e-05 seconds
t0 = time.clock()
print fibonacci(10)
print time.clock() - t0, "seconds to compute fibonacci(10)"

# processing time is 6e-05 seconds
t0 = time.clock()
print fibonacciMemo(10)
print time.clock() - t0, "seconds to compute fibonacciMemo(10)"

# processing time is 0.000489 seconds 
t0 = time.clock()
print fibonacci(15)
print time.clock() - t0, "seconds to compute fibonacci(15)"

# processing time is 0.000453
t0 = time.clock()
print fibonacciMemo(15)
print time.clock() - t0, "seconds to compute fibonacciMemo(15)"

# processing time is 0.000489 seconds 
t0 = time.clock()
print fibonacci(58)
print time.clock() - t0, "seconds to compute fibonacci(58)"

# processing time is 0.000453
t0 = time.clock()
print fibonacciMemo(58)
print time.clock() - t0, "seconds to compute fibonacciMemo(58)"