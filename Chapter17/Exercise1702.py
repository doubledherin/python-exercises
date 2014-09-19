"""
Exercise 17.2
Write an init method for the Point class that takes x and y as optional parameters
and assigns them to the corresponding attributes.
"""

class Point():
	"""Represents a point in 2-D space."""
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y