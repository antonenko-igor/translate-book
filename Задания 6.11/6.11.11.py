s = input("Введите слово содержащее букву а(русский):  ")

for i in s:	
	if i != "а":
		print(i,end="")
	else:
		print(i)
