from random import randint
r = eval(input("Количество рядов:  "))
c = eval(input("Количество столбцов: "))
print()
print("Случайный двумерный массив")
L = []
for i in range(r):
	M = []
	for j in range(c):
		M.append(randint(0,9))
	L.append(M)
for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j], end = "  ")
	print()
print()
print()
print("Координаты элемента(номера рядов и столбцов)")
for i in range(len(L)):
	for j in range(len(L[i])):
		print("(",i,",",j,")", end = " ")
	print()
print()
print("Координаты элемента(номер элемента)")
a = 0
for i in range(len(L)):
	for j in range(len(L[i])):
		if a >9:
			print(a, end = "  ")
		else:
			print( " "+str(a) + " ", end = "  ")		
		a += 1
	print()
print()
x = eval(input("Введите номер элемента: "))
print(L[x//c][x%c])
r, c = eval(input("Введите координаты элемента(через запятую): "))
print(L[r][c])		