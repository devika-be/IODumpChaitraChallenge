""" 
Day22: Write a program to find first non-repeating character in a string.
"""

#Program

string = "pythonprogram"
index = -1
fnc = ""
for i in string:
	if string.count(i) == 1:
		fnc += i
		break
	else:
		index += 1
if index == 1:
	print("Either all characters are repeating or string is empty")
else:
	print("First non-repeating character is", fnc)
