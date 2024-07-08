L = []
for i in range(1,1001):
	if i % 7 == 0:
		L.append(i)
M = []
for i in L:
	s = str(i)
	if s[-1:] == str(6):
		M.append(s)
print(" ".join(M)) 