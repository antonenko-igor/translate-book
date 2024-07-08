def digital_root(number):
	s = str(number)
	while True:
		n = 0
		for i in range(len(s)):
			n += int(s[i])
		s = str(n)
		if len(s) == 1:
			return s 
			break			
print(digital_root(45893))		