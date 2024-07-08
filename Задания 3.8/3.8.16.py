""" Вычисление католической Пасхи"""
from math import floor
Y = eval(input("Введите год: "))
C = int(Y/100)
m = ((15 + C - floor(C/4) - floor((8*C + 13)/25)))%30
n = ((4 + C - floor(C/4)))%7
a = Y%4
b = Y%7
c = Y%19
d = (19*c + m)%30
e = (2*a + 4*b +6*d + n)%7
if d ==29 and e == 6:
	print(" 19 Апреля")
if d ==28 and e ==  6 and (m == 2 or m == 5 or m == 10 or m == 13 /n
   or m == 16 or m == 21 or m == 24 or m == 39):
	print("18 Апреля")
if (22 + d + e) > 31:
	print((d+e-9), "Апреля")
else:
	print(22 + d + e, "Марта")  