"""
Exercise 18.1
Write a __cmp__ method for Time objects. 

Hint: you can use tuple comparison, but you also might consider using 
integer subtraction.
"""

class Time():
	"""Represents the time of day.

	attributes are hour, minute and second
	"""

	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self. minute = minute
		self.second = second

	def __cmp__(self, other):
		time1 = self.hour, self.minute, self.second
		time2 = other.hour, other.minute, other.second
		return cmp(time1, time2)

t1 = Time(12, 58, 59)
t2 = Time(12, 59, 0)

if __name__ == "__main__":
	print t1 > t2   # False
	print t1 < t2   # True
	print t1 == t2  # False
	print t1 != t2  # True


