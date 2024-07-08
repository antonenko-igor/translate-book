# written by Antonenko Igor(Орск)
# one-time pad (The Vigenère cipher)

from random import randint

message = input("Введите сообщение(русский): - ")
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
secret = []
key = []
num = []
for i in range(len(message)):
	char = message[i].lower()
	if char in alphabet:
		shift = randint(0,32)
		num.append(shift)
		key.append(alphabet[shift])
		enc = (alphabet.index(char) + shift)%32
		secret.append(alphabet[enc])
	else:
		secret.append(char)
print("Зашифрованное сообщение: ", "".join(secret))
print("Ключ: ","".join(key)) 
