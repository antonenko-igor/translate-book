temp = eval(input("Введите значение температуры: "))
unit = eval(input("Единица измерения: Цельсии-1 или Фаренгейты-2 :"))
if unit == 1:
	print("Температура равна",(9/5)*temp+32,"в Фаренгейтах.")
else:
    print("Температура равна",(5/9)*(temp-32),"в Цельсиях.")	