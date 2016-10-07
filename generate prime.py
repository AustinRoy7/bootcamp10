def generate_prime (n):
	for j in range (2, n):
		prime = True
		for i in range (2, j):
			if (j % i == 0):
				prime = False
		if prime:
			print (j)