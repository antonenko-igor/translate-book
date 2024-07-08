from random import choice, shuffle, sample
from string import ascii_letters, punctuation, digits
source = ascii_letters + punctuation + digits

C = sample(source, 18) *2
P = C
shuffle(P)
L = []
for i in range(6):
	M = []
	for j in range(6):
		x = choice(P)
		M.append(x)
		P.remove(x)
	L.append(M)
for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j],end = "   ")
	print()  