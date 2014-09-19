"""
Exercise 17.4
Write an add method for the Point class.
"""

class Point():
	"""Represents a point in 2D space."""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return "x = %g and y = %g." % (self.x, self.y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return x, y

point1 = Point(3.0, 4.0)
point2 = Point(1.0, 1.0)


if __name__ == "__main__":
	print point1 + point2


