string = input("Введите строку:  ")
letter = input("Введите букву:  ")
i = 2
string = string.lower()
letter = letter.lower()

while i!= 0:
	if letter in string:
		print("Индекс равен  ",string.index(letter))
		i = 1
		break		
	i = 0
if i == 0:
	print(letter," не найдена.")