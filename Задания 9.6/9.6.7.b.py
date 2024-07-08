string = input("Введите строку:  ")
letter = input("Введите букву:  ")
string = string.lower()
letter = letter.lower()
for i in string:	
	if i == letter:
		print("Индекс равен ",string.index(letter))
		break
else:
	print(letter, "не найдена.")
