from random import randint

L = []
for i in range(10):
	M = []
	for j in range(10):
		M.append(randint(1,100))
	L.append(M)
print(L)
print()

for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j],end = " ")
	print()

print("Наибольшее значение в третьей строке: ", max(L[2])) 