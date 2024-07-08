words = [line.strip() for line in open('wordlist.txt')]
v = "aeiou"

for word in words:
	count = 0
	for i in range(len(word)):
		if word[i] in v:
			count += 1
	if count >= 9:
		print(word) 