alphabet = "abcdefghijklmnopqrstuvwxyz"
L = []
words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	word_back = word[::-1]
	L.append(word_back)
M = []
for i in range(26):
	for w in L:	
		if w[0] == alphabet[i]:
			M.append(w)
print(M[-1::])  



	