formula = input("Введите формулу:   ")
x = 0
y = 0
for i in formula:
	if i == "(":
		x = x + 1
	if i == ")":
		y = y + 1
if x == y:
	print("Формула правильная.")
else:
	print("Формула неправильная.")  