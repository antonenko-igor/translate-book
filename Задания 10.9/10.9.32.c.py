from random import choice

N = []
for _ in range(100):
	L = []
	M = ["H","T"]
	for _ in range(200):
		L.append(choice(M))

	longest = 0
	s = 0
	for i in L:
		if i == "H":
			s += 1
		else:
			s = 0

		if s > longest:
			longest = s 
	N.append(longest)
	
print("Средняя длина наибольшего ряда 'орла' равна ",sum(N)/100) 



	
