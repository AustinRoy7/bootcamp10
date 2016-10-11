def factorial(n):
  #Checks number,calculates and returns it's factorial
	if n == 1 or n ==0:
		return n
	else:
		return n*factorial(n-1)
