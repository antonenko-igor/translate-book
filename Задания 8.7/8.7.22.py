from random import randint

L = []
for i in range(5):
	M = []
	for j in range(5):
		M.append(randint(0,1))
	L.append(M)
i = eval(input("Введите номер строки:  "))
j = eval(input("Введите номер столбца: "))
if L[i-1][j-1] == 1:
	print("Попал")
else:
	print("Мимо")  