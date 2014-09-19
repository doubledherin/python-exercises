"""
Exercise 10.8

The (so-called) Birthday Paradox:

1. Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

2. If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. 

Hint: you can generate random birthdays with the randint function in the random module.

You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox.
"""
import random

# Question 1
def has_duplicates(t):
    sorted_list = sorted(t)
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return True
    return False
    

#print has_duplicates([1,2,3,4,5,1])   #True
#print has_duplicates([1,2,3,4,5])   #False
#print has_duplicates(["hey", [1,2,3], "hey", 4,5,6]) #True 

# Question 2. Takes a number of people n and returns the chances that two
# of those people have the same birthday.
# Assuming a uniform distribution of birthdays (even though that's not
# the case in reality)

# Helper function that repeats a Boolean-returning f function 100 times 
# and returns a percentage of times it returns True
def odds_checker(f):
    count = 0
    for i in range(1000):
        if f():
            count += 1
    return count/1000.0
    
def same_birthday_chances():
    days_of_year = []
    for i in range(23):
        days_of_year.append(random.randint(1, 365))
    print days_of_year
    return has_duplicates(days_of_year)

print odds_checker(same_birthday_chances)