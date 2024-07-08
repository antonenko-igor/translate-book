words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word:
		print(word)  
