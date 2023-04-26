""" 
Day24: Write a program that takes a list of integers as input and returns a new list that contains only one element that appears more than once in the original list.
"""

#Program

def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated

list1 = [10, 20, 30, 20, 20, 30, 40,
		50, -20, 60, 60, -20, -20]
print (Repeat(list1))
