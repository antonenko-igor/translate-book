L = []

for i in range(100000,990000):
	x = str(i)
	if x == x[: :-1]:
		L.append(int(x))

for i in range(len(L)-1):
	n = L[i+1]-L[i]
	if n<20:
		print(L[i],"-",L[i+1]) 
	

		
