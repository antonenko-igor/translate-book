score = eval(input("Введите результат теста:  "))
highest = score
lowest = score

for i in range(9):
	score = eval(input("Введите результат теста:  "))
	if score > highest:
		highest = score
	if score < lowest:
		lowest = score
print("Наибольшее значение - ",highest )
print("Наименьшее значение - ",lowest)		