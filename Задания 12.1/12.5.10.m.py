words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if "q" in word and "qu" not in word:
		print(word)  
