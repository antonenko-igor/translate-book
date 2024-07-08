from random import randint

for i in range(10):
	word = input("Введите слово - ")
	r = randint(1, len(word)- 1)
	print(word[-r:] + word[0:len(word) - r]) 








