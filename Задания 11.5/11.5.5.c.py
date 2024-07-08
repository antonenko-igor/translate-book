n = eval(input("Количество команд: "))
scores = {}
for i in range(n):
	name = input("Название команды: ")
	w = eval(input("Количество побед: "))
	l = eval(input("Количество поражений: "))
	scores[name] = [w,l]
w_rec = []
for i in scores:
	if scores[i][0] > 0:
		w_rec.append(i)

print(w_rec) 
