L = eval(input("Введите список содержащий числа от 1 до 12: "))

M = []
for i in L:
	if i > 10:
		i = 10
	M.append(i)
print(M) 