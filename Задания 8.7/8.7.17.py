from random import randint
L = []
for i in range(4): 
	M =[]
	for j in range(4):
		M.append(randint(0,9))
	L.append(M)
print(L)

for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j], end="  ")
	print()

s = 0
for i in range(len(L)):
	for j in range(len(L[i])):
		s = s + L[i][j]
		
print("Среднее значение всех элементов списка ",s/16)			
