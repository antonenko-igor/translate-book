lines = [line.strip() for line in open('scores.txt')]
M = []
for line in lines:
	L = line.split(' ')	
	M.append(int(L[2]))
	M.append(int(L[4]))
print(sum(M)/len(M)) 

    



