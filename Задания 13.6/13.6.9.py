def factors(n):
	L = []
	for i in range(1,n + 1):
		if n % i == 0:
			L.append(i)
	return L 
print(factors(840)) 