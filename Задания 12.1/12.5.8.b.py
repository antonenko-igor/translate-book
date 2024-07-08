lines = [line.strip() for line in open('scores.txt')]
team = input("Введите название команды из scores.txt -  ")

loss = 0
win = 0
for line in lines:
	L = line.split(' ')
	if L[1] == team:
		if int(L[2]) > int(L[4]):
			win += 1
		else:
			loss += 1

	if L[3] == team:
		if int(L[4]) > int(L[2]):
			win += 1
		else:
			loss += 1
print("Побед - ", win, "Поражений - ", loss) 
		