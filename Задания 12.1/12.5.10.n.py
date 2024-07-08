words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if "zu" in word:
		print(word)  