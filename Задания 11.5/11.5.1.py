print("Для окончания ввода введите - да.")
d = {}
while True:
	n = input("Введите наименование товара: ")
	if n == "да":
		break
	p = eval(input("Введите цену: "))
	d[n] = p 
while True:
	a = input("Введите наименование товара: ")
	if a in d:
		print(d[a])
	else:
		print("Товар отсутствует в словаре.")  

