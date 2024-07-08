lines = [line.strip() for line in open('scores.txt')]
d = {}
M = []
for line in lines:
	L = line.split(' ')
	if L[1] not in M :
		M.append(L[1])
	if  L[3] not in M:
		M.append(L[3])
C = []	
for i in M:
	w = 0
	op = 0
	for line in lines:
		L = line.split(' ')
		if L[1] == i:
			w += int(L[2])
			op += int(L[4])
		if L[3] == i:
			w += int(L[4])
			op += int(L[2])
	if w < op:
		c = i,w,op
		C.append(c)
print(C) 	
    
			

