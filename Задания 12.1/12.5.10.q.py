words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if "z" in word and "w" in word:
		print(word)  
