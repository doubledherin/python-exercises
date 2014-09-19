"""Exercise 16.6

Write a function called mul_time that takes a Time object and a number and returns
a new Time object that contains the product of the original Time and the number.

Then use mul_time to write a function that takes a Time object that represents the 
finishing time in a race, and a number that represents the distance, and returns a 
Time object that represents the
average pace (time per mile).
"""

class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

def print_time(time):
	return "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

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

def mul_time(finish_time, distance):
	finish_time_in_seconds = time_to_seconds(finish_time)
	#print "finish_time_in_seconds is: ", finish_time_in_seconds
	pace_in_seconds = finish_time_in_seconds / distance
	#print "pace_in_seconds is: ", pace_in_seconds
	pace_in_time = seconds_to_time(pace_in_seconds)
	return print_time(pace_in_time)

def tests(time):
	if time.hour < 0 or time.minute < 0 or time.second < 0:
		return False
	if time.minute >= 60 or time.second >= 60:
		return False
	if time_to_seconds(int_to_time(time)) != time:
		return False
	return True

def main():
	# if I run 5 miles in 40 minutes

	time1 = Time()
	time1.hour = 0
	time1.minute = 40
	time1.second = 00
	distance = 5


	print 'My finish time was', print_time(time1)

	print 'In that time, I went %d miles.' % distance

	print 'That means my average pace was', mul_time(time1, distance), "per mile."

if __name__ == '__main__':
	main()








