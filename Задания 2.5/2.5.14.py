height = eval(input("Введите значение высоты ромба:  "))
h = int(height/2)
for i in range(h):
	print(" "*((h-1)-i),"*" " "*i + "*")
for i in range(h):
	print(" "*i,"*" " "*((h-1)-i) + "*")
input() 