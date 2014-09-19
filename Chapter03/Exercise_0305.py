"""
Exercise 3.5. 

This exercise can be done using only the statements and other features we have learned so far.

1. Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated sequence:

print '+', '-'

If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.

print '+',
print '-'

The output of these statements is '+ -'.

A print statement all by itself ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns

"""

# Item no. 1
# ----------
p = " +"
m = " -"    
l = " |"
s = "  "
hseg = (p + m * 4) 
vseg = (l + s * 4) 


def draw_4box_grid():
    for i in range(2):
        print hseg * 2 + p 
        for i in range(3):
            print vseg * 2 + l
    print hseg * 2 + p
    
draw_4box_grid()

# Item no. 2
# ----------

def draw_16box_grid():
    for i in range(4):
        print hseg * 4 + p 
        for i in range(3):
            print vseg * 4 + l
    print hseg * 4 + p

    
draw_16box_grid()

    
