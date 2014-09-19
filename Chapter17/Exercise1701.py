"""
Exercise 17.1

Rewrite time_to_int (from Section 16.4) as a method. It is probably not appropriate
to rewrite int_to_time as a method; what object you would invoke it on?
"""
class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""
	def time_to_seconds(self):
		"""turns hours, minutes, seconds into the equivalent number of seconds"""

		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

def main():

	time1 = Time()
	time1.hour = 10
	time1.minute = 1
	time1.second = 30

	return time1.time_to_seconds()   # 36090


if __name__ == "__main__":
	print main()