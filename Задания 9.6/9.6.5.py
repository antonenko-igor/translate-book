print("Для окончания ввода введите отрицательное число.")
score = 0
scores = []
grades = []

while score >= 0:
	score = eval(input("Введите результат теста:  "))
	scores.append(score)
for score in scores:
	if score > 90:
		grades.append("A")
	elif score > 60:
		grades.append("B")
	elif score > 60:
		grades.append("C")
	elif score > 50:
		grades.append("D")
	elif score > 40:
		grades.append("E")
	elif score > 0:
		grades.append("F")
	elif score < 0:
		scores.pop()
print(scores)
print(grades)
print("Имеется ",grades.count("A"),"A's")
print("Среднее число результатов теста -",sum(scores)/len(scores)) 
		
