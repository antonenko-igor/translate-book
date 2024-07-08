words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if len(word) == 4 and word[0] == word[-1:]:
		print(word) 