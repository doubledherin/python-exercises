"""
Exercise 5.5. Read the following function and see if you can figure out what it does. Then run it (see the examples in Chapter 4).

"""
try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *



world = TurtleWorld()
bob = Turtle()
#bob.delay = 0.01

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    
    draw(t, length, n-1)
    
    rt(t, 2*angle)
    
    draw(t, length, n-1)
    
    lt(t, angle)
    
    bk(t, length*n)

draw(bob, 5, 10)

wait_for_user()