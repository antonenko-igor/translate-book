year = eval(input("Введите год: "))
c = 0
for i in range(1600, year+1):
	if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
		c = c + 1
print( "Количество високосных годов равняется ", c) 
