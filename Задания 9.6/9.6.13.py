from random import randint
won = 0
lost = 0
tie = 0
i = 1
print("Бумага - 1,Камень - 2,Ножницы - 3")
while True:
	r = randint(1,3)
	print("Раунд -",i)
	g = eval(input("Ваш ход - "))
	if r == 1 and g == 1 or r == 2 and g == 2 or r ==3 and g == 3:
		tie = tie + 1
	if r == 2 and g == 3 or r == 3 and g == 1 or r == 3 and g == 1 \
	   or r == 1 and g == 2:
		lost = lost + 1
	if r == 3 and g == 2 or r == 1 and g == 3 or r == 1 and g == 3 \
	   or r == 2 and g == 1:
		won = won + 1
	if lost == 3:
		print("Выиграл компьютер.")
		break
	if won == 3:
		print("Выиграл игрок.")
		break
	i = i + 1
	if i == 6:
		break
print("Игра закончена.")
print("Ничья - ",tie)
print("Поражений - ",lost)
print("Побед - ",won) 
