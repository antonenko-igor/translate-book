hour = eval(input("Введите час:  "))
unit = eval(input("am (1) или pm (2)? "))
future = eval(input("Сколько часов вперед?  "))
if  unit == 1 and future <= 3:
	print("Новый час: ",(hour + future)%12, "am")
if  unit == 1 and future > 3:
	print("Новый час: ",(hour + future)%12, "pm")
if  unit == 2 and future <= 3:
	print("Новый час: ",(hour + future)%12,  "pm")
if  unit == 2 and future > 3:
	print("Новый час: ",(hour + future)%12,  "am")  




