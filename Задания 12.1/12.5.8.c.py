lines = [line.strip() for line in open('scores.txt')]
d = {}
M = []
for line in lines:
	L = line.split(' ')
	if L[1] not in M :
		M.append(L[1])
	if  L[3] not in M:
		M.append(L[3])
	
for i in M:
	d[i] = []
	for line in lines:
		L = line.split(' ')
		dim = abs(int(L[2]) - int(L[4]))
		if dim >= 30:
			if L[1] == i and int(L[2]) < int(L[4]):
				d[i].append(dim)
			if L[3] == i and int(L[4]) < int(L[2]):
				d[i].append(dim)
for i in M:
	if len(d[i]) < 3:
		del d[i]
print(d) 


	









	
