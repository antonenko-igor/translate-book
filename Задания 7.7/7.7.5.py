L = eval(input("Введите список строк:  "))

M = []
for i in range(len(L)):
	M.append(L[i][1:])
print(M)    