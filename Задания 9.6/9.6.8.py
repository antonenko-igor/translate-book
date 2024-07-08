num1 = eval(input("Введите первое число: "))
num2 = eval(input("Введите второе число : "))

while num1 != 0 and num2 != 0:
	if num1 > num2:
		num1 = num1 % num2
	else:
		num2 = num2 % num1
print(num1 + num2) 




















	
	