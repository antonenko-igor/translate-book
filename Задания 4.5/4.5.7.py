num_1 = eval(input("Введите первое число: "))
num_2 = eval(input("Введите второе число: "))
dif = 0
if num_1 > num_2:
	dif = num_1 - num_2
else:
    dif = num_2 - num_1
if dif <= 0.001:
    print("Близко")
else:
    print("Не близко")    