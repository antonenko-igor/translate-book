def primes(n=100):
	L = []
	p = 2
	while n > 0:
		for i in range(2, p//2 + 1):
			if p % i == 0:
				break
		else:
			L.append(p)
			n -= 1
		p += 1
	return(L) 


print(primes())




	
	