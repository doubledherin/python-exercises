"""
Exercise 16.2

Write a boolean function called is_after that takes two Time objects, t1 and t2,
and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don't use an if
statement.
"""
class Time():
	"""Represents the time of day.

	attributes: hour, minute, second
	"""

def is_after(t1, t2):
	smash1 = int("%.2d%.2d%.2d" % (t1.hour, t1.minute, t1.second))
	smash2 = int("%.2d%.2d%.2d" % (t2.hour, t2.minute, t2.second))
	print smash1, smash2
	print smash1 > smash2
	return smash1 > smash2

time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 31

time3 = Time()
time3.hour = 1
time3.minute = 59
time3.second = 1

time4 = Time()
time4.hour = 9
time4.minute = 39
time4.second = 3


is_after(time1, time1) # False
is_after(time1, time2) # False
is_after(time1, time3) # True
is_after(time1, time4) # True
is_after(time2, time1) # True
is_after(time2, time2) # False
is_after(time2, time3) # True
is_after(time2, time4) # True
is_after(time3, time1) # False
is_after(time3, time2) # False
is_after(time3, time3) # False
is_after(time3, time4) # False
is_after(time4, time1) # False
is_after(time4, time2) # False
is_after(time4, time3) # True
is_after(time4, time4) # False


