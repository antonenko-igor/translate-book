from random import randint
L = [[0 for i in range(5)] for i in range(5)]
for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j],end="  ")
	print()
print()

n = 0
while n < 10:	
	i = randint(0,4)
	j = randint(0,4)
	if L[i][j] == 0:
		L[i][j] = 1
		n = n + 1
for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j],end="  ")
	print()  




