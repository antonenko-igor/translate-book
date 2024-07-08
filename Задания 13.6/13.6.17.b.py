def primes(start=2, n=100):
	L = []
	while n > 0:
		for i in range(2, start//2 + 1):
			if start % i == 0:
				break
		else:
			L.append(start)
			n -= 1
		start += 1
	return L 
	



print(primes(30,50))

