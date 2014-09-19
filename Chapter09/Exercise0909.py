"""
Exercise 9.9

Here's another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):

Recently I had a visit with my mom, and we realized that the two digits that make up my age when 
reversed resulted in her age. For example, if she's 73, I'm 37. 

We wondered how often this has happened over the years, but we got sidetracked with other topics 
and we never came up with an answer.

When I got home, I figured out that the digits of our ages have been reversible six times so far. 
I also figured out that if we,re lucky, it would happen again in a few years, and if we're really 
lucky, it would happen one more time after that. 

In other words, it would have happened 8 times over all. 

So the question is, how old am I now? 

Write a Python program that searches for solutions to this Puzzler. 

Hint: you might find the string method zfill useful.

"""
import string


                
def check_age_rev(x, y):
    x_str = "%02d" % x
    y_str = "%02d" % y
    
    if x_str == y_str[::-1]: 
        return True
    return False

def age_finder():
    for i in range(1, 100):
        age_son = string.zfill(str(i), 2)
        age_mom = age_son[::-1]
        delta = int(age_mom) - int(age_son)
        if delta > 10:
            count = 1
            son_init = int(age_son)
            mom_init = int(age_mom)
            son_next = 0
            mom_next = 0
            for time in range(mom_init, 121):
                son_next += 1
                mom_next += 1
                if check_age_rev(son_next, mom_next):
                    #print son_next, mom_next
                    count += 1
            if count == 8:
                print age_son, age_mom 
                
            
                                 
                    
            
#print check_age_rev(10, 10)           
age_finder()