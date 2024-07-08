def sum_digits(n):
	s = str(n)
	n = 0
	for i in range(len(s)):
		n += int(s[i])
	return n 
print(sum_digits(555)) 