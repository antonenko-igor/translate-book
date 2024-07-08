from random import randint

rand = randint(1,10)
num = eval(input("Введите число: "))
if num == rand:
	print("Вы угадали!")
else:
    print("Неправильно! Число равно ",rand)	