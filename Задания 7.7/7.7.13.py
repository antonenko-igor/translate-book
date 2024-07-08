L = eval(input("Введите список:  "))

M = []
for i in L:
	if i not in M:
		M.append(i)
print(M) 