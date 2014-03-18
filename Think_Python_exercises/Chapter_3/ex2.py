def print_grid():
    plus = " + "
    minuses = " - " * 4
    pipe = " | "
    blanks = "   " * 4
    horizontal = plus + ((minuses + plus) * 4) + "\n"
    verticals = (pipe + ((blanks + pipe) * 4) + "\n") * 4
    print (horizontal + verticals) * 4 + horizontal
        
print_grid()
