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
		if L[1] == i:
			d[i].append(int(L[2]))
		if L[3] == i:
			d[i].append(int(L[4]))
C = []
for i in d:
	average = round(sum(d[i])/len(d[i]), 2)
	if average >= 70:
		n = i,average
		C.append(n)		
print(C) 
