alphabet = "abcdefghijklmnopqrstuvwxyz"
L = []
for i in alphabet:
	for j in alphabet:
		for z in alphabet:
			L.append(i + j + z)

words = [line.strip() for line in open('wordlist.txt')]
M = []
for i in L:
	if i in words:
		M.append("Python" + i[0].upper() + i[1:3])
print(M)  

