from random import choice

word = input("Введите слово: ")
W = list(word)
A = []
for i in range(len(W)):
	letter = choice(W)
	A.append(letter)
	W.remove(letter)
print("".join(A))  
	
