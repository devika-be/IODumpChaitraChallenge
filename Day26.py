""" 
Day26: Implement a function that takes a string as a input and returns the minimum number of insertions required to make the string a palindrome.
"""

#Program

import sys
def findMinInsertions(str, l, h):

	# Base Cases
	if (l > h):
		return sys.maxsize
	if (l == h):
		return 0
	if (l == h - 1):
		return 0 if(str[l] == str[h]) else 1

	
	if(str[l] == str[h]):
		return findMinInsertions(str, l + 1, h - 1)
	else:
		return (min(findMinInsertions(str, l, h - 1),
					findMinInsertions(str, l + 1, h)) + 1)

if __name__ == "__main__":
	
	str = "geeks"
	print(findMinInsertions(str, 0, len(str) - 1))

