from random import choice
words = [line.strip() for line in open('wordlist.txt')]
while True:
	w = choice(words)
	if len(w) == 5:
		flag = 0
		for i in w:
			if w.count(i) != 1:
				flag = 1
		if flag == 0:
			break
print(w)
print()
print("У Вас 5 попыток отгадать слово")
c = 0
for i in range(5):
	letter = input("Введите букву(английский):  ")
	if letter in w:
		c += 1
	if i == 4:
		print("Выбранное слово - ", w)
		print("Всего угадано букв - ", c) 


	




