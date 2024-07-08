words = [line.strip() for line in open('wordlist.txt')]
alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = 0
for word in words:
	l = 0
	for character in word:
		if character != "-":
			l += 1
	letters += l
d = {}
for letter in alphabet:
	count = 0
	for word in words:
		x = word.count(letter)
		count += x
	d[letter] = round((count/letters) * 100,2)
print(d) 

