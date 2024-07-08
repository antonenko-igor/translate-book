from random import randint
money = 100
while True:
	p = randint(0,1)
	guess = eval(input("Выберите - орел(1) или решка(0) - "))
	if p == guess:
		money = money + 9
		print("Правильно.")
	else:
		money = money - 10
		print("Неправильно!")
	print("Количество денег",money)
	if money >= 200:
		print("Вы выиграли! Ваши деньги - ",money)
		break
	if money <= 0:
		print("Вы проиграли.Ваши деньги - ",money)
		break 