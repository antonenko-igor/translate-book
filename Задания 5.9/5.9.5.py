num = eval(input("Введите число - "))
count = 0
for i in range(1,(num + 1)):
	if num % i == 0:
		count = count + i
print("Сумма делителей числа - ",count)		