""" 
Day19: Take a character and print whether the character is uppercase or lowercase or number or special character.
"""

#Program

def check(ch):

	if (ch >= 'A' and ch <= 'Z'):
		print(ch,"is an UpperCase character");

	elif (ch >= 'a' and ch <= 'z'):
		print(ch,"is an LowerCase character");
	else:
		print(ch,"is not an alphabetic character");

    
ch = 'A';

check(ch);


ch = 'a';

check(ch);


ch = '0';

check(ch);

