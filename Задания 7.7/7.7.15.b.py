# written by Antonenko Igor(Orsk)
secret = input("Введите зашифрованное сообщение(русский): - ")
key = input("Введите ключ: - ")
 
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
decrypted = []
for i in range(len(secret)):
	letter = secret[i]
	if letter in alphabet:
		dec_shift = ((alphabet.index(letter) + 32) - alphabet.index(key[i]))%32
		decrypted.append(alphabet[dec_shift])
	else:
		decrypted.append(letter)
print("Расшифрованное сообщение: ", "".join(decrypted))	