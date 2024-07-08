items = eval(input("Сколько вещей Вы покупаете?:  "))
if items < 10:
	print("Общая стоимость равна: ",items*12)
elif items <= 99:
	print("Общая стоимость равна: ",items*10)
elif items >= 100:
    print("Общая стоимость равна: ",items*7)	