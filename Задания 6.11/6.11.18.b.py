string = input("Введите строку:   ")
letter = input("Введите букву:   ")

x = 0
for i in range(len(string)):	
	if string[i] == letter:
		x = x + 1
print("Буква ",letter,"встречается в строке ",x,"раз(а).") 
