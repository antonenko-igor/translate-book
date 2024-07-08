flag = 0
for i in range(10):
	score = eval(input("Введите результат теста:  "))
	if score > 100:
		flag = 1
print()
if flag == 1:
	print("Значение больше 100 введено.") 