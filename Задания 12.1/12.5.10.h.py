words = [line.strip() for line in open('wordlist.txt')]
l = 0
for word in words:
	if len(word) > l:
		l =len(word)
		l_word = word
print(l_word)  
