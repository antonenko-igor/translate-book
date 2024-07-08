words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if word == word[::-1] and len(word) > 1:
		print(word) 

	