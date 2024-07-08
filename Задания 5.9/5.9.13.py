from random import randint
s = 0

for i in range(1,11):
	x = randint(1,10)
	y = randint(1,10)
	print("Вопрос",i,"  ", x,"X",y)
	z = eval(input())
	if x * y == z:
		s = s + 1
		print("Правильно!")
	else:
		print("Неправильно.Ответ равен "," ",x * y)	    	
print("Всего правильных ответов -",s)  
