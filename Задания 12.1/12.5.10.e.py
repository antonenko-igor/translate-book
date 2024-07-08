words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if "a" not in word and "e" not in word and "i" not in word and "o" not in \
	word and "u" not in word:
		print(word)  
