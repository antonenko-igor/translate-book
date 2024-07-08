words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if "a" in word and "b" in word and "c" in word and "d" in word and "f" in word:
		print(word)  