x = eval(input("Сколько чисел Фибоначчи вывести? - "))
a = 0
b = 1
print(b, end = ",  ")
for i in range(x):
	c = a + b
	print(c, end =",  ")
	a = b
	b = c 
