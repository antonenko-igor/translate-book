words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if len(word) >= 8:
		w_rev = word[-4::]
		if word[:4] == w_rev[::-1]:
			print(word) 
		
	