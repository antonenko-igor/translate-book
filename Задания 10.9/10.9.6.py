L1 = eval(input("Введите первый список: "))
L2 = eval(input("Введите второй список: "))

flag = 0
for ent in L2:
	if ent in L1:
		flag = 1
if flag == 1:
	print("Имеют общие элементы. ")
else:
	print("Нет общих элементов.") 

