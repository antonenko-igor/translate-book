print("Для окончания ввода введите - да.")
d = {}
while True:
	n = input("Введите наименование товара: ")
	if n == "да":
		break
	p = eval(input("Введите стоимость: "))
	d[n] = p 
x = eval(input("Введите сумму в долларах: "))
for i in d:
	if d[i] < x:
		print(i)  