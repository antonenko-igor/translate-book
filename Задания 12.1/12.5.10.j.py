words = [line.strip() for line in open('wordlist.txt')]
L = []
for w in words:
	L.append(w[::-1])
for i in words:
	if i in L:
		print(i,"-",i[::-1])  

	
		