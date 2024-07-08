words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if len(word) == 2:
		print(word) 