n = eval(input("Количество команд: "))
scores = {}
for i in range(n):
	name = input("Введите название команды: ")
	w = eval(input("Количество побед: "))
	l = eval(input("Количество поражений: "))
	scores[name] = [w,l]
t = input("Введите название команды: ")
print("Выигрыш в процентах команды ",t," равны ",(scores[t][0]/sum(scores[t]))*100) 

