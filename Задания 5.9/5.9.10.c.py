a = eval(input("Введите число - "))
b = eval(input("Введите число - "))
if a < b:
	high_1 = b
	high_2 = a 
else:
	high_1 = a 
	high_2 = b
for i in range(8):
	num = eval(input("Введите число -"))
	if  high_2 < num < high_1:
		high_2 = num	
	elif num > high_1:
		high_2 = high_1
		high_1 = num
	
print("Второе самое большое число -",high_2) 