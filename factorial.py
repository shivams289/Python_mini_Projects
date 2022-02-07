#5! = 5* 4! = 5*4*3! = 5*4*...1!
#base case is when n=1

def factorial(n):
	 if n == 1:
	 	return 1

	 return n*factorial(n-1)

print(factorial(10))