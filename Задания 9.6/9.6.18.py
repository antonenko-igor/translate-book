from random import randint
L = [[0 for i in range(6)] for i in range(6)]
count = 0
while count < 12:
	x = randint(0,5)
	y = randint(0,5)
	if L[x][y] != 1:
		L[x][y] = 1
		count = count + 1	    
for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j],end="  ")
	print() 

