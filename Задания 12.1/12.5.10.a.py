words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if word[-3:] == "ime":
		print(word)
print() 
