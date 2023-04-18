""" 
Day17: Write a program to check whether s is a substring of a str or not.
"""

#Program

string = "Python is Programming language" 
substring = "Python" 

s = string.split()

# if substring is present in the given string then it gives output as yes
if substring in s:
	print("yes")
else:
	print("no")
