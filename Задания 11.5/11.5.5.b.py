n = eval(input("Количество команд: "))
scores = {}
for i in range(n):
	name = input("Введите название команды: ")
	w = eval(input("Количество побед: "))
	l = eval(input("Количество поражений: "))
	scores[name] = [w,l]
w_team = []
for i in scores.values():
	w_team.append(i[0])
print(w_team) 