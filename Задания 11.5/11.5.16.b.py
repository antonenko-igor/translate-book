num = eval(input("Введите число:  "))

val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

con_num = ""
i = 0
while num > 0:
	for _ in range(num // val[i]):
		con_num += rom[i]
		num -= val[i]
	i += 1 
print(con_num) 