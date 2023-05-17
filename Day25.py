""" 
Day25: Write a program to taking median of two sorted Arrays of different sizes.
"""

#Program

def Solution(arr):

	n = len(arr)

	if n % 2 == 0:
		z = n // 2
		e = arr[z]
		q = arr[z - 1]
		ans = (e + q) / 2
		return ans
		
	else:
		z = n // 2
		ans = arr[z]
		return ans

if __name__ == "__main__":
	
	arr1 = [ -5, 3, 6, 12, 15 ]
	arr2 = [ -12, -10, -6, -3, 4, 10 ]

	arr3 = arr1 + arr2

	arr3.sort()

	print("Median = ", Solution(arr3))
	
