"""
Exercise 17.5

Write an add method for Points that works with either a Point object or a tuple:

If the second operand is a Point, the method should return a new Point whose
x coordinate is the sum of the x coordinates of the operands, and likewise for 
the y coordinates.

If the second operand is a tuple, the method should add the first element of 
the tuple to the x coordinate and the second element to the y coordinate, and 
return a new Point with the result.
"""

class Point():
	"""Represents a point in 2D space."""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return "x = %g and y = %g." % (self.x, self.y)

	def __add__(self, other):
		if isinstance(other, Point):
			x = self.x + other.x
			y = self.y + other.y
			return x, y
		else:
			x = self.x + other[0]
			y = self.y + other[1]
			return x, y

point1 = Point(3.0, 4.0)
point2 = (1.0, 1.0)

if __name__ == "__main__":
	print point1 + point1	# 6.0, 8.0
	print point1 + point2	#4.0, 5.0

