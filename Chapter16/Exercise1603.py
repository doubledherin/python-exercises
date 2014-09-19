"""
Exercise 16.3
Write a correct version of increment that doesn't contain any loops.

def increment(time, seconds):
	time.second += seconds
	if time.second >= 60:
		time.second -= 60
	time.minute += 1
	if time.minute >= 60:
		time.minute -= 60
		time.hour += 1
"""


class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""


def increment(time, seconds):
	time.second += seconds
	add_minutes, time.second = divmod(time.second, 60)
	time.minute += add_minutes
	add_hours, time.minute = divmod(time.minute, 60)
	print add_hours
	time.hour += add_hours
	time.hour = time.hour % 12

	return time.hour, time.minute, time.second


time = Time()
time.hour = 11
time.minute = 59
time.second = 30


print increment(time, 1)
print increment(time, 10)
print increment(time, 30)
print increment(time, 50)
print increment(time, 155)

