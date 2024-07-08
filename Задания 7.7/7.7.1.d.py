L = eval(input("Введите список целых чисел: "))
flag = 0

for i in L:
	if i == 5:
		flag = 1		
if flag == 1:
	print("Да")
else:
	print("Нет")  
