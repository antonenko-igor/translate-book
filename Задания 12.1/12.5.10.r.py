words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if len(word) >= 5:
		if word[0] == "a" and word[2] == "e" and word[4] == "i":
			print(word) 
