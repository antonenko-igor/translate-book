d = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = [line.strip() for line in open('wordlist.txt')]
for i in range(26):
	count = 0
	for word in words:
		if alphabet[i] in word:
			count += 1
	d[alphabet[i]] = "{:.1f}".format(int(count/len(words)*100))
print(d) 
		



