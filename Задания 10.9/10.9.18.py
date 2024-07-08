L = []
print("Для окончания ввода введите: - да")
while True:
	s = input("Введите футбольный счет в формате(счет побед - счет поражений):  ")
	if s == "да":
		break
	x = s.split("-")
	L.append(int(x[0]))
	L.append(int(x[1]))
print(L)
print("Наибольший счет равен -",max(L))
print("Наименьший счет равен - ",min(L)) 

