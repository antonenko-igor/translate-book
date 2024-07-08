string = input("Введите строку:   ")

for i in range(len(string)):
	letter = input("Введите букву:  ")
	if string[i] == letter:
		print("Буква содержится в строке.")
	else:
		print("Буква не содержится в строке.") 
		
