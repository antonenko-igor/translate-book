from random import choice
M = ["H","T"]
L = []

for _ in range(100):
	s = 0
	n = 0
	while s != 5:
		f = choice(M)
		n += 1
		if f == "H":
			s += 1
			if s == 5:
				L.append((n-5))
				
		else:
			s = 0
print(sum(L)/100) 

