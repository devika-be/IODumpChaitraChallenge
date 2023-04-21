""" 
Day20: Write a program to implement an algorithm to find the nth fibonacci number.
"""

# Python Program

# Method 1 ( Use recursion ) :

def Fibonacci(n):
	if n<= 0:
		print("Incorrect input")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(10))


# OR


# Method 2 ( Use Dynamic Programming ) : 

# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1

FibArray = [0, 1]

def fibonacci(n):
	if n<0:
		print("Incorrect input")
	elif n<= len(FibArray):
		return FibArray[n-1]
	else:
		temp_fib = fibonacci(n-1)+fibonacci(n-2)
		FibArray.append(temp_fib)
		return temp_fib

print(fibonacci(9))


# OR


# Method 3 ( Using Arrays ) : 

# creating an array in the function to find the
#nth number in fibonacci series. [0, 1, 1, ...]

def fibonacci(n):
	if n <= 0:
		return "Incorrect Output"
	data = [0, 1]
	if n > 2:
		for i in range(2, n):
			data.append(data[i-1] + data[i-2])
	return data[n-1]

print(fibonacci(9))


