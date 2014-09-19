"""
Exercise 16.7

The datetime module provides date and time objects that are similar to the Date
and Time objects in this chapter, but they provide a rich set of methods and operators. 
Read the documentation at http://docs.python.org/2/library/datetime.html.

1. Use the datetime module to write a program that gets the current date and prints the day of
the week.
2. Write a program that takes a birthday as input and prints the user's age and the number of
days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other.
That's their Double Day. Write a program that takes two birthdays and computes their Double
Day.
4. For a little more challenge, write the more general version that computes the day when one
person is n times older than the other.
"""

#########Question 1###############
import datetime

def todays_date_and_day():
	month = datetime.datetime.now().strftime("%B")
	date = datetime.datetime.now().strftime("%d")
	year = datetime.datetime.now().strftime("%Y")
	day = datetime.datetime.now().strftime("%A")
	return "Today's date is %s %s, %s, and it's a %s." % (month, date, year, day)

if __name__ == '__main__':
	print todays_date_and_day()

#########Question 2###############

def age(dob):
	now = datetime.datetime.now()

	try:
		birthday = dob.replace(year=now.year)
	except ValueError: # raised when the birthday is Feb. 29 and the current year is not a leapyear.
		birthday = dob.replace(year=now.year, month = now.month + 1, day=1)

	if birthday > now: # hasn't had a birthday this year
		age = now.year - dob.year - 1
		return age	
	else:
		age = now.year - dob.year # already had a birthday this year
		return age

def time_until_next_birthday(dob):
	now = datetime.datetime.now()
	try:
		birthday = dob.replace(year=now.year)
	except ValueError: # raised when the birthday is Feb. 29 and the current year is not a leapyear.
		birthday = dob.replace(year=now.year, month = now.month + 1, day=1)

	if birthday > now: # hasn't had a birthday this year
		next_birthday = birthday - now
		return next_birthday
	else:
		age = now.year - dob.year # already had a birthday this year
		birthday = birthday.replace(year=now.year + 1)
		next_birthday = birthday - now
		return next_birthday

my_birthday = datetime.datetime(1971,10, 15)
age = age(my_birthday)
next_birthday = time_until_next_birthday(my_birthday)


if __name__ == '__main__':
	print "Your birthday is", my_birthday
	print "You are %d years old." % age
	print "Your next birthday will be in", next_birthday

#########Question 3###############
def double_day(bd1, bd2):
	delta = abs(bd1 - bd2)
	youngest_person_bday = max(bd1, bd2)
	double_day = youngest_person_bday + delta
	return double_day

other_birthday = datetime.datetime(1978, 2, 15)
double_day = double_day(my_birthday, other_birthday)

if __name__ == '__main__':
	print "The other person's birthday is", other_birthday
	print "Your double day with that other person is", double_day

#########Question 4###############
"""
4. For a little more challenge, write the more general version that computes the day when one
person is n times older than the other.
"""
def n_day(bd1, bd2, n):
	delta = abs(bd1 - bd2)
	youngest_person_bday = max(bd1, bd2)
	n_day = youngest_person_bday + (delta/(n-1))
	return n_day

n_day = n_day(my_birthday, other_birthday, 5)


if __name__ == '__main__':
	print "Your n-day with the other person is", n_day

	