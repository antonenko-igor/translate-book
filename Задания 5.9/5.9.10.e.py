a = eval(input('Введите результат теста: '))
b = eval(input('Введите результат теста: '))
if a < b:
    low_1 = a
    low_2 = b
else:
    low_1 = b
    low_2 = a
s = a + b
for i in range(8):
	a = eval(input("Введите результат теста: "))
	s = s + a
	if low_1 < a < low_2:
		low_2 = a
	elif a < low_1:
		low_2 = low_1
		low_1 = a
print("Среднее значение без двух наименьших значений - ",(s-low_1-low_2)/8,) 