""" 
Day21: Implement a function to check if a given string contains a valid email address.
"""

# Python Program

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):

	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

if __name__ == '__main__':

	# Enter the email
	email = "devika326@gmail.com"
	check(email)

	email = "my.ownsite@our-earth.org"
	check(email)

	email = "ankitrai326.com"
	check(email)
