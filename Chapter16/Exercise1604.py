"""
Exercise 16.4

Write a "pure" version of increment that creates and returns a new Time object
rather than modifying the parameter.
"""

class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

def print_time(time):
	print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

def seconds_to_time(seconds):
	"""turns a number of seconds into the equivalent hours, minutes, and seconds."""

	time = Time()
	num_minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(num_minutes, 60)
	return time

def time_to_seconds(time):
	"""turns hours, minutes, seconds into the equivalent number of seconds"""

	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds

def sum_times(time1, time2):
	"""Adds two times together."""
	assert tests(t1) and tests(t2)
	seconds = time_to_seconds(time1) + time_to_seconds(time2)
	return seconds_to_time(seconds)

def tests(time):
	if time.hour < 0 or time.minute < 0 or time.second < 0:
		return False
	if time.minute >= 60 or time.second >= 60:
		return False
	if time_to_seconds(int_to_time(time)) != time:
		return False
	return True

def increment(time, seconds):
	x = time_to_seconds(time)
	y = x + seconds
	res = seconds_to_time(y)
	return res

def main():
	# if we add 350 seconds to 11:12:30

	time1 = Time()
	time1.hour = 11
	time1.minute = 12
	time1.second = 30
	seconds = 350
	time1_in_seconds = time_to_seconds(time1)
	new_time_in_seconds = time1_in_seconds + seconds
	new_time = seconds_to_time(new_time_in_seconds)

	print 'We start with',
	print_time(time1)

	print 'We add %d seconds' % seconds

	print 'That gives us', print_time(new_time)

if __name__ == '__main__':
	main()








