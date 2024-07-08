L = [1]
for i in range(11):
	if i == 0:
		L.append(1)
	else:
		for j in range(i):
			L.append(0)
		L.append(1)
print(L) 		
	
