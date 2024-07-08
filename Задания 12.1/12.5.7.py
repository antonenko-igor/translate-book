l = [line.strip() for line in open('baseball.txt')]

for i in range(len(l) - 1):
	L = l[i].split("\t")
	if int(L[6]) > 20 and int(L[10]) > 20:
		print(L[0],L[6],L[10])	
	