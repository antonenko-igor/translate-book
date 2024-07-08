L = []
c = 0
for i in range(8):
	M = []
	for j in range(8):
		t = c + j
		if t % 2 == 1:
		    M.append(2)
		else:
		    M.append(1)
	c = c + 1
	L.append(M)

for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j],end = "  ")
	print() 

	
