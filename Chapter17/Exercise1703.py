"""
Exercise 17.3. Write a str method for the Point class. 
Create a Point object and print it.
"""

class Point():
	"""Represents a point in 2D space."""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return "x = %g and y = %g" % (self.x, self.y)


point = Point(3.5, 4.0)
print point
