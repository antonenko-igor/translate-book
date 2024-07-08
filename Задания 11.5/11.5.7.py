from random import randint
L = []
for i in range(5):
	M = []
	for j in range(5):
		M.append(randint(1,10))
	L.append(M)
M = []
for row in L:
	for j in row:
		M.append(j)
M.sort()

d = {}
for i in range(1,11):
	d[str(i)] = M.count(i)
print(d) 
