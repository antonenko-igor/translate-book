from random import randint

for i in range(1,11):
	num_1 = randint(1,10)
	num_2 = randint(1,10)
	print("Вопрос",i,"  ", num_1,"X",num_2)
	mul = eval(input())
	if num_1*num_2 == mul:
		print("Правильно !")
	else:		
	    print("Неправильно! Ответ равен"," ", num_1*num_2)	
