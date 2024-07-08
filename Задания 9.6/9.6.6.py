from random import randint

secret_num = randint(1,100)
num_guesses = 0
guess = 0
while guess != secret_num and num_guesses <= 4:
	guess = eval(input('Введите Вашу догадку (1-100): '))
	num_guesses = num_guesses + 1
	if guess < secret_num:
		if num_guesses != 4:
		    print('ВЫШЕ.', 5-num_guesses, 'попытки осталось.\n')
		else:
			print("ВЫШЕ. 1 попытка осталась.\n")		           
	elif guess > secret_num:
		if num_guesses != 4:
		    print('НИЖЕ.', 5-num_guesses, 'попыток осталось.\n')
		else:
			print("НИЖЕ. 1 попытка осталась.\n")
	else:
		print('Вы угадали!')
if num_guesses==5 and guess != secret_num:
    print('Вы проиграли. Правильное число - ', secret_num) 