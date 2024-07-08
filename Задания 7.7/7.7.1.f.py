L = eval(input("Введите список целых чисел: "))

del L[0]
del L[-1:]
L.sort()
print(L) 
	