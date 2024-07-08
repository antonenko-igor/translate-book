words = [line.strip() for line in open('wordlist.txt')]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for word in words:
	for i in range(23):
		if alphabet[i]*2 in word and word[-3:] != "lly":
			print(word)
			break 
		
			