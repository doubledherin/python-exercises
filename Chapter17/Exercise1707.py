"""
Exercise 17.7
This exercise is a cautionary tale about one of the most common, and difficult to
find, errors in Python. 

Write a definition for a class named Kangaroo with the following methods:
1. An __init__ method that initializes an attribute named pouch_contents to an 
empty list.
2. A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents.
3. A __str__ method that returns a string representation of the Kangaroo object 
and the contents
of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables 
named kanga and roo, and then adding roo to the contents of kanga's pouch.

Download http://thinkpython.com/code/BadKangaroo.py. 

It contains a solution to the previous problem with one big, nasty bug. 
Find and fix the bug.
If you get stuck, you can download http://thinkpython.com/code/GoodKangaroo.py,
which explains the problem and demonstrates a solution.
"""

class Kangaroo(object):
	"""I have no idea what this does yet."""

	def __init__(self, contents=[]):
		self.pouch_contents = contents

	def __str__(self):
		"""returns a string that contains the name of the kangaroo and 
		the contents of its pouch.
		"""
		t = [ object.__str__(self) + ' has this in her pouch:' ]
		for thing in self.pouch_contents:
			x = '   ' + object.__str__(thing)
			t.append(x)
		return '\n'.join(t)

	def put_in_pouch(self, thing):
		self.pouch_contents.append(thing)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch("Skittles")
kanga.put_in_pouch("Mountain Dew")
kanga.put_in_pouch(roo)

if __name__ == "__main__":
	print kanga
	print roo


