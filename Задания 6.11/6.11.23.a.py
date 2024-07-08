string = "Введите строку для шифрования: "
encripted = ""

for i in range(3):
	for j in range(i, len(string),3):
		encripted = encripted + string[j]
print(encripted) 