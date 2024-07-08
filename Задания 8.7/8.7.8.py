from random import choice,shuffle

names = input("Введите имена через запятую:  ")
entries = eval(input("Введите количество вхождений каждого имени через запятую:  "))
L = names.split(",")
X = list(entries)
M = []
for i in range(len(X)):
	for _ in range(X[i]):
		M.append(L[i])	
	shuffle(M)
print("Лотерею выиграл",choice(M))  