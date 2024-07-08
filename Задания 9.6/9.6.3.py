weight = eval(input("Введите вес(в кг):  "))

while weight < 0:
	weight = eval(input("Ошибка! Введите корректный вес:  "))
print("Вес в фунтах равен ",weight*2.2) 
	