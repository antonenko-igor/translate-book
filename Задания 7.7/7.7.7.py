L = eval(input("Введите первый список:   "))
M = eval(input("Введите второй список(того же размера):  "))

N = []
for i in range(len(M)):
	N.append(L[i] + M[i])
print(N) 
