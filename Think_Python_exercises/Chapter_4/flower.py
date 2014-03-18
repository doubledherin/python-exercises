from swampy.TurtleWorld import *
import math
from ex4_3 import *

def petal(t, r, angle):
    """Uses a turtle (t) to draw a petal using two arcs with radius r and with a given angle that subtends the arcs"""
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower():
    petal(bob, 100, 90)
#arc(bob, 100, 90)
#lt(bob, 90)
"""arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
arc(bob, 200, 90)
lt(bob, 90)
"""


wait_for_user()





    



