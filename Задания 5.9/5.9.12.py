from random import randint
s = 0

for i in range(5):
	num = randint(1,10)
	guess = eval(input("Введите ответ -"))
	if guess == num:
		s = s + 10
	else:
		s = s - 1
print("Ваш счет -",s)		