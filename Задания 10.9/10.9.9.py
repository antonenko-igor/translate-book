count = 0
L = []
for i in range(10001):
	n = str(i)
	for j in n:
		if j == str(3):
			count += 1
			L.append(n)		
print(" ".join(L)) 
	