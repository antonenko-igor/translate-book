def number_of_factors(n):
	count = 0
	for i in range(1,n + 1):
		if n % i == 0:
			count += 1
	return count
print(number_of_factors(840)) 