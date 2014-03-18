def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n-1)
    
def print_hello():
    print "hello"


do_n(print_hello, 5)