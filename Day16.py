""" 
Day16 : Write a Program to find the kth largest element of any random list.
"""

#Program

def kLargest(arr, k):
	# Sort the given array arr in reverse
	# order.
	arr.sort(reverse=True)
	# Print the first kth largest elements
	for i in range(k):
		print(arr[i], end=" ")

# Driver code
arr = [1, 23, 12, 9, 30, 2, 50]
# n = len(arr)
k = 3
kLargest(arr, k)

