"""
Exercise 9.8. 
Here's another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

"I was driving on the highway the other day, and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. 
So, if my car had 300,000 miles, for example, I'd see 3-0-0-0-0-0.
Now, what I saw that day was very interesting. I noticed that the last 4 digits weres palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.

One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. 

One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? 

One mile later, all 6 were palindromic!

The question is, what was on the odometer when I first looked?"

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements. 

Solution: http://thinkpython.com/code/cartalk2.py.
"""

def pal():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    # generates 6-digit numbers with last 4 being palindromes
                    
                    test = "%06d" % (int("%d%d%d%d%d%d" % (k,l,i,j,j,i)) + 1)
                    
                    # tests whether last 5 is a palindrome
                    if test[1:] == test[-1:0:-1]:
                        test2 = "%06d" % (int(test) + 1)
                        
                        # tests whether middle 4 is a palindrome
                        if test2[1:-1] == test2[-2:0:-1]:
                            test3 = "%06d" % (int(test2) + 1)
                            
                            # tests whether all 6 are a palindrome
                            if test3 == test3[::-1]:
                                print ((int(test)-1), test, test2, test3) 
                    
                    
                    
                    
    
        
pal()
        
        
        
        
        
        