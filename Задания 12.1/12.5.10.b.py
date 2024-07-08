words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	if word[1:4] == "ave":
		print(word)
print()  