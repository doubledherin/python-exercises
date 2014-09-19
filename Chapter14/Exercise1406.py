"""
Exercise 14.6

The urllib module provides methods for manipulating URLs and downloading
information from the web. The following example downloads and prints a secret message from
thinkpython.com:

import urllib
conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
	print line.strip()

Run this code and follow the instructions you see there. 

http://www.uszip.com/zip/02492

Write a program that prompts the user for a zip code and prints the
name and population of the corresponding town.

<p>
Note: the text you get from uszip.com is in HTML, the language most
web pages are written in.  Even if you don't know HTML, you should be
able to extract the information you are looking for.

"""

import urllib, string


zip = raw_input("Enter a 5-digit U.S. ZIP code, and I'll tell you the city and population >> ")

while True:
	if len(zip) != 5 or not zip.isdigit():
		zip = raw_input("Enter a 5-digit ZIP code, and I'll tell you the city and population >> ")
	else:
		break

page = urllib.urlopen('http://www.uszip.com/zip/' + zip)
for line in page.fp:
	line = line.strip()
	if '<h2><strong>' in line:
		print line
	if 'Total population' in line:
		print line

page.close()


