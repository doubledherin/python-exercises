"""A number, a, is a power of b if it is divisible by b and if 
a/b is a power of b. Write a function called is_power that takes
parameters a and b and returns True if a is a power of b. 
Note: You will have to think about the base case."""

def is_power(a, b):
    if a == b:
        # print True
        return True
    if a % b == 0:
        is_power(a/b, b)
    else:
        # print False
        return False

is_power(16, 16)