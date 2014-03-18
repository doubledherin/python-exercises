from swampy.TurtleWorld import *
import math


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, n, length):
    """
    Uses a turtle (t) to draw a regular polygon with n sides, each with given length.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def circle(t, r):
    """
    Uses a turtle (t) to draw a circle with radius r
    """
    arc(t, r, 360)

def arc(t, r, angle):
    """
    Uses a turtle (t) to draw an arc with radius r and
    with length as a fraction of a circle (angle/360)
    """    
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle)/ n
    lt(t, step_angle/2)
    
    polyline(t, n, step_length, step_angle)
        
    rt(t, step_angle/2)            
            
def polyline(t, n, length, angle):
    """
    Uses a turtle (t) to draw n line segments with the 
    given length and angle (in degrees) between them
    """
    
    for i in range(n):
        fd(t, length)
        lt(t, angle)
    
